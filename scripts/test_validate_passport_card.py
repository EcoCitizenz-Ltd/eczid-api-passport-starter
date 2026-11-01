#!/usr/bin/env python3
"""Regression tests for the zero-dependency Passport Carry-Card validator."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_passport_card.py"

PARENT = "ECZ-ZZ-EXAMPL"
CHILD = f"{PARENT}::API_PASSPORT-4F9Q2A"
ENCODED_CHILD = "ECZ-ZZ-EXAMPL%3A%3AAPI_PASSPORT-4F9Q2A"


def base_card() -> dict:
    return {
        "schema": "eczid.passport-carry-card",
        "schema_version": "1.0",
        "ecz_id": CHILD,
        "passport_family": "api",
        "resolver_url": f"https://resolver.ecocitizenz.org/p/{ENCODED_CHILD}",
        "machine_proof_url": f"https://api.ecocitizenz.com/api/p/{ENCODED_CHILD}.json",
        "parent_ecz_id": PARENT,
        "subject_url": "https://api.example.com",
    }


class ValidatorContractTests(unittest.TestCase):
    def run_card(self, card: dict, *, allow_example: bool = False) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "card.json"
            path.write_text(json.dumps(card), encoding="utf-8")
            cmd = [sys.executable, str(VALIDATOR), str(path)]
            if allow_example:
                cmd.append("--allow-example")
            return subprocess.run(cmd, text=True, capture_output=True, check=False)

    def test_current_api_child_contract_passes(self) -> None:
        result = self.run_card(base_card())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_example_fixture_requires_explicit_allow_example(self) -> None:
        card = base_card()
        card["extensions"] = {"example_fixture": True}
        denied = self.run_card(card)
        self.assertNotEqual(denied.returncode, 0)
        self.assertIn("example fixture", denied.stderr)
        allowed = self.run_card(card, allow_example=True)
        self.assertEqual(allowed.returncode, 0, allowed.stderr)

    def test_legacy_noncanonical_id_is_rejected(self) -> None:
        card = base_card()
        card["ecz_id"] = "ECZ-GB-EXAMPLE-API"
        result = self.run_card(card)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("child passport_family requires", result.stderr)

    def test_family_type_code_mismatch_is_rejected(self) -> None:
        card = base_card()
        card["ecz_id"] = f"{PARENT}::MCP_PASSPORT-4F9Q2A"
        card["resolver_url"] = (
            "https://resolver.ecocitizenz.org/p/"
            "ECZ-ZZ-EXAMPL%3A%3AMCP_PASSPORT-4F9Q2A"
        )
        card["machine_proof_url"] = (
            "https://api.ecocitizenz.com/api/p/"
            "ECZ-ZZ-EXAMPL%3A%3AMCP_PASSPORT-4F9Q2A.json"
        )
        result = self.run_card(card)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires child type code 'API_PASSPORT'", result.stderr)

    def test_parent_mismatch_is_rejected(self) -> None:
        card = base_card()
        card["parent_ecz_id"] = "ECZ-ZZ-OTHERS"
        result = self.run_card(card)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must match the parent encoded", result.stderr)

    def test_legacy_resolver_route_is_rejected(self) -> None:
        card = base_card()
        card["resolver_url"] = f"https://resolver.ecocitizenz.org/passport/{CHILD}"
        result = self.run_card(card)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical human Resolver route", result.stderr)

    def test_wrong_machine_proof_route_is_rejected(self) -> None:
        card = base_card()
        card["machine_proof_url"] = f"https://resolver.ecocitizenz.org/api/p/{ENCODED_CHILD}.json"
        result = self.run_card(card)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("canonical machine proof route", result.stderr)


if __name__ == "__main__":
    unittest.main()
