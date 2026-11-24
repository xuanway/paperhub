---
title: "OS2G: A High-Performance DPU Offloading Architecture for GPU-based Deep Learning with Object Storage"
description: "ASPLOS 2025 · Session 2B · OS2G：面向对象存储与 GPU 深度学习的高性能 DPU 卸载架构"
tags:
  - "ASPLOS2025"
  - "Session 2B"
  - "Distributed Computing"
---

# OS2G: A High-Performance DPU Offloading Architecture for GPU-based Deep Learning with Object Storage

**中文标题：** OS2G：面向对象存储与 GPU 深度学习的高性能 DPU 卸载架构

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zhen Jin (Zhejiang University,Alibaba Group), Yiquan Chen (Alibaba Group), Mingxu Liang (Alibaba Group), Yijing Wang (Alibaba Group), Guoju Fang (Alibaba Group), Ao Zhou (Alibaba Group), Keyao Zhang (Zhejiang University), Jiexiong Xu (Zhejiang University), Wenhai Lin (Zhejiang University), Yiquan Lin (Zhejiang University), Shushu Zhao (Alibaba Group), Wenkai Shi (Alibaba Group), Zhenhua He (Alibaba Group), Shishun Cai (Alibaba Group), Wenzhi Chen (Zhejiang University)

**单位：** Zhejiang University,Alibaba Group；Alibaba Group；Zhejiang University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716265) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Object storage is increasingly attractive for deep learning (DL) applications due to its cost-effectiveness and high scalability. However, it exacerbates CPU burdens in DL clusters due to intensive object storage processing and multiple data movements. Data processing unit (DPU) offloading is a promising solution, but naively offloading the existing object storage client leads to severe performance degradation. Besides, only offloading the object storage client still involves redundant data movements, as data must first transfer from the DPU to the host and then from the host to the GPU, which continues to consume valuable host resources. In this paper, we propose OS2G, a high-performance offloading architecture designed to free up valuable CPU resources while providing high-performance storage services for DL applications. The key idea of OS2G is to offload the object storage client to a DPU and enable direct data transfer between the DPU and GPU. Specifically, we design a high-performance OS2G Client running on the DPU, utilizing asynchrony, pre-reading, and concurrency strategies to provide high-performance object storage services. Additionally, we propose the GPUDirect DPU (GDD) technique for OS2G to optimize the data path, allowing direct data transfer between the DPU-accelerated storage system and the GPU computing system, fully bypassing the host. Results demonstrate that compared to S3FS and S3Connector, OS2G reduces the execution time of the ResNet18 model by 34.3% and 50.4%, and also decreases CPU consumption by 61.9% and 57.7%, respectively.

## 中文摘要

由于成本效益高且可扩展性强，对象存储对深度学习（DL）应用越来越有吸引力。然而，密集的对象存储处理与多次数据移动加剧了 DL 集群中的 CPU 负担。数据处理单元（DPU）卸载是一种有前景的方案，但简单地卸载现有的对象存储客户端会导致严重的性能下降。此外，仅卸载对象存储客户端仍会引入冗余的数据移动，因为数据必须先从 DPU 传输到主机，再从主机传输到 GPU，这持续消耗着宝贵的主机资源。本文提出 OS2G，一种高性能卸载架构，旨在释放宝贵的 CPU 资源，同时为 DL 应用提供高性能存储服务。OS2G 的核心思想是将对象存储客户端卸载到 DPU，并实现 DPU 与 GPU 之间的直接数据传输。具体而言，我们设计了一个运行在 DPU 上的高性能 OS2G Client，利用异步、预读与并发策略来提供高性能的对象存储服务。此外，我们为 OS2G 提出了 GPUDirect DPU（GDD）技术以优化数据路径，允许在 DPU 加速的存储系统与 GPU 计算系统之间直接传输数据，完全绕过主机。结果表明，与 S3FS 和 S3Connector 相比，OS2G 将 ResNet18 模型的执行时间分别减少了 34.3% 和 50.4%，并将 CPU 消耗分别降低了 61.9% 和 57.7%。

## 英文关键词

DPU Offloading, Direct Data Transfer, GPU, Object Storage, Deep Learning

## 中文关键词

DPU 卸载；直接数据传输；GPU；对象存储；深度学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716265)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2025](../index.md)
