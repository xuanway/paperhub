---
title: "FlacIO: Flat and Collective I/O for Container Image Service"
description: "FAST 2025 · Cloud Storage · 以记录内存状态的运行时镜像替代按磁盘状态组织的容器镜像，冷启动最高快 23 倍"
tags:
  - "FAST2025"
  - "Cloud Storage"
  - "container image"
  - "lazy loading"
---

# FlacIO: Flat and Collective I/O for Container Image Service

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">容器冷启动按磁盘状态拉镜像，网络上全是随机小 I/O，放大最高 3.1 倍。FlacIO 改为按服务记录根文件系统内存状态的运行时镜像，配合宿主内核的运行时页缓存，把装载压成少量小 I/O 加一次大 I/O，冷启动延迟相比全量镜像与懒加载分别缩短至原来的 1/23 与 1/4.6。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Cloud Storage</p>
</div>

**中文标题**：FlacIO：面向容器镜像服务的扁平与集体 I/O

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/liu-yubo](https://www.usenix.org/conference/fast25/presentation/liu-yubo)

**论文 PDF**：[fast25-liu-yubo.pdf](https://www.usenix.org/system/files/fast25-liu-yubo.pdf)

**作者**：Yubo Liu、Hongbo Li、Mingrui Liu、Rui Jing、Jian Guo、Bo Zhang、Hanjun Guo、Yuxin Ren、Ning Jia（Huawei Technologies Co., Ltd.）

**会议**：FAST 2025 · Santa Clara, CA · 第 87–101 页

**Session**：Cloud Storage · 2025-02-25 14:00–15:20 · Chair：Ming Zhao（Arizona State University）

**所属 Session**：[Cloud Storage](index.md) · [FAST 2025](../index.md)

**关键词**：container image, lazy loading, cold startup, runtime image, page cache

---

## 英文摘要

This paper examines the I/O bottlenecks in the container image service. With a comprehensive analysis of existing solutions, we reveal that they suffer from high I/O amplification and excessive network traffic. Furthermore, we identify that the root cause of these problems lies in the storage-oriented and global-oriented container image abstraction. This work proposes a memory-oriented and service-oriented image abstraction, called runtime image, which represents the memory state of the root file system of the container service. The runtime image enables efficient network transfer and fast root file system construction. We design and implement FlacIO, an I/O accelerator based on the runtime image for container image service. FlacIO introduces an efficient runtime image structure that works in conjunction with a runtime page cache on a host node to achieve efficient image service. Our evaluation shows that FlacIO reduces the container cold startup latency by up to 23 and 4.6 times compared to existing full image and lazy loading solutions, respectively. In real-world applications, FlacIO achieves up to 2.25 and 1.7 times performance speedup over other systems in the object storage and machine learning training scenarios, respectively.

## 中文摘要

本文考察容器镜像服务中的 I/O 瓶颈。通过全面分析现有方案，本文发现这些方案存在严重的 I/O 放大与过高的网络流量，并进一步指出问题的根因在于以磁盘状态为中心、以全局为单位组织容器镜像的抽象方式。本文提出一种以内存状态为中心、以服务为单位的镜像抽象——runtime image，它表示容器服务根文件系统的内存状态，使镜像能够被高效地网络传输并快速重建根文件系统。本文设计并实现了 FlacIO——一个基于 runtime image、面向容器镜像服务的 I/O 加速器；它引入高效的 runtime image 结构，并与宿主节点上的运行时页缓存协同工作，以实现高效的镜像服务。评估表明，相比现有的全量镜像与懒加载方案，FlacIO 把容器冷启动延迟分别最高降低 23 倍与 4.6 倍（即缩短至原来的 1/23 与 1/4.6）；在真实应用中，FlacIO 在对象存储与机器学习训练场景下分别相对其他系统取得最高 2.25 倍与 1.7 倍的性能加速。

## 一句话总结

> 容器启动真正要读的内存页是确定的，按服务把这份状态打成扁平镜像，冷启动就从随机小 I/O 变成一次顺序大 I/O。

## 研究背景与问题

- 冷启动要把镜像从 registry 节点拉到宿主节点再启动服务，全量加载的 I/O 放大可达所需数据的数十倍，大镜像的延迟不可接受。
- 懒加载（CRFS、Nydus、DADI）按文件、64KB chunk 或块粒度按需取数，把 Deploy 阶段延迟压低 98% 以上，却把重 I/O 推到执行 entrypoint 的 Ready 阶段，该阶段延迟上涨 9 倍以上，按需加载期间的网络开销可占总开销的 90%。
- 预取只是把 I/O 重放一遍，改变优先级而不减少网络流量；缓存/共享、fork、P2P 等缓解方案要占用宿主 DRAM 与网络，资源紧张时仍有一定比例的容器必须冷启动，多租户下还有安全问题。
- 作者把根因归到 storage-oriented（记录磁盘状态）与 global-oriented（一个镜像服务多个服务）的镜像抽象，导致镜像数据的 I/O 无法被优化。

## 核心贡献

- 提出 runtime image 抽象：用 memory-oriented（记录根文件系统内存状态）与 service-oriented（一服务一镜像）取代按磁盘状态、全局共享组织的镜像。
- 设计 runtime image 结构：从 base 镜像中抽取 I/O trace 命中的数据，去重后放入连续空间，用内置的文件索引与页表寻址。
- 设计 RTPC（Runtime Page Cache）：嵌入 OverlayFS 并叠在 VFS page cache 之上，提供一组新的 OS 原语，容器平台把镜像注入内核后即可挂载根文件系统。
- 把 FlacIO 适配到 CRFS 与 Nydus 两套主流懒加载系统，并保留无 runtime image 时回退懒加载的路径。

## 方法与技术要点

- 镜像生成：启动容器后用基于探针（probe-based）的 I/O tracing 精确采集根文件系统上的 I/O，送到 registry 节点异步生成 runtime image，不阻塞正常服务。
- 扁平化传输：冷启动只用几个小 I/O 取镜像描述、一次大 I/O 取镜像数据，把懒加载阶段几十万个小包换成批量传输，从源头消掉网络放大。
- RTPC 拦截与回落：根文件系统挂载到 RTPC 上，命中由 RTPC 直接处理，未命中重定向到原生 VFS，因此不必为容器重建一条完整 I/O 栈。
- 增量装载：同一 base 镜像派生的多个 runtime image 支持增量加载与注入，只计入不存在的页、跳过重复页，服务数增加时延迟不随镜像增大而增长。
- 兼容与回退：冷启动时检测是否存在对应 runtime image，没有则回退到原有懒加载，保证镜像格式与容器生态兼容。

## 评估与主要结果

- 测试床为宿主与 registry 两台经 TCP/IP 互联的节点，基线为全量镜像与 CRFS、Nydus、DADI(-Trace) 懒加载：冷启动延迟相比全量镜像最高缩短至 1/23、相比懒加载最高缩短至 1/4.6（正文另述 4.7 倍）。
- Pytorch 容器 import torch 冷启动：懒加载方案把 Deploy 阶段缩短 98% 以上但 Ready 阶段延长 9 倍以上，总延迟比全量加载低约 80%；FlacIO 把 Ready 阶段延迟再降 70% 以上。
- 对象存储场景向 Memcached 插入 1 万、10 万、100 万个 2KB 对象：CRFS+FlacIO 与 Nydus+FlacIO 吞吐是其他系统的 2.2 倍与 1.9 倍，100 万对象时分别比 CRFS、Nydus 高 8.6% 与 6.6%。
- Keras 训练 MNIST 的 ML 场景比全量镜像、CRFS、Nydus、DADI 分别快 70.1%、52.1%、53.5%、32%；八节点各扩八个 Postgres 容器的集群扩缩容中，CRFS+FlacIO、Nydus+FlacIO 总耗时分别比 CRFS、Nydus 快 55.1% 与 22.5%。

[返回 Cloud Storage](index.md) · [返回 FAST 2025](../index.md)
