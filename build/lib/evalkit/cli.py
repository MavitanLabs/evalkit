import argparse, json
from .core import run
def main():
    p=argparse.ArgumentParser(description="Run repeatable dataset-backed agent evaluations")
    p.add_argument("cases"); p.add_argument("outputs", help="JSON object mapping case IDs to outputs"); a=p.parse_args()
    print(json.dumps(run(a.cases,json.loads(a.outputs)),indent=2))

if __name__ == "__main__": main()
