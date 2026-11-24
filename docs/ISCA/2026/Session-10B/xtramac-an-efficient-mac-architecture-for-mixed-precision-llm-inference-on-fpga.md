---
title: "XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA"
description: "ISCA 2026 · Session 10B · XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA"
tags:
  - "ISCA2026"
  - "Session 10B"
  - "ML Accelerators 2"
---

# XtraMAC: An Efficient MAC Architecture for Mixed-Precision LLM Inference on FPGA

**中文标题：** XtraMAC: 面向 FPGA 上混合精度 LLM 推理的高效 MAC 架构

**所属 Session：** [Session 10B](index.md) · [ISCA 2026](../index.md)

**作者：** Feng Yu, Hongshi Tan, Yao Chen, Weng-Fai Wong, Bingsheng He

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The widespread adoption of mixed-precision quantization in large language models (LLMs) has created demand for hardware that can efficiently perform multiply–accumulate (MAC) operations across mixed datatypes and switch datatypes at runtime. Existing FPGA-based MAC solutions fall short due to limitations in fixed-datatype design, inefficient spatial or temporal resource sharing, and poor support for mixed-precision execution. These limitations collectively lead to under-utilization of DSP resources, limiting achievable parallelism and throughput. In this work, we present XtraMAC, a novel MAC architecture that unifies integer, floating-point, and mixed-precision operations within a single, datatype-adaptive microarchitecture. XtraMAC decomposes all supported MAC formats into a shared integer mantissa product with lightweight sign and exponent handling, enabling dynamic operand packing and efficient DSP resource sharing with constant latency and initiation interval of one across all datatypes. Evaluated on an AMD Xilinx U55c FPGA, XtraMAC achieves 1.4–2.0× higher compute density, reduces per-operation LUT, FF, and DSP consumption by 27–51%, and delivers up to 1.9× greater energy efficiency and 1.2× speedup on representative mixed-precision LLM workloads. The implementation of XtraMAC is open-sourced at https://github.com/Xtra-Computing/XtraMAC.

## 中文摘要

大语言模型（LLM）中混合精度量化的广泛采用，催生了对能够在混合数据类型上高效执行乘累加（MAC）运算并在运行时切换数据类型的硬件的需求。现有的基于 FPGA 的 MAC 方案因固定数据类型设计的局限、空间或时间资源共享效率低下，以及对混合精度执行支持不足而难以胜任。这些局限共同导致 DSP 资源利用率不足，限制了可实现的并行度与吞吐量。在本工作中，我们提出 XtraMAC，一种新颖的 MAC 架构，在单一的数据类型自适应微架构内统一了整数、浮点与混合精度运算。XtraMAC 将所有支持的 MAC 格式分解为共享的整数尾数乘积，并辅以轻量的符号与指数处理，从而实现动态操作数打包与高效的 DSP 资源共享，且在所有数据类型下保持恒定的延迟与为 1 的启动间隔。在 AMD Xilinx U55c FPGA 上评估，XtraMAC 实现了 1.4–2.0× 更高的计算密度，将每次操作的 LUT、FF 和 DSP 消耗降低 27–51%，并在代表性混合精度 LLM 工作负载上带来最高 1.9× 的能效提升和 1.2× 的加速。XtraMAC 的实现已开源于 https://github.com/Xtra-Computing/XtraMAC。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：Xtra-Computing/XtraMAC](https://github.com/Xtra-Computing/XtraMAC)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 10B](index.md) · [返回 ISCA 2026](../index.md)
