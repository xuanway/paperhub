---
title: "Count2Multiply: Reliable In-Memory High-Radix Counting"
description: "HPCA 2026 · Processing-in-Memory Architectures"
tags:
  - "HPCA2026"
  - "Processing-in-Memory Architectures"
---

# Count2Multiply: Reliable In-Memory High-Radix Counting

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Processing-in-Memory Architectures。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Processing-in-Memory Architectures</p>
</div>

**论文链接**：
**作者**：Joao Paulo Cardoso de Lima TU Dresden, ScaDS.AI , Benjamin F. Morris III Duke University , Asif Ali Khan TU Dresden, Germany , Jeronimo Castrillon TU Dresden, Germany , Alex Jones Syracuse University
**会议**：HPCA 2026

---

## 中文标题

Count2Multiply：可靠的存内高基数计数

## 英文摘要

Computing-in-memory (CIM) has been demonstrated across various memory technologies, from memristive crossbars for analog dot-products to large-scale digital bitwise operations in commodity DRAM and other non-volatile memory technologies. However, current CIM solutions face challenges related to latency and reliability. CIM fidelity lags considerably behind standard memory access fidelity. Furthermore, bulk-bitwise CIM, though highly parallel, requires long latency for multiplication and addition due to bit-serial execution. This paper presents Count2Multiply, a digital CIM framework that performs multiplication, addition, and other operations using high-radix, massively parallel counting enabled by bulk-bitwise in-memory operations. Designed to meet fault tolerance requirements, Count2Multiply integrates traditional row-wise error correction codes, such as Hamming and BCH, to address the high error rates in existing CIM designs. We demonstrate Count2Multiply in commodity DRAMs, achieving on average 1.5× speedup, 4.6× higher energy efficiency (GOPS/Watt), and 4.4× better area efficiency (GOPS/mm²) over NVIDIA A100; and 9.7×, 8.1×, and 12.9× improvements, respectively, over SIMDRAM.

## 中文摘要

存内计算（CIM）已在多种存储技术上得到实现与验证，从用于模拟点积计算的忆阻交叉阵列，到商用 DRAM 及其他非易失性存储技术中的大规模数字位运算。然而，现有 CIM 方案面临时延与可靠性方面的挑战：CIM 的保真度明显落后于标准内存访问的保真度；批量位运算式 CIM 虽高度并行，但由于按位串行执行，乘法与加法等运算需要较长时延。本文提出 Count2Multiply，一个数字 CIM 框架，利用批量位运算式存内操作实现的高基数、大规模并行计数来执行乘法、加法等运算。为满足容错要求，Count2Multiply 集成传统的行向纠错码（如 Hamming 码与 BCH 码），以应对现有 CIM 设计中普遍存在的高错误率。我们在商用 DRAM 上实现了 Count2Multiply，相比 NVIDIA A100 平均取得 1.5 倍加速、4.6 倍更高的能效（GOPS/Watt）和 4.4 倍更好的面积效率（GOPS/mm²）；相比 SIMDRAM 分别提升 9.7 倍、8.1 倍和 12.9 倍。
