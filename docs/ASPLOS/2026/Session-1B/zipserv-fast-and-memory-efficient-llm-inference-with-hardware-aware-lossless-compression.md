---
title: "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression"
description: "ASPLOS 2026 · Session 1B · ZipServ：基于硬件感知无损压缩的快速、内存高效的 LLM 推理"
tags:
  - "ASPLOS2026"
  - "Session 1B"
  - "LLM Serving: Latency & Scheduling"
---

# ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression

**中文标题：** ZipServ：基于硬件感知无损压缩的快速、内存高效的 LLM 推理

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ruibo FAN (Data Science and Analytics Thrust, HKUST(GZ)), Xiangrui YU (Data Science and Analytics Thrust, HKUST(GZ)), Xinglin Pan (Data Science and Analytics Thrust, HKUST(GZ)), Zeyu Li (Data Science and Analytics Thrust, HKUST(GZ)), Weile Luo (Data Science and Analytics Thrust, HKUST(GZ)), QIANG WANG (Harbin Institute of Technology (Shenzhen)), Wei Wang (Hong Kong University of Science and Technology), Xiaowen Chu (Data Science and Analytics Thrust, HKUST(GZ))

**单位：** Data Science and Analytics Thrust, HKUST(GZ)；Harbin Institute of Technology (Shenzhen)；Hong Kong University of Science and Technology

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790250) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Lossless model compression holds tremendous promise for alleviating the memory and bandwidth bottlenecks in bitexact Large Language Model (LLM) serving. However, existing approaches often result in substantial inference slowdowns due to fundamental design mismatches with GPU architectures: at the kernel level, variable-length bitstreams produced by traditional entropy codecs break SIMT parallelism; at the system level, decoupled pipelines lead to redundant memory traffic. We present ZipServ, a lossless compression framework co-designed for efficient LLM inference. ZipServ introduces Tensor-Core-Aware Triple Bitmap Encoding (TCA-TBE), a novel fixed-length format that enables constant-time, parallel decoding, together with a fused decompression-GEMM (ZipGEMM) kernel that decompresses weights on-the-fly directly into Tensor Core registers. This "load-compressed, compute-decompressed" design eliminates intermediate buffers and maximizes compute intensity. Experiments show that ZipServ reduces the model size by up to 30%, achieves up to 2.21× kernel-level speedup over NVIDIA's cuBLAS, and expedites end-to-end inference by an average of 1.22× over vLLM. ZipServ is the first lossless compression system that provides both storage savings and substantial acceleration for LLM inference on GPUs.

## 中文摘要

无损模型压缩在缓解位精确（bit-exact）大型语言模型（LLM）服务中的内存与带宽瓶颈方面具有巨大前景。然而，由于与 GPU 架构的根本性设计错配，现有方法往往导致显著的推理减速：在内核层面，传统熵编码器产生的变长比特流破坏了 SIMT 并行性；在系统层面，解耦的流水线导致冗余的内存流量。我们提出 ZipServ，一个为高效 LLM 推理协同设计的无损压缩框架。ZipServ 引入张量核心感知的三重位图编码（Tensor-Core-Aware Triple Bitmap Encoding, TCA-TBE），一种新颖的定长格式，可实现常数时间的并行解码，并配合融合解压-GEMM（ZipGEMM）内核，将权重即时解压直接送入 Tensor Core 寄存器。这种“加载压缩数据、计算解压数据”的设计消除了中间缓冲区并最大化计算强度。实验表明，ZipServ 将模型大小最多减少 30%，相比 NVIDIA 的 cuBLAS 实现最高 2.21× 的内核级加速，并相比 vLLM 将端到端推理平均加速 1.22×。ZipServ 是首个在 GPU 上为 LLM 推理同时提供存储节省与显著加速的无损压缩系统。

## 英文关键词

LLM Inference, Lossless Compression, GEMM, GPU, Tensor Core

## 中文关键词

LLM 推理；无损压缩；GEMM；GPU；Tensor Core

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790250)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2026](../index.md)
