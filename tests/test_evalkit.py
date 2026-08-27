import json, tempfile, unittest
from evalkit.core import run
class EvalTests(unittest.TestCase):
    def test_pass(self):
        f=tempfile.NamedTemporaryFile(mode="w",delete=False); json.dump([{"id":"a","contains":"yes"}],f); f.close()
        self.assertEqual(run(f.name,{"a":"yes indeed"})["passed"],1)
    def test_fail(self):
        f=tempfile.NamedTemporaryFile(mode="w",delete=False); json.dump([{"id":"a","contains":"yes"}],f); f.close()
        self.assertEqual(run(f.name,{"a":"no"})["passed"],0)
if __name__ == "__main__": unittest.main()
