---
title: "EFFACT: A Highly Efficient Full-Stack FHE Acceleration Platform"
description: "HPCA 2025 · The Poker Face of FHE"
tags:
  - "HPCA2025"
  - "The Poker Face of FHE"
---

# EFFACT: A Highly Efficient Full-Stack FHE Acceleration Platform

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Poker Face of FHE。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Poker Face of FHE</p>
</div>

**论文链接**：
**作者**：Yi Huang (Tsinghua University), Xinsheng Gong (Tsinghua University), Xiangyu Kong (Tsinghua University), Dibei Chen (Tsinghua University), Jianfeng Zhu (Tsinghua University), Wenping Zhu (Tsinghua University), Liangwei Li (Tsinghua University), Mingyu Gao (Tsinghua University), Aoyang Zhang (Tsinghua University), Shaojun Wei (Tsinghua University), Leibo Liu (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

EFFACT：一个高效的全栈 FHE 加速平台

## 英文摘要

Fully Homomorphic Encryption (FHE) is a set of powerful cryptographic schemes that allows computation to be performed directly on encrypted data with an unlimited depth. Despite FHE’s promising in privacy-preserving computing, yet in most FHE schemes, ciphertext generally blows up thousands of times compared to the original message, and the massive amount of data load from off-chip memory for bootstrapping and privacy-preserving machine learning applications (such as HELR, ResNet-20), both degrade the performance of FHE-based computation. Several hardware designs have been proposed to address this issue, however, most of them require enormous resources and power. An acceleration platform with easy programmability, high efficiency, and low overhead is a prerequisite for practical application. This paper proposes EFFACT, a highly efficient full-stack FHE acceleration platform with a compiler that provides comprehensive optimizations and vector-friendly hardware. We start by examining the computational overhead across different real-world benchmarks to highlight the potential benefits of reallocating computing resources for efficiency enhancement Then we make a design space exploration to find an optimal SRAM size with high utilization and low cost. On the other hand, EFFACT features a novel optimization named streaming memory access which is proposed to enable high throughput with limited SRAMs. Regarding the software-side optimization, we also propose a circuit-level function unit reuse scheme, to substantially reduce the computing resources without performance degradation. Moreover, we design novel NTT and automorphism units that are suitable for a cost-sensitive and highly efficient architecture, leading to low area. For generality, EFFACT is also equipped with an ISA and a compiler backend that can support several FHE schemes like CKKS, BGV, and BFV. We provide both FPGA and ASIC versions of EFFACT. On account of our full stack design, FPGA-EFFACT outperforms the SOTA FPGA accelerators in gmean by 1.22x. Meanwhile, ASIC-EFFACT shows increased improvements in terms of the performance per chip area and the performance per Watt compared with the SOTA ASIC works.

## 中文摘要

全同态加密（FHE）是一类强大的密码学方案，允许直接在密文上做任意深度的计算。尽管 FHE 在隐私保护计算中前景广阔，但在大多数 FHE 方案中密文相比原始消息通常会膨胀数千倍，而自举与隐私保护机器学习应用（如 HELR、ResNet-20）需要从片外内存加载海量数据，两者都降低了 FHE 计算性能。已有若干硬件设计试图解决该问题，但大多需要巨大的资源与功耗。一个易于编程、高效且低开销的加速平台是走向实际应用的前提。本文提出 EFFACT，一个高效的全栈 FHE 加速平台，配有提供全面优化的编译器和向量友好的硬件。我们先考察不同真实基准的计算开销，以凸显重新分配计算资源提升效率的潜在收益；然后进行设计空间探索，寻找高利用率、低开销的最优 SRAM 容量。EFFACT 还提出名为流式内存访问的新优化，用以在有限 SRAM 下实现高吞吐。在软件侧，我们还提出电路级功能单元复用方案，在不降低性能的前提下大幅减少计算资源。此外，我们设计了适用于成本敏感高效架构的新型 NTT 与自同构单元，面积更小。为保持通用性，EFFACT 还配备 ISA 与编译器后端，支持 CKKS、BGV 和 BFV 等多种 FHE 方案。我们提供 EFFACT 的 FPGA 与 ASIC 两个版本。得益于全栈设计，FPGA-EFFACT 在几何平均上以 1.22 倍优于最先进的 FPGA 加速器；同时，ASIC-EFFACT 在单位芯片面积性能和每瓦性能上相比最先进的 ASIC 工作有更大提升。
