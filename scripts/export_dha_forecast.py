import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rll.dha_fisher import run_reference_forecast


def main() -> None:
    out_dir = REPO_ROOT / "results" / "dha"
    out_dir.mkdir(parents=True, exist_ok=True)
    forecast = run_reference_forecast()
    out_file = out_dir / "fisher_forecast_reference.json"
    out_file.write_text(json.dumps(forecast, indent=2), encoding="utf-8")
    print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
