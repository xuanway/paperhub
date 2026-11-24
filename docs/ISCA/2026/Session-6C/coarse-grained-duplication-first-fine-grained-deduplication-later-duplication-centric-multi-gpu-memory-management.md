---
title: "Coarse-Grained Duplication First, Fine-Grained Deduplication Later: Duplication-Centric Multi-GPU Memory Management"
description: "ISCA 2026 · Session 6C · Coarse-Grained Duplication First, Fine-Grained Deduplication Later: Duplication-Centric Multi-GPU Memory Management"
tags:
  - "ISCA2026"
  - "Session 6C"
  - "GPUs and Compilation"
---

# Coarse-Grained Duplication First, Fine-Grained Deduplication Later: Duplication-Centric Multi-GPU Memory Management

**中文标题：** 先粗粒度复制，后细粒度去重：以复制为中心的多 GPU 内存管理

**所属 Session：** [Session 6C](index.md) · [ISCA 2026](../index.md)

**作者：** Xiangyue Huang, Yanan Guo, Yuanchao Xu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Multi-GPU systems have become popular to meet the growing demands for high parallelism and large memory capacity via unified virtual memory (UVM). However, performance is often constrained by non-uniform memory access (NUMA) overheads due to frequent data sharing across GPUs. Prior work adopts fine-grained page migration and duplication to reduce remote access overheads, but our characterization of recent NVLinks shows that such designs fail to fully exploit their capabilities. In particular, nonlinear latency–size scaling, negligible contention, and abundant bandwidth favor coarse-grained transfers. While coarse-grained approaches better utilize NVLink bandwidth, they can introduce excessive remote accesses and update overheads. We propose CDFD, a duplication-centric mechanism that combines coarse-grained duplication to maximize bandwidth utilization with selective fine-grained deduplication to mitigate unnecessary remote updates. By leveraging idle GPU memory capacity and dynamically refining duplication decisions, CDFD balances performance and overhead. Experimental results show that CDFD achieves average performance improvements of 66% and 65% over state-of-the-art methods GPS and GRIT, respectively.

## 中文摘要

多 GPU 系统通过统一虚拟内存（UVM）满足日益增长的高并行度和大内存容量需求，因而日益流行。然而，由于 GPU 间频繁的数据共享，性能常受限于非统一内存访问（NUMA）开销。先前工作采用细粒度页迁移与复制来降低远程访问开销，但我们对近期 NVLink 的表征显示，这类设计未能充分利用其能力。具体而言，非线性的延迟-大小缩放关系、可忽略的争用以及充裕的带宽都有利于粗粒度传输。虽然粗粒度方法能更好地利用 NVLink 带宽，但会引入过多的远程访问与更新开销。我们提出 CDFD，一种以复制为中心的机制，将最大化带宽利用率的粗粒度复制与减少不必要远程更新的选择性细粒度去重相结合。通过利用空闲的 GPU 内存容量并动态细化复制决策，CDFD 在性能与开销之间取得平衡。实验结果表明，CDFD 相比最先进方法 GPS 和 GRIT 分别实现平均 66% 和 65% 的性能提升。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2026](../index.md)
