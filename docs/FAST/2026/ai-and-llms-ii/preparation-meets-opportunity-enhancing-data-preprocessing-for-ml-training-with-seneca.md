---
title: "Preparation Meets Opportunity: Enhancing Data Preprocessing for ML Training With Seneca"
description: "FAST 2026 · AI and LLMs II · 第 221–238 页"
tags:
  - "FAST2026"
  - "AI and LLMs II"
---

# Preparation Meets Opportunity: Enhancing Data Preprocessing for ML Training With Seneca

**中文标题**：准备与机遇相遇：利用 Seneca 增强机器学习训练的数据预处理

**Session**：AI and LLMs II · 2026-02-25 10:50–12:30 · Chair：Jian Zhang（The Hong Kong University of Science and Technology）

**作者**：Omkar Desai, Syracuse University; Ziyang Jiao, Huaibei Normal University; Shuyi Pei, Samsung Semiconductor; Janki Bhimani, Florida International University; Bryan S. Kim, Syracuse University

**会议**：FAST 2026 · Santa Clara, CA · 第 221–238 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/desai](https://www.usenix.org/conference/fast26/presentation/desai)

**论文 PDF**：[fast26-desai.pdf](https://www.usenix.org/system/files/fast26-desai.pdf)

---

## 英文摘要

Input data preprocessing is a common bottleneck when concurrently training multimedia machine learning (ML) models in modern systems. To alleviate these bottlenecks and reduce the training time for concurrent jobs, we present Seneca, a data loading system that optimizes cache partitioning and data sampling for the data storage and ingestion (DSI) pipeline. The design of Seneca contains two key techniques. First, Seneca uses a performance model for the data pipeline to optimally partition the cache for three different forms of data (encoded, decoded, and augmented). Second, Seneca opportunistically serves cached data over uncached ones during random batch sampling so that concurrent jobs benefit from each other. We implement Seneca by modifying PyTorch and demonstrate its effectiveness by comparing it against several state-of-the-art caching systems for DNN training. Seneca reduces the makespan by 45.23% compared to PyTorch and increases data processing throughput by up to 3.45× compared to the next best dataloader.

## 中文摘要

在现代系统中并发训练多媒体机器学习（ML）模型时，输入数据预处理是一个常见瓶颈。为缓解这些瓶颈并缩短并发作业的训练时间，我们提出 Seneca，一个针对数据存储与摄取（DSI）流水线优化缓存分区和数据采样的数据加载系统。Seneca 的设计包含两项关键技术。第一，Seneca 使用数据流水线的性能模型，为三种不同形式的数据（编码、解码和增强）最优地划分缓存。第二，Seneca 在随机批次采样期间优先提供已缓存数据而非未缓存数据，使并发作业能够彼此受益。我们通过修改 PyTorch 实现 Seneca，并通过与多个最先进的 DNN 训练缓存系统比较来证明其有效性。与 PyTorch 相比，Seneca 将完工时间（makespan）缩短 45.23%，与次优数据加载器相比，将数据处理吞吐量最多提升 3.45 倍。
