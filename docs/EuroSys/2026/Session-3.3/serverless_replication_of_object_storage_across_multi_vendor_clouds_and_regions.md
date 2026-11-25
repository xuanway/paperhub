---
title: "Serverless Replication of Object Storage across Multi-Vendor Clouds and Regions"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Junyi Shu (School of Computer Science, Peking University and UCLA), Xiaolong Hua"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# Serverless Replication of Object Storage across Multi-Vendor Clouds and Regions

**中文标题：** 跨多云厂商与多区域的对象存储无服务器复制

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Junyi Shu (School of Computer Science, Peking University and UCLA), Xiaolong Huang (School of Computer Science, Peking University), Gang Huang (School of Computer Science, Peking University), Hong Mei (School of Computer Science, Peking University), Xuanzhe Liu (School of Computer Science, Peking University), Xin Jin (School of Computer Science, Peking University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769367)

## 英文摘要

Cross-cloud data replication is vital for improving reliability and performance. Since cloud providers lack native support, users turn to open-source solutions that rely on VMs. However, these are slow to provision, leading to high replication delays and costs. We propose a serverless approach for data replication using cloud functions, which cut provisioning overhead from tens of seconds to just a few. While functions offer sufficient bandwidth, they suffer from performance asymmetry across clouds and variability among instances. Our system, 𝜆Replica, mitigates this uncertainty through proactive planning and adaptive runtime adjustments. Prior to replication, 𝜆Replica formulates an SLO-compliant plan. During runtime, it employs decentralized scheduling to manage slow instances and uses changelog propagation and batching to further reduce costs. Implemented on three major clouds, 𝜆Replica outperforms existing solutions by reducing replication delay by 61%-99% with cost savings of up to three orders of magnitude. On production traces, it keeps p99.99 replication delay below 10 seconds.

## 中文摘要

跨云数据复制对提升可靠性与性能至关重要。由于云厂商缺乏原生支持，用户转而使用依赖虚拟机的开源方案。然而这类方案配置缓慢，导致复制延迟高、成本高昂。我们提出一种使用云函数进行数据复制的无服务器方法，将配置开销从数十秒缩短至仅数秒。尽管云函数可提供足够的带宽，但它们在不同云之间存在性能不对称，且实例之间存在性能波动。我们的系统 𝜆Replica 通过主动规划与运行时自适应调整来缓解这种不确定性。在复制开始之前，𝜆Replica 制定符合 SLO 的计划；在运行过程中，它采用去中心化调度来应对慢实例，并利用变更日志传播与批处理进一步降低成本。𝜆Replica 在三大主流云上实现，相比现有方案将复制延迟降低 61%–99%，成本节省最多可达三个数量级。在生产负载轨迹上，它可将 p99.99 复制延迟保持在 10 秒以内。

**英文关键词：** Cloud Computing, Serverless Computing, Data Replication, Object Storage

**中文关键词：** 云计算、无服务器计算、数据复制、对象存储

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
