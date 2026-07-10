# AGENTS.md

## Project Goal

The baseline reference for this repository is the SCoPP paper *Scalable Coverage Path Planning of Multi-Robot Teams for Monitoring Non-Convex Areas* (arXiv:2103.14709) and the authors' official code.

The current goal is not just reproduction. The goal is to improve KPI under the same baseline and optimize the result for multi-robot indoor coverage path planning.

## Reference Policy

1. Keep the paper and official code as the baseline reference.
2. Preserve paper/official-code reference for clustering, conflict auction, and coverage-path planning.
3. Put improvements in separate paths, settings, and artifacts.
4. Compare like with like: same map, same allocation, same constraints.
5. Keep direct-distance and executable-distance separate in reporting.

## Working Direction

- Use reproduction to define the baseline, not to define the final target.
- Treat baseline clustering and related steps as reference behavior.
- Use separate artifacts for comparison experiments and KPI improvement.
- Optimize for indoor flight and report the assumptions explicitly.

## Sub-agent Roles

Use sub-agents only when the task has a bounded, separable scope. The detailed role definitions and usage rules live in [docs/subagents.md](docs/subagents.md).

## Current Core Artifacts

- `artifacts/path_planner_exec_only_v1.json`
- `artifacts/path_planner_exec_only_v1.png`
- `artifacts/executable_kpi_result.md`

## Validation

When behavior changes, update the relevant tests together with the code.

Default validation:

```powershell
python -m pytest
```

If full tests are too heavy for the current step, at minimum run:

```powershell
python -m compileall .
```

## Summary

Keep the SCoPP paper and official code as the baseline reference, but center the project on better KPI and indoor-flight optimization. Baseline clustering and other core components stay as reference behavior; improvement experiments are managed separately.
