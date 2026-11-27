---
title: "Zebra: Efficient Redundant Array of Zoned Namespace SSDs Enabled by Zone Random Write Area (ZRWA)"
description: "HPCA 2025 · Stashing your Winnings"
tags:
  - "HPCA2025"
  - "Stashing your Winnings"
---

# Zebra: Efficient Redundant Array of Zoned Namespace SSDs Enabled by Zone Random Write Area (ZRWA)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stashing your Winnings。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stashing your Winnings</p>
</div>

**论文链接**：
**作者**：Tianyang Jiang (Huawei Technologies), Guangyan Zhang (Tsinghua University), Xiaojian Liao (Beihang University), Yuqi Zhou (China University of Geosciences, Beijing)
**会议**：HPCA 2025

---

## 中文标题

Zebra：借助分区随机写区（ZRWA）实现的高效 ZNS SSD 冗余阵列

## 英文摘要

Zoned Namespace (ZNS) SSDs have emerged as a promising solution for eliminating device-level garbage collection and achieving predictable performance through the zone abstraction, which supports append-only writes. However, integrating ZNS SSDs into RAID configurations presents challenges, particularly concerning partial parity updates (PPUs) due to the no-overwrite property of ZNS SSDs. Existing solutions introduce dedicated metadata zones to manage PPUs, but these zones become performance bottlenecks, especially under high PPU workloads. In this paper, we introduce Zebra, a novel architecture for ZNS RAID that leverages the Zone Random Write Area (ZRWA) feature of modern ZNS SSDs. Our key insight is that the SSD’s write buffer (or ZRWA) in front of each zone is ideal for PPUs that exhibit a repeated sequential overwrite I/O pattern. By ensuring that the parity chunk fits within the ZRWA window, Zebra enables efficient PPUs within the ZRWA. Combined with a set of techniques, Zebra ensures both high performance and reliability. We evaluate Zebra on both large-zone and small-zone ZNS SSDs, two typical ZNS models. Our experiments with micro and application benchmarks show that Zebra improves the throughput by 1.1×-4.2× compared to RAIZN, a state-of-the-art ZNS RAID system.

## 中文摘要

分区命名空间（ZNS）SSD 已成为一种有前景的方案，可通过支持仅追加写的分区抽象消除设备级垃圾回收并实现可预测性能。但将 ZNS SSD 集成到 RAID 配置中面临挑战，尤其是其不可覆盖写特性导致的局部校验更新（PPU）问题。现有方案引入专用元数据分区管理 PPU，但这些分区成为性能瓶颈，尤其在高 PPU 负载下。本文提出 Zebra，一种利用现代 ZNS SSD 的分区随机写区（ZRWA）特性的新型 ZNS RAID 架构。我们的洞见是：分区前的 SSD 写缓冲（即 ZRWA）非常适合呈现重复顺序覆盖 I/O 模式的 PPU。通过确保校验块位于 ZRWA 窗口内，Zebra 可在 ZRWA 内实现高效的 PPU。结合一系列技术，Zebra 兼顾高性能与可靠性。我们在两种典型 ZNS 模型——大分区与小分区 ZNS SSD 上评估了 Zebra。微基准与应用基准实验表明，与最先进的 ZNS RAID 系统 RAIZN 相比，Zebra 将吞吐提升 1.1-4.2 倍。
