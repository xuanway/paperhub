---
title: "CoFS: A Filesystem for Fast Container Startup"
description: "FAST 2026 · Virtualization · 第 415–424 页"
tags:
  - "FAST2026"
  - "Virtualization"
---

# CoFS: A Filesystem for Fast Container Startup

**中文标题**：CoFS：面向快速容器启动的文件系统

**Session**：Virtualization · 2026-02-25 16:10–17:30 · Chair：Mai Zheng（Iowa State University）

**作者**：Li Wang, Jinxu Du, Yang Yang, Qingbo Wu, Tao Liu, and Haoze Wu, KylinSoft

**会议**：FAST 2026 · Santa Clara, CA · 第 415–424 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/wang-li](https://www.usenix.org/conference/fast26/presentation/wang-li)

**论文 PDF**：[fast26-wang-li.pdf](https://www.usenix.org/system/files/fast26-wang-li.pdf)

---

## 英文摘要

The running of applications in containers has emerged as a popular trend in the industry. The cold start of a container involves a sequential time-consuming process of image downloading and image unpacking. The high cold-start latency significantly prolongs the startup time of containerized applications and could potentially violate responsiveness SLAs in serverless computing or during service automatic scaling to handle burst requests. To accelerate container startup, state-of-the-art systems pull the container image on demand. Unfortunately, they suffer from userspace I/O interposition overhead, maintainability, and/or performance fluctuation.

This paper presents CoFS, a novel filesystem based on extended FUSE for fast container startup. The insight is that the container image is built only once with a fixed read-only filesystem tree from the perspective of containers. This motivates CoFS to construct a minimal perfect hash function (MPHF) at image building time and to store metadata of files in a container image in a dense array indexed by their hash value. MPHF is collision-free and space-optimal. Leveraging the excellent properties of MPHF, CoFS accomplishes lookup request through less than one single I/O operation in most cases (unless the filename is excessively long) from kernel space, effectively avoiding the costly userspace lookup process in FUSE. Furthermore, CoFS constructs another MPHF that enables parallel lookup based on full path hashing, so as to further accelerate the path resolution. For data access, CoFS leverages sparse files provided by the in-kernel host filesystem to implement fine-grained data caching, and accesses cached data from kernel space. The evaluation shows that CoFS outperforms state-of-the-art systems that achieve fast container startup, and compared to fuse-loopback, a FUSE-based loopback filesystem, the lookup performance improves by up to 86%.

## 中文摘要

在容器中运行应用已成为业界的一种流行趋势。容器的冷启动涉及镜像下载和镜像解包这一耗时的串行过程。高冷启动延迟显著延长了容器化应用的启动时间，并可能在无服务器计算或服务自动伸缩以处理突发请求时违反响应性 SLA。为加速容器启动，最先进的系统按需拉取容器镜像。遗憾的是，它们存在用户态 I/O 拦截开销、可维护性和/或性能波动等问题。

本文提出 CoFS，一种基于扩展 FUSE 的新型文件系统，用于快速容器启动。其洞见在于：从容器视角看，容器镜像只构建一次，并具有固定的只读文件系统树。这促使 CoFS 在镜像构建时构造最小完美哈希函数（MPHF），并将容器镜像中文件的元数据存储在一个按其哈希值索引的稠密数组中。MPHF 无冲突且空间最优。借助 MPHF 的优良特性，CoFS 在内核空间大多数情况下通过少于一次 I/O 操作完成查找请求（除非文件名过长），从而有效避免 FUSE 中代价高昂的用户态查找过程。此外，CoFS 构造了另一个 MPHF，支持基于完整路径哈希的并行查找，以进一步加速路径解析。在数据访问方面，CoFS 利用内核宿主文件系统提供的稀疏文件实现细粒度数据缓存，并从内核空间访问缓存数据。评估表明，CoFS 优于实现快速容器启动的最先进系统，并且与基于 FUSE 的回环文件系统 fuse-loopback 相比，查找性能最高提升 86%。
