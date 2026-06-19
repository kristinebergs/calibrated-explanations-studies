"""
Template experiment script.

Run from the repo root:
    python -m studies.<study-name>.experiments.run_experiment

Replace this file with one or more study-specific scripts.
Each script should:
  - Accept CLI flags for key parameters (use argparse).
  - Write results to ../results/ relative to this file.
  - Be runnable as a module: python -m studies.<study-name>.experiments.<name>
"""
from __future__ import annotations

import argparse
import pathlib

RESULTS_DIR = pathlib.Path(__file__).parent.parent / "results"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="<Study> experiment")
    parser.add_argument("--quick", action="store_true", help="Smoke run with reduced data")
    parser.add_argument("--out", default=str(RESULTS_DIR / "results.pkl"), help="Output path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # TODO: implement experiment
    raise NotImplementedError("Replace this template with your experiment code.")


if __name__ == "__main__":
    main()
