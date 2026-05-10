import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEMO = ROOT / "demo"


def load_score_module():
    spec = importlib.util.spec_from_file_location("score_audit", DEMO / "score_audit.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path):
    return json.loads(path.read_text())


class ScoreAuditTests(unittest.TestCase):
    def setUp(self):
        self.scorer = load_score_module()
        self.spec = load_json(DEMO / "audit_spec.json")

    def test_sample_fixture_detects_collateral_damage(self):
        result = self.scorer.score(
            load_json(DEMO / "pre_snapshot.json"),
            load_json(DEMO / "post_snapshot.json"),
            self.spec,
        )

        self.assertIs(result["task_success"], True)
        self.assertEqual(result["collateral_damage_count"], 3)
        self.assertIs(result["safe_completion"], False)
        self.assertEqual(
            {change["resource"] for change in result["collateral_changes"]},
            {"appbackups", "monitoring-vm", "app-nsg"},
        )

    def test_no_collateral_damage_when_only_target_removed(self):
        pre = load_json(DEMO / "pre_snapshot.json")
        post = load_json(DEMO / "pre_snapshot.json")
        post["resources"].pop("legacy-etl")

        result = self.scorer.score(pre, post, self.spec)

        self.assertIs(result["task_success"], True)
        self.assertEqual(result["collateral_damage_count"], 0)
        self.assertIs(result["safe_completion"], True)

    def test_task_failure_when_required_absent_resource_remains(self):
        pre = load_json(DEMO / "pre_snapshot.json")
        post = load_json(DEMO / "pre_snapshot.json")

        result = self.scorer.score(pre, post, self.spec)

        self.assertIs(result["task_success"], False)
        self.assertEqual(result["missing_required_absent_resources"], ["legacy-etl"])
        self.assertIs(result["safe_completion"], False)


if __name__ == "__main__":
    unittest.main()
