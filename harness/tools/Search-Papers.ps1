#Requires -Version 5.1
<#
.SYNOPSIS
    논문 메타데이터 검색 보조 도구 (Semantic Scholar / Crossref / OpenAlex / arXiv).

.DESCRIPTION
    literature-researcher Skill 이 사용하는 보조 스크립트. 웹 검색 결과와 달리 DOI·초록·인용수 같은
    구조화된 메타데이터를 공개 API 에서 받아 표(markdown) 또는 JSON 으로 출력한다.
    API 키가 필요 없는 엔드포인트만 사용하며, 검색 결과의 서지정보만 다룬다 (본문은 가져오지 않음).

.EXAMPLE
    pwsh -File harness/tools/Search-Papers.ps1 -Query "three-level NPC inverter DC-link capacitor condition monitoring" -Source all -Limit 20
    pwsh -File harness/tools/Search-Papers.ps1 -Query "neutral point current harmonic NPC" -Source semanticscholar -YearFrom 2015 -Json
    pwsh -File harness/tools/Search-Papers.ps1 -Citations 10.1109/TPEL.2016.2xxxxx      # 이 논문을 인용한 논문
    pwsh -File harness/tools/Search-Papers.ps1 -References 10.1109/TPEL.2016.2xxxxx     # 이 논문이 인용한 논문
    (Windows PowerShell 5.1 이면 pwsh 대신 powershell 을 사용)
