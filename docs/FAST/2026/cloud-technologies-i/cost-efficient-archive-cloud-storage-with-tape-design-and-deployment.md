---
title: "Cost-efficient Archive Cloud Storage with Tape: Design and Deployment"
description: "FAST 2026 · Cloud Technologies I · 第 19–34 页"
tags:
  - "FAST2026"
  - "Cloud Technologies I"
---

# Cost-efficient Archive Cloud Storage with Tape: Design and Deployment

**中文标题**：基于磁带的高性价比归档云存储：设计与部署

**Session**：Cloud Technologies I · 2026-02-24 09:15–10:35 · Chair：Ming Zhao（Arizona State University）

**作者**：Qing Wang, Tsinghua University; Fan Yang, Qiang Liu, and Geng Xiao, Huawei Cloud; Yongpeng Chen and Hao Lan, Tsinghua University; Leiming Chen, Bangzhu Chen, Chenrui Liu, Pingchang Bai, Bin Huang, Zigan Luo, Mingyu Xie, and Yu Wang, Huawei Cloud; Youyou Lu, Tsinghua University; Huatao Wu, Huawei Cloud; Jiwu Shu, Tsinghua University and Minjiang University

**会议**：FAST 2026 · Santa Clara, CA · 第 19–34 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/wang](https://www.usenix.org/conference/fast26/presentation/wang)

**论文 PDF**：[fast26-wang.pdf](https://www.usenix.org/system/files/fast26-wang.pdf)

---

## 英文摘要

TapeOBS is an archive storage service offered by Huawei Cloud, which delivers high cost-efficiency by leveraging tape to store large volumes of archived data. Although tape boasts a low total cost of ownership, its inherent characteristics (e.g., a limited number of drives within a tape library) pose unique challenges when developing a large-scale distributed storage system. To address these challenges, we take a holistic approach in designing TapeOBS. At the high level, we introduce a fully asynchronous tape pool, which supports data scheduling and erasure coding in a batched manner, aligning with the features of tape hardware. Within a tape library, we design a tape-tailored local storage engine and incorporate techniques such as dedicated drives to optimize performance. TapeOBS began its gradual rollout at the end of 2022 and officially started serving customers in 2024. As of this writing, TapeOBS has stored hundreds of petabytes of raw user data.

## 中文摘要

TapeOBS 是华为云提供的一项归档存储服务，它利用磁带存储海量归档数据，从而实现高成本效益。尽管磁带具有较低的总拥有成本（TCO），但其固有特性（例如单个磁带库中驱动器数量有限）在构建大规模分布式存储系统时带来了独特挑战。为应对这些挑战，我们在设计 TapeOBS 时采取了整体性方法。在高层，我们引入全异步磁带池，以批处理方式支持数据调度和纠删编码，从而与磁带硬件的特性相匹配。在磁带库内部，我们设计了面向磁带定制的本地存储引擎，并采用专用驱动器等技术来优化性能。TapeOBS 于 2022 年底开始逐步上线，并于 2024 年正式为客户提供服务。截至本文撰写时，TapeOBS 已存储数百 PB 的原始用户数据。
