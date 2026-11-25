LEAP: A Self-Supervised Per-Cycle Toggle Propagation Model Supports Fast, Transferable, and Early Analysis of Layout Power
Authors：
[Wenkai LI](https://63dac.conference-program.com/?post_type=page&p=15&uid=91566662620660660201)，[Yuchao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03438700010529625741)，[Ziyan Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=2259987640179897564)，[Yao Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6294307449303409391)，[Wenji Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0880747726699421348)，[Mengming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=69110175844035149381)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

LEAP：支持快速、可迁移且早期版图功耗分析的自监督逐周期翻转传播模型

## 英文摘要

Accurate power analysis is critical in VLSI design, as it directly impacts power optimization strategies. However, traditional approaches are often hindered by the substantial runtime required for per-cycle toggle propagation in the netlist, which propagates register toggle information through combinational logic. To address this, we propose LEAP, the first work to enable per-cycle toggle propagation prediction with both high accuracy and efficiency. This is achieved through a novel, linear-complexity graph transformer capable of simulating toggle propagation, along with specially designed self-supervised pre-training tasks that enable the model to capture circuit structure and functionality. LEAP achieves a 7.6× speedup over the EDA tool in toggle propagation, and attains a near-perfect area under the Precision-Recall curve (PR-AUC) of 0.99 for prediction results. Moreover, LEAP can be seamlessly integrated with other machine learning based power models into LEAP-Power. This integration enables precise per-cycle layout power prediction directly from post-synthesis netlists, achieving a mean absolute percentage error (MAPE) of only 4.55%. By bypassing toggle propagation in the netlist, LEAP-Power delivers substantial runtime gains, running 5.3× faster than the model without LEAP.

## 中文摘要

精确的功耗分析在 VLSI 设计中至关重要，因为它直接影响功耗优化策略。然而，传统方法常常受制于网表中逐周期翻转传播所需的巨大运行时间，该过程通过组合逻辑传播寄存器的翻转信息。为此，我们提出 LEAP，这是首个同时实现高精度与高效率的逐周期翻转传播预测工作。这得益于一种新颖的、具有线性复杂度的图 Transformer，它能够模拟翻转传播，以及专门设计的自监督预训练任务，使模型得以捕捉电路结构与功能。LEAP 在翻转传播上相比 EDA 工具实现了 7.6× 的加速，并在预测结果上达到近乎完美的 PR 曲线下面积（PR-AUC）0.99。此外，LEAP 可以与其他基于机器学习的功耗模型无缝集成，形成 LEAP-Power。该集成能够直接从综合后网表进行精确的逐周期版图功耗预测，平均绝对百分比误差（MAPE）仅为 4.55%。通过绕过网表中的翻转传播，LEAP-Power 带来了显著的运行时间收益，比未使用 LEAP 的模型快 5.3×。
