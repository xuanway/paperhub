---
title: "ECC Enabled Reliable and Performant Processing-in-Memory"
description: "ISCA 2026 · Session 2B · ECC Enabled Reliable and Performant Processing-in-Memory"
tags:
  - "ISCA2026"
  - "Session 2B"
  - "Memory Systems and PIM/PNM"
---

# ECC Enabled Reliable and Performant Processing-in-Memory

**中文标题：** ECC 赋能的可靠高性能存内处理

**所属 Session：** [Session 2B](index.md) · [ISCA 2026](../index.md)

**作者：** Jeageun Jung, Margaret Lee, Mattan Erez

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

We introduce a Processing-in-Memory (PIM) architecture with tailored error checking and correcting (ECC) mechanisms to address reliability challenges from scaling errors and physical faults. PIMs can significantly improve computing efficiency by integrating computing devices directly within memory chips, but their reliability has not been explored in detail. It is important to ensure reliability against variable retention time (VRT) scaling errors and multi-bit errors in modern DRAM. Our proposed reliable bank-PIM architecture not only accurately detects multi-bit errors and corrects at the rank-level but also avoids the high performance impact of repetitive rank-level corrections. We develop a Codeword Flip method that is specifically designed to mask errors caused by VRT weak cells. This strategy effectively reduces the risk of silent data corruption (SDC) and has a negligible performance impact. With an odd-even bank pipelining approach, which achieves PIM unit utilization of 90%, our ECC mechanism could decrease the likelihood of SDC to 400× lower than traditional bank-PIM configuration over a five-year operational period. Moreover, it shows the potential 4× performance enhancement over rank-PIM in certain micro-benchmarks and end-to-end performance improvements in LLM applications.

## 中文摘要

我们提出了一种采用定制化纠错码（ECC）机制的存内处理（PIM）架构，以应对因规模缩放误差和物理故障带来的可靠性挑战。PIM通过将计算器件直接集成在内存芯片内部来显著提升计算效率，但其可靠性尚未被详细探索。确保针对现代DRAM中可变保持时间（VRT）缩放误差和多比特错误的可靠性至关重要。我们提出的可靠bank级PIM架构不仅能准确检测多比特错误并在rank级进行纠错，还能避免重复rank级纠错带来的高性能影响。我们开发了一种专门用于屏蔽VRT弱单元导致的错误的码字翻转方法。该策略有效降低了静默数据损坏（SDC）的风险，且性能影响可忽略不计。通过一种奇偶bank流水线方法实现了90%的PIM单元利用率，我们的ECC机制在五年运行周期内可将SDC概率降至传统bank-PIM配置的1/400。此外，在某些微基准测试和LLM应用的端到端性能中，它展现出相比rank-PIM高达4倍的性能提升潜力。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 2B](index.md) · [返回 ISCA 2026](../index.md)
