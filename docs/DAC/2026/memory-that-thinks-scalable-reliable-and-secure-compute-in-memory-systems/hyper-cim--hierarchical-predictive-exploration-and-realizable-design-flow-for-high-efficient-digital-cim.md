HYPER-CIM: Hierarchical Predictive Exploration and Realizable Design Flow for High-Efficient Digital CIM
Authors：
[An Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=93848846160645309421)，[Yuhui Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=19035657665257829471)，[Yuhuai Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0478059605750623273)，[Tianhui Jiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8699908682175624088)，[Xiaoxue Zhong](https://63dac.conference-program.com/?post_type=page&p=15&uid=16820511183968586231)，[Defa Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=11106095046691667)，[Arindam Basu](https://63dac.conference-program.com/?post_type=page&p=15&uid=77558097807363534821)，[Xin Si](https://63dac.conference-program.com/?post_type=page&p=15&uid=06525473388796445)，[Jun Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=094443)

## 中文标题

HYPER-CIM：面向高效数字存内计算的分层预测式探索与可落地设计流程

## 英文摘要

Computing-in-Memory (CIM) is a promising solution to the memory wall, yet most prior studies optimize only one level—macro, accelerator, or architecture—rather than the full stack. This work presents HYPER-CIM, a hierarchical predictive exploration and realizable design flow that integrates all three levels. We build a scalable, fully digital CIM template in 28 nm with tunable accumulation length, local storage length, precision, parallel channels, and pipeline depth. More than 8k silicon-consistent design points were used to train a multi-head hierarchical circuit-optimization (MHCO) surrogate model, which predicts power, performance, and area (PPA) across 297M configurations. The resulting CIM “white-box” model offers circuit-faithful visibility for architecture-level design-space exploration (DSE) and Pareto search. Guided by this flow, we fabricated and silicon-verified four processing-element (PE)-flow CIM macros and one cross-level-flow CIM (CF-CIM) macro in 28 nm CMOS technology. Based on chip test results, the best-performing macro achieves 90.8 TOPS/W and 1.23 TOPS/mm2, yielding a figure-of-merit (FoM) improvement of 31.12×–3.8×106 over prior CIM designs. Under identical specifications, the CF-CIM improves energy efficiency from 52.13 TOPS/W to 67.9 TOPS/W and area efficiency from 0.41 TOPS/mm2 to 0.51 TOPS/mm2.

## 中文摘要

存内计算（CIM）是应对存储墙问题的有前景方案，但既有研究大多仅优化宏单元、加速器或架构中的单一层次，而非全栈协同。本文提出 HYPER-CIM，一套融合上述三个层次的分层预测式探索与可落地设计流程。我们在 28 nm 工艺下构建了可扩展的全数字 CIM 模板，其累加长度、本地存储长度、精度、并行通道数与流水线深度均可调。利用超过 8k 个与硅片一致的设计点训练多头分层电路优化（MHCO）代理模型，该模型可在 297M 种配置上预测功耗、性能与面积（PPA）。由此得到的 CIM“白盒”模型为架构级设计空间探索（DSE）与 Pareto 搜索提供了贴合电路的可视性。在该流程指导下，我们在 28 nm CMOS 工艺下流片并完成硅验证了四个处理单元（PE）流 CIM 宏单元与一个跨层次流 CIM（CF-CIM）宏单元。基于芯片测试结果，性能最佳的宏单元实现 90.8 TOPS/W 与 1.23 TOPS/mm2，相较已有 CIM 设计将品质因数（FoM）提升 31.12×–3.8×10^6。在相同规格下，CF-CIM 将能效从 52.13 TOPS/W 提升至 67.9 TOPS/W，面积效率从 0.41 TOPS/mm2 提升至 0.51 TOPS/mm2。

## 英文关键词

Computing-in-memory, SRAM, design-space exploration, artificial intelligence

## 中文关键词

存内计算、SRAM、设计空间探索、人工智能
