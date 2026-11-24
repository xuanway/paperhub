---
title: "Cloudscape: A Study of Storage Services in Modern Cloud Architectures"
description: "FAST 2025 · Cloud Storage · 把 396 个 AWS 架构访谈视频标注成可查询数据集，量化云上存储服务的真实用法"
tags:
  - "FAST2025"
  - "Cloud Storage"
  - "cloud architecture"
  - "storage services"
---

# Cloudscape: A Study of Storage Services in Modern Cloud Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">云上系统如何选存储、如何组合存储，长期只有零散案例而缺少可查询的大规模证据。Cloudscape 把 AWS 官方 396 个架构视频标注成含数据流的有向图数据集，发现 S3 出现在 68% 的系统、分布式文件系统仅 4%，约一半架构同时使用两种以上存储服务。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Cloud Storage</p>
</div>

**中文标题**：Cloudscape：现代云架构中的存储服务研究

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/satija](https://www.usenix.org/conference/fast25/presentation/satija)

**论文 PDF**：[fast25-satija.pdf](https://www.usenix.org/system/files/fast25-satija.pdf)

**作者**：Sambhav Satija、Chenhao Ye、Ranjitha Kosgi、Aditya Jain、Romit Kankaria、Yiwei Chen、Andrea C. Arpaci-Dusseau、Remzi H. Arpaci-Dusseau（University of Wisconsin–Madison）；Kiran Srinivasan（NetApp）

**会议**：FAST 2025 · Santa Clara, CA · 第 103–121 页

**Session**：Cloud Storage · 2025-02-25 14:00–15:20 · Chair：Ming Zhao（Arizona State University）

**所属 Session**：[Cloud Storage](index.md) · [FAST 2025](../index.md)

**关键词**：cloud architecture, storage services, object storage, dataset, AWS, serverless

---

## 英文摘要

We present Cloudscape, a dataset of nearly 400 cloud architectures deployed on AWS. We perform an in-depth analysis of the usage of storage services in cloud systems. Our findings include: S3 is the most prevalent storage service (68%), while file system services are rare (4%); heterogeneity is common in the storage layer; storage services primarily interface with Lambda and EC2, while also serving as the foundation for more specialized ML and analytics services. Our findings provide a concrete understanding of how storage services are deployed in real-world cloud architectures, and our analysis of the popularity of different services grounds existing research.

## 中文摘要

本文发布 Cloudscape——一个包含近 400 个部署在 AWS 上的云架构的数据集，并对云系统中存储服务的使用进行了深入分析。研究发现包括：S3 是最普遍的存储服务（68%），文件系统服务则很少（4%）；存储层普遍存在异构；存储服务主要与 Lambda 和 EC2 对接，同时也为更专用的机器学习与分析服务提供基础。这些发现给出了存储服务在真实云架构中如何部署的具体认识，而本文对不同服务流行度的分析也为已有研究提供了依据。

## 一句话总结

> 云上存储的真实分布不是文件系统而是对象存储：S3 覆盖 68% 的系统，约一半架构把数据摊在两种以上服务里。

## 研究背景与问题

- 云已是主流部署平台，2023 年云计算基础设施投资约占全球 IT 基础设施支出的 60%，但除 Snowflake 等少数知名系统外，人们对云上系统整体如何搭建几乎一无所知。
- 选哪种存储服务是架构的关键决策，但从业者缺少可借鉴的集体经验汇总，存储研究者也不知道该把精力放在哪里才能放大影响。
- 已有的真实系统研究要么看单机集群的资源画像，要么看私有云内部系统（如 GFS、f4、Haystack），缺少从公有云用户视角考察存储服务如何被组合、如何被其他服务调用的工作。

## 核心贡献

- 构建 Cloudscape：396 个部署在 AWS 上的架构，每个编码为含节点、数据边/元边与工作流的有向图，并附文本注记与数据类型定性标注（176 个架构）。
- 给出可复现的标注方法：3 名成员先在 50 个架构上迭代定规范，再培训 3 名成员扩到全量，最终 340 个（85.9%）架构可用于定量分析，其余因交互描述含糊被排除。
- 围绕三个研究问题给出存储服务画像：架构功能目标是否影响选型、存储与其他服务如何交互且存了什么数据、专用 ML 与分析服务如何使用存储层。
- 公开数据集与分析脚本，并据此提出研究对象存储工作负载、跨服务一致性与 ML/分析服务同对象存储协同设计的具体建议。

## 方法与技术要点

- 数据来源：AWS 维护的架构访谈视频播放列表，取 2024 年前发布、覆盖 2019 年 3 月至 2023 年 12 月共 5 年、11 种语言、平均约 6 分钟的视频，每个视频描述一家公司中某个团队的架构。
- 结构化标注：节点表示服务（含用户与公司内部平台），数据边表示用户数据流动、元边表示请求触发或应答；工作流是同步的调用与数据移动序列，边带序号以还原顺序。
- 口述优先原则：讲解与白板所画不一致时以口述为准；遇到 SQS 等异步消息总线会拆出新工作流，把异步语义显式化。
- 定性与校验：为存储服务内的数据类型打标，用于回答定量统计看不到的问题；并用 StackOverflow 数据集的 AWS 标签分布交叉验证结论。

## 评估与主要结果

- 规模与偏差：数据集含 396 个架构，分析用 340 个（85.9%）；来源仅限 AWS，作者明确承认存在选择偏差，但没有找到规模相当的其他云厂商数据源。
- 存储选型：S3 出现在 68% 的系统；40% 用键值存储（如 DynamoDB）、30% 用 SQL 数据库（如 RDS）；分布式文件系统（如 Elastic File System）很少，仅 4%；约一半架构同时使用两种以上存储服务。
- 计算耦合与数据类型：存储服务主要对接 Lambda 与 EC2；serverless 计算出现在约 60% 的架构中，近 20% 的系统只用 serverless。
- 交叉验证：在 StackOverflow 数据集的 AWS 标签统计中 S3、EC2、Lambda 同样最普遍，与 Cloudscape 的服务热度结论一致。

## 代码与研究制品

- [代码仓库](https://github.com/WiscADSL/Cloudscape)

[返回 Cloud Storage](index.md) · [返回 FAST 2025](../index.md)
