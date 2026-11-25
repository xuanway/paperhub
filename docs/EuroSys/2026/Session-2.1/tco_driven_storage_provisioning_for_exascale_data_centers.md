---
title: "TCO-driven Storage Provisioning for Exascale Data Centers"
description: "EuroSys 2026 · File Systems & Storage · Timothy Kim (Carnegie Mellon University), Saurabh Kadekodi (Google), Arif Mercha"
tags:
  - "EuroSys2026"
  - "File Systems & Storage"
---

# TCO-driven Storage Provisioning for Exascale Data Centers

**中文标题：** TCO驱动的百亿亿级数据中心存储配置

**所属 Session：** [Session 2.1: File Systems & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：File Systems & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · File Systems & Storage</p>
</div>

**作者**：Timothy Kim (Carnegie Mellon University), Saurabh Kadekodi (Google), Arif Merchant (Google), Prashant Nema (Microsoft), Jai Menon (Microsoft), Rashmi Vinayak (Carnegie Mellon University), Gregory R. Ganger (Carnegie Mellon University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803599)

## 英文摘要

Recent changes in data temperatures and storage device characteristics, both mechanical disk-drives (HDDs) and solid-state drives (SSDs), expand the set of deployment options for exascale storage. Until recently, exascale storage systems followed a pattern of placing most data on HDDs with smaller amounts of SSD storage used for caching and performance-critical workloads. Exascale storage provisioning and dataset placement trade-offs have now changed.

This paper describes a total cost of ownership (TCO) model that captures primary aspects of modern deployments and uses it to explore the new trade-off space. Using capacity and performance telemetry information for 43 production datasets+workloads at two large hyperscalers, we show significant changes from prior analyses of workloads and storage placement decisions across a multitude of storage device types. We also introduce a storage cluster TCO optimizer that identifies the lowest-TCO grouping and assignment of datasets to device types, exposing a number of insights that can help guide future deployments. For example, our analysis shows that the highest-density SSDs are particularly favorable for clusters with heavy AI/ML workloads but are only cost-effective at exascale when combined with high-density HDDs. Finally, we use our framework to evaluate how storage provisioning and overall TCO change as a function of key parameters like device write amplification, cluster power bounds, and the maximum number of device types allowed.

## 中文摘要

近期数据温度与存储设备特性的变化——无论是机械硬盘（HDD）还是固态盘（SSD）——扩大了百亿亿级存储的部署选项集合。直到不久前，百亿亿级存储系统仍遵循一种模式：将大部分数据放在HDD上，用较少的SSD用于缓存和性能关键型工作负载。如今，百亿亿级存储的配置与数据集放置权衡已经发生变化。

本文描述了一个总拥有成本（TCO）模型，它刻画了现代部署的主要方面，并利用该模型探索新的权衡空间。基于两家大型超大规模云服务商共43个生产数据集与工作负载的容量和性能遥测信息，我们展示了与既有工作负载分析以及跨多种存储设备类型的放置决策相比的显著变化。我们还提出了一个存储集群TCO优化器，它能够找出TCO最低的数据集分组与设备类型分配方案，并揭示了一系列有助于指导未来部署的洞见。例如，我们的分析表明，最高密度的SSD对承载繁重AI/ML工作负载的集群尤为有利，但只有在与高密度HDD结合时，其在百亿亿级规模下才具有成本效益。最后，我们使用该框架评估存储配置与整体TCO如何随设备写入放大、集群功耗上限以及允许的设备类型最大数量等关键参数而变化。

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
