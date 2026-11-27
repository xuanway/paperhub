Powerpath: Internal-Probe-Free Search Interval Reduction for Efficient Statistical Sequential Constraint Characterization
Authors：
[Junzhuo Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=7563623746191940127)，[Li Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=47810283929829819371)，[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Ting-Jung Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=1498611451604654405)，[Lei He](https://63dac.conference-program.com/?post_type=page&p=15&uid=079243)

## 中文标题

Powerpath：面向高效统计时序约束表征的无内部探针搜索区间缩减方法

## 英文摘要

Sequential-constraint characterization consumes up to 80% of library signoff runtime. Traditional path-based methods rely on internal-node observability and fragile topology analysis, requiring extra simulations. They fail fundamentally for toggle-unexpected arcs such as hold and removal, where no robust internal voltage transitions exist. We present power-path, an internal-probe-free method that extracts a physics-grounded supply-current signature from the mandatory reference-delay simulation, enabling universal constraint estimation across all arc types without additional SPICE costs. An affine calibration using lookup table vertices refines the raw estimator for nominal characterization; for statistical deployment, an online ridge regression progressively tightens search intervals across Monte Carlo samples. Evaluated on pre/post-layout TSMC 5 nm and 12 nm libraries across 5 PVT corners, power-path achieves 1.5× speedup with affine calibration and 3.6× with statistical calibration, while maintaining signoff-grade accuracy. The approach requires no topology analysis or additional simulations. We open-source our code and data1.

## 中文摘要

时序约束表征最多可占用库签核运行时间的 80%。传统基于路径的方法依赖内部节点可观测性与脆弱的拓扑分析，并且需要额外的仿真。对于 hold、removal 等翻转不可预期的弧，由于不存在稳健的内部电压跳变，这类方法从根本上失效。我们提出 power-path，一种无需内部探针的方法，它从必需的参考延迟仿真中提取具有物理依据的电源电流特征，从而在无额外 SPICE 开销的前提下实现对全部弧类型的通用约束估计。利用查找表顶点进行仿射校准，可在标称表征下对原始估计器加以修正；在统计部署中，在线岭回归可随蒙特卡洛样本逐步收紧搜索区间。在 TSMC 5 nm 与 12 nm 库的布局前/布局后版本、覆盖 5 个 PVT 工艺角的评估中，power-path 在保持签核级精度的同时，仿射校准下取得 1.5× 加速，统计校准下取得 3.6× 加速。该方法无需拓扑分析或额外仿真。我们开源了代码与数据。

## 英文关键词

Sequential Constraint Timing Characterization, Statistical Standard Cell Library Characterization, Path-based, Path-difference

## 中文关键词

时序约束时序表征、统计标准单元库表征、基于路径的方法、路径差分
