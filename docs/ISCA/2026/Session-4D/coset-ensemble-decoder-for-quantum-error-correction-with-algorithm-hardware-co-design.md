---
title: "Coset Ensemble Decoder for Quantum Error Correction with Algorithm–Hardware Co-Design"
description: "ISCA 2026 · Session 4D · Coset Ensemble Decoder for Quantum Error Correction with Algorithm–Hardware Co-Design"
tags:
  - "ISCA2026"
  - "Session 4D"
  - "Quantum 1"
---

# Coset Ensemble Decoder for Quantum Error Correction with Algorithm–Hardware Co-Design

**中文标题：** 算法-硬件协同设计的量子纠错陪集集成解码器

**所属 Session：** [Session 4D](index.md) · [ISCA 2026](../index.md)

**作者：** Shuang Liang, Jubo Xu, Giulio Bassanino, Qianzhou Wang, Yidong Zhou, Yuncheng Lu, Zhiwen Mo, Paul Kelly, Bo Yuan, Wayne Luk, Hongxiang Fan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Reliable large-scale quantum computation relies on fault-tolerant architectures, where quantum error correction (QEC) continuously extracts and decodes error syndromes in real time. A critical component in QEC is the decoder, a classical subsystem that must simultaneously deliver high logical accuracy and ultra-low latency. This paper presents a novel algorithm– hardware co-design that improves the accuracy–latency trade-off over existing approaches such as vanilla Minimum-Weight Perfect Matching (MWPM) and Union-Find (UF) decoders. At the algorithmic level, we introduce coset ensemble decoding, which improves UF decoding by explicitly exploiting logically equivalent cosets. Our method performs ensemble forest exploration to generate multiple coset-consistent candidates and aggregates them to approximate coset-level maximum-likelihood decoding. We further reduce computational and memory complexity via reverse-order elimination and lossless graph compression, without sacrificing accuracy. At the hardware level, we design a domain-specific architecture that temporally reuses resources, avoiding the code-distance-proportional resource growth in prior spatial architectures. Several optimizations, such as multi-bank memory hashing and hierarchical ID mapping, are proposed to mitigate pipeline stalls and memory conflicts under highly concurrent access patterns. Under a circuit-level depolarizing noise model, our co-design approach achieves a better accuracy–latency trade-off than prior MWPM- and UF-based decoders, while reducing FPGA LUT consumption by up to 8.2 times compared with reported UF-based decoder resources. The tunable candidate number further exposes a flexible design knob, enabling users to tailor decoding performance to the requirements of different fault-tolerant workloads. Our implementation is publicly available at https://github.com/IMSeonL/coset-ensemble-decoder.


## 中文摘要

可靠的大规模量子计算依赖容错架构，其中量子纠错（QEC）实时持续提取并解码错误综合征。解码器是 QEC 中的关键组件，这个经典子系统必须同时提供高逻辑精度和超低延迟。本文提出一种新颖的算法-硬件协同设计，相比现有方法（如朴素最小权重完美匹配（MWPM）和 Union-Find（UF）解码器）改善了精度-延迟权衡。在算法层面，我们引入陪集集成解码（coset ensemble decoding），通过显式利用逻辑等价的陪集来改进 UF 解码。我们的方法执行集成森林探索以生成多个陪集一致的候选，并将它们聚合以近似陪集级最大似然解码。我们进一步通过逆序消除和无损图压缩降低计算与内存复杂度，而不牺牲精度。在硬件层面，我们设计了一种领域专用架构，在时间上复用资源，避免此前空间架构中与码距成比例的资源增长。我们提出多 bank 内存哈希和层次化 ID 映射等多项优化，以缓解高并发访问模式下的流水线停顿和内存冲突。在电路级去极化噪声模型下，我们的协同设计相比此前基于 MWPM 和 UF 的解码器实现了更好的精度-延迟权衡，同时相比已报道的 UF 解码器资源，FPGA LUT 消耗最多减少 8.2 倍。可调的候选数量进一步提供了灵活的设计旋钮，使用户能够针对不同容错工作负载的需求定制解码性能。我们的实现已公开在 https://github.com/IMSeonL/coset-ensemble-decoder。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：ihc-fan-lab/coset-ensemble-decoder](https://github.com/ihc-fan-lab/coset-ensemble-decoder)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4D](index.md) · [返回 ISCA 2026](../index.md)
