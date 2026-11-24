---
title: "Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization"
description: "ISCA 2026 · Session 3A · Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization"
tags:
  - "ISCA2026"
  - "Session 3A"
  - "ML Accelerators 1"
---

# Omni-LUT: Energy-Efficient LUT-based Accelerator with Hardware-Aware KV Cache Quantization

**中文标题：** Omni-LUT: 具备硬件感知 KV 缓存量化的高能效 LUT 加速器

**所属 Session：** [Session 3A](index.md) · [ISCA 2026](../index.md)

**作者：** Cheng-Han Tsai, Kuan-Chen Chou, Yu-Hsin Wang, Chieh-Dun Wen, Tsung Tai Yeh

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Large language model (LLM) inference incurs substantial computation and energy consumption. Lookup-table (LUT)-based general matrix multiplication (GEMM) accelerators reduce this burden by replacing costly multiplications with table lookups. However, existing designs only support activation-weight GEMM (AW-GEMM) in LLM linear layers, while LUT execution for activation-activation GEMM (AA-GEMM) in attention has not been realized. As AA-GEMM is a major contributor to the computation and energy costs of LLM inference in long-context scenarios, supporting both GEMM types–not just AW-GEMM–is crucial. To solve this problem, we propose Omni-LUT, a hardware-software co-designed LUT-based GEMM accelerator that supports both AW-GEMM in linear layers and AA-GEMM in attention with efficient LUT execution. Omni-LUT uses a hardware-aware Key-Value (KV) cache quantization design that combines offline calibration with lightweight online quantization, preserving model accuracy while enabling compatibility with LUT-based GEMM accelerators. It also supports a more accurate quantization direction by leveraging quantization compensation during LUT creation. Omni-LUT further comprises a phase-adaptive hybrid-stationary LUT-based systolic array to improve the efficiency of both the prefill and decode phases in LLMs. Across diverse long context workloads, Omni-LUT achieves 1.25×–1.91× higher energy efficiency than the state-of-the-art (SOTA) LUT-based GEMM accelerator under an equal peak-throughput hardware setup, while maintaining competitive model accuracy compared with SOTA KV quantization methods.

## 中文摘要

大语言模型（LLM）推理消耗大量计算和能源。基于查找表（LUT）的通用矩阵乘法（GEMM）加速器通过用查表操作替换昂贵的乘法运算来减轻这一负担。然而，现有设计仅支持LLM线性层中的激活-权值GEMM（AW-GEMM），而注意力机制中激活-激活GEMM（AA-GEMM）的LUT执行尚未实现。由于AA-GEMM是长上下文场景中LLM推理计算和能源成本的主要贡献者，支持两种GEMM类型——而不仅仅是AW-GEMM——至关重要。为解决此问题，我们提出Omni-LUT，一种软硬件协同设计的基于LUT的GEMM加速器，通过高效的LUT执行同时支持线性层中的AW-GEMM和注意力中的AA-GEMM。Omni-LUT采用硬件感知的键值（KV）缓存量化设计，结合离线校准与轻量在线量化，在保持模型精度的同时实现与LUT-based GEMM加速器的兼容性。它还通过在LUT创建过程中利用量化补偿来支持更精确的量化方向。Omni-LUT进一步包含相位自适应混合驻留的基于LUT的脉动阵列，以提高LLM中预填充和解码两个阶段的效率。在多样化的长上下文工作负载下，Omni-LUT在等峰值吞吐量硬件配置下，相比最先进的基于LUT的GEMM加速器实现了1.25×–1.91×的能效提升，同时与最先进的KV量化方法相比保持了有竞争力的模型精度。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2026](../index.md)
