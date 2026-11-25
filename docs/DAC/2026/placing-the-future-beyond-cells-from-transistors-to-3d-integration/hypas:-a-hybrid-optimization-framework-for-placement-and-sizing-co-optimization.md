HyPAS: A Hybrid Optimization Framework for Placement and Sizing Co-Optimization
Authors：
[Fangzhou Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=70986091953490229061)，[Wuqian Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=845843)，[Bo-Ying Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5659897065256443041)，[An-Chieh Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37870427944038357381)，[HAN-WEN TSAO](https://63dac.conference-program.com/?post_type=page&p=15&uid=7999980767939073594)，[Yuyang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=8432721704885972621)，[Yun Shao](https://63dac.conference-program.com/?post_type=page&p=15&uid=29335073385199985661)，[Chun-Yao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=065343)，[Bei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=991243)

## 中文标题

HyPAS：面向布局与尺寸协同优化的混合优化框架

## 英文摘要

Incremental placement optimization improves PPA by refining cell locations, gate sizing, and buffering under physical constraints. Conventional incremental flows, composed of discrete heuristic stages with separate timing analyses, often converge slowly and yield inconsistent PPA gains due to the lack of a unified formulation. Recent differentiable placement methods enable scalable gradient-based refinement on smooth surrogates of wirelength, density, and timing but remain fragile near legality and timing-closure boundaries. To combine their strengths, we propose HyPAS, a hybrid framework that integrates discrete sign-off optimization with differentiable gradient refinement for placement and sizing co-optimization. The discrete stage, implemented with OpenROAD, ensures legality, timing closure, and buffer-aware repair; while the differentiable stage, built on DREAMPlace, performs gradient-guided placement and sizing using a GNN-based timing-power surrogate. A straight-through estimator (STE) bridges continuous gradients with discrete library parameters, enabling end-to-end physical co-optimization. Experiments show HyPAS delivers superior PPA gains with competitive runtime against 2025 ICCAD CAD Contest results and SOTA methods.

## 中文摘要

增量式布局优化通过在物理约束下精化单元位置、门尺寸与缓冲器插入来改善 PPA。由相互独立的启发式阶段与各自独立的时序分析所构成的传统增量流程往往收敛缓慢，且由于缺乏统一的形式化描述，其 PPA 收益并不稳定。近期的可微布局方法能够针对线长、密度与时序的光滑代理模型进行可扩展的梯度式精化，但在合法性边界与时序收敛边界附近仍较为脆弱。为结合两类方法的优势，我们提出 HyPAS，一个将离散签核优化与可微梯度精化相融合的混合框架，用于布局与尺寸的协同优化。离散阶段基于 OpenROAD 实现，确保合法性、时序收敛以及考虑缓冲器的修复；可微阶段基于 DREAMPlace 构建，利用基于 GNN 的时序—功耗代理模型执行梯度引导的布局与尺寸优化。直通估计器（STE）在连续梯度与离散库参数之间建立桥梁，从而实现端到端的物理协同优化。实验表明，与 2025 ICCAD CAD Contest 结果及 SOTA 方法相比，HyPAS 在具有竞争力的运行时间下取得了更优的 PPA 收益。
