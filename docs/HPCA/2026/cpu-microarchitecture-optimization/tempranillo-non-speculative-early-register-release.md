---
title: "Tempranillo: Non-Speculative Early Register Release"
description: "HPCA 2026 · CPU Microarchitecture Optimization"
tags:
  - "HPCA2026"
  - "CPU Microarchitecture Optimization"
---

# Tempranillo: Non-Speculative Early Register Release

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: CPU Microarchitecture Optimization。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · CPU Microarchitecture Optimization</p>
</div>

**论文链接**：
**作者**：Carlos Escuin Computing Systems Lab, Huawei Technologies Switzerland AG , Paolo Salvatore Galfano Computing Systems Laboratory, Zurich Research Center, Huawei Technologies, Switzerland , Davide Basilio Bartolini Computing Systems Laboratory, Zurich Research Center, Huawei Technologies, Switzerland , Leeor Peled Boole Labs, Tel-Aviv Research Center, Huawei Technologies, Israel , Mehdi Alipour Computing Systems Laboratory, Zurich Research Center, Huawei Technologies, Switzerland
**会议**：HPCA 2026

---

## 中文标题

Tempranillo：非推测式寄存器提前释放

## 英文摘要

Limited by the breakdown of technology scaling, CPU architects are looking for creative solutions to deliver performance improvements while unable to traditionally scale up microarchitectural structures. One promising approach is engineering a microarchitecture that uses resources more efficiently, for example, by recycling them faster to relieve pressure on critical structures and making them look bigger than they are. The physical register file (PRF) is a key structure that faces severe area and power constraints that limit its (and the whole CPU’s) scalability. Based on this observation, previous work proposed solutions to reduce the pressure on the PRF by reducing the time each register remains allocated. In this paper, we corroborate earlier findings that the early release of registers is a promising approach to reduce the occupancy of the PRF and we identify novel tight conditions for safely releasing registers. Based on this analysis, we design Tempranillo: an aggressive, non-speculative microarchitecture to release registers as early as possible without requiring additional recovery mechanisms. Tempranillo delivers up to 3.3% and 11.8% performance improvement over conventional release on single-threaded and a 2-way SMT CPUs, respectively. Additionally, Tempranillo requires modest storage overheads, translating into a performance improvement per KiB of storage of up to 2.6% and 9.3% for single-thread and 2-way SMT, respectively. Our evaluation shows that Tempranillo improves over both the state-of-the-art non-speculative and speculative proposals.

## 中文摘要

受技术缩放失效的限制，CPU 架构师在无法按传统方式扩大微架构结构的同时，正寻求创造性的方案来提升性能。一种有前景的做法是设计能更高效利用资源的微架构，例如通过更快地回收资源来缓解关键结构的压力，使其看起来比实际更大。物理寄存器堆（PRF）是面临严峻面积与功耗约束的关键结构，这些约束限制了它乃至整个 CPU 的可扩展性。基于这一观察，先前工作提出了通过缩短每个寄存器保持分配的时间来缓解 PRF 压力的方案。本文证实了此前的发现，即寄存器提前释放是降低 PRF 占用率的有效途径，并识别出可安全释放寄存器的新紧致条件。基于该分析，我们设计了 Tempranillo：一种激进的非推测式微架构，尽可能早地释放寄存器而无需额外的恢复机制。Tempranillo 在单线程与 2 路 SMT CPU 上分别比传统释放带来最高 3.3% 与 11.8% 的性能提升。此外，Tempranillo 所需的存储开销适中，折算为每 KiB 存储的性能提升在单线程与 2 路 SMT 下分别最高达 2.6% 与 9.3%。我们的评估表明，Tempranillo 优于最先进的非推测式与推测式方案。
