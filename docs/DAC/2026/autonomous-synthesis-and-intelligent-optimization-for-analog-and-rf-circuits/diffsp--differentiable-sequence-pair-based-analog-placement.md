Diffsp: Differentiable Sequence Pair-Based Analog Placement
Authors：
[Peng Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=35263480881481101501)，[Mingzi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=24746776806155805071)，[Yapeng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=1472746777532170421)，[Yuyang Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=8432721704885972621)，[Tinghuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=64168005757594372121)，[Tsung-Yi Ho](https://63dac.conference-program.com/?post_type=page&p=15&uid=568743)，[Bei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=991243)

## 中文标题

DiffSP：基于可微序列对的模拟电路布局

## 英文摘要

Analog placement with compact representations is traditionally solved using heuristic or simulated annealing methods that are difficult to integrate with a differentiable optimization engine. This paper introduces DiffSP, a differentiable sequence-pair-based analog placement method that bridges discrete combinatorial representation with continuous gradient optimization. We derive a smooth relaxation of the sequence pair constraint graph via Gumbel–Sinkhorn relaxation, which allows area, wirelength, and symmetry objectives to be jointly optimized via automatic gradient calculation. A MILP-based legalization stage then enforces exact geometric and symmetry constraints. Experiments on industrial-level OTA benchmarks show that DiffSP achieves better placement quality and post-layout performance metrics than state-of-the-art analog placers with significantly reduced runtime.

## 中文摘要

采用紧凑表示的模拟电路布局传统上使用启发式或模拟退火方法求解，这些方法难以与可微优化引擎集成。本文提出 DiffSP，一种基于可微序列对的模拟电路布局方法，将离散组合表示与连续梯度优化衔接起来。我们通过 Gumbel–Sinkhorn 松弛导出序列对约束图的平滑松弛，从而可通过自动梯度计算联合优化面积、线长和对称性目标。随后基于 MILP 的合法化阶段强制执行精确的几何与对称性约束。在工业级 OTA 基准上的实验表明，DiffSP 相比最先进的模拟布局器获得更好的布局质量和后版图性能指标，同时显著缩短运行时间。
