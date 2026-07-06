from pathlib import Path

from scopp.algorithm.clustering import cluster_map
from scopp.map.grid import discretize_map
from scopp.map.io import load_map

ROOT = Path(__file__).resolve().parents[2]


def test_official_minibatch_is_reproducible_with_seed() -> None:
    mapped = discretize_map(load_map(ROOT / "examples/maps/indoor_lab.yaml"))
    first = cluster_map(mapped, profile="official_minibatch", random_seed=17)
    second = cluster_map(mapped, profile="official_minibatch", random_seed=17)
    assert first == second
    assert first.profile == "official_minibatch"
    assert first.random_seed == 17


def test_official_profile_associates_each_node_once() -> None:
    mapped = discretize_map(load_map(ROOT / "examples/maps/indoor_lab.yaml"))
    result = cluster_map(mapped, profile="official_minibatch", random_seed=0)
    assert {cluster.node_id for cluster in result.clusters} == {node.id for node in mapped.source.node_starts}
    assert len(result.conflict_cell_ids) > 0


def test_official_profile_runs_full_pipeline() -> None:
    from scopp.algorithm.auction import allocate_conflict_cells
    from scopp.algorithm.path_planning import plan_coverage_paths

    mapped = discretize_map(load_map(ROOT / "examples/maps/indoor_lab.yaml"))
    clustered = cluster_map(mapped, profile="official_minibatch", random_seed=0)
    allocation = allocate_conflict_cells(mapped, clustered)
    plan = plan_coverage_paths(mapped, allocation)
    assert sum(len(path.cell_ids) for path in plan.paths) == len(mapped.cells)
    assert {path.node_id for path in plan.paths} == {node.id for node in mapped.source.node_starts}
