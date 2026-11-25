---
title: "ScaleDFS: Accelerating Decentralized and Private File Sharing via Scaling Directed Acyclic Graph Processing"
description: "HPDC 2024 · Session 8 — Communication & Storage"
tags:
  - "HPDC2024"
  - "Session 8"
  - "Communication & Storage"
---

# ScaleDFS: Accelerating Decentralized and Private File Sharing via Scaling Directed Acyclic Graph Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 8</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658690)

**作者**：Mansub Song, Lan Anh Nguyen, Sunggon Kim, Hyeonsang Eom, Yongseok Son

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

This paper introduces a novel file system, ScaleDFS, designed to accelerate decentralized file sharing for a private network, leveraging the potential of scaling file management based on directed acyclic graph (DAG) on modern hardware. Specifically, in ScaleDFS, we first design a DAG builder that parallelizes the construction of DAG nodes for a file while preserving critical orders to speed up the uploading process. Second, we introduce a DAG reader that retrieves leaf DAG nodes in parallel without graph traversal assisted by a devised DAG cache to accelerate the downloading process. Finally, we present a DAG remover that rapidly identifies obsolete DAG nodes/data and removes them in parallel to mitigate the garbage collection overhead without compromising consistency. We implement ScaleDFS based on IPFS and demonstrate that ScaleDFS outperforms IPFS by up to 3.7⇥, 1.8⇥, and 12.6⇥ in realistic file, private blockchain, and gateway workloads, respectively.

## 中文摘要

本文提出一种新颖的文件系统 ScaleDFS，旨在为私有网络加速去中心化文件共享，利用在现代硬件上基于有向无环图（DAG）扩展文件管理的潜力。具体而言，在 ScaleDFS 中，我们首先设计 DAG 构建器，它在保持关键顺序的同时并行构建文件的 DAG 节点，以加速上传过程。其次，我们引入 DAG 读取器，借助设计的 DAG 缓存，无需图遍历即可并行取回叶 DAG 节点，以加速下载过程。最后，我们提出 DAG 删除器，快速识别过时的 DAG 节点/数据并并行删除，在不损害一致性的前提下缓解垃圾回收开销。我们基于 IPFS 实现 ScaleDFS，并证明在真实文件、私有区块链与网关负载下，ScaleDFS 相比 IPFS 分别最高快 3.7 倍、1.8 倍与 12.6 倍。

## 英文关键词

Decentralized File System, Merkle-DAG, Private Network

## 中文关键词

去中心化文件系统，Merkle-DAG，私有网络

---

[← 返回 Session 8 — Communication & Storage](index.md)
