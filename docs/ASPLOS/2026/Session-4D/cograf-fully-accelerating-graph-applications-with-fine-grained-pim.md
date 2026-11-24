---
title: "CoGraf: Fully Accelerating Graph Applications with Fine-Grained PIM"
description: "ASPLOS 2026 · Session 4D · CoGraf：以细粒度 PIM 全面加速图应用"
tags:
  - "ASPLOS2026"
  - "Session 4D"
  - "Processing-in-Memory"
---

# CoGraf: Fully Accelerating Graph Applications with Fine-Grained PIM

**中文标题：** CoGraf：以细粒度 PIM 全面加速图应用

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Mehmetali Semi Yenimol (Uppsala University), Anirban Nag (Huawei), Chang Hyun Park (Uppsala University), David Black-Schaffer (Uppsala University)

**单位：** Uppsala University；Huawei

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790142) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Processing-in-Memory (PIM) delivers enormous performance by taking advantage of internal DRAM bandwidth and parallelism. However, graph applications are difficult to adapt to PIM due to their irregular access patterns. We present the first Fine-Grained PIM (FGPIM) design that fully accelerates vertex-centric push-based graph applications by accelerating both their update (computing vertex updates) and apply (summing up the updates) phases. For the update phase, we design a tuple-based LLC that can coalesce at different granularities to group graph updates together and propose multi-DRAM column processing FGPIM instructions to match the cache coalescing to the row-level parallelism of the FGPIM. With this acceleration, the apply phase becomes the bottleneck, and we propose bank-parallel FGPIM instructions with predicates to allow FGPIM to accelerate the conditional updates as well. We achieve an average speedup in the region of interest of 1.8×/3× compared to naive FGPIM and 4.4×/9.8× compared to state-of-the-art non-PIM baseline (HBM2/DDR4), and DRAM energy reduction of 67%/86% and 88%/94%. These results show the importance of providing a complete solution that accelerates both the update and apply phases.

## 中文摘要

存内处理（Processing-in-Memory, PIM）通过利用 DRAM 内部带宽与并行性带来巨大的性能提升。然而，图应用因其不规则的访存模式而难以适配 PIM。我们提出首个细粒度 PIM（Fine-Grained PIM, FGPIM）设计，通过同时加速以顶点为中心的 push 型图应用的 update（计算顶点更新）与 apply（汇总更新）两个阶段，实现对这类应用的全面加速。针对 update 阶段，我们设计了一种基于元组（tuple）的 LLC，它能够以不同粒度进行合并（coalesce），从而将图更新聚合在一起；并提出多 DRAM 列处理的 FGPIM 指令，使缓存合并与 FGPIM 的行级并行性相匹配。在这一加速下，apply 阶段成为瓶颈，因此我们提出带谓词的 bank 并行 FGPIM 指令，使 FGPIM 也能加速条件更新。在感兴趣区间内，相比朴素 FGPIM 我们取得平均 1.8×/3× 的加速，相比最先进的非 PIM 基线（HBM2/DDR4）取得 4.4×/9.8× 的加速，并实现 67%/86% 与 88%/94% 的 DRAM 能耗降低。这些结果表明，提供同时加速 update 与 apply 两个阶段的完整解决方案至关重要。

## 英文关键词

Processing-In-Memory (PIM), Graph Processing, Irregular Memory, Cache Coalescing

## 中文关键词

存内处理（PIM）；图处理；不规则访存；缓存合并

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790142)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2026](../index.md)
