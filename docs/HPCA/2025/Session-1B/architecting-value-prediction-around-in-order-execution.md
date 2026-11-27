---
title: "Architecting Value Prediction around In-Order Execution"
description: "HPCA 2025 · Speculating in Vegas"
tags:
  - "HPCA2025"
  - "Speculating in Vegas"
---

# Architecting Value Prediction around In-Order Execution

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Speculating in Vegas。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Speculating in Vegas</p>
</div>

**论文链接**：
**作者**：Ravenel Pierre (Kalray), Arthur Perais (CNRS), Frédéric Pétrot (Grenoble INP), Benoît Dupon de Dinechin (Kalray)
**会议**：HPCA 2025

---

## 中文标题

围绕顺序执行的值预测架构设计

## 英文摘要

In the search for performance, in-order execution cannot expect to prevail as older long latency instructions prevent younger ones from issuing. Although stall-on-use processors allow independent instructions to issue in the shadow of a cache miss, the compiler cannot always find enough independent work to keep pipeline resources busy. In this paper, we study how both value prediction based on address prediction and direct value prediction can be built into an in-order pipeline to unlock significant performance. We further show that the in-order execution property provides advantages in that the pipeline may speculate aggressively without suffering from any recovery penalty. Finally, we combine this data speculation infrastructure with a reworked cache hierarchy that relies on a fast first level cache that can be written speculatively. We show that such an in-order pipeline can reach a performance level that is comparable to an equally – although moderately – wide out-of-order processor, without requiring support for partial out-of-order execution such as out-of-order memory hazard handling or full-fledged register renaming. Overall, we increase the performance of a 32-entry scoreboard, 4-issue in-order processor based on a scaled up Open Hardware Group CVA6 by 38.4% (geomean), achieving 86.7% and 46.3% of the gains brought by comparable out-of-order processors featuring 32/16-entry and 64/32-entry Reorder Buffer and scheduler, respectively.

## 中文摘要

在追求性能的过程中，顺序执行难以胜出，因为较早的长延迟指令会阻止较年轻的指令发射。尽管遇停顿即停（stall-on-use）的处理器允许独立指令在缓存缺失的阴影下发射，但编译器并非总能找到足够的独立工作来让流水线资源保持忙碌。本文研究如何将基于地址预测的值预测与直接值预测同时构建到顺序流水线中，以释放显著的性能。我们进一步表明，顺序执行特性带来优势：流水线可以激进地推测，而不会遭受任何恢复惩罚。最后，我们将这一数据推测基础设施与重新设计的缓存层次结构相结合，后者依赖可被推测写入的快速一级缓存。我们表明，这样的顺序流水线可以达到与同等（尽管适度）宽度的乱序处理器相媲美的性能水平，而无需支持部分乱序执行，例如乱序内存冒险处理或完整的寄存器重命名。总体而言，我们使基于放大的 Open Hardware Group CVA6 的 32 项记分板、4 发射顺序处理器性能提升 38.4%（几何平均），分别达到具有 32/16 项与 64/32 项重排序缓冲与调度器的同等乱序处理器所带来收益的 86.7% 与 46.3%。
