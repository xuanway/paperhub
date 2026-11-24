---
title: "Towards Efficient Flash Caches with Emerging NVMe Flexible Data Placement SSDs"
description: "EuroSys 2025 · Storage · Michael Allison (Samsung Electronics), Arun George (Samsung Electronics), Javier"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Towards Efficient Flash Caches with Emerging NVMe Flexible Data Placement SSDs

**中文标题：** 利用新型 NVMe 灵活数据放置 SSD 实现高效闪存缓存

**所属 Session：** [Session 8.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Michael Allison (Samsung Electronics), Arun George (Samsung Electronics), Javier Gonzalez (Samsung Electronics), Dan Helmick (Samsung Electronics), Vikash Kumar (Samsung Electronics), Roshan R Nair (Samsung Electronics), Vivek Shah (Samsung Electronics)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696091)

## 英文摘要

NVMe Flash-based SSDs are widely deployed in data centers to cache working sets of large-scale web services. As data centers face increasing sustainability demands, such as reduced carbon emissions, efficient management of Flash overprovisioning and endurance has become crucial. Our analysis demonstrates that mixing data with different lifetimes on Flash blocks results in high device garbage collection costs, which either reduce device lifetime or necessitate host overprovisioning. Targeted data placement on Flash to minimize data intermixing and thus device write amplification shows promise for addressing this issue.

The NVMe Flexible Data Placement (FDP) proposal is a newly ratified technical proposal aimed at addressing data placement needs while reducing the software engineering costs associated with past storage interfaces, such as ZNS and Open-Channel SSDs. In this study, we explore the feasibility, benefits, and limitations of leveraging NVMe FDP primitives for data placement on Flash media in CacheLib, a popular open-source Flash cache widely deployed and used in Meta’s software ecosystem as a caching building block. We demonstrate that targeted data placement in CacheLib using NVMe FDP SSDs helps reduce device write amplification, embodied carbon emissions, and power consumption with almost no overhead to other metrics. Using multiple production traces and their configurations from Meta and Twitter, we show that an ideal device write amplification of ~1 can be achieved with FDP, leading to improved SSD utilization and sustainable Flash cache deployments.

## 中文摘要

基于 NVMe 闪存的 SSD 被广泛部署在数据中心，用于缓存大规模 Web 服务的工作集。随着数据中心面临日益增长的可持续性要求（如降低碳排放），高效管理闪存的预留空间和耐久性变得至关重要。我们的分析表明，将生命周期不同的数据混放在闪存块上会导致高昂的设备垃圾回收开销，这要么缩短设备寿命，要么需要主机额外预留空间。在闪存上进行有针对性的数据放置，以最小化数据混杂从而减少设备写放大，为解决该问题展现了前景。

NVMe 灵活数据放置（FDP）提案是一项新近获批的技术提案，旨在满足数据放置需求，同时降低与以往存储接口（如 ZNS 和 Open-Channel SSD）相关的软件工程成本。在本研究中，我们探索在 CacheLib 中利用 NVMe FDP 原语在闪存介质上进行数据放置的可行性、收益与局限。CacheLib 是一个流行的开源闪存缓存，作为缓存构件在 Meta 的软件生态中被广泛部署和使用。我们证明，在 CacheLib 中使用 NVMe FDP SSD 进行有针对性的数据放置有助于降低设备写放大、隐含碳排放和功耗，而几乎不增加其他指标的开销。使用来自 Meta 和 Twitter 的多种生产 trace 及其配置，我们表明借助 FDP 可实现约 1 的理想设备写放大，从而提升 SSD 利用率并实现可持续的闪存缓存部署。

**英文关键词：** Flash, SSD, Storage, Caching, FDP, Data placement, Small objects

**中文关键词：** 闪存、SSD、存储、缓存、FDP、数据放置、小对象

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
