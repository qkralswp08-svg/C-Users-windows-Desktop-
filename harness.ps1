#Requires -Version 5.1
<#
.SYNOPSIS
    캡 노화진단 프로젝트용 AI Research Harness 진입점.

.DESCRIPTION
    사용자의 자연어 요청을 받아
      1) Claude CLI 실행 환경을 확인하고
      2) .claude/skills/*/SKILL.md 를 읽어 사용 가능한 Skill 목록을 만들고
      3) 요청 문장의 키워드로 필요한 Skill 을 고른 뒤 (여러 개 조합 가능)
      4) 선택된 Skill 지침 + 요청 + 최근 작업 기록을 하나의 "작업 지시서"(harness/runs/*.md)로 만들고
      5) Claude Code 를 실행한다 (기본: 대화형, -Print: 일회성 출력).
    AI 로직은 전부 SKILL.md / 템플릿 / config.json 에 있으므로 이 스크립트는 "실행기" 역할만 한다.

    새 Skill 추가: .claude/skills/<이름>/SKILL.md 파일 하나만 만들면 자동 인식된다 (`-NewSkill 이름` 으로 템플릿 생성).
    설정 변경:   harness/config.json (프로필, 라우터, Claude 옵션).
    지시서 문구: harness/templates/brief.md

.EXAMPLE
    .\harness.ps1
        요청을 물어본 뒤 Skill 을 자동 선택해서 Claude 대화형 세션을 연다.
.EXAMPLE
    .\harness.ps1 iSa2 전류에서 어떤 고조파가 큰지 확인해줘
        따옴표 없이 써도 된다. 키워드로 npc-inverter-expert, signal-analyzer 등이 선택된다.
.EXAMPLE
    .\harness.ps1 paper "NPC DC-link capacitor 노화진단 논문 찾아줘"
        첫 단어가 프로필(config.json 의 profiles) 이면 그 프로필의 Skill 을 사용한다.
.EXAMPLE
    .\harness.ps1 -Skills matlab,npc "..."      # Skill 직접 지정 (부분 이름 허용)
    .\harness.ps1 -Print "..."                 # 대화형 대신 결과만 출력하고 workspace/results 에 저장
    .\harness.ps1 -DryRun "..."                # 어떤 Skill 이 선택되고 어떤 지시서가 만들어지는지만 확인
    .\harness.ps1 -List                        # Skill / 프로필 목록
    .\harness.ps1 -Check                       # Claude 실행 환경 점검
    .\harness.ps1 -Continue                    # 직전 Claude 대화 이어가기
    .\harness.ps1 -NewSkill cnn-input-analysis # 새 Skill 템플릿 생성
#>
[CmdletBinding()]
param(
    # 요청 문장. 첫 단어가 프로필 이름이면 프로필로 해석하고 나머지를 요청으로 본다.
    [Parameter(Position = 0, ValueFromRemainingArguments = $true)]
    [string[]] $Request,

    # Skill 을 직접 지정 (쉼표 구분, 부분 이름 허용). 지정하면 라우터를 건너뛴다.
    [string[]] $Skills,

    # 대화형 대신 일회성 실행: 결과를 콘솔에 출력하고 workspace/results 에 저장한다.
    [switch] $Print,

    # 실제로 Claude 를 실행하지 않고 Skill 선택 결과와 지시서만 보여준다.
    [switch] $DryRun,

    # Skill 과 프로필 목록만 출력.
    [switch] $List,

    # Claude CLI / 인증 / 폴더 구조 점검만 수행.
    [switch] $Check,

    # 직전 Claude 대화를 이어간다 (claude --continue).
    [switch] $Continue,

    # 특정 세션 ID 로 이어간다 (claude --resume <id>).
    [string] $Resume,

    # 새 Skill 템플릿을 .claude/skills/<이름>/SKILL.md 로 생성한다.
    [string] $NewSkill,

    # Claude 모델 지정 (예: sonnet, opus). 비우면 Claude 기본값 / config.json 값.
    [string] $Model,

    # 프로젝트 루트. 기본값은 이 스크립트가 있는 폴더.
    [string] $ProjectRoot,

    # 로그를 남기지 않는다.
    [switch] $NoLog
)

# ============================================================================
# 0. 기본 설정: 인코딩, 경로, 오류 처리
# ============================================================================
Set-StrictMode -Version 2.0
$ErrorActionPreference = 'Stop'

# 한글 폴더/한글 출력이 깨지지 않도록 콘솔과 자식 프로세스 인코딩을 UTF-8 로 맞춘다.
try {
    [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
    $OutputEncoding = [System.Text.Encoding]::UTF8
} catch { }

$script:Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$script:IsWin     = ($env:OS -eq 'Windows_NT')

if ([string]::IsNullOrWhiteSpace($ProjectRoot)) { $ProjectRoot = $PSScriptRoot }
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path

$Paths = @{
    Root      = $ProjectRoot
    Harness   = Join-Path $ProjectRoot 'harness'
    Config    = Join-Path (Join-Path $ProjectRoot 'harness') 'config.json'
    Templates = Join-Path (Join-Path $ProjectRoot 'harness') 'templates'
    Runs      = Join-Path (Join-Path $ProjectRoot 'harness') 'runs'
    Skills    = Join-Path (Join-Path $ProjectRoot '.claude') 'skills'
    Context   = Join-Path $ProjectRoot 'context'
    Results   = Join-Path (Join-Path $ProjectRoot 'workspace') 'results'
    Logs      = Join-Path $ProjectRoot 'logs'
}

# ============================================================================
# 1. 출력 도우미
# ============================================================================
function Write-Head([string]$Text) { Write-Host ""; Write-Host "== $Text" -ForegroundColor Cyan }
function Write-Info([string]$Text) { Write-Host "   $Text" }
function Write-Ok  ([string]$Text) { Write-Host "   [OK] $Text" -ForegroundColor Green }
function Write-Warn([string]$Text) { Write-Host "   [!] $Text" -ForegroundColor Yellow }
function Write-Bad ([string]$Text) { Write-Host "   [X] $Text" -ForegroundColor Red }

function Read-Utf8File([string]$Path) {
    # PowerShell 5.1 은 BOM 없는 UTF-8 을 ANSI 로 읽으므로 항상 UTF-8 로 명시한다.
    return [System.IO.File]::ReadAllText($Path, [System.Text.Encoding]::UTF8)
}
function Write-Utf8File([string]$Path, [string]$Text) {
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    [System.IO.File]::WriteAllText($Path, $Text, $script:Utf8NoBom)
}
function Append-Utf8File([string]$Path, [string]$Text) {
    $dir = Split-Path -Parent $Path
    if (-not (Test-Path -LiteralPath $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
    [System.IO.File]::AppendAllText($Path, $Text, $script:Utf8NoBom)
}

# ============================================================================
# 2. 설정 로딩 (harness/config.json)
# ============================================================================
function Get-HarnessConfig {
    if (-not (Test-Path -LiteralPath $Paths.Config)) {
        throw "설정 파일이 없습니다: $($Paths.Config)"
    }
    try {
        return (Read-Utf8File $Paths.Config | ConvertFrom-Json)
    } catch {
        throw "harness/config.json 을 읽을 수 없습니다 (JSON 문법 확인): $($_.Exception.Message)"
    }
}

# PSCustomObject 에서 속성을 안전하게 꺼낸다 (없으면 기본값).
function Get-Prop($Object, [string]$Name, $Default = $null) {
    if ($null -eq $Object) { return $Default }
    $p = $Object.PSObject.Properties[$Name]
    if ($null -eq $p -or $null -eq $p.Value) { return $Default }
    return $p.Value
}

# ============================================================================
# 3. Claude CLI 탐지 및 환경 확인
#    - 특정 설치 경로를 가정하지 않고 PATH → 알려진 위치 순으로 실제 존재하는 실행 파일을 찾는다.
# ============================================================================
function Find-ClaudeCli($Config) {
    $candidates = New-Object System.Collections.Generic.List[string]

    # (1) 명시적 지정: config.json → 환경변수
    $cfgPath = Get-Prop (Get-Prop $Config 'claude') 'path' ''
    if ($cfgPath) { $candidates.Add($cfgPath) }
    if ($env:HARNESS_CLAUDE_PATH) { $candidates.Add($env:HARNESS_CLAUDE_PATH) }

    # (2) PATH 에 있는 claude (Windows 는 .exe > .cmd > 그 외 순으로 선호)
    $found = @(Get-Command claude -All -ErrorAction SilentlyContinue)
    if ($found.Count -gt 0) {
        $ranked = $found | Sort-Object {
            $src = $_.Source
            if     ($src -match '\.exe$') { 0 }
            elseif ($src -match '\.cmd$') { 1 }
            elseif ($src -match '\.bat$') { 2 }
            elseif ($src -match '\.ps1$') { 3 }
            else { 4 }
        }
        foreach ($f in $ranked) { if ($f.Source) { $candidates.Add($f.Source) } }
    }

    # (3) 알려진 설치 위치 (네이티브 설치기 / npm 전역 설치)
    if ($script:IsWin) {
        if ($env:USERPROFILE) { $candidates.Add((Join-Path $env:USERPROFILE '.local\bin\claude.exe')) }
        if ($env:APPDATA)     { $candidates.Add((Join-Path $env:APPDATA 'npm\claude.cmd')) }
        if ($env:LOCALAPPDATA){ $candidates.Add((Join-Path $env:LOCALAPPDATA 'Programs\claude-code\claude.exe')) }
    } else {
        if ($env:HOME) { $candidates.Add((Join-Path $env:HOME '.local/bin/claude')) }
        $candidates.Add('/usr/local/bin/claude')
    }

    foreach ($c in $candidates) {
        if ([string]::IsNullOrWhiteSpace($c)) { continue }
        if (Test-Path -LiteralPath $c -PathType Leaf) { return (Resolve-Path -LiteralPath $c).Path }
    }
    return $null
}

function Get-ClaudeVersion([string]$Cli) {
    try {
        $out = & $Cli --version 2>$null
        if ($LASTEXITCODE -eq 0 -and $out) { return ([string]($out | Select-Object -First 1)).Trim() }
    } catch { }
    return $null
}

# 로그인 상태: 'ok' | 'no' | 'unknown'
function Get-ClaudeAuthState([string]$Cli) {
    try {
        $out = & $Cli auth status --json 2>$null
        $text = ($out -join "`n")
        if ($text -match '"loggedIn"\s*:\s*true')  { return 'ok' }
        if ($text -match '"loggedIn"\s*:\s*false') { return 'no' }
    } catch { }
    if ($env:ANTHROPIC_API_KEY) { return 'ok' }
    return 'unknown'
}

function Show-EnvironmentCheck($Config, [string]$Cli) {
    Write-Head "환경 점검"
    Write-Info "프로젝트 루트 : $($Paths.Root)"
    Write-Info "PowerShell    : $($PSVersionTable.PSVersion) ($($PSVersionTable.PSEdition))"
    if ($script:IsWin) {
        Write-Info "실행 정책     : $(Get-ExecutionPolicy -Scope CurrentUser) (CurrentUser) / $(Get-ExecutionPolicy) (유효)"
    }

    if ($Cli) {
        Write-Ok "Claude CLI     : $Cli"
        $ver = Get-ClaudeVersion $Cli
        if ($ver) { Write-Ok "버전           : $ver" } else { Write-Warn "버전 확인 실패 (--version 응답 없음)" }
        switch (Get-ClaudeAuthState $Cli) {
            'ok'      { Write-Ok "인증           : 로그인됨" }
            'no'      { Write-Bad "인증           : 로그인 안 됨 → 'claude auth login' 또는 ANTHROPIC_API_KEY 설정" }
            default   { Write-Warn "인증           : 확인 불가 (구버전 CLI 이거나 'auth status' 미지원). 실행하면서 확인됨" }
        }
    } else {
        Write-Bad "Claude CLI 를 찾지 못했습니다."
        Write-Info "설치: PowerShell 에서  irm https://claude.ai/install.ps1 | iex   (또는 npm i -g @anthropic-ai/claude-code)"
        Write-Info "이미 설치했다면 harness/config.json 의 claude.path 또는 환경변수 HARNESS_CLAUDE_PATH 에 실행 파일 경로를 적어주세요."
    }

    Write-Head "폴더 구조"
    foreach ($k in 'Skills','Context','Templates','Runs','Results','Logs') {
        $p = $Paths[$k]
        if (Test-Path -LiteralPath $p) { Write-Ok ("{0,-10} {1}" -f $k, $p) } else { Write-Warn ("{0,-10} 없음: {1}" -f $k, $p) }
    }
    $claudeMd = Join-Path $Paths.Root 'CLAUDE.md'
    if (Test-Path -LiteralPath $claudeMd) { Write-Ok "CLAUDE.md  (프로젝트 Context, Claude 가 자동 로드)" } else { Write-Warn "CLAUDE.md 없음" }
    $ctx = Join-Path $Paths.Context 'project-context.md'
    if (Test-Path -LiteralPath $ctx) {
        if ((Read-Utf8File $ctx) -match 'TODO') { Write-Warn "context/project-context.md 에 TODO 항목이 남아 있습니다 → '.\harness.ps1 init' 으로 초안 작성 가능" }
    }
}

# ============================================================================
# 4. Skill 로딩 (.claude/skills/<name>/SKILL.md)
#    frontmatter 예:
#      ---
#      name: matlab-analyzer
#      description: ...
#      keywords: [matlab, fft, 고조파]
#      order: 40
#      ---
# ============================================================================
function ConvertFrom-Frontmatter([string]$Text) {
    # 반환: @{ Meta = <hashtable>; Body = <string> }
    $meta = @{}
    $body = $Text
    $m = [regex]::Match($Text, '^\uFEFF?---\s*\r?\n(.*?)\r?\n---\s*\r?\n?', [System.Text.RegularExpressions.RegexOptions]::Singleline)
    if ($m.Success) {
        $body = $Text.Substring($m.Length)
        $lines = $m.Groups[1].Value -split "\r?\n"
        $currentKey = $null
        foreach ($line in $lines) {
            if ($line -match '^\s*#') { continue }
            if ($line -match '^([A-Za-z0-9_\-]+)\s*:\s*(.*)$') {
                $currentKey = $Matches[1].ToLowerInvariant()
                $val = $Matches[2].Trim()
                if ($val -match '^\[(.*)\]$') {
                    # 인라인 리스트: [a, b, c]
                    $items = $Matches[1] -split ',' | ForEach-Object { $_.Trim().Trim('"').Trim("'") } | Where-Object { $_ }
                    $meta[$currentKey] = @($items)
                } elseif ($val -eq '') {
                    $meta[$currentKey] = @()   # 블록 리스트 시작 가능
                } else {
                    $meta[$currentKey] = $val.Trim('"').Trim("'")
                }
            } elseif ($line -match '^\s*-\s+(.*)$' -and $currentKey) {
                # 블록 리스트:  - item
                $item = $Matches[1].Trim().Trim('"').Trim("'")
                if ($meta[$currentKey] -is [array]) { $meta[$currentKey] += $item } else { $meta[$currentKey] = @($item) }
            }
        }
    }
    return @{ Meta = $meta; Body = $body }
}

function Get-Skills {
    $list = New-Object System.Collections.Generic.List[object]
    if (-not (Test-Path -LiteralPath $Paths.Skills)) { return ,$list }
    foreach ($dir in Get-ChildItem -LiteralPath $Paths.Skills -Directory | Sort-Object Name) {
        $file = Join-Path $dir.FullName 'SKILL.md'
        if (-not (Test-Path -LiteralPath $file)) { continue }
        try {
            $parsed = ConvertFrom-Frontmatter (Read-Utf8File $file)
        } catch {
            Write-Warn "Skill 파일을 읽지 못했습니다: $file ($($_.Exception.Message))"; continue
        }
        $meta = $parsed.Meta
        $name = $meta['name']; if (-not $name) { $name = $dir.Name }
        $order = 50; if ($meta['order']) { [int]::TryParse([string]$meta['order'], [ref]$order) | Out-Null }
        $kw = @(); if ($meta['keywords']) { $kw = @($meta['keywords']) }
        $list.Add([pscustomobject]@{
            Name        = [string]$name
            Description = [string](Get-HashValue $meta 'description' '')
            Keywords    = $kw
            Order       = $order
            CombineWith = @(Get-HashValue $meta 'combine-with' @())
            Path        = $file
            RelPath     = ($file.Substring($Paths.Root.Length).TrimStart('\','/') -replace '\\','/')
            Body        = $parsed.Body.Trim()
        })
    }
    return ,$list
}
function Get-HashValue([hashtable]$H, [string]$Key, $Default) { if ($H.ContainsKey($Key)) { return $H[$Key] } else { return $Default } }

# 사용자가 -Skills 로 준 이름(부분 이름 허용)을 실제 Skill 로 해석
function Resolve-SkillNames([string[]]$Names, $AllSkills) {
    $resolved = New-Object System.Collections.Generic.List[object]
    foreach ($raw in ($Names -split ',' | ForEach-Object { $_.Trim() } | Where-Object { $_ })) {
        $exact = $AllSkills | Where-Object { $_.Name -eq $raw }
        if ($exact) { $resolved.Add($exact); continue }
        $partial = @($AllSkills | Where-Object { $_.Name -like "*$raw*" })
        if ($partial.Count -eq 1) { $resolved.Add($partial[0]); continue }
        if ($partial.Count -gt 1) { throw "Skill 이름 '$raw' 이(가) 여러 개와 일치합니다: $(($partial | ForEach-Object Name) -join ', ')" }
        throw "Skill '$raw' 을(를) 찾을 수 없습니다. -List 로 목록을 확인하세요."
    }
    # 이름 기준 중복 제거 (Select-Object -Unique 는 객체 비교가 불안정해서 사용하지 않음)
    $seen = @{}; $unique = @()
    foreach ($s in ($resolved | Sort-Object Order, Name)) { if (-not $seen.ContainsKey($s.Name)) { $seen[$s.Name] = $true; $unique += $s } }
    return $unique
}

# ============================================================================
# 5. Skill Router — 요청 문장의 키워드로 필요한 Skill 을 고른다.
#    의도적으로 단순하게 유지: 키워드 포함 개수 = 점수. (Skill 이름 직접 언급 = 가중치 3)
#    맞는 Skill 이 없으면 config.router.defaultSkills 사용.
# ============================================================================
function Select-SkillsForRequest([string]$Text, $AllSkills, $Config) {
    $router     = Get-Prop $Config 'router'
    $maxSkills  = [int](Get-Prop $router 'maxSkills' 4)
    $minScore   = [int](Get-Prop $router 'minScore' 1)
    $defaults   = @(Get-Prop $router 'defaultSkills' @('project-analyzer'))

    $lower = $Text.ToLowerInvariant()
    $scored = foreach ($s in $AllSkills) {
        $hits = New-Object System.Collections.Generic.List[string]
        $score = 0
        if ($lower.Contains($s.Name.ToLowerInvariant())) { $score += 3; $hits.Add("이름:$($s.Name)") }
        foreach ($k in $s.Keywords) {
            $kl = ([string]$k).ToLowerInvariant()
            if ($kl -and $lower.Contains($kl)) { $score += 1; $hits.Add($k) }
        }
        [pscustomobject]@{ Skill = $s; Score = $score; Hits = $hits }
    }

    $chosen = @($scored | Where-Object { $_.Score -ge $minScore } | Sort-Object @{Expression='Score';Descending=$true}, @{Expression={$_.Skill.Order}} | Select-Object -First $maxSkills)
    $reason = ''
    if ($chosen.Count -eq 0) {
        $chosen = @($scored | Where-Object { $defaults -contains $_.Skill.Name })
        $reason = "키워드 일치 없음 → 기본 Skill 사용 ($($defaults -join ', '))"
    } else {
        $reason = ($chosen | ForEach-Object { "$($_.Skill.Name)[$($_.Hits -join ',')]" }) -join ' ; '
    }
    # 파이프라인 순서(order)로 정렬해서 반환
    $ordered = @($chosen | Sort-Object { $_.Skill.Order }, { $_.Skill.Name } | ForEach-Object { $_.Skill })
    return @{ Skills = $ordered; Reason = $reason }
}

# ============================================================================
# 6. 작업 지시서(brief) 생성 — 템플릿(harness/templates/brief.md) 의 {{...}} 를 채운다.
# ============================================================================
function Get-RecentResearchLog([int]$Count) {
    $file = Join-Path $Paths.Context 'research-log.md'
    if ($Count -le 0 -or -not (Test-Path -LiteralPath $file)) { return '' }
    $text = Read-Utf8File $file
    # "## " 로 시작하는 항목 단위로 나눠 마지막 N 개만 사용
    $parts = [regex]::Split($text, '(?m)^(?=## )') | Where-Object { $_.Trim() -and $_.TrimStart().StartsWith('## ') }
    if (-not $parts) { return '' }
    $tail = @($parts | Select-Object -Last $Count)
    return (($tail | ForEach-Object { $_.Trim() }) -join "`n`n")
}

function New-Brief([string]$RequestText, $ChosenSkills, [string]$Reason, [string]$Mode, $Config) {
    $tplPath = Join-Path $Paths.Templates 'brief.md'
    if (-not (Test-Path -LiteralPath $tplPath)) { throw "지시서 템플릿이 없습니다: $tplPath" }
    $tpl = Read-Utf8File $tplPath

    $now   = Get-Date
    $names = ($ChosenSkills | ForEach-Object Name) -join ', '

    $sections = foreach ($s in $ChosenSkills) {
        "### Skill: $($s.Name)`n(원본: $($s.RelPath))`n`n$($s.Body)`n"
    }

    $allSkillLines = ($script:AllSkillsForBrief | Sort-Object Order, Name | ForEach-Object { "- ``$($_.Name)``: $($_.Description)" }) -join "`n"

    $recentN = [int](Get-Prop (Get-Prop $Config 'router') 'recentLogEntries' 3)
    $recent  = Get-RecentResearchLog $recentN
    $recentSection = ''
    if ($recent) { $recentSection = "## 최근 작업 기록 (context/research-log.md 마지막 $recentN 개)`n`n$recent`n" }

    $text = $tpl.Replace('{{DATE}}', $now.ToString('yyyy-MM-dd HH:mm')).
                 Replace('{{DATE_SHORT}}', $now.ToString('yyyy-MM-dd')).
                 Replace('{{MODE}}', $Mode).
                 Replace('{{SKILL_NAMES}}', $names).
                 Replace('{{ROUTE_REASON}}', $Reason).
                 Replace('{{REQUEST}}', $RequestText.Trim()).
                 Replace('{{RECENT_LOG_SECTION}}', $recentSection).
                 Replace('{{ALL_SKILLS}}', $allSkillLines).
                 Replace('{{SKILL_SECTIONS}}', (($sections) -join "`n"))

    $file = Join-Path $Paths.Runs ("{0}-brief.md" -f $now.ToString('yyyyMMdd-HHmmss'))
    Write-Utf8File $file $text
    return @{ Path = $file; Text = $text; RelPath = ($file.Substring($Paths.Root.Length).TrimStart('\','/') -replace '\\','/') }
}

# ============================================================================
# 7. 로그 (logs/harness-YYYY-MM.md) — 요청 / Skill / 결과 요약 / 오류만 기록. 비밀정보는 기록하지 않는다.
# ============================================================================
function Write-HarnessLog($Config, [hashtable]$Entry) {
    if ($NoLog) { return }
    if (-not [bool](Get-Prop (Get-Prop $Config 'log') 'enabled' $true)) { return }
    try {
        $dirName = [string](Get-Prop (Get-Prop $Config 'log') 'dir' 'logs')
        $dir  = Join-Path $Paths.Root $dirName
        $file = Join-Path $dir ("harness-{0}.md" -f (Get-Date).ToString('yyyy-MM'))
        $req  = [string]$Entry.Request
        if ($req.Length -gt 300) { $req = $req.Substring(0, 300) + ' …' }
        $sb = New-Object System.Text.StringBuilder
        [void]$sb.AppendLine(("## {0} | {1} | {2}" -f (Get-Date).ToString('yyyy-MM-dd HH:mm:ss'), $Entry.Mode, $Entry.Status))
        [void]$sb.AppendLine("- 요청: " + ($req -replace '\r?\n', ' '))
        [void]$sb.AppendLine("- Skill: " + $Entry.Skills)
        if ($Entry.Profile) { [void]$sb.AppendLine("- 프로필: " + $Entry.Profile) }
        if ($Entry.Brief)   { [void]$sb.AppendLine("- 지시서: " + $Entry.Brief) }
        if ($Entry.Result)  { [void]$sb.AppendLine("- 결과: " + $Entry.Result) }
        if ($Entry.Error)   { [void]$sb.AppendLine("- 오류: " + $Entry.Error) }
        [void]$sb.AppendLine()
        Append-Utf8File $file $sb.ToString()
    } catch {
        Write-Warn "로그 기록 실패: $($_.Exception.Message)"
    }
}

# ============================================================================
# 8. Claude 실행
# ============================================================================
function Get-ClaudeCommonArgs($Config) {
    # 주의: PowerShell 자동 변수와 겹치지 않도록 $list 사용. 빈 리스트가 null 로 풀리지 않도록 ',' 로 반환.
    $list = New-Object System.Collections.Generic.List[string]
    $c = Get-Prop $Config 'claude'
    $model = $Model; if (-not $model) { $model = [string](Get-Prop $c 'model' '') }
    if ($model) { $list.Add('--model'); $list.Add($model) }
    $pm = [string](Get-Prop $c 'permissionMode' '')
    if ($pm) { $list.Add('--permission-mode'); $list.Add($pm) }
    foreach ($a in @(Get-Prop $c 'extraArgs' @())) { if ($a) { $list.Add([string]$a) } }
    return ,$list
}

# 대화형: Claude Code 세션을 열고 첫 메시지로 "지시서를 읽고 시작하라"를 보낸다.
# (긴 텍스트를 명령줄 인자로 넘기면 Windows 에서 따옴표/길이 문제가 생기므로 지시서는 파일로 전달한다.)
# 주의: 이 함수의 출력을 변수에 담으면 Claude 의 화면 출력이 파이프로 잡혀 TUI 가 깨진다.
#       반드시 문장(statement)으로 호출하고, 종료 코드는 $script:ClaudeExitCode 로 받는다.
function Invoke-ClaudeInteractive([string]$Cli, $Config, $Brief, [string]$RequestText) {
    # 첫 메시지는 짧게, 따옴표 없이. (claude.cmd 셸 경유 시 코드페이지 문제를 피하려고 특수기호도 ASCII 만 사용)
    $preview = ($RequestText -replace '[\r\n"]+', ' ').Trim()
    if ($preview.Length -gt 80) { $preview = $preview.Substring(0, 80) + '...' }
    $first = "[Harness] 요청: $preview -> 먼저 $($Brief.RelPath) 파일을 읽고, 그 작업 지시서에 따라 작업을 시작하라."

    $cliArgs = Get-ClaudeCommonArgs $Config
    $cliArgs.Add($first)

    Write-Head "Claude Code 시작 (대화형)"
    Write-Info "종료: /exit 또는 Ctrl+C 두 번.  이어가기: .\harness.ps1 -Continue"
    Write-Host ""
    $script:ClaudeExitCode = 0
    Push-Location -LiteralPath $Paths.Root
    try {
        & $Cli @cliArgs
        $script:ClaudeExitCode = $LASTEXITCODE
    } finally { Pop-Location }
}

# 일회성: 지시서 전체를 표준입력으로 넘기고 JSON 결과를 받는다.
function Invoke-ClaudePrint([string]$Cli, $Config, $Brief, [string]$RequestText) {
    $cliArgs = Get-ClaudeCommonArgs $Config
    $cliArgs.Add('-p'); $cliArgs.Add('--output-format'); $cliArgs.Add('json')
    foreach ($a in @(Get-Prop (Get-Prop $Config 'claude') 'printExtraArgs' @())) { if ($a) { $cliArgs.Add([string]$a) } }

    Write-Head "Claude 실행 (일회성, 결과만 출력)"
    Write-Info "작업 중... (탐색 범위에 따라 수 분 걸릴 수 있음)"
    $errFile = [System.IO.Path]::GetTempFileName()
    $raw = $null
    Push-Location -LiteralPath $Paths.Root
    try {
        $prev = $ErrorActionPreference; $ErrorActionPreference = 'Continue'
        try { $raw = ($Brief.Text | & $Cli @cliArgs 2>$errFile) } finally { $ErrorActionPreference = $prev }
        $code = $LASTEXITCODE
    } finally { Pop-Location }

    $stderr = ''
    if (Test-Path -LiteralPath $errFile) { $stderr = (Read-Utf8File $errFile).Trim(); Remove-Item -LiteralPath $errFile -Force -ErrorAction SilentlyContinue }
    $text = (@($raw) -join "`n").Trim()

    $result = $null; $meta = $null
    if ($text) {
        try {
            $json = $text | ConvertFrom-Json
            $result = [string](Get-Prop $json 'result' '')
            $meta = $json
        } catch { $result = $text }   # JSON 이 아니면 원문 그대로
    }
    if ($code -ne 0 -or -not $result) {
        $msg = "Claude 실행 실패 (exit $code)"
        if ($stderr) { $msg += "`n$stderr" }
        if ($text -and -not $result) { $msg += "`n$text" }
        throw $msg
    }
    if ($meta -and [bool](Get-Prop $meta 'is_error' $false)) { throw "Claude 오류 응답: $result" }

    # 결과 저장
    $slug = ($RequestText -replace '[\\/:*?"<>|\r\n]+', ' ').Trim()
    if ($slug.Length -gt 40) { $slug = $slug.Substring(0, 40) }
    $out = Join-Path $Paths.Results ("{0}-{1}.md" -f (Get-Date).ToString('yyyyMMdd-HHmmss'), ($slug -replace '\s+', '_'))
    $header = "# 결과: $($RequestText.Trim())`n`n- 일시: $((Get-Date).ToString('yyyy-MM-dd HH:mm'))`n- Skill: $(($Brief.Skills | ForEach-Object Name) -join ', ')`n- 지시서: $($Brief.RelPath)`n"
    if ($meta) { $header += "- 세션: $(Get-Prop $meta 'session_id' '') / 비용: `$$(Get-Prop $meta 'total_cost_usd' '?') / 턴: $(Get-Prop $meta 'num_turns' '?')`n" }
    Write-Utf8File $out ($header + "`n---`n`n" + $result + "`n")

    Write-Host ""
    Write-Host $result
    Write-Host ""
    Write-Ok "결과 저장: $out"
    return @{ Result = $result; File = $out; Meta = $meta }
}

# ============================================================================
# 9. 보조 명령: -List, -NewSkill
# ============================================================================
function Show-SkillList($AllSkills, $Config) {
    Write-Head "Skill 목록 (.claude/skills/*/SKILL.md)"
    if ($AllSkills.Count -eq 0) { Write-Warn "Skill 이 없습니다."; return }
    foreach ($s in ($AllSkills | Sort-Object Order, Name)) {
        Write-Host ("   {0,-24} [{1,2}] {2}" -f $s.Name, $s.Order, $s.Description) -ForegroundColor White
        if ($s.Keywords.Count -gt 0) { Write-Host ("   {0,-24}      키워드: {1}" -f '', (($s.Keywords | Select-Object -First 12) -join ', ')) -ForegroundColor DarkGray }
    }
    Write-Head "프로필 (.\harness.ps1 <프로필> ""요청"")"
    $profiles = Get-Prop $Config 'profiles'
    if ($profiles) {
        foreach ($p in $profiles.PSObject.Properties | Where-Object { $_.Name -ne '_comment' }) {
            $sk = (@(Get-Prop $p.Value 'skills' @())) -join ', '
            Write-Host ("   {0,-10} {1}" -f $p.Name, (Get-Prop $p.Value 'description' '')) -ForegroundColor White
            Write-Host ("   {0,-10} → {1}" -f '', $sk) -ForegroundColor DarkGray
        }
    }
    Write-Host ""
}

