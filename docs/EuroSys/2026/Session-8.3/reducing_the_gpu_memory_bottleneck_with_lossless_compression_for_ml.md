---
title: "Reducing the GPU Memory Bottleneck with Lossless Compression for ML"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · Aditya Kamath (University of Washington), Arvind Krishnamurthy (University of Wa"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# Reducing the GPU Memory Bottleneck with Lossless Compression for ML

**中文标题：** 用无损压缩缓解机器学习中的 GPU 内存瓶颈

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：Aditya Kamath (University of Washington), Arvind Krishnamurthy (University of Washington/Google), Marco Canini (KAUST), Simon Peter (University of Washington)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803595)

## 英文摘要

Machine learning (ML) training and inference often process data sets far exceeding GPU memory capacity, forcing them to rely on PCIe for on-demand tensor transfers, causing critical transfer bottlenecks. Lossy compression has been proposed to relieve bottlenecks but introduces workload-dependent accuracy loss, making it complex or even prohibitive to use in existing ML deployments.

We explore lossless compression as an alternative that avoids this deployment complexity. We identify where lossless compression can be integrated into ML pipelines while minimizing interference with GPU execution. Based on our findings, we introduce Invariant Bit Packing (IBP), a novel lossless compression algorithm designed to minimize data transfer time for ML. IBP identifies and eliminates invariant bits across groups of tensors, improving throughput through GPU-optimized decompression that leverages warp parallelism, low-overhead bit operations, and asynchronous PCIe transfers. We provide easy-to-use APIs, showcasing them by adding IBP support to GNN training, as well as DLRM and LLM inference frameworks. IBP achieves, on average, 74% faster GNN training, 180% faster DLRM embedding lookup, and 25% faster LLM inference.

## 中文摘要

机器学习（ML）训练与推理所处理的数据集往往远超 GPU 内存容量，迫使其依赖 PCIe 按需传输张量，从而造成严重的传输瓶颈。有损压缩已被提出用于缓解瓶颈，但会引入依赖负载的精度损失，使其在现有 ML 部署中使用起来复杂甚至不可行。

我们探索无损压缩作为替代方案，以避免这种部署复杂性。我们确定了无损压缩可集成到 ML 流水线的位置，同时尽量减少对 GPU 执行的干扰。基于这些发现，我们提出不变位打包（Invariant Bit Packing，IBP），一种新型无损压缩算法，旨在最小化 ML 中的数据传输时间。IBP 识别并消除张量组之间的不变位，并通过面向 GPU 优化的解压来提升吞吐，该解压利用了 warp 并行、低开销位操作和异步 PCIe 传输。我们提供了易用的 API，并通过为 GNN 训练以及 DLRM 和 LLM 推理框架添加 IBP 支持来展示其用法。IBP 平均使 GNN 训练提速 74%、DLRM 嵌入查表提速 180%、LLM 推理提速 25%。

**英文关键词：** lossless compression, GPU systems, PCIe bottleneck, data movement, machine learning systems, tensor compression, GNN, DLRM, LLM inference

**中文关键词：** 无损压缩、GPU 系统、PCIe 瓶颈、数据移动、机器学习系统、张量压缩、GNN、DLRM、LLM 推理

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
