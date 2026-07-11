# Third-Party Notices and Attribution

This project uses open-source software and is informed by published research. This notice distinguishes upstream reference behavior, installed dependencies, and project-specific extensions.

## SCoPP upstream reference

- Project: *Scalable Coverage Path Planning of Multi-Robot Teams for Monitoring Non-Convex Areas*
- Official repository: https://github.com/adamslab-ub/SCoPP
- Repository license: MIT License
- Paper: L. Collins, P. Ghassemi, S. Chowdhury, K. Dantu, E. Esfahani, and D. Doermann, ICRA 2021, arXiv:2103.14709
- Code reference used for parity review: `monitoring_algorithms.py` and `SCoPP_settings.py` from the upstream `main` branch

The present repository is an independently structured derivative implementation. It preserves SCoPP behavior as an explicit comparison baseline for clustering, conflict-cell auction, and `paper_nn`; it is not represented as an official SCoPP release or a byte-for-byte reproduction.

Project-specific extensions include:

- indoor Cartesian map and boundary policies;
- no-fly-zone geometry and valid-cell executable routing;
- metric closure over the 4-neighbor valid-cell graph;
- deterministic cheapest insertion plus 2-opt under `approx_metric_tsp`;
- direct/executable KPI separation and experiment UIs.

The upstream SCoPP license and copyright notice remain available in its official repository. If upstream source files or substantial source fragments are copied into this repository in the future, their MIT copyright and license text must accompany those copies.

## Runtime dependencies

The project installs and imports the following third-party Python packages rather than vendoring their source code:

- PyYAML
- Matplotlib
- NumPy
- scikit-learn
- Shapely

The test environment additionally uses pytest. Each dependency remains governed by its own license and copyright notices as distributed by its maintainers.

## Project license status

This notice does not select a license for the original work in this repository. The repository owner should add a root `LICENSE` file before inviting unrestricted reuse or external contributions.
