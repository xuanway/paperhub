---
title: "Serverless Cold Starts and Where to Find Them"
description: "EuroSys 2025 · Cloud and Serverless Computing · Artjom Joosen (Huawei), Ahmed Hassan (Huawei), Martin Asenov (Huawei), Rajkarn S"
tags:
  - "EuroSys2025"
  - "Cloud and Serverless Computing"
---

# Serverless Cold Starts and Where to Find Them

**中文标题：** 无服务器冷启动及其所在

**所属 Session：** [Session 7.1: Cloud and Serverless Computing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Serverless Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Serverless Computing</p>
</div>

**作者**：Artjom Joosen (Huawei), Ahmed Hassan (Huawei), Martin Asenov (Huawei), Rajkarn Singh (Huawei), Luke Darlow (Huawei), Jianfeng Wang (Huawei), Qiwen Deng (Huawei), Adam Barker (Huawei, University of St Andrews)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696073)

## 英文摘要

This paper analyzes a month-long trace of 85 billion user requests and 11.9 million cold starts from Huawei’s serverless cloud platform. Our analysis spans workloads from five data centers. We focus on cold starts and provide a comprehensive examination of the underlying factors influencing the number and duration of cold starts. These factors include trigger types, request synchronicity, runtime languages, and function resource allocations. We investigate components of cold starts, including pod allocation time, code and dependency deployment time, and scheduling delays, and examine their relationships with runtime languages, trigger types, and resource allocation. We introduce pod utility ratio to measure the pod’s useful lifetime relative to its cold start time, giving a more complete picture of cold starts, and see that some pods with long cold start times have longer useful lifetimes. Our findings reveal the complexity and multifaceted origins of the number, duration, and characteristics of cold starts, driven by differences in trigger types, runtime languages, and function resource allocations. For example, cold starts in Region 1 take up to 7 seconds, dominated by dependency deployment time and scheduling. In Region 2, cold starts take up to 3 seconds and are dominated by pod allocation time. Based on this, we identify opportunities to reduce the number and duration of cold starts using strategies for multi-region scheduling. Finally, we suggest directions for future research to address these challenges and enhance the performance of serverless cloud platforms.

## 中文摘要

本文分析了来自华为无服务器云平台为期一个月、包含 850 亿次用户请求和 1190 万次冷启动的跟踪数据。我们的分析覆盖五个数据中心的工作负载。我们聚焦冷启动，全面考察影响冷启动数量和时长的底层因素。这些因素包括触发类型、请求同步性、运行时语言以及函数资源分配。我们研究了冷启动的各个组成部分，包括 Pod 分配时间、代码与依赖部署时间以及调度延迟，并考察它们与运行时语言、触发类型和资源分配的关系。我们引入 Pod 效用比来衡量 Pod 的有用生命周期相对于其冷启动时间的比例，从而更完整地刻画冷启动，并发现一些冷启动时间较长的 Pod 其有用生命周期也更长。我们的发现揭示了冷启动的数量、时长与特征具有复杂性且成因多元，由触发类型、运行时语言和函数资源分配的差异所驱动。例如，区域 1 的冷启动最长可达 7 秒，主要由依赖部署时间和调度主导；区域 2 的冷启动最长可达 3 秒，主要由 Pod 分配时间主导。基于此，我们识别出利用多区域调度策略来减少冷启动数量和时长的机会。最后，我们提出了未来研究方向，以应对这些挑战并提升无服务器云平台的性能。

**英文关键词：** cloud, serverless, datasets, cold starts, time series

**中文关键词：** 云、无服务器、数据集、冷启动、时间序列

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
