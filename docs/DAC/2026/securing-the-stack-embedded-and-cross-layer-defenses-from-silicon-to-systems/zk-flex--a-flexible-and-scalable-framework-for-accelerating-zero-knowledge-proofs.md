ZK-Flex: A Flexible and Scalable Framework for Accelerating Zero-Knowledge Proofs
Authors：
[Adiwena Putra](https://63dac.conference-program.com/?post_type=page&p=15&uid=1716373520848132964)，[Cuong Duong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1490485570800825692)，[Anh Pham](https://63dac.conference-program.com/?post_type=page&p=15&uid=58933911636567531481)，[Joo Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=013143)

## 中文标题

ZK-Flex：一个灵活且可扩展的零知识证明加速框架

## 英文摘要

Zero-knowledge proofs (ZKP) allows a prover to convince a verifier of computational correctness without revealing private data, ensuring both privacy and verifiability. However, proof generation is highly compute-intensive, dominated by polynomial (POLY) and elliptic-curve (EC) operations. These workloads pose two key challenges for hardware acceleration: (1) efficiently supporting diverse large-precision modular multiplications, and (2) maintaining high utilization across workloads that dynamically shift between POLY and EC stages. Existing reconfigurable accelerators address these issues only partially, remaining limited in precision scalability, algorithmic flexibility, and resource efficiency. To overcome these limitations, we propose ZK-Flex, a flexible and scalable software–hardware co-designed framework for accelerating ZKP proof generation. The software layer incorporates POLY and EC optimizers that reduce computation through hardware-and workload-aware algorithmic choices, while the hardware integrates TCore, a Toom–Cook–based multi-precision core with a flexible NoC and a linked-list memory mechanism that improves parallelism under limited memory capacity. Across representative ZKP benchmarks, ZK-Flex achieves 5–11× speedup and up to 3.8× higher area efficiency over the state of the art, establishing a new foundation for high-performance, reconfigurable ZKP acceleration.

## 中文摘要

零知识证明（ZKP）使证明者能够在不泄露私有数据的前提下向验证者证明计算的正确性，从而同时保证隐私性与可验证性。然而，证明生成高度计算密集，主要由多项式（POLY）和椭圆曲线（EC）运算主导。这些工作负载给硬件加速带来两个关键挑战：(1) 高效支持多种大精度模乘；(2) 在 POLY 与 EC 阶段之间动态切换的工作负载中保持高利用率。现有可重构加速器只能部分解决这些问题，在精度可扩展性、算法灵活性和资源效率方面仍受限。为克服上述局限，我们提出 ZK-Flex，一个灵活且可扩展的软硬件协同设计框架，用于加速 ZKP 证明生成。软件层引入了 POLY 和 EC 优化器，通过硬件感知与工作负载感知的算法选择减少计算量；硬件层集成了 TCore——一个基于 Toom–Cook 的多精度核心，并配有灵活的 NoC 和链表式存储机制，可在有限存储容量下提升并行度。在代表性 ZKP 基准测试中，ZK-Flex 相比现有最优工作实现了 5–11 倍加速和最高 3.8 倍的面积效率提升，为高性能、可重构的 ZKP 加速奠定了新的基础。

## 英文关键词

Zero-Knowledge Proof, Hardware Accelerator, Reconfigurable Architecture

## 中文关键词

零知识证明、硬件加速器、可重构架构