function New-SkillFromTemplate([string]$Name) {
    $safe = ($Name.Trim().ToLowerInvariant() -replace '[^a-z0-9\-]+', '-').Trim('-')
    if (-not $safe) { throw "Skill 이름은 영문 소문자/숫자/하이픈으로 지정하세요 (예: cnn-input-analysis)" }
    $dir  = Join-Path $Paths.Skills $safe
    $file = Join-Path $dir 'SKILL.md'
    if (Test-Path -LiteralPath $file) { throw "이미 존재합니다: $file" }
    $tpl = Read-Utf8File (Join-Path $Paths.Templates 'SKILL.template.md')
    Write-Utf8File $file ($tpl.Replace('{{NAME}}', $safe))
    Write-Ok "새 Skill 템플릿 생성: $file"
    Write-Info "description / keywords / 절차를 채우면 바로 라우터와 Claude 가 인식합니다. ('.\harness.ps1 skill ""...""' 로 Claude 에게 작성을 맡길 수도 있음)"
}

# ============================================================================
# 10. 메인
# ============================================================================
$exitCode = 0
$logEntry = @{ Mode = ''; Status = ''; Request = ''; Skills = ''; Profile = ''; Brief = ''; Result = ''; Error = '' }
$config = $null
try {
    $config = Get-HarnessConfig

    # --- 보조 명령 ---
    if ($NewSkill) { New-SkillFromTemplate $NewSkill; exit 0 }

    $cli = Find-ClaudeCli $config
    if ($Check) { Show-EnvironmentCheck $config $cli; Show-SkillList (Get-Skills) $config; exit 0 }

    $allSkills = Get-Skills
    $script:AllSkillsForBrief = $allSkills
    if ($List) { Show-SkillList $allSkills $config; exit 0 }

    if (-not $cli -and -not $DryRun) {
        Show-EnvironmentCheck $config $null
        throw "Claude CLI 를 찾지 못해 실행할 수 없습니다."
    }

    # --- 이어가기 ---
    if ($Continue -or $Resume) {
        $cliArgs = Get-ClaudeCommonArgs $config
        if ($Resume) { $cliArgs.Add('--resume'); $cliArgs.Add($Resume) } else { $cliArgs.Add('--continue') }
        $logEntry.Mode = 'continue'; $logEntry.Request = "(이어가기 $Resume)"; $logEntry.Skills = '-'
        Write-Head "직전 Claude 대화 이어가기"
        Push-Location -LiteralPath $Paths.Root
        try { & $cli @cliArgs; $exitCode = $LASTEXITCODE } finally { Pop-Location }
        $logEntry.Status = if ($exitCode -eq 0) { 'ok' } else { "exit $exitCode" }
        Write-HarnessLog $config $logEntry
        exit $exitCode
    }

    # --- 요청 / 프로필 해석 ---
    $tokens = @($Request | Where-Object { $_ -ne $null })
    $profileName = ''; $profile = $null
    $profiles = Get-Prop $config 'profiles'
    if ($tokens.Count -gt 0 -and $profiles) {
        $cand = $profiles.PSObject.Properties[$tokens[0].ToLowerInvariant()]
        if ($cand -and $cand.Name -ne '_comment') {
            $profileName = $cand.Name; $profile = $cand.Value
            $tokens = @($tokens | Select-Object -Skip 1)
        }
    }
    $requestText = ($tokens -join ' ').Trim()
    if (-not $requestText -and $profile) { $requestText = [string](Get-Prop $profile 'request' '') }

    if (-not $requestText) {
        Write-Head "캡 노화진단 Research Harness"
        Write-Info "프로젝트: $($Paths.Root)"
        Write-Info "Skill $($allSkills.Count)개 로드됨. 자연어로 요청하면 필요한 Skill 을 자동 선택합니다. (-List 로 목록, -Skills 로 직접 지정)"
        if ($profileName) { Write-Info "프로필: $profileName" }
        Write-Host ""
        $requestText = (Read-Host "요청").Trim()
        if (-not $requestText) { Write-Warn "요청이 비어 있어 종료합니다."; exit 0 }
    }
    $logEntry.Request = $requestText; $logEntry.Profile = $profileName

    # --- Skill 선택: -Skills > 프로필 > 라우터 ---
    $chosen = @(); $reason = ''
    if ($Skills -and $Skills.Count -gt 0) {
        $chosen = Resolve-SkillNames $Skills $allSkills
        $reason = "사용자 지정 (-Skills)"
    } elseif ($profile) {
        $chosen = Resolve-SkillNames @(Get-Prop $profile 'skills' @()) $allSkills
        $reason = "프로필 '$profileName'"
    } else {
        $r = Select-SkillsForRequest $requestText $allSkills $config
        $chosen = @($r.Skills); $reason = $r.Reason
    }
    if ($chosen.Count -eq 0) { throw "선택된 Skill 이 없습니다. .claude/skills 폴더와 config.json 의 defaultSkills 를 확인하세요." }
    $logEntry.Skills = (($chosen | ForEach-Object Name) -join ', ')

    Write-Head "Skill 선택"
    foreach ($s in $chosen) { Write-Host ("   → {0,-24} {1}" -f $s.Name, $s.Description) }
    Write-Host "   근거: $reason" -ForegroundColor DarkGray

    # --- 지시서 생성 ---
    $mode = if ($Print) { 'print' } else { 'interactive' }
    $brief = New-Brief $requestText $chosen $reason $mode $config
    $brief.Skills = $chosen
    $logEntry.Mode = $mode; $logEntry.Brief = $brief.RelPath
    Write-Info "지시서: $($brief.RelPath)"

    if ($DryRun) {
        Write-Head "DryRun — 실행하지 않음"
        Write-Info "Claude CLI: $(if ($cli) { $cli } else { '(없음)' })"
        Write-Info "실행 인자 : $((Get-ClaudeCommonArgs $config) -join ' ') $(if ($Print) { '-p --output-format json (지시서를 stdin 으로 전달)' } else { '"[Harness] ... 지시서를 읽고 시작하라"' })"
        Write-Host ""
        Write-Host $brief.Text
        $logEntry.Status = 'dry-run'
        Write-HarnessLog $config $logEntry
        exit 0
    }

    # --- 실행 ---
    if ($Print) {
        $res = Invoke-ClaudePrint $cli $config $brief $requestText
        $summary = ($res.Result -replace '\s+', ' ').Trim()
        if ($summary.Length -gt 200) { $summary = $summary.Substring(0, 200) + ' …' }
        $logEntry.Result = "$summary (저장: $($res.File.Substring($Paths.Root.Length).TrimStart('\','/')))"
        $logEntry.Status = 'ok'
    } else {
        Invoke-ClaudeInteractive $cli $config $brief $requestText
        $exitCode = $script:ClaudeExitCode
        if ($null -eq $exitCode) { $exitCode = 0 }
        $logEntry.Status = if ($exitCode -eq 0) { 'ok' } else { "exit $exitCode" }
        $logEntry.Result = "대화형 세션 종료 (exit $exitCode). 이어가기: .\harness.ps1 -Continue"
    }
    Write-HarnessLog $config $logEntry
}
catch {
    $exitCode = 1
    $msg = $_.Exception.Message
    Write-Host ""
    Write-Bad $msg
    if ($_.InvocationInfo -and $_.InvocationInfo.ScriptLineNumber) {
        Write-Info "위치: $(Split-Path -Leaf $_.InvocationInfo.ScriptName):$($_.InvocationInfo.ScriptLineNumber)  (문제 보고 시 이 줄 번호를 알려주세요)"
    }
    if ($null -ne $config) {
        if (-not $logEntry.Mode) { $logEntry.Mode = 'setup' }
        $logEntry.Status = 'error'; $logEntry.Error = ($msg -replace '\r?\n', ' | ')
        Write-HarnessLog $config $logEntry
    }
}
exit $exitCode
