---
title: "ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs"
description: "ISCA 2026 · Session 6A · ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs"
tags:
  - "ISCA2026"
  - "Session 6A"
  - "LLM 4"
---

# ENEC: A Lossless AI Model Compression Method Enabling Fast Inference on Ascend NPUs

**中文标题：** ENEC: 面向 Ascend NPU 快速推理的无损 AI 模型压缩方法

**所属 Session：** [Session 6A](index.md) · [ISCA 2026](../index.md)

**作者：** Jinwu Yang, Jiaan Wu, Zedong Liu, Xinyang Ma, Hairui Zhao, Yida Gu, Yuanhong Huang, Xingchen Liu, Wenjing Huang, Zheng Wei, Jing Xing, Yili Ma, Qingyi Zhang, Baoyi An, Zhongzhe Hu, Shaoteng Liu, Xia Zhu, Jiaxun Lu, Guangming Tan, Dingwen Tao

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The rapid scaling of Large Language Models presents significant challenges for their deployment and inference, particularly on resource-constrained specialized AI hardware accelerators such as Huawei’s Ascend NPUs, where weight transfer has become a critical performance bottleneck. While lossless compression can preserve model accuracy and reduce data volume, existing lossless compression algorithms exhibit extremely low throughput when ported to the Ascend NPUs. In this paper, we propose ENEC, a novel lossless compression method specifically customized for AI model weights and optimized for Ascend Neural Processing Units. ENEC adopts a block-based fixed-length encoding scheme and incorporates a series of optimizations: bit-width quantization with hierarchical halving bit-packing, vectorized branch-free integer transformation, and dependency-decoupled intra-segment scan. Experimental results demonstrate that ENEC outperforms existing state-of-the-art NPU compressors in both compression ratio and throughput. Compared to leading GPU solutions, ENEC achieves a 3.43× higher throughput than DietGPU and a 1.12× better compression ratio than nvCOMP. By reducing weight transmission overhead, ENEC significantly improves end-to-end inference performance, achieving up to a 6.3× speedup. On Ascend NPUs, ENEC is the first open-source lossless compression algorithm for model weights that achieves performance comparable to state-of-the-art GPU compressors, offering an effective solution for deploying large-scale AI models.

## 中文摘要

随着大语言模型规模的快速扩张，其部署与推理面临重大挑战，尤其是在华为昇腾 NPU 等资源受限的专用 AI 硬件加速器上，权重传输已成为关键性能瓶颈。尽管无损压缩能够保持模型精度并减少数据量，但现有无损压缩算法移植到昇腾 NPU 时吞吐率极低。本文提出 ENEC，一种专为 AI 模型权重定制并针对昇腾神经网络处理器优化的新型无损压缩方法。ENEC 采用基于块的定长编码方案，并引入一系列优化：带层次化折半位打包的位宽量化、向量化的无分支整数变换，以及依赖解耦的段内扫描。实验结果表明，ENEC 在压缩率与吞吐率上均优于现有最先进的 NPU 压缩器。与领先的 GPU 方案相比，ENEC 的吞吐率比 DietGPU 高 3.43 倍，压缩率比 nvCOMP 好 1.12 倍。通过降低权重传输开销，ENEC 显著提升了端到端推理性能，最高实现 6.3 倍加速。在昇腾 NPU 上，ENEC 是首个达到与最先进 GPU 压缩器相当性能的模型权重开源无损压缩算法，为部署大规模 AI 模型提供了有效方案。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：hpdss-group/ENEC](https://github.com/hpdss-group/ENEC)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2026](../index.md)
