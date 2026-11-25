Compilation Pipeline for Predicting Algorithmic Break-Even in an Early-Fault-Tolerant Surface Code Architecture
Authors：
[Tianyi Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=838743)，[Joseph Sullivan](https://63dac.conference-program.com/?post_type=page&p=15&uid=9484645628760922165)，[Sivaprasad Omanakuttan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8467036829259580715)，[Michael Perlin](https://63dac.conference-program.com/?post_type=page&p=15&uid=3834180171347277819)，[Ruslan Shaydulin](https://63dac.conference-program.com/?post_type=page&p=15&uid=862945958430404032)

## 中文标题

用于预测早期容错表面码架构中算法盈亏平衡点的编译流程

## 英文摘要

Recent experimental progress in realizing the surface code on hardware has materially advanced the prospects for fault-tolerant quantum computation. This progress creates urgency for the development of compilation workflows that directly target the forthcoming generation of devices with thousands of physical qubits, for which algorithm execution becomes practical. We develop a pipeline for compiling logical algorithms into physical circuits for the surface code, and use this pipeline to identify the requirements for achieving algorithmic break-even—where error correction improves the performance of a quantum algorithm—for two prominent quantum algorithms: the quantum approximate optimization algorithm (QAOA) and quantum phase estimation (QPE). Our pipeline integrates several open-source software tools, and leverages recent advances in error-aware unitary gate synthesis, high-fidelity magic state production, and the calculation of correlation surfaces. We perform classical simulations of physical Clifford proxy circuits produced by our pipeline, and find that both 5-qubit QAOA and QPE can reach algorithmic break-even with 2517 physical qubits (surface code distance 𝑑= 11) at physical error rates of 𝑝= 10−3, or 1737 physical qubits (𝑑= 9) at 𝑝= 5 × 10−4. Our work thereby identifies conditions for achieving algorithmic break-even with near-term quantum hardware and paves the way towards an end-to-end compiler for early-fault-tolerant surface code architectures.

## 中文摘要

近期在硬件上实现表面码的实验进展显著提升了容错量子计算的前景。这一进展使得开发直接面向即将到来的、具有数千个物理量子比特的器件的编译工作流变得迫切，因为只有在这类器件上算法执行才变得可行。我们开发了一条将逻辑算法编译为表面码物理电路的流水线，并利用该流水线来确定两种重要量子算法——量子近似优化算法（QAOA）与量子相位估计（QPE）——实现算法盈亏平衡（即纠错使量子算法性能得到改善）所需的条件。我们的流水线集成了若干开源软件工具，并利用了误差感知酉门综合、高保真魔法态制备以及关联面计算方面的最新进展。我们对流水线生成的物理 Clifford 代理电路进行了经典模拟，发现 5 量子比特的 QAOA 与 QPE 均可在物理错误率 p = 10−3 时以 2517 个物理量子比特（表面码距离 d = 11）达到算法盈亏平衡，或在 p = 5 × 10−4 时以 1737 个物理量子比特（d = 9）达到。我们的工作由此确定了利用近期量子硬件实现算法盈亏平衡的条件，并为面向早期容错表面码架构的端到端编译器铺平了道路。
