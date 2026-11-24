---
title: "Towards Condensed and Efficient Read-Only File System via Sort-Enhanced Compression"
description: "FAST 2026 · Cloud Technologies I · 第 35–52 页"
tags:
  - "FAST2026"
  - "Cloud Technologies I"
---

# Towards Condensed and Efficient Read-Only File System via Sort-Enhanced Compression

**中文标题**：基于排序增强压缩的紧凑高效只读文件系统

**Session**：Cloud Technologies I · 2026-02-24 09:15–10:35 · Chair：Ming Zhao（Arizona State University）

**作者**：Hao Huang, Yifeng Zhang, Yanqi Pan, Wen Xia, Xiangyu Zou, and Darong Yang, Harbin Institute of Technology, Shenzhen; Jubin Zhong and Hua Liao, Huawei Technologies Co., Ltd

**会议**：FAST 2026 · Santa Clara, CA · 第 35–52 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/huang](https://www.usenix.org/conference/fast26/presentation/huang)

**论文 PDF**：[fast26-huang.pdf](https://www.usenix.org/system/files/fast26-huang.pdf)

---

## 英文摘要

Read-only compressed file systems have become increasingly popular in space-sensitive scenarios, such as IoT and Docker containers. To construct condensed images, they divide the data into blocks (e.g., 1 MB) and compress blocks separately. However, we observe that block-based compression cannot fully utilize the compression benefits due to the *data mixture* problem, while its performance issues hinder practical usage.

We propose RubikFS, a sort-enhanced read-only file system. Our key idea is to solve *data mixture* by sorting and clustering similar data chunks in a file system-favored block granularity. This is achieved by *similarity sorter*, which builds a similarity graph to measure the similarity of data chunks and clusters similar chunks by subgraph partitioning. Moreover, sorting can also group data with the same hotness to minimize read amplification. We then introduce an array of techniques, including *data grouper*, *data chunker*, and *hotness grouper*, to implement condensed and efficient RubikFS. Experiments suggest that, compared to existing read-only compressed file systems, RubikFS increases the compression ratio by up to 42.60% and reduces unnecessary reads by up to 70.70%.

## 中文摘要

只读压缩文件系统在对空间敏感的场景中日益流行，例如物联网（IoT）和 Docker 容器。为构建紧凑的镜像，这类系统将数据划分为块（例如 1 MB），并分别压缩各块。然而，我们观察到，由于数据混杂（data mixture）问题，基于块的压缩无法充分利用压缩收益，同时其性能问题也阻碍了实际应用。

我们提出 RubikFS，一种排序增强的只读文件系统。其核心思想是以文件系统友好的块粒度对相似数据块进行排序和聚类，从而解决数据混杂问题。这通过相似性排序器（similarity sorter）实现：它构建相似性图来衡量数据块的相似度，并通过子图划分对相似块进行聚类。此外，排序还可以将热度相同的数据分组，以最小化读放大。随后，我们引入一系列技术，包括数据分组器（data grouper）、数据分块器（data chunker）和热度分组器（hotness grouper），以实现紧凑高效的 RubikFS。实验表明，与现有的只读压缩文件系统相比，RubikFS 将压缩率最高提升 42.60%，并将不必要的读取最多减少 70.70%。
