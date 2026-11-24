---
title: "Deft: A Scalable Tree Index for Disaggregated Memory"
description: "EuroSys 2025 · Memory Tiering and Disaggregation · Jing Wang (Tsinghua University), Qing Wang (Tsinghua University), Yuhao Zhang (T"
tags:
  - "EuroSys2025"
  - "Memory Tiering and Disaggregation"
---

# Deft: A Scalable Tree Index for Disaggregated Memory

**中文标题：** 面向解耦内存的可扩展树索引

**所属 Session：** [Session 6.2: Memory Tiering and Disaggregation](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Memory Tiering and Disaggregation。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Memory Tiering and Disaggregation</p>
</div>

**作者**：Jing Wang (Tsinghua University), Qing Wang (Tsinghua University), Yuhao Zhang (Tsinghua University), Jiwu Shu (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696062)

## 英文摘要

Memory disaggregation has become an inexorable trend in data centers and the cloud. By physically separating compute and memory resources into independent pools and connecting them with high-speed networks, memory disaggregation enables high resource utilization and elastic resource scaling. However, traditional tree-based indexes become inefficient on disaggregated memory: (1) large tree nodes can easily saturate network bandwidth due to I/O amplification, yet small tree nodes increase network round trips; (2) expensive concurrency control schemes restrict the scalability.

We present Deft, a tree-based index for disaggregated memory that delivers high throughput and scalability. Deft 1) introduces segmented internal nodes and hash-based leaf nodes for fine-grained access patterns to achieve low I/O amplification without increasing the index height; 2) proposes a scalable write-write concurrency control scheme on top of the tailored node structure with a one-sided shared-exclusive lock, improving scalability for concurrent update and insert operations; 3) proposes a lightweight and correct read-write concurrency control scheme, improving scalability for efficient lock-free search operations. Our experimental results demonstrate that Deft achieves high performance and scalability on disaggregated memory, and outperforms state-of-the-art ordered indexes by 2.4-9.5× under various workloads.

## 中文摘要

内存解耦已成为数据中心和云中不可阻挡的趋势。通过将计算与内存资源在物理上分离为独立的资源池并以高速网络互连，内存解耦实现了高资源利用率和弹性资源伸缩。然而，传统的树形索引在解耦内存上变得效率低下：（1）大的树节点会因 I/O 放大而轻易占满网络带宽，而小的树节点又会增加网络往返次数；（2）开销高昂的并发控制方案限制了可扩展性。

我们提出 Deft，一种面向解耦内存的树形索引，可提供高吞吐与高可扩展性。Deft 1）引入分段内部节点和基于哈希的叶节点，以细粒度的访问模式实现低 I/O 放大，且不增加索引高度；2）在定制的节点结构之上提出一种可扩展的写-写并发控制方案，采用单边共享-独占锁，提升并发更新与插入操作的可扩展性；3）提出一种轻量且正确的读-写并发控制方案，提升高效无锁查找操作的可扩展性。实验结果表明，Deft 在解耦内存上实现了高性能与高可扩展性，在多种负载下比最先进的有序索引快 2.4–9.5 倍。

**英文关键词：** Disaggregated Memory, Index, RDMA

**中文关键词：** 解耦内存、索引、RDMA

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
