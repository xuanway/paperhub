---
title: "CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM"
description: "ISCA 2026 · Session 4A · CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM"
tags:
  - "ISCA2026"
  - "Session 4A"
  - "LLM 2"
---

# CHIME: A Case for Efficient Long-Context Attention-FC Disaggregated Inference with DIMM-PIM

**中文标题：** CHIME: 基于 DIMM-PIM 的高效长上下文注意力-FC 解耦推理

**所属 Session：** [Session 4A](index.md) · [ISCA 2026](../index.md)

**作者：** Qingyuan Liu, Liyan Chen, Haocheng Wang, Yanning Yang, Dong Du, Zhigang Mao, Naifeng Jing, Yubin Xia, Haibo Chen

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Attention-FC Disaggregated (AFD) LLM inference systems offload memory-bound Attention operations to memory-rich accelerators (e.g., CPUs, HBM-PIM) while retaining compute-bound Fully-Connected (FC) operations on GPUs. In this paper, we first design a Disaggregated Roofline Model (DRM) to characterize AFD performance, revealing that system throughput is constrained by the accelerator’s limiting factor: either memory bandwidth or capacity. We observe that prior AFD systems often overlook these constraints and fail to balance them, leading to resource underutilization or constrained throughput. Therefore, we propose CHIME, the first AFD system integrating DIMM-PIM, which is a case of the new accelerator that strikes the balance with scalable capacity and bandwidth. To address the synchronization challenges inherent to the distributed cooperating DRAM chips in DIMM-PIM, CHIME employs bubble-free pipelining and hybrid-grained re-layout for efficient attention computation. Furthermore, it maximizes cross-device resource utilization via rankset-granular communication-computation overlapping and alignment-predicting scheduling. Evaluations show CHIME achieves up to 5.15× speedup over state-of-the-art HBM-PIM solutions.

## 中文摘要

本文面向长上下文大语言模型推理中的注意力—全连接（AFD）解耦执行：将受内存约束的 Attention 卸载到内存容量丰富的加速器，并在 GPU 上执行计算密集的 FC。作者提出解耦 Roofline 模型，指出系统吞吐量受加速器内存带宽或容量瓶颈制约，并据此设计首个集成 DIMM-PIM 的 AFD 系统 CHIME。为提高注意力计算及跨设备协作效率，CHIME 采用无气泡流水线、混合粒度重布局、rankset 粒度的通信—计算重叠和对齐预测调度。评测显示，相较先进的 HBM-PIM 方案，CHIME 最高实现 5.15× 加速。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4A](index.md) · [返回 ISCA 2026](../index.md)
