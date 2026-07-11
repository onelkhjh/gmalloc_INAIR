# Executable KPI Result

![Executable KPI graph](./path_planner_exec_only_v1.png)

동일한 `official_minibatch` 할당, `seed=0`, `auction_bias=0.5` 조건에서 `approx_metric_tsp`만 사용해 KPI를 다시 산출했다. 경로 평가는 셀 중심의 직선거리와 별도로 valid cell 사이의 4-neighbor grid-adjacent executable 경로 및 no-fly zone 차단을 적용했다. Public-code NN 대비 executable makespan은 50.656 m에서 43.266 m로 14.59% 감소했고, 팀 총 executable 거리는 167.506 m에서 147.184 m로 12.13% 감소했다.

## Node-level summary

| Node | Approx Metric-TSP exec (m) | NN exec (m) | Improvement |
|---|---:|---:|---:|
| node-04 | 33.886 | 44.971 | 24.65% |
| node-03 | 43.266 | 50.656 | 14.59% |
| node-02 | 30.277 | 30.277 | 0.00% |
| node-01 | 39.754 | 41.602 | 4.44% |

## Team-level summary

| KPI | Approx Metric-TSP | Public-code NN | Improvement |
|---|---:|---:|---:|
| Direct makespan (m) | 41.179 | 47.772 | 13.80% |
| Direct total distance (m) | 136.467 | 145.718 | 6.35% |
| Executable makespan (m) | 43.266 | 50.656 | 14.59% |
| Executable total distance (m) | 147.184 | 167.506 | 12.13% |

`approx_metric_tsp`는 모든 로봇에 deterministic insertion + 2-opt를 동일하게 적용한다. `legacy_exact_tsp` 결과는 이 표와 KPI 계산에 포함하지 않았다.
