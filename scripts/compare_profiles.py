"""Compare deterministic and official-style SCoPP clustering profiles."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from scopp.experiment import run_experiment


def summary(report):
    return {
        "profile": report.clustering_profile,
        "random_seed": report.random_seed,
        "node_cell_counts": [node.cell_count for node in report.node_metrics],
        "node_distances_m": [node.distance_m for node in report.node_metrics],
        "conflict_cells": report.conflict_cell_count,
        "cell_count_range": report.cell_count_range,
        "makespan_distance_m": report.makespan_distance_m,
        "total_distance_m": report.total_distance_m,
        "runtime_s": report.timings.total_s,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("map_file", type=Path)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output", type=Path, default=Path("artifacts/profile_comparison.json"))
    args = parser.parse_args()
    deterministic = run_experiment(args.map_file, clustering_profile="deterministic_lloyd")
    official = run_experiment(args.map_file, clustering_profile="official_minibatch", random_seed=args.seed)
    result = {
        "map": deterministic.map_name,
        "deterministic_lloyd": summary(deterministic),
        "official_minibatch": summary(official),
        "difference": {
            "conflict_cells": official.conflict_cell_count - deterministic.conflict_cell_count,
            "makespan_distance_m": official.makespan_distance_m - deterministic.makespan_distance_m,
            "total_distance_m": official.total_distance_m - deterministic.total_distance_m,
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
