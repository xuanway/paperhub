Compart: Community-Guided Post-Coarsening for High-Quality Hypergraph Partitioning
Authors：
[Yugao Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7474132413567388679)，[Zhicheng Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1701010475988725104)，[Yuchao Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=03438700010529625741)，[Mengming Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=69110175844035149381)，[Jing Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=97987884326682291051)，[Zhiyao Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=263843)

## 中文标题

ComPart：面向高质量超图划分的社区引导粗化后处理

## 英文摘要

Hypergraph partitioning is a critical step in the design of complex embedded systems, essential for optimizing task mapping on heterogeneous MPSoCs and enabling multi-FPGA prototyping. Many existing methods rely on community detection to identify modules with dense internal and sparse external connections, typically utilizing them to constrain the coarsening phase—a widely adopted paradigm. In this work, we propose ComPart, a generalized framework that integrates diverse community detection methods to uncover high-quality clusterings throughout the post-coarsening stages (i.e., initial partitioning and uncoarsening). These discovered cluster-ings serve as distinct structural guides, enabling the refinement process to identify superior partitioning solutions. Our framework offers two key advantages: (1) it establishes a new paradigm that leverages community structures detected during uncoarsening to escape local optima and explore globally meaningful solution subspaces, transcending the limitations of standard local refinements; and (2) it flexibly accommodates both existing and future community detection methods. Furthermore, we theoretically generalize locally-dense decomposition—originally from graphs—to the hypergraph domain. We provide the formal extension and necessary proofs to apply this technique to hypergraphs, marking its first application in hypergraph partitioning. Specifically, we utilize this rigorously derived decomposition to guide the initial partitioning phase toward superior starting points. Experimental results on standard benchmarks demonstrate that our method consistently outperforms state-of-the-art methods in solution quality.

## 中文摘要

超图划分是复杂嵌入式系统设计中的关键步骤，对于优化异构 MPSoC 上的任务映射、支撑多 FPGA 原型验证至关重要。许多现有方法依赖社区发现来识别内部连接稠密、外部连接稀疏的模块，并通常利用其约束粗化阶段——这是一种被广泛采用的范式。在本工作中，我们提出 ComPart，一个通用框架，集成多种社区发现方法，在粗化后各阶段（即初始划分与解粗化）中挖掘高质量聚类。这些发现的聚类作为不同的结构引导，使精化过程能够识别更优的划分解。我们的框架有两点关键优势：（1）它建立了一种新范式，利用解粗化过程中检测到的社区结构跳出局部最优并探索全局有意义的解子空间，超越标准局部精化的局限；（2）它可灵活容纳现有与未来的社区发现方法。此外，我们从理论上将原用于图的局部稠密分解推广到超图领域，给出了将该技术应用于超图的正式扩展与必要证明，这是该技术在超图划分中的首次应用。具体而言，我们利用这一严格推导的分解引导初始划分阶段走向更优的起点。在标准基准上的实验结果表明，我们的方法在解质量上始终优于现有先进方法。
