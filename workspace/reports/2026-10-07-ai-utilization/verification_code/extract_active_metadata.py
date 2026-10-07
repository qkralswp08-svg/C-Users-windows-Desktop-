import ast, sys, json, collections
src = open(sys.argv[1], encoding="utf-8").read()
tree = ast.parse(src)
consts = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name):
        name = node.targets[0].id
        if name in ("TWO_CONDITION_OUTER_TRAIN_FILES","TWO_CONDITION_TEST_FILES","THREE_CONDITION_TEST_FILES","CONDITION_EXPERIMENTS"):
            consts[name] = ast.literal_eval(node.value)
rows=[]
for axis,cfg in consts["CONDITION_EXPERIMENTS"].items():
    for part in ("train_files","unseen_files"):
        for r in cfg.get(part,[]):
            rows.append(dict(src="1cond:"+axis, role="TRAIN" if part=="train_files" else "UNSEEN_1C", **{k:r.get(k) for k in ["file_key","label","condition_name","fundamental_frequency_hz","switching_frequency_hz","output_fundamental_voltage_v","load_resistance_ohm","load_inductor_mh"]}))
for name,role in [("TWO_CONDITION_OUTER_TRAIN_FILES","TRAIN_2C_OUTER"),("TWO_CONDITION_TEST_FILES","UNSEEN_2C"),("THREE_CONDITION_TEST_FILES","UNSEEN_3C")]:
    for r in consts[name]:
        rows.append(dict(src=name, role=role, **{k:r.get(k) for k in ["file_key","label","condition_name","fundamental_frequency_hz","switching_frequency_hz","output_fundamental_voltage_v","load_resistance_ohm","load_inductor_mh"]}))
import csv
w=csv.DictWriter(open(sys.argv[2],"w",newline="",encoding="utf-8"),fieldnames=list(rows[0].keys()))
w.writeheader(); w.writerows(rows)
print("other keys in CONDITION_EXPERIMENTS cfg:", {a:list(c.keys()) for a,c in consts["CONDITION_EXPERIMENTS"].items()})
