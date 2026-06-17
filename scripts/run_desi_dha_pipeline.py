import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from rll.desi_dha_extractor import run_dha_pipeline


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", default=None)
    parser.add_argument("--seed", type=int, default=12345)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    res = run_dha_pipeline(data_path=args.data_path, rng_seed=args.seed)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, indent=2), encoding="utf-8")
    print(f"saved {out}")


if __name__ == "__main__":
    main()
