Leveraging AI-Inspired Hardware Architecture to Enhance LPN Acceleration in Post-Quantum Cryptography
Authors：
[Yingxue Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5433840407820171398)，[Jiliang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=395738577118476173)

## 中文标题

借鉴 AI 启发硬件架构增强后量子密码中的 LPN 加速

## 英文摘要

Learning Parity with Noise (LPN) has emerged as a promising foundational primitive for constructing advanced post-quantum cryptography (PQC). However, existing LPN accelerators primarily optimize isolated computation while overlooking execution flow and suffering from data transfer bottlenecks. Recent advances in AI accelerators have demonstrated remarkable capabilities attributed to their novel architecture paradigms. Inspired by this insight, this work presents LHPA, the first AI-inspired hardware accelerator for LPN acceleration on FPGAs. LHPA implements a heterogeneous architecture comprising configurable hardware engines, with hierarchical XOR-reduction trees integrated to accelerate large-scale computations. Then, LHPA integrates a coalesced access handler to accommodate multi-transfer and single-bit characteristics, thereby improving data transfer efficiency. Next, LHPA employs a stage-level scheduling strategy to optimize execution flow and establishes a bandwidth-oriented performance model to balance computational parallelism with bandwidth demands. By integrating design principles from AI accelerators with domain-specific optimizations tailored for LPN, LHPA achieves a 52.80× performance gain over the state-of-the-art LPN architecture and delivers 36.69×∼247.35× improvements compared to emerging PQC architectures.

## 中文摘要

带噪声学习奇偶（LPN）问题已成为构造高级后量子密码（PQC）的一种有前景的基础原语。然而，现有 LPN 加速器主要优化孤立计算，忽略了执行流，并受制于数据传输瓶颈。近期 AI 加速器的进展展现了其新颖架构范式所带来的卓越能力。受此启发，本文提出 LHPA，首个在 FPGA 上加速 LPN 的 AI 启发硬件加速器。LHPA 实现了由可配置硬件引擎构成的异构架构，并集成层次化 XOR 归约树以加速大规模计算。随后，LHPA 集成合并访问处理器以适配多传输与单比特特性，从而提升数据传输效率。接着，LHPA 采用阶段级调度策略优化执行流，并建立面向带宽的性能模型，以平衡计算并行度与带宽需求。通过融合 AI 加速器的设计原则与面向 LPN 的领域专用优化，LHPA 相较最先进 LPN 架构取得 52.80 倍的性能提升，相较新兴 PQC 架构提升 36.69∼247.35 倍。

## 英文关键词

Post-Quantum Cryptography (PQC), Learning Parity with Noise (LPN), AI-inspired Hardware Architecture, LPN Acceleration

## 中文关键词

后量子密码（PQC）、带噪声学习奇偶（LPN）、AI 启发硬件架构、LPN 加速
