# Multi-robot Indoor Coverage Path Planning

이 저장소는 SCoPP 논문 *Scalable Coverage Path Planning of Multi-Robot Teams for Monitoring Non-Convex Areas* (arXiv:2103.14709)과 저자의 공식 코드를 기준선으로 두고, 같은 조건에서 더 나은 KPI를 만들며 실내 비행에 적합하게 최적화하는 실험 저장소이다.

논문과 공식 코드는 clustering, auction, coverage path planning의 reference baseline으로 유지한다. 여기서 재현은 기준선을 정의하는 역할이고, 실제 초점은 비교 실험과 개선 결과에 있다. 즉, “논문을 얼마나 그대로 구현했는가”보다 “같은 상태에서 얼마나 더 좋은 결과를 만들었는가”를 더 중요하게 본다.

이 프로젝트는 Multi-robot Indoor Coverage Path Planning 관점에서, 실내 환경에서 실제로 쓰기 좋은 경로와 KPI를 만드는 쪽으로 진행한다. 따라서 direct-distance와 executable-distance를 섞지 않고, 같은 맵과 같은 할당과 같은 제약 조건에서만 비교한다.

## 핵심 방향

- baseline reference: SCoPP 논문 + 공식 코드
- comparison focus: 같은 상태에서의 KPI 비교
- optimization focus: multi-robot indoor flight에 더 적합한 경로와 지표
- reporting discipline: direct-distance와 executable-distance를 섞지 않음
- reference retention: clustering, auction, coverage path planning은 기준선으로 유지

## 현재 핵심 산출물

- `artifacts/path_planner_exec_only_v1.json`
- `artifacts/path_planner_exec_only_v1.png`
- `artifacts/executable_kpi_result.md`

## 실행

```powershell
python -m pip install -e ".[test]"
python -m pytest
python scripts/build_path_ui.py examples/maps/indoor_lab.yaml --output artifacts/path_ui.html
python scripts/build_progress_ui.py --output artifacts/progress_ui.html
python scripts/build_path_comparison_ui.py examples/maps/indoor_lab.yaml --output artifacts/path_comparison_ui.html --seed 0 --bias 0.5
python scripts/compare_path_planners.py examples/maps/indoor_lab.yaml --seed 0 --bias 0.5 --output artifacts/path_planner_exec_only_v1.json --plot artifacts/path_planner_exec_only_v1.png
```

## exec-only 비교 결과

핵심 비교 결과는 `artifacts/path_planner_exec_only_v1.png` 이다. 이 결과는 동일한 `grid-adjacent executable` 모델과 no-fly 차단 조건에서 Metric-TSP와 public-code NN을 비교한다.

요약 문서는 `artifacts/executable_kpi_result.md` 에 있다.

## 서브 에이전트

서브 에이전트 역할과 사용 원칙은 [docs/subagents.md](docs/subagents.md) 에 정리되어 있다.

## 참고

- `path_ui.html`, `progress_ui.html`, `path_comparison_ui.html` 은 Python 스크립트가 생성하는 UI 템플릿이다.
- 최종 KPI 요약에서는 direct-distance 수치를 사용하지 않는다.

---

# Multi-robot Indoor Coverage Path Planning

This repository uses the SCoPP paper *Scalable Coverage Path Planning of Multi-Robot Teams for Monitoring Non-Convex Areas* (arXiv:2103.14709) and the official author code as the baseline reference, while pursuing better KPI under the same conditions and optimizing the result for indoor flight.

The paper and official code remain the reference baseline for clustering, auction, and coverage path planning. In this project, reproduction defines the baseline; the main focus is on comparison experiments and improved results. The key question is not whether the paper was copied exactly, but whether the same state produces a better outcome.

The project is framed as Multi-robot Indoor Coverage Path Planning, so the priority is practical indoor behavior: routes, metrics, and comparisons that are actually suitable for indoor flight. Direct-distance and executable-distance are never mixed; comparisons are always made under the same map, the same allocation, and the same constraints.

## Core direction

- baseline reference: SCoPP paper + official code
- comparison focus: KPI under the same state
- optimization focus: paths and metrics better suited for multi-robot indoor flight
- reporting discipline: do not mix direct-distance and executable-distance
- reference retention: clustering, auction, and coverage path planning stay as baseline behavior

## Current checked-in artifacts

- `artifacts/path_planner_exec_only_v1.json`
- `artifacts/path_planner_exec_only_v1.png`
- `artifacts/executable_kpi_result.md`

## Run

```powershell
python -m pip install -e ".[test]"
python -m pytest
python scripts/build_path_ui.py examples/maps/indoor_lab.yaml --output artifacts/path_ui.html
python scripts/build_progress_ui.py --output artifacts/progress_ui.html
python scripts/build_path_comparison_ui.py examples/maps/indoor_lab.yaml --output artifacts/path_comparison_ui.html --seed 0 --bias 0.5
python scripts/compare_path_planners.py examples/maps/indoor_lab.yaml --seed 0 --bias 0.5 --output artifacts/path_planner_exec_only_v1.json --plot artifacts/path_planner_exec_only_v1.png
```

## Exec-only comparison result

The main comparison artifact is `artifacts/path_planner_exec_only_v1.png`. It compares Metric-TSP and public-code NN under the same `grid-adjacent executable` model with no-fly blocking.

The summary report is `artifacts/executable_kpi_result.md`.

## Sub-agents

The sub-agent roles and usage rules are documented in [docs/subagents.md](docs/subagents.md).

## Notes

- `path_ui.html` is the main route exploration UI.
- `progress_ui.html` is the main project progress UI.
- `path_comparison_ui.html` is the executable comparison UI.
- Final KPI reporting does not use direct-distance numbers.
