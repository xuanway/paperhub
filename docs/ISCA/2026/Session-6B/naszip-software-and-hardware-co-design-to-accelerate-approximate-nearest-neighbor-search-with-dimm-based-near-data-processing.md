---
title: "NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing"
description: "ISCA 2026 · Session 6B · NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing"
tags:
  - "ISCA2026"
  - "Session 6B"
  - "Deep Learning / Memory Acceleration"
---

# NasZip: Software and Hardware Co-Design to Accelerate Approximate Nearest Neighbor Search with DIMM-Based Near-Data Processing

**中文标题：** NasZip: 基于 DIMM 近数据处理加速近似最近邻搜索的软硬件协同设计

**所属 Session：** [Session 6B](index.md) · [ISCA 2026](../index.md)

**作者：** Cheng Zou, Shuo Yang, Chen Nie, Yu Zou, Yu He, Chao Jiang, Limin Xiao, Weifeng Zhang, Zhezhi He

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As large language models (LLMs) continue to advance, retrieval-augmented generation (RAG) has become the key mechanism for expanding model knowledge and reducing hallucinations. Central to RAG is approximate nearest neighbor search (ANNS), which retrieves database vectors most similar to a given query. However, distance calculation over high-dimensional vectors is inherently memory-bound, causing retrieval performance to be constrained by I/O bandwidth on mainstream platforms such as CPUs and GPUs. Although many prior early exiting (EE) techniques attempt to reduce memory accesses by only computing partial dimensions, the partial distance converges too slowly to the EE threshold, which ultimately limits their performance gains. To address these challenges, we propose NASZIP, a hardware-software co-designed framework that integrates near-data processing (NDP) with a novel feature-level early exiting guided by statistics-based principal component analysis (PCA). Instead of relying solely on partial distances, NASZIP incorporates estimation and correction parameters to approximate full-dimensional distances accurately, enabling earlier exiting without compromising accuracy. We further introduce a bit-level NDP-aware dynamic-float scheme that significantly reduces memory access for vector data. On the hardware side, we develop a data-aware neighbor list mapping strategy that reduces neighbor-retrieval latency and inter-channel communication overhead, complemented by a dedicated cache that exploits data locality and enhances prefetch efficiency. With these co-optimized techniques, NASZIP delivers speedups of up to 8.4×/1.4× over CPU baseline and state-of-the-art GPU implementation at equal accuracy. Relative to the state-of-the-art NDP ANNS accelerator ANSMET, NASZIP achieves 1.69× performance improvement.

## 中文摘要

随着大语言模型（LLM）的持续发展，检索增强生成（RAG）已成为扩展模型知识、减少幻觉的关键机制。RAG 的核心是近似最近邻搜索（ANNS），它检索与给定查询最相似的数据库向量。然而，高维向量上的距离计算本质上是内存受限的，导致检索性能在 CPU 和 GPU 等主流平台上受 I/O 带宽制约。尽管许多先前的提前退出（EE）技术试图通过仅计算部分维度来减少内存访问，但部分距离收敛到 EE 阈值过慢，最终限制了其性能收益。为应对这些挑战，我们提出 NASZIP，一个软硬件协同设计的框架，将近数据处理（NDP）与一种由基于统计的主成分分析（PCA）引导的新型特征级提前退出相结合。NASZIP 不单纯依赖部分距离，而是引入估计与校正参数来准确逼近全维距离，从而在不损失精度的情况下实现更早退出。我们进一步提出一种位级 NDP 感知的动态浮点方案，显著减少向量数据的内存访问。在硬件方面，我们开发了数据感知的邻居列表映射策略，降低邻居检索延迟和通道间通信开销，并辅以利用数据局部性、提升预取效率的专用缓存。借助这些协同优化技术，NASZIP 在相同精度下相比 CPU 基线实现最高 8.4 倍加速，相比最先进的 GPU 实现 1.4 倍加速。相对于最先进的 NDP ANNS 加速器 ANSMET，NASZIP 实现 1.69 倍的性能提升。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Intelligent-Computing-Research-Group/NasZip](https://github.com/Intelligent-Computing-Research-Group/NasZip)
- [实验材料归档（Zenodo 19453078）](https://zenodo.org/records/19453078)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2026](../index.md)
