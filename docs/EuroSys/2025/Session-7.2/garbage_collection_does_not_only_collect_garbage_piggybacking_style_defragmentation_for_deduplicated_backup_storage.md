---
title: "Garbage Collection Does Not Only Collect Garbage: Piggybacking-Style Defragmentation for Deduplicated Backup Storage"
description: "EuroSys 2025 · Storage · Dingbang Liu (Harbin Institute of Technology, Shenzhen), Xiangyu Zou (Harbin Ins"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Garbage Collection Does Not Only Collect Garbage: Piggybacking-Style Defragmentation for Deduplicated Backup Storage

**中文标题：** 垃圾回收不只是回收垃圾：面向去重备份存储的搭载式碎片整理

**所属 Session：** [Session 7.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Dingbang Liu (Harbin Institute of Technology, Shenzhen), Xiangyu Zou (Harbin Institute of Technology, Shenzhen), Tao Lu (DapuStor), Philip Shilane (Dell Technologies), Wen Xia (Harbin Institute of Technology, Shenzhen), Wenxuan Huang (Harbin Institute of Technology, Shenzhen), Yanqi Pan (Harbin Institute of Technology, Shenzhen), Hao Huang (Harbin Institute of Technology, Shenzhen)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717493)

## 英文摘要

Deduplication is widely used in backup storage and reduces storage overhead by allowing backups to share common data chunks. However, it naturally disrupts the sequential layout of backup images, leading to fragmentation, which slows down backup restoration. Existing solutions to this issue often come with trade-offs, either reducing deduplication effectiveness or introducing significant I/O overhead.

In this paper, we propose GCCDF, a novel approach that enhances the efficiency of deduplication-based backup storage. It reorders data as part of garbage collection to eliminate fragmentation, avoiding additional I/O costs. During the reordering, it effectively groups related data for better locality and aligns with the storage layout in backup storage. Evaluation results demonstrate that GCCDF significantly improves restoration speed, offsets data migration overhead, and preserves the deduplication ratio.

## 中文摘要

去重被广泛用于备份存储，通过让备份共享公共数据块来降低存储开销。然而，它天然地破坏了备份镜像的顺序布局，导致碎片化，从而拖慢备份恢复速度。针对该问题的现有方案往往需要权衡，要么降低去重效果，要么引入显著的 I/O 开销。

本文提出 GCCDF，一种提升基于去重的备份存储效率的新方法。它在垃圾回收过程中重排数据以消除碎片化，从而避免额外的 I/O 开销。在重排过程中，它有效地将相关数据分组以获得更好的局部性，并与备份存储的存储布局对齐。评估结果表明，GCCDF 显著提升了恢复速度，抵消了数据迁移开销，并保持了去重率。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
