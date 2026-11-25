---
title: "Efficient Data Passing for Serverless Inference Workflows: A GPU-Centric Approach"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Hao Wu (HUST), Yaochen Liu (HUST), Minchen Yu (CUHK-Shenzhen), Qizhen Weng (Tele"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# Efficient Data Passing for Serverless Inference Workflows: A GPU-Centric Approach

**中文标题：** 面向无服务器推理工作流的高效数据传递：一种以 GPU 为中心的方法

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Hao Wu (HUST), Yaochen Liu (HUST), Minchen Yu (CUHK-Shenzhen), Qizhen Weng (TeleAI), Junxiao Deng (HUST), Yue Yu (HUST), Hao Fan (HUST), Song Wu (HUST), Wei Wang (HKUST), Hai Jin (HUST)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769336)

## 英文摘要

Serverless computing offers a compelling paradigm for deploying machine learning inference workflows composed of heterogeneous CPU and GPU functions. However, existing data-passing solutions in serverless systems primarily rely on host memory for data exchange (host-centric), leading to substantial data movement and salient I/O overhead. Moreover, modern GPU communication libraries (e.g., NCCL, NVSHMEM, UCX) are ill-suited to serverless environments, suffering from redundant data copies, underutilized transfer bandwidth, and inefficient temporary GPU storage.

In this paper, we present GRouter, a GPU-centric data plane system designed for serverless inference workflows. GRouter first introduces a unified data passing framework that abstracts host-to-GPU and GPU-to-GPU communication while leveraging function placement to reduce redundant copies. It then aggregates available bandwidth across PCIe links, NVLinks, and NICs to enable parallel transfers with performance isolation between functions. GRouter also implements elastic GPU storage that adapts to idle memory availability and varying data transfer demands. Evaluations on real-world inference services show that GRouter reduces data passing latency by up to 87% and improves throughput by up to 1.74× compared to state-of-the-art GPU communication libraries.

## 中文摘要

无服务器计算为部署由异构 CPU 与 GPU 函数组成的机器学习推理工作流提供了颇具吸引力的范式。然而，现有无服务器系统中的数据传递方案主要依赖主机内存进行数据交换（以主机为中心），导致大量数据移动和显著的 I/O 开销。此外，现代 GPU 通信库（如 NCCL、NVSHMEM、UCX）并不适配无服务器环境，存在冗余数据拷贝、传输带宽利用不足以及临时 GPU 存储效率低下等问题。

本文提出 GRouter，一个面向无服务器推理工作流的以 GPU 为中心的数据面系统。GRouter 首先引入统一的数据传递框架，抽象主机到 GPU 与 GPU 到 GPU 的通信，同时借助函数放置减少冗余拷贝。随后，它聚合 PCIe 链路、NVLink 与网卡上的可用带宽，实现带函数间性能隔离的并行传输。GRouter 还实现了弹性 GPU 存储，可自适应空闲内存可用量与不断变化的数据传输需求。在真实推理服务上的评估表明，与最先进的 GPU 通信库相比，GRouter 将数据传递延迟最多降低 87%，吞吐最多提升 1.74×。

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
