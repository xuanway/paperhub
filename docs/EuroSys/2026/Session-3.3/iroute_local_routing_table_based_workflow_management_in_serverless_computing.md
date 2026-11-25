---
title: "iRoute: Local Routing Table-based Workflow Management in Serverless Computing"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Yiming Li (Tianjin University), Laiping Zhao (Tianjin University), Zhiyuan Su (I"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# iRoute: Local Routing Table-based Workflow Management in Serverless Computing

**中文标题：** iRoute：无服务器计算中基于本地路由表的工作流管理

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Yiming Li (Tianjin University), Laiping Zhao (Tianjin University), Zhiyuan Su (IEIT SYSTEMS CO., LTD.), Guowei Liu (Tianjin University), Wenhao Huang (Tianjin University), Kang Chen (Tsinghua University), Zhaolin Duan (Tianjin University), Jingjie Zong (Tianjin University), Wenxin Li (Tianjin University), Deze Zeng (China University of Geosciences), Dong Zhang (Inspur (Jinan) Data Technology Co., Ltd), Wenyu Qu (Tianjin University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769318)

## 英文摘要

Serverless computing typically relies on the centralized orchestrator and gateway for function-level and instance-level workflow management. Their intermediary intervention approaches fail to meet the strict microsecond-scale latency requirements of web services. To accelerate workflow execution, prior works have proposed offloading function dependencies to local functions and maintaining connections between frequently invoked instances. However, these methods still suffer from high routing lookup overhead and poor resource efficiency

To address these issues, we propose offloading both orchestrating and routing capabilities from global to local to enable universal 1-hop transfers without compromising resource efficiency. We introduce iRoute, a local routing table-based solution for workflow management. It adopts a dual-layer architecture, where local routing controllers make correct routing decisions while concurrently cooperating with a centralized coordinator to ensure consistency across multiple local routing tables. iRoute can achieve sub-millisecond data transmission latency while maintaining high resource efficiency. Our experimental results demonstrate that iRoute outperforms state-of-the-art systems by up to 27.3× on latency, and improve the throughput by up to 6.7×.

## 中文摘要

无服务器计算通常依赖集中式编排器和网关来进行函数级和实例级的工作流管理。它们的中介干预方式无法满足 Web 服务严格的微秒级延迟要求。为加速工作流执行，先前工作提出将函数依赖卸载到本地函数，并维护频繁调用实例之间的连接。然而，这些方法仍然面临路由查找开销高和资源效率差的问题。

为解决这些问题，我们提出将编排与路由能力从全局卸载到本地，以实现通用的单跳传输，同时不损害资源效率。我们引入 iRoute，一种基于本地路由表的工作流管理方案。它采用双层架构，本地路由控制器做出正确的路由决策，同时与集中式协调器协作，以确保多个本地路由表之间的一致性。iRoute 能够实现亚毫秒级的数据传输延迟，同时保持高资源效率。我们的实验结果表明，iRoute 在延迟上比最先进的系统最高优 27.3×，并将吞吐量提升最多 6.7×。

**英文关键词：** Serverless Computing, Local Routing Table, Data Transfer

**中文关键词：** 无服务器计算、本地路由表、数据传输

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
