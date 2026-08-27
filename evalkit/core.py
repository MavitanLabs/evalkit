import json
from pathlib import Path

def run(cases_path, outputs):
    cases=json.loads(Path(cases_path).read_text())
    results=[]
    for case in cases:
        actual=outputs.get(case["id"], "")
        expected=case.get("contains")
        results.append({"id":case["id"],"passed": expected in actual if expected else bool(actual)})
    return {"passed":sum(x["passed"] for x in results),"total":len(results),"results":results}
