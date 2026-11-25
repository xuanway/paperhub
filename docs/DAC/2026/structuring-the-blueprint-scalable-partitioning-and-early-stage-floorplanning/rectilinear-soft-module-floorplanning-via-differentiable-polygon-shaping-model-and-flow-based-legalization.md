Rectilinear Soft Module Floorplanning via Differentiable Polygon Shaping Model and Flow-Based Legalization
Authors：
[Fuxing Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=615843)，[Qiyuan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=915843)，[Hao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=715843)，[Hao Gu](https://63dac.conference-program.com/?post_type=page&p=15&uid=020843)，[Wenxing Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=732843)，[xinning liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=025843)，[Ziran Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=127643)

## 中文标题

基于可微多边形塑形模型与流驱动合法化的直角软模块布局规划

## 英文摘要

Fixed-outline floorplanning remains a critical challenge in VLSI physical design, particularly for modern System-on-Chips (SoCs) that employ rectilinear soft modules to maximize area utilization and reduce wirelength. Existing methods adopt an incremental optimization strategy, introducing rectilinear shape considerations only after obtaining an initial rectangular solution. These approaches restrict module flexibility in early stages, limit the solution space, and degrade the final Quality of Results (QoR). We propose a unified floorplanning framework that, for the first time, seamlessly integrates the optimization of rectilinear soft modules into both global floorplanning and legalization stages. To address the computational challenges posed by rectilinear polygons, we introduce a differentiable polygon shaping model that represents and dynamically optimizes module shapes using a structured set of continuous variables during global floorplanning. We further design an augmented Lagrangian method to efficiently manage complex constraints with theoretical convergence guarantees, enhancing solution quality and stability. During legalization, we ingeniously model the problem as a minimum-cost flow formulation, where the objective is to minimize the total displacement, thereby ensuring a legal and high-quality final floorplan. Experimental results on GSRC and MCNC benchmarks demonstrate that our method achieves better solution quality, reducing half-perimeter wirelength by an average of 4% and up to 14% compared with state-of-the-art floorplanners, while maintaining competitive runtime performance.

## 中文摘要

固定轮廓布局规划仍是 VLSI 物理设计中的关键挑战，对于采用直角软模块以最大化面积利用率并降低线长的现代片上系统（SoC）尤为如此。现有方法采用增量式优化策略，仅在获得初始矩形解之后才引入直角形状的考量。这类方法在早期阶段限制了模块的灵活性，缩小了解空间，并降低了最终结果质量（QoR）。我们提出一个统一的布局规划框架，首次将直角软模块的优化无缝集成到全局布局规划与合法化两个阶段。为应对直角多边形带来的计算挑战，我们引入可微多边形塑形模型，在全局布局规划期间使用一组结构化连续变量表示并动态优化模块形状。我们进一步设计增广拉格朗日方法，以高效处理复杂约束并具有理论收敛保证，从而提升解质量与稳定性。在合法化阶段，我们巧妙地将问题建模为最小费用流形式，目标是最小化总位移，从而确保最终布局合法且高质量。在 GSRC 与 MCNC 基准上的实验结果表明，我们的方法取得了更优的解质量，与先进布局规划器相比，半周长线长平均降低 4%，最高降低 14%，同时保持有竞争力的运行时间。

## 英文关键词

Electronic Design Automation, Floorplanning, Rectilinear Soft Modules, Augmented Lagrangian Method, Minimum-Cost Flow

## 中文关键词

电子设计自动化、布局规划、直角软模块、增广拉格朗日方法、最小费用流
