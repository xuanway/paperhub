---
title: "MMAscope: Microarchitectural Characterization of Multi-Precision Arithmetic Pipelines in Modern Tensor Cores"
description: "MICRO 2026 · Session 6A · MMAscope：现代张量核中多精度算术流水线的微架构特征分析"
tags:
  - "MICRO2026"
  - "Tensor Core"
---

# MMAscope: Microarchitectural Characterization of Multi-Precision Arithmetic Pipelines in Modern Tensor Cores

**中文标题：** MMAscope：现代张量核中多精度算术流水线的微架构特征分析

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Xuelei Yu, Peng Liu

**来源：** MICRO 2026，pp. 1898–1914；[DOI](https://doi.org/10.1109/MICRO67795.2026.00134)

## 英文摘要

NVIDIA Tensor Core arithmetic pipelines are microarchitecturally undocumented, yet their hidden constraints provide a hardware-level explanation for the FP8 training divergence (gradient instability and NaN proliferation) observed on Hopper hardware. We present MMAscope, a deterministic probing framework that recovers six intra-pipeline properties through Discriminant Numeric Probes: rounding mode, accumulation sequence, dot-product unit width (W_DP), normalization triggers, intermediate mantissa retention depth, and datapath topology. Evaluated across Volta, Ampere, Hopper, and Blackwell, MMAscope yields four findings. (1)~For each input precision, the accumulator type (FP32 vs. FP16) affects only the terminal rounding policy, not the internal reduction geometry; FP16 and BF16 additionally share an identical reduction tree. (2)~The Hopper FP8 to FP32 pipeline retains only 13 intermediate fractional bits, ten fewer than the FP32 mantissa and the sole configuration where the buffer is narrower than the destination format, the central precision deficit behind Hopper FP8 training instability. (3)~Blackwell corrects this to 25 bits, consistent with its FP16 BF16 guard convention. (4)~Blackwell NVFP4 employs a distinct W_DP=64 pipeline with a 35-bit buffer and hardware Block Micro-Scaling, one of three measurably distinct FP4 call paths. To show that the methodology is not NVIDIA specific, we further port MMAscope to AMD CDNA3 (MI300X), recovering its IEEE round to nearest (even) rounding and a 2-step sequential chain architecture. These measurements provide the first quantitative, architecture-spanning characterization of Tensor Core arithmetic pipeline constraints.

## 中文摘要

NVIDIA Tensor Core 算术管道在微架构上没有记录，但其隐藏的约束为在 Hopper 硬件上观察到的 FP8 训练发散（梯度不稳定和 NaN 扩散）提供了硬件级解释。我们提出了 MMAscope，一种确定性探测框架，它通过判别式数字探针恢复六个管道内属性：舍入模式、累加序列、点积单元宽度 (W_DP)、归一化触发器、中间尾数保留深度和数据路径拓扑。通过对 Volta、Ampere、Hopper 和 Blackwell 进行评估，MMAscope 得出了四项发现。 (1)~对于每个输入精度，累加器类型（FP32 与 FP16）仅影响终端舍入策略，而不影响内部归约几何； FP16 和 BF16 另外共享相同的归约树。 (2)~Hopper FP8 到 FP32 管道仅保留 13 个中间小数位，比 FP32 尾数少 10 个，并且是缓冲区比目标格式窄的唯一配置，这是 Hopper FP8 训练不稳定背后的主要精度缺陷。 (3)~Blackwell 将此修正为 25 位，与其 FP16 BF16 保护约定一致。 (4)~Blackwell NVFP4 采用独特的 W_DP=64 管道，具有 35 位缓冲区和硬件块微缩放，这是三个可测量的不同 FP4 调用路径之一。为了表明该方法不是 NVIDIA 特有的，我们进一步将 MMAscope 移植到 AMD CDNA3 (MI300X)，将其 IEEE 舍入恢复为最接近（偶数）舍入和 2 步顺序链架构。这些测量结果首次提供了 Tensor Core 算术管道约束的定量、跨架构表征。

## 中文关键词

微架构特征分析；张量核架构；多精度算术；矩阵乘累加；软硬件协同设计

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.22077206](https://doi.org/10.5281/zenodo.22077206)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