#>
[CmdletBinding(DefaultParameterSetName = 'Search')]
param(
    [Parameter(ParameterSetName = 'Search', Mandatory = $true, Position = 0)]
    [string] $Query,

    # semanticscholar | crossref | openalex | arxiv | all
    [Parameter(ParameterSetName = 'Search')]
    [ValidateSet('semanticscholar', 'crossref', 'openalex', 'arxiv', 'all')]
    [string] $Source = 'all',

    [Parameter(ParameterSetName = 'Search')]
    [int] $YearFrom = 0,

    # 이 DOI 를 인용한 논문 목록 (Semantic Scholar)
    [Parameter(ParameterSetName = 'Citations', Mandatory = $true)]
    [string] $Citations,

    # 이 DOI 가 인용한 논문 목록 (Semantic Scholar)
    [Parameter(ParameterSetName = 'References', Mandatory = $true)]
    [string] $References,

    [int] $Limit = 15,

    # JSON 으로 출력 (기본: markdown 표)
    [switch] $Json,

    # 초록 포함 (표가 길어짐)
    [switch] $WithAbstract,

    # OpenAlex polite pool 용 이메일 (선택). 지정하지 않으면 보내지 않는다.
    [string] $Mailto = ''
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'
try { [Console]::OutputEncoding = [System.Text.Encoding]::UTF8 } catch { }
try { [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12 } catch { }

# ----------------------------------------------------------------------------
# HTTP: PowerShell 5.1 이 UTF-8 응답을 잘못 디코딩하는 문제를 피하려고 바이트로 받아 직접 디코딩한다.
# ----------------------------------------------------------------------------
function Invoke-Api([string]$Url, [string]$Accept = 'application/json') {
    $headers = @{ 'Accept' = $Accept; 'User-Agent' = 'cap-aging-harness/1.0 (research literature search)' }
    $resp = Invoke-WebRequest -Uri $Url -Headers $headers -UseBasicParsing -TimeoutSec 40
    $bytes = $null
    if ($resp.PSObject.Properties['RawContentStream'] -and $resp.RawContentStream) {
        $ms = New-Object System.IO.MemoryStream
        $resp.RawContentStream.Position = 0
        $resp.RawContentStream.CopyTo($ms)
        $bytes = $ms.ToArray()
    }
    if ($bytes -and $bytes.Length -gt 0) { return [System.Text.Encoding]::UTF8.GetString($bytes) }
    return [string]$resp.Content
}
function Get-Json([string]$Url) { return (Invoke-Api $Url | ConvertFrom-Json) }
function Enc([string]$s) { return [System.Uri]::EscapeDataString($s) }
function Get-Prop($o, [string]$n, $d = $null) {
    if ($null -eq $o) { return $d }
    $p = $o.PSObject.Properties[$n]; if ($null -eq $p -or $null -eq $p.Value) { return $d }; return $p.Value
}

# 공통 레코드 형식으로 변환. 모든 파서는 다음 필드를 채운다.
function New-Record {
    param($Source, $Title, $Authors, $Year, $Venue, $Doi, $Url, $Abstract, $Cited)
    [pscustomobject]@{
        source   = $Source
        title    = [string]$Title
        authors  = [string]$Authors
        year     = $Year
        venue    = [string]$Venue
        doi      = [string]$Doi
        url      = [string]$Url
        cited_by = $Cited
        abstract = [string]$Abstract
    }
}

# ----------------------------------------------------------------------------
# 출처별 검색
# ----------------------------------------------------------------------------
function Search-SemanticScholar([string]$Q, [int]$N, [int]$YFrom) {
    $fields = 'title,authors,year,venue,externalIds,abstract,citationCount,url'
    $url = "https://api.semanticscholar.org/graph/v1/paper/search?query=$(Enc $Q)&limit=$N&fields=$fields"
    if ($YFrom -gt 0) { $url += "&year=$YFrom-" }
    $j = Get-Json $url
    foreach ($p in @(Get-Prop $j 'data' @())) { ConvertFrom-S2Paper $p }
}
function ConvertFrom-S2Paper($p) {
    $ext = Get-Prop $p 'externalIds'
    $doi = [string](Get-Prop $ext 'DOI' '')
    $arx = [string](Get-Prop $ext 'ArXiv' '')
    $link = [string](Get-Prop $p 'url' '')
    if (-not $link -and $doi) { $link = "https://doi.org/$doi" }
    if (-not $link -and $arx) { $link = "https://arxiv.org/abs/$arx" }
    $authors = (@(Get-Prop $p 'authors' @()) | ForEach-Object { Get-Prop $_ 'name' '' } | Where-Object { $_ }) -join ', '
    New-Record 'semanticscholar' (Get-Prop $p 'title' '') $authors (Get-Prop $p 'year' $null) (Get-Prop $p 'venue' '') $doi $link (Get-Prop $p 'abstract' '') (Get-Prop $p 'citationCount' $null)
}
function Get-SemanticScholarLinks([string]$Doi, [string]$Kind, [int]$N) {
    # Kind: citations (이 논문을 인용) | references (이 논문이 인용)
    $fields = 'title,authors,year,venue,externalIds,abstract,citationCount,url'
    $id = $Doi; if ($id -notmatch '^(DOI:|ARXIV:|CorpusId:)' -and $id -match '^10\.') { $id = "DOI:$id" }
    $url = "https://api.semanticscholar.org/graph/v1/paper/$(Enc $id)/$Kind`?limit=$N&fields=$fields"
    $j = Get-Json $url
    $key = if ($Kind -eq 'citations') { 'citingPaper' } else { 'citedPaper' }
    foreach ($row in @(Get-Prop $j 'data' @())) { $p = Get-Prop $row $key; if ($p) { ConvertFrom-S2Paper $p } }
}

function Search-Crossref([string]$Q, [int]$N, [int]$YFrom) {
    $url = "https://api.crossref.org/works?query=$(Enc $Q)&rows=$N&select=DOI,title,author,issued,container-title,URL,abstract,is-referenced-by-count"
    if ($YFrom -gt 0) { $url += "&filter=from-pub-date:$YFrom" }
    if ($Mailto) { $url += "&mailto=$(Enc $Mailto)" }
    $j = Get-Json $url
    foreach ($p in @(Get-Prop (Get-Prop $j 'message') 'items' @())) {
        $title = (@(Get-Prop $p 'title' @()) | Select-Object -First 1)
        $venue = (@(Get-Prop $p 'container-title' @()) | Select-Object -First 1)
        $year = $null
        $dp = Get-Prop (Get-Prop $p 'issued') 'date-parts'   # 형식: [[2020, 5, 1]] (PowerShell 이 바깥 배열을 풀 수 있음)
        if ($dp) { $first = @($dp)[0]; if ($first -is [array]) { $first = @($first)[0] }; if ("$first" -match '^\d{4}$') { $year = [int]$first } }
        $authors = (@(Get-Prop $p 'author' @()) | ForEach-Object { ((Get-Prop $_ 'given' '') + ' ' + (Get-Prop $_ 'family' '')).Trim() } | Where-Object { $_ }) -join ', '
        $abs = [string](Get-Prop $p 'abstract' '') -replace '<[^>]+>', '' -replace '\s+', ' '
        New-Record 'crossref' $title $authors $year $venue (Get-Prop $p 'DOI' '') (Get-Prop $p 'URL' '') $abs.Trim() (Get-Prop $p 'is-referenced-by-count' $null)
    }
}

function Search-OpenAlex([string]$Q, [int]$N, [int]$YFrom) {
    $url = "https://api.openalex.org/works?search=$(Enc $Q)&per-page=$N&select=id,doi,title,authorships,publication_year,primary_location,cited_by_count,abstract_inverted_index"
    if ($YFrom -gt 0) { $url += "&filter=from_publication_date:$YFrom-01-01" }
    if ($Mailto) { $url += "&mailto=$(Enc $Mailto)" }
    $j = Get-Json $url
    foreach ($p in @(Get-Prop $j 'results' @())) {
        $authors = (@(Get-Prop $p 'authorships' @()) | ForEach-Object { Get-Prop (Get-Prop $_ 'author') 'display_name' '' } | Where-Object { $_ }) -join ', '
        $venue = [string](Get-Prop (Get-Prop (Get-Prop $p 'primary_location') 'source') 'display_name' '')
        $doi = ([string](Get-Prop $p 'doi' '')) -replace '^https?://doi\.org/', ''
        $abs = ConvertFrom-InvertedIndex (Get-Prop $p 'abstract_inverted_index')
        $link = if ($doi) { "https://doi.org/$doi" } else { [string](Get-Prop $p 'id' '') }
        New-Record 'openalex' (Get-Prop $p 'title' '') $authors (Get-Prop $p 'publication_year' $null) $venue $doi $link $abs (Get-Prop $p 'cited_by_count' $null)
    }
}
function ConvertFrom-InvertedIndex($idx) {
    # OpenAlex 는 초록을 {단어: [위치...]} 형태로 준다 → 위치 순으로 재조립
    if ($null -eq $idx) { return '' }
    $pos = @{}
    foreach ($prop in $idx.PSObject.Properties) { foreach ($i in @($prop.Value)) { $pos[[int]$i] = $prop.Name } }
    if ($pos.Count -eq 0) { return '' }
    return (($pos.Keys | Sort-Object | ForEach-Object { $pos[$_] }) -join ' ')
}

function Search-Arxiv([string]$Q, [int]$N, [int]$YFrom) {
    $url = "http://export.arxiv.org/api/query?search_query=all:$(Enc $Q)&max_results=$N&sortBy=relevance"
    $xmlText = Invoke-Api $url 'application/atom+xml'
    [xml]$xml = $xmlText
    $ns = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
    $ns.AddNamespace('a', 'http://www.w3.org/2005/Atom')
    foreach ($e in $xml.SelectNodes('//a:entry', $ns)) {
        $title = ($e.SelectSingleNode('a:title', $ns).InnerText -replace '\s+', ' ').Trim()
        $authors = (@($e.SelectNodes('a:author/a:name', $ns)) | ForEach-Object { $_.InnerText }) -join ', '
        $pub = $e.SelectSingleNode('a:published', $ns).InnerText
        $year = $null; if ($pub -match '^(\d{4})') { $year = [int]$Matches[1] }
        if ($YFrom -gt 0 -and $year -and $year -lt $YFrom) { continue }
        $id = $e.SelectSingleNode('a:id', $ns).InnerText
        $abs = ($e.SelectSingleNode('a:summary', $ns).InnerText -replace '\s+', ' ').Trim()
        $doiNode = $e.SelectSingleNode('*[local-name()="doi"]')
        $doi = if ($doiNode) { $doiNode.InnerText } else { '' }
        New-Record 'arxiv' $title $authors $year 'arXiv' $doi $id $abs $null
    }
}

# ----------------------------------------------------------------------------
# 병합(DOI/제목 기준 중복 제거) 과 출력
# ----------------------------------------------------------------------------
function Merge-Records($Records) {
    # DOI 가 같거나(우선) 정규화한 제목이 같으면 같은 논문으로 보고 빈 칸을 서로 보강한다.
    $byDoi = @{}; $byTitle = @{}; $out = New-Object System.Collections.Generic.List[object]
    foreach ($r in $Records) {
        if ($null -eq $r) { continue }
        $doiKey   = if ($r.doi) { $r.doi.ToLowerInvariant() } else { '' }
        $titleKey = (([string]$r.title).ToLowerInvariant() -replace '[^a-z0-9가-힣]', '')
        $ex = $null
        if ($doiKey -and $byDoi.ContainsKey($doiKey)) { $ex = $byDoi[$doiKey] }
        elseif ($titleKey -and $byTitle.ContainsKey($titleKey)) { $ex = $byTitle[$titleKey] }
        if ($ex) {
            foreach ($f in 'abstract', 'venue', 'authors', 'url', 'doi') { if (-not $ex.$f -and $r.$f) { $ex.$f = $r.$f } }
            if ($null -eq $ex.cited_by -and $null -ne $r.cited_by) { $ex.cited_by = $r.cited_by }
            if ($ex.source -notmatch [regex]::Escape($r.source)) { $ex.source = ($ex.source + '+' + $r.source) }
            if ($ex.doi) { $byDoi[$ex.doi.ToLowerInvariant()] = $ex }
            continue
        }
        if ($doiKey)   { $byDoi[$doiKey] = $r }
        if ($titleKey) { $byTitle[$titleKey] = $r }
        $out.Add($r)
    }
    return ,$out
}
function Write-MarkdownTable($Records) {
    if ($WithAbstract) {
        Write-Output '| # | 제목 | 저자 | 연도 | 출처(학술지) | DOI/URL | 인용수 | 검색출처 | 초록 |'
        Write-Output '|---|---|---|---|---|---|---|---|---|'
    } else {
        Write-Output '| # | 제목 | 저자 | 연도 | 출처(학술지) | DOI/URL | 인용수 | 검색출처 |'
        Write-Output '|---|---|---|---|---|---|---|---|'
    }
    $i = 0
    foreach ($r in $Records) {
        $i++
        $link = if ($r.doi) { $r.doi } else { $r.url }
        $auth = $r.authors; if ($auth.Length -gt 60) { $auth = $auth.Substring(0, 60) + '…' }
        $cells = @($i, ($r.title -replace '\|', '/'), ($auth -replace '\|', '/'), $r.year, ($r.venue -replace '\|', '/'), $link, $r.cited_by, $r.source)
        if ($WithAbstract) { $abs = $r.abstract -replace '\|', '/'; if ($abs.Length -gt 400) { $abs = $abs.Substring(0, 400) + '…' }; $cells += $abs }
        Write-Output ('| ' + (($cells | ForEach-Object { [string]$_ }) -join ' | ') + ' |')
    }
}

# ----------------------------------------------------------------------------
# 메인
# ----------------------------------------------------------------------------
$records = New-Object System.Collections.Generic.List[object]
$errors  = New-Object System.Collections.Generic.List[string]

function Add-Results([string]$Label, [scriptblock]$Fn) {
    try { foreach ($r in @(& $Fn)) { $records.Add($r) } }
    catch { $errors.Add("$Label 실패: $($_.Exception.Message)") }
}

switch ($PSCmdlet.ParameterSetName) {
    'Citations'  { Add-Results 'semanticscholar citations'  { Get-SemanticScholarLinks $Citations 'citations' $Limit } }
    'References' { Add-Results 'semanticscholar references' { Get-SemanticScholarLinks $References 'references' $Limit } }
    default {
        if ($Source -in 'semanticscholar', 'all') { Add-Results 'semanticscholar' { Search-SemanticScholar $Query $Limit $YearFrom } }
        if ($Source -in 'crossref', 'all')        { Add-Results 'crossref'        { Search-Crossref $Query $Limit $YearFrom } }
        if ($Source -in 'openalex', 'all')        { Add-Results 'openalex'        { Search-OpenAlex $Query $Limit $YearFrom } }
        if ($Source -in 'arxiv', 'all')           { Add-Results 'arxiv'           { Search-Arxiv $Query $Limit $YearFrom } }
    }
}

$merged = Merge-Records $records
if ($Json) {
    # (빈 List 를 @() 로 감싸면 PowerShell 바인더 오류가 나므로 ToArray() 사용)
    $payload = [ordered]@{ query = $Query; count = $merged.Count; errors = $errors.ToArray(); results = $merged.ToArray() }
    Write-Output ($payload | ConvertTo-Json -Depth 6)
} else {
    if ($PSCmdlet.ParameterSetName -eq 'Search') { Write-Output "검색어: $Query  (출처: $Source, 결과 $($merged.Count)건, 중복 제거됨)" }
    else { Write-Output "$($PSCmdlet.ParameterSetName): $(if ($Citations) { $Citations } else { $References })  (결과 $($merged.Count)건)" }
    Write-Output ''
    Write-MarkdownTable $merged
    if ($errors.Count -gt 0) { Write-Output ''; foreach ($e in $errors) { Write-Output "[!] $e" } }
    Write-Output ''
    Write-Output '주의: 위 표는 메타데이터(제목/초록)만이다. 세부 주장(특정 고조파, 수식, 실험결과)은 본문을 확인하기 전까지 "미확인" 으로 취급할 것.'
}
if ($merged.Count -eq 0 -and $errors.Count -gt 0) { exit 1 }
exit 0
