---
title: "Themis: Finding Imbalance Failures in Distributed File Systems via a Load Variance Model"
description: "EuroSys 2025 · Distributed Systems · Yuanliang Chen (Tsinghua University), Fuchen Ma (Tsinghua University), Yuanhang "
tags:
  - "EuroSys2025"
  - "Distributed Systems"
---

# Themis: Finding Imbalance Failures in Distributed File Systems via a Load Variance Model

**中文标题：** 通过负载方差模型发现分布式文件系统的不平衡故障

**所属 Session：** [Session 3.1: Distributed Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Distributed Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Distributed Systems</p>
</div>

**作者**：Yuanliang Chen (Tsinghua University), Fuchen Ma (Tsinghua University), Yuanhang Zhou (Tsinghua University), Zhen Yan (Tsinghua University), Qing Liao (Harbin Institute of Technology), Yu Jiang (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696082)

## 英文摘要

A distributed file system (DFS) is a file system that spans across multiple file servers or multiple locations. The load balancing mechanism in a DFS is crucial, as it optimizes resource utilization across all nodes and improves response times. However, incorrect load scheduling or implementation errors in load balancing algorithms can lead to system imbalance, hang-ups, and even crashes. Such imbalance failures may be critical and pose a significant threat to the availability and security of distributed file systems.

This paper presents a detailed study of real-world imbalance failures in four widely used DFSes, exploring their symptoms and triggering conditions. We found that test cases that incorporate both client requests and system configuration inputs are crucial for exposing these imbalances. However, generating such high-quality test cases is challenging due to the extensive combinations of these two input spaces. Guided by our study, we designed a testing framework named Themis. To efficiently prune the search space, Themis first models both the request and configuration inputs and transforms them into operation sequences. It then employs load variance-guided fuzzing to thoroughly explore the operation sequence and constantly generate test cases that make nodes loaded as differently as possible. Finally, Themis introduces a load detector to monitor the resource usage of each distributed node and precisely identify any imbalances. Themis has detected 10 new imbalance failures in four real-world DFSes, which have been addressed by the respective maintainers.

## 中文摘要

分布式文件系统（DFS）是跨越多个文件服务器或多个位置的文件系统。DFS 中的负载均衡机制至关重要，因为它优化所有节点上的资源利用率并改善响应时间。然而，错误的负载调度或负载均衡算法中的实现错误可能导致系统失衡、挂起甚至崩溃。此类失衡故障可能十分严重，对分布式文件系统的可用性和安全性构成重大威胁。

本文对四款广泛使用的 DFS 中真实出现的失衡故障进行了详细研究，探讨了其症状与触发条件。我们发现，同时包含客户端请求和系统配置输入的测试用例对于暴露这些失衡至关重要。然而，由于这两类输入空间的组合极为庞大，生成此类高质量测试用例颇具挑战。在研究结果的指导下，我们设计了名为 Themis 的测试框架。为高效剪枝搜索空间，Themis 首先对请求输入和配置输入建模，并将其转化为操作序列。随后，它采用负载方差引导的模糊测试来充分探索操作序列，并持续生成使各节点负载尽可能不同的测试用例。最后，Themis 引入负载检测器来监控每个分布式节点的资源使用情况，并精确识别任何失衡。Themis 在四个真实 DFS 中检测到 10 个新的失衡故障，这些故障已由各自的维护者修复。

**英文关键词：** Testing, Distributed File System, Load Balance

**中文关键词：** 测试、分布式文件系统、负载均衡

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
