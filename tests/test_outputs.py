import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def load_report():
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_exists_and_has_exact_schema():
    """Verifies success criterion 1: /app/report.json exists, is valid JSON, and contains exactly the required keys."""
    assert REPORT_PATH.exists(), "expected /app/report.json to exist"
    report = load_report()
    assert isinstance(report, dict)
    assert set(report.keys()) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_total_requests():
    """Verifies success criterion 2."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Verifies success criterion 3."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Verifies success criterion 4."""
    assert load_report()["top_path"] == "/index.html"
