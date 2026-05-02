import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rll.ln1pz_extractor import run_catalog_extraction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--omega-init", type=float, default=0.91)
    args = parser.parse_args()

    result = run_catalog_extraction(args.input, args.output, omega_init=args.omega_init)
    Path(args.summary).parent.mkdir(parents=True, exist_ok=True)
    Path(args.summary).write_text(json.dumps(result.__dict__, indent=2), encoding="utf-8")
    print(f"saved {args.output} and {args.summary}")


if __name__ == "__main__":
    main()
