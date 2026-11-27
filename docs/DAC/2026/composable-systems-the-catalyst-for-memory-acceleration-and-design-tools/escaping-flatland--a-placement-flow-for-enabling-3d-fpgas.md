Escaping Flatland: A Placement Flow for Enabling 3D FPGAs
Authors：
[Cong "Callie" Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=516143)，[Andrew Kahng](https://63dac.conference-program.com/?post_type=page&p=15&uid=296643)，[Bodhisatta Pramanik](https://63dac.conference-program.com/?post_type=page&p=15&uid=40392695949679201931)，[Ismael Youssef](https://63dac.conference-program.com/?post_type=page&p=15&uid=092843)

## 中文标题

逃离平面国：一种支持 3D FPGA 的布局流程

## 英文摘要

3D field-programmable gate arrays (FPGAs) promise higher performance through vertical integration. However, existing placement tools, largely inherited from 2D frameworks, fail to capture the unique delay characteristics and optimization dynamics of 3D fabrics. We introduce a 3D FPGA placement flow that integrates partitioning-based initialization, adaptive cost scheduling, refined delay estimation, and a simulated annealing move set — all targeted at 3D FPGA architecture. Together, these enhancements improve timing estimates and the exploration of layer assignments during placement. Compared to Verilog-To-Routing (VTR), our experiments show geometric-mean (max) critical-path delay reductions of ∼3% (∼7%), ∼2% (∼4%), ∼3% (∼8%), and ∼6% (∼18%) for four 3D architectures: 3D CB, 3D CB-O, 3D CB-I, and 3D SB, respectively. We also achieve geometric-mean (max) routed wirelength reductions of ∼1% (∼3%), ∼2% (∼8%), < 1% (∼5%), and ∼5% (∼10%), respectively. Our work will be permissively open-sourced on GitHub.

## 中文摘要

三维现场可编程门阵列（3D FPGA）通过垂直集成有望带来更高的性能。然而，现有布局工具大多继承自 2D 框架，无法捕捉 3D 结构特有的延迟特性和优化动态。我们提出一种 3D FPGA 布局流程，它集成了基于划分的初始化、自适应代价调度、精细化的延迟估计以及模拟退火移动集——所有这些都针对 3D FPGA 架构。这些改进共同提升了时序估计以及在布局过程中对层分配的探索。与 Verilog-To-Routing（VTR）相比，我们的实验表明，对于四种 3D 架构：3D CB、3D CB-O、3D CB-I 和 3D SB，关键路径延迟的几何平均（最大）降低分别约为 3%（约 7%）、约 2%（约 4%）、约 3%（约 8%）和约 6%（约 18%）。我们还分别实现了约 1%（约 3%）、约 2%（约 8%）、< 1%（约 5%）和约 5%（约 10%）的布线线长几何平均（最大）降低。我们的工作将以宽松许可在 GitHub 上开源。
