---
title: "SkySync: Accelerating File Synchronization with Collaborative Delta Generation"
description: "FAST 2026 · Cloud Technologies II · 第 461–476 页"
tags:
  - "FAST2026"
  - "Cloud Technologies II"
---

# SkySync: Accelerating File Synchronization with Collaborative Delta Generation

**中文标题**：SkySync：通过协同增量生成加速文件同步

**Session**：Cloud Technologies II · 2026-02-26 09:00–10:20 · Chair：Uday Kiran Jonnala（Dell Technologies）

**作者**：Zhihao Zhang, Xiamen University and Alibaba Cloud; Huiba Li, Alibaba Cloud; Lu Tang, Xiamen University; Guangtao Xue, Shanghai Jiao Tong University; Jiwu Shu, Tsinghua University; Yiming Zhang, Shanghai Jiao Tong University and Xiamen University

**会议**：FAST 2026 · Santa Clara, CA · 第 461–476 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zhang-zhihao](https://www.usenix.org/conference/fast26/presentation/zhang-zhihao)

**论文 PDF**：[fast26-zhang-zhihao.pdf](https://www.usenix.org/system/files/fast26-zhang-zhihao.pdf)

---

## 英文摘要

File synchronization (sync) is of increasing significance for not only intra-cloud but also inter-cloud applications and services, as cloud computing is evolving into the Sky computing paradigm with the illusion of utility computing on an infrastructure of multiple geographically-distributed clouds. However, existing file sync schemes, mainly including fixed-sized chunking (FSC) based sync and content-defined-chunking (CDC) based sync, heavily rely on complex algorithms for generating the delta data. These algorithms perform costly processing operations including (i) file chunking, (ii) chunk checksum computation, and (iii) chunk searching, which incur high computational overhead thus lowering sync performance. This paper presents SkySync, a novel file sync scheme based on collaborative delta generation. Our insight is that the conventional storage layer has already maintained rich metadata (like checksums and cryptographic digests) for management purpose, e.g., to verify integrity and detect errors. Therefore, we leverage the existent metadata of the storage layer to obtain the chunk checksums with simple adaptation and combination, thus effectively reducing the computational overhead. We further streamline the chunk searching process by reusing checksum data produced during prior computations. We have implemented the FSC-based and CDC-based SkySync schemes by enhancing the communication protocol of the state-of-the-art rsync and dsync, respectively. Evaluation results show that compared to the existing file sync schemes (rsync and dsync), SkySync significantly reduces the computational overhead by up to 89.3% and improves the client and server sync performance by 1.1× ∼2×, while maintaining a consistent level of network traffic.

## 中文摘要

随着云计算正演变为 Sky 计算范式——在由多个地理分布式云组成的基础设施上提供如公用计算般的体验，文件同步（sync）不仅对云内应用和服务，而且对跨云应用和服务都日益重要。然而，现有文件同步方案（主要包括基于固定大小分块（FSC）的同步和基于内容定义分块（CDC）的同步）严重依赖复杂算法来生成增量数据。这些算法执行代价高昂的处理操作，包括 (i) 文件分块、(ii) 块校验和计算和 (iii) 块搜索，从而带来高计算开销并降低同步性能。本文提出 SkySync，一种基于协同增量生成的新型文件同步方案。我们的洞见是：传统存储层已经为管理目的（例如验证完整性和检测错误）维护了丰富的元数据（如校验和与密码学摘要）。因此，我们利用存储层已有的元数据，通过简单的适配和组合获得块校验和，从而有效降低计算开销。我们进一步通过复用先前计算中产生的校验和数据来简化块搜索过程。我们分别通过增强最先进 rsync 和 dsync 的通信协议，实现了基于 FSC 和基于 CDC 的 SkySync 方案。评估结果表明，与现有文件同步方案（rsync 和 dsync）相比，SkySync 将计算开销最多降低 89.3%，并将客户端和服务器同步性能提升 1.1–2 倍，同时保持一致的网络流量水平。
