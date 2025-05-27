from importlib import import_module
from pathlib import Path
import sys

# Ensure src directory is on the path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_imports():
    assert import_module("uptime_sla")
