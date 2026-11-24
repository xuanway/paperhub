---
title: "ACOS: Apple’s Geo-Distributed Object Store at Exabyte Scale"
description: "FAST 2026 · Cloud Technologies I · 第 53–66 页"
tags:
  - "FAST2026"
  - "Cloud Technologies I"
---

# ACOS: Apple’s Geo-Distributed Object Store at Exabyte Scale

**中文标题**：ACOS：Apple 的 EB 级地理分布式对象存储

**Session**：Cloud Technologies I · 2026-02-24 09:15–10:35 · Chair：Ming Zhao（Arizona State University）

**作者**：Benjamin Baron, Aline Bousquet, Eric Metens, Swapnil Pimpale, Nick Puz, Marc de Saint Sauveur, Varsha Muzumdar, and Vinay Ari, Apple

**会议**：FAST 2026 · Santa Clara, CA · 第 53–66 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/baron](https://www.usenix.org/conference/fast26/presentation/baron)

**论文 PDF**：[fast26-baron.pdf](https://www.usenix.org/system/files/fast26-baron.pdf)

**说明**：论文标题与摘要已根据 FAST ’26 Errata Slip #1 更新（原标题为 McQueen）。

---

## 英文摘要

Over the last two decades, with the advent of mobile computing and Internet streaming, Apple has expanded its user base and services significantly. With this growth, we have seen an increased volume and diversity of data storage, ranging from backups, personal photos and videos, to music libraries, TV shows, and live streaming. In this paper, we present ACOS, Apple's object store designed to meet the specific requirements of user-facing and internal services, by accommodating a wide range of content and access patterns. ACOS has been in production for over a decade, storing several exabytes of objects and serving billions of requests per day. With its geo-replicated architecture using both local and regional replication mechanisms, ACOS is cost-efficient and highly scalable, available, and durable. The evaluation of our production deployment shows its throughput and latency performance as well as its resilience to hardware and data center failures. This paper presents the design and evolution of ACOS, evaluates its performance in production, and demonstrates its capacity to scale and support Apple's current storage needs and future growth.

## 中文摘要

过去二十年，随着移动计算和互联网流媒体的兴起，Apple 的用户群和服务规模显著扩大。伴随这一增长，数据存储的量与多样性不断增加，涵盖备份、个人照片与视频、音乐库、电视节目以及直播等。本文介绍 ACOS，这是 Apple 的对象存储，旨在通过支持广泛的内容类型和访问模式，满足面向用户的服务与内部服务的特定需求。ACOS 已在生产环境运行十余年，存储了数 EB 的对象，每天处理数十亿次请求。其地理复制架构同时采用本地复制和区域复制机制，因而具备成本效益，并具有高可扩展性、高可用性和高持久性。对我们生产部署的评估展示了其吞吐量和延迟性能，以及在硬件和数据中心故障下的韧性。本文介绍了 ACOS 的设计与演进，评估了其在生产环境中的性能，并说明其能够扩展并支撑 Apple 当前存储需求和未来增长的能力。
