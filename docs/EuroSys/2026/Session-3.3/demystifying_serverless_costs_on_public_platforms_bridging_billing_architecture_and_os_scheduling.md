---
title: "Demystifying Serverless Costs on Public Platforms: Bridging Billing, Architecture, and OS Scheduling"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Changyuan Lin (University of British Columbia), Yuanzhi Ma (Johns Hopkins Univer"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# Demystifying Serverless Costs on Public Platforms: Bridging Billing, Architecture, and OS Scheduling

**中文标题：** 揭开公有平台无服务器成本之谜：贯通计费、架构与操作系统调度

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Changyuan Lin (University of British Columbia), Yuanzhi Ma (Johns Hopkins University), Mohammad Shahrad (University of British Columbia)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769374)

## 英文摘要

Public cloud serverless platforms have attracted a large user base due to their high scalability, plug-and-play deployment model, and pay-per-use billing. However, compared to virtual machines and container hosting services, modern serverless offerings typically impose higher per-unit time and resource charges. Additionally, billing practices such as wall-clock time allocation-based billing, invocation fees, and usage rounding up can further increase costs.

This work, for the first time, holistically demystifies these costs by conducting an in-depth, top-down characterization and analysis from user-facing billing models, through request serving architectures, and down to operating system scheduling on major public serverless platforms. We quantify, for the first time, how current billing practices inflate billable resources up to 4.35× beyond actual consumption. Also, our analysis reveals previously unreported cost drivers, such as operational patterns of serving architectures that create overheads, details of resource allocation during keepalive periods, and OS scheduling granularity effects that directly impact both performance and billing. By tracing the sources of costs from billing models down to OS scheduling, we uncover the rationale behind today’s expensive serverless billing model and practices and provide insights for designing performant and cost-effective serverless systems.

## 中文摘要

公有云无服务器平台凭借高可扩展性、即插即用的部署模式和按使用量付费的计费方式，吸引了庞大的用户群体。然而，与虚拟机和容器托管服务相比，现代无服务器服务通常收取更高的单位时间与单位资源费用。此外，按墙上时钟时间分配计费、调用费用以及用量向上取整等计费做法还会进一步推高成本。

本工作首次从面向用户的计费模型出发，经由请求服务架构，直至操作系统调度，在主流公有无服务器平台上开展深入的自顶向下刻画与分析，从而整体性地揭开这些成本之谜。我们首次量化了当前计费做法如何将可计费资源膨胀至实际消耗的4.35倍。此外，我们的分析揭示了以往未被报告的成本驱动因素，例如服务架构的运行模式所造成的开销、保活（keepalive）期间资源分配的细节，以及直接影响性能与计费的OS调度粒度效应。通过从计费模型向下追踪至OS调度的成本来源，我们揭示了当今昂贵无服务器计费模型与做法背后的逻辑，并为设计高性能且高性价比的无服务器系统提供了洞见。

**英文关键词：** Serverless Computing, Cloud Computing, Performance Measurements, Billing Models, OS Scheduling

**中文关键词：** 无服务器计算、云计算、性能测量、计费模型、操作系统调度

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
