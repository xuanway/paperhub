ATTINA: Spatial Acceleration of Additive Number Theoretic Transform for Energy-Efficient zkSNARKs at the Edge
Authors：
[Yanze Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=92905309856896317131)，[Devin Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=92278277716991856011)，[Md Tanvir Arafin](https://63dac.conference-program.com/?post_type=page&p=15&uid=321843)

## 中文标题

ATTINA：面向边缘能效 zkSNARK 的加性数论变换空间加速

## 英文摘要

Modern zero-knowledge proof (ZKP) schemes are moving from costly elliptic curve-based systems towards algebraic proof systems. This transition is ushering in a new era of broad adoption of hardware-friendly ZKPs, implementable even on resource-constrained edge devices. Algebraic structures, such as towers of binary fields, are core components of such schemes, and they require hardware and algorithmic innovation to realize advanced ZKPs, such as Binius and Binius-FRI, efficiently. Hence, this paper introduces the ATTINA framework, a high-throughput additive number theoretic transform (ANTT) accelerator operating over extended binary fields. ANTT is the most computationally intensive task for realizing Binius. ATTINA partitions ANTT tasks into multiple subtasks and strategically allocates them to processing elements (PEs) and hardware programmable logic (PL) kernels in an interleaved computing pattern. ATTINA features a scalable architecture that enables dynamic parameter changes for different cryptographic applications. To understand its applicability, this paper implements ATTINA on an edge-deployable heterogeneous Versal adaptive system-on-chip (ASoC) platform. ATTINA on Versal ASoC maintains a throughput of 10 Gb/s. ATTINA outperforms a benchmark CPU implementation of ANTT on a high-end processor (i9-14900K) by 139× and a PE-only implementation by 38× in terms of latency while operating at ≤5W for a 4096-point ANTT. ATTINA’s code is published at https://github.com/SPIRE-GMU/binius-spire for evaluation and reproducible research.

## 中文摘要

现代零知识证明（ZKP）方案正从代价高昂的基于椭圆曲线的系统转向代数证明系统。这一转变正开启硬件友好型 ZKP 广泛落地的新时代，使其甚至可在资源受限的边缘设备上实现。诸如二进制域塔之类的代数结构是此类方案的核心组成部分，要高效实现 Binius、Binius-FRI 等先进 ZKP，需要在硬件与算法层面进行创新。因此，本文提出 ATTINA 框架，一个在扩域二进制域上运行的高吞吐加性数论变换（ANTT）加速器。ANTT 是实现 Binius 时计算最密集的任务。ATTINA 将 ANTT 任务划分为多个子任务，并以交错计算模式将其策略性地分配到处理单元（PE）与硬件可编程逻辑（PL）内核上。ATTINA 具有可扩展架构，可针对不同密码应用动态改变参数。为考察其适用性，本文在可部署于边缘的异构 Versal 自适应片上系统（ASoC）平台上实现了 ATTINA。Versal ASoC 上的 ATTINA 保持 10 Gb/s 的吞吐率。对于 4096 点 ANTT，ATTINA 的延迟分别比高端处理器（i9-14900K）上的基准 CPU 实现低 139 倍、比仅用 PE 的实现低 38 倍，同时功耗不超过 5W。ATTINA 的代码已发布于 https://github.com/SPIRE-GMU/binius-spire，以供评估与可复现研究。

## 英文关键词

Binius, Additive Number Theoretic Transform, Coarse-grained reconfigurable architecture (CGRA), Heterogeneous Architecture

## 中文关键词

Binius、加性数论变换、粗粒度可重构架构（CGRA）、异构架构
