---
title: "Reviving In-Storage Hardware Compression on ZNS SSDs through Host-SSD Collaboration"
description: "HPCA 2025 · Stashing your Winnings"
tags:
  - "HPCA2025"
  - "Stashing your Winnings"
---

# Reviving In-Storage Hardware Compression on ZNS SSDs through Host-SSD Collaboration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stashing your Winnings。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stashing your Winnings</p>
</div>

**论文链接**：
**作者**：Yingjia Wang (The Chinese University of Hong Kong), Tao Lu (DapuStor), Yuhong Liang (The Chinese University of Hong Kong), Xiang Chen (DapuStor), Ming-Chang Yang (The Chinese University of Hong Kong)
**会议**：HPCA 2025

---

## 中文标题

通过主机与 SSD 协同重振 ZNS SSD 上的盘内硬件压缩

## 英文摘要

Zoned Namespace (ZNS) is an emerging SSD interface with great potential for performance and cost in large-scale cloud SSD deployments. Enabling in-storage hardware compression on ZNS SSDs is promising for further enhancing the cost-effectiveness of ZNS-based storage infrastructures. However, based on our investigation, existing solutions based on the host-transparent methodology are sub-optimal on ZNS SSDs due to two intrinsic challenges: (1) locating compressed chunks and (2) harvesting space savings from compression. In this paper, we for the first time revisit the compression storage system architecture on the emerging ZNS SSD and propose to decouple compression execution with indexing. We propose CCZNS (CC: collaborative compression), an advanced ZNS interface that revives in-storage hardware compression on ZNS SSDs through a novel host-SSD collaborative approach. We present how CCZNS can benefit host software by performing a case study on RocksDB and ZenFS. Extensive experiments demonstrate that the CCZNS-based storage system significantly outperforms existing system solutions.

## 中文摘要

分区命名空间（ZNS）是一种新兴的 SSD 接口，在大规模云 SSD 部署中于性能和成本两方面都具有巨大潜力。在 ZNS SSD 上启用盘内硬件压缩，有望进一步提升基于 ZNS 的存储基础设施的成本效益。然而，根据我们的调研结果，基于主机透明方法的现有方案在 ZNS SSD 上并非最优，原因在于两个内在的挑战：(1) 定位已压缩的数据块；(2) 从压缩中回收空间节省。本文首次针对新兴的 ZNS SSD 重新审视压缩存储系统架构，并提出将压缩执行与索引解耦。我们提出 CCZNS（CC：协同压缩），一种先进的 ZNS 接口，它通过一种新颖的主机-SSD 协同方法来重振 ZNS SSD 上的盘内硬件压缩。我们还通过对 RocksDB 与 ZenFS 的案例研究，展示了 CCZNS 如何使主机软件受益。大量实验表明，基于 CCZNS 的存储系统显著优于现有的系统方案。
