---
title: "Hey Hey, My My, Skewness Is Here to Stay: Challenges and Opportunities in Cloud Block Store Traffic"
description: "EuroSys 2025 · Virtualization · Haonan Wu (Shanghai Jiao Tong University), Erci Xu (Shanghai Jiao Tong Universit"
tags:
  - "EuroSys2025"
  - "Virtualization"
---

# Hey Hey, My My, Skewness Is Here to Stay: Challenges and Opportunities in Cloud Block Store Traffic

**中文标题：** 偏斜依然存在：云块存储流量的挑战与机遇

**所属 Session：** [Session 5.2: Virtualization](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Virtualization</p>
</div>

**作者**：Haonan Wu (Shanghai Jiao Tong University), Erci Xu (Shanghai Jiao Tong University), Ligang Wang (Alibaba Group), Yuandong Hong (Alibaba Group), Changsheng Niu (Alibaba Group), Bo Shi (Alibaba Group), Lingjun Zhu (Alibaba Group), Jinnian He (Alibaba Group), Dong Wu (Alibaba Group), Weidong Zhang (Alibaba Group), Qiuping Wang (Alibaba Group), Changhong Wang (Alibaba Group), Xinqi Chen (Alibaba Group), Guangtao Xue (Shanghai Jiao Tong University), Yi-Chao Chen (Shanghai Jiao Tong University), Dian Ding (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696068)

## 英文摘要

Elastic Block Storage (EBS) has a pivotal role in modern data center infrastructure, providing reliable, high-performance and flexible block storage service to users. In Alibaba Cloud, EBS is the most widely used service and has been supporting the operation of millions of virtual disks. However, even with layers of load balancing and caching, we still observe significant traffic skewness across the EBS stack. This motivates us to comprehensively investigate symptoms and root causes behind the traffic patterns and, more importantly, explore the fixes for the identified issues.

In this paper, we collect 310 million IO traces from approximately 60k virtual machines and 140k virtual disks deployed in our EBS. Based on extensive statistical analysis, we examine the traffic skewness across multiple components of the EBS stack. We identify four typical symptoms related to the IO virtualization framework, traffic throttle, storage cluster management and cache. For each symptom, we further explore the potential solutions along with the challenges.

## 中文摘要

弹性块存储（EBS）在现代数据中心基础设施中发挥着关键作用，为用户提供可靠、高性能且灵活的块存储服务。在阿里云，EBS 是使用最广泛的服务，支撑着数百万块虚拟磁盘的运行。然而，即使有多层负载均衡和缓存，我们仍观察到整个 EBS 栈中存在显著的流量偏斜。这促使我们全面研究流量模式背后的症状与根因，更重要的是，探索针对所发现问题的修复方案。

本文从部署于我们 EBS 中的约 6 万台虚拟机和 14 万块虚拟磁盘收集了 3.1 亿条 IO trace。基于大量的统计分析，我们考察了 EBS 栈中多个组件上的流量偏斜情况。我们识别出四类典型症状，分别涉及 IO 虚拟化框架、流量限速、存储集群管理和缓存。针对每种症状，我们进一步探讨了潜在的解决方案及其面临的挑战。

**英文关键词：** Compute-Storage Disaggregation, Elastic Block Storage, Load Balancing, Cache

**中文关键词：** 计算存储解耦、弹性块存储、负载均衡、缓存

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
