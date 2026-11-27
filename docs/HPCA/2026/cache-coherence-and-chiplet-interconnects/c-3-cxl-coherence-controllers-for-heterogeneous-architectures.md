---
title: "$C^3$ : CXL Coherence Controllers for Heterogeneous Architectures"
description: "HPCA 2026 · Cache Coherence and Chiplet Interconnects"
tags:
  - "HPCA2026"
  - "Cache Coherence and Chiplet Interconnects"
---

# $C^3$ : CXL Coherence Controllers for Heterogeneous Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Cache Coherence and Chiplet Interconnects。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Cache Coherence and Chiplet Interconnects</p>
</div>

**论文链接**：
**作者**：Anatole Lefort Technical University of Munich (TUM) , David Schall Technical University of Munich , Nicolò Carpentieri Technical University of Munich , Julian Pritzi Technical University of Munich , Soham Chakraborty TU Delft , Nicolai Oswald NVIDIA , Pramod Bhatotia TU Munich
**会议**：HPCA 2026

---

## 中文标题

C3：面向异构架构的 CXL 一致性控制器

## 英文摘要

We introduce C3, a systematic methodology for designing Compute Express Link (CXL) coherence controllers, to overcome interoperability challenges that arise from the mismatch of coherence protocols and memory consistency models in heterogeneous CXL-connected systems. Crucially, CXL lacks a unified heterogeneous computing interface, which can lead to unpredictable and inconsistent behavior when multiple heterogeneous devices decide to share cache-coherent CXL memory. C3 acts as a pivotal interface between diverse heterogeneous compute units, bridging the semantic differences without necessitating disruptive changes to existing system architectures. Our approach hinges on two key principles: delegating memory operations across coherence domains and enforcing atomicity at domain boundaries, thereby preserving the native memory consistency model semantics of each unit. We implement C3 as a generic gem5 model and validate its correctness through exhaustive litmus testing. We also show that C3 incurs minimal performance overhead compared to unified native coherence protocols.

## 中文摘要

我们提出 C3，一套用于设计 Compute Express Link（CXL）一致性控制器的系统化方法，以克服在由 CXL 连接的异构系统中，因一致性协议与内存一致性模型不匹配而产生的互操作性挑战。关键在于，CXL 缺少统一的异构计算接口，当多个异构设备决定共享缓存一致的 CXL 内存时，这可能引发不可预测且不一致的行为。C3 充当各类异构计算单元之间的关键接口，在不要求对现有系统架构做颠覆性改动的前提下弥合语义差异。我们的方法基于两条关键原则：跨一致性域委派内存操作，以及在域边界强制原子性，从而保留每个单元原生的内存一致性模型语义。我们将 C3 实现为通用的 gem5 模型，并通过穷举的 litmus 测试验证其正确性。我们还表明，与统一的原生一致性协议相比，C3 的性能开销极小。
