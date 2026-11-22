---
title: "Not All Dot Products Are Equal: The Hidden MMA Arithmetic Design Space Drives Cross-Architecture LLM Inference Gaps"
description: "MICRO 2026 · Session 1A · 并非所有点积都相同：隐藏的 MMA 算术设计空间导致跨架构 LLM 推理差异"
tags:
  - "MICRO2026"
  - "GPU"
  - "LLM Inference"
  - "Numerical Precision"
---

# Not All Dot Products Are Equal: The Hidden MMA Arithmetic Design Space Drives Cross-Architecture LLM Inference Gaps

**中文标题：** 并非所有点积都相同：隐藏的 MMA 算术设计空间导致跨架构 LLM 推理差异

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Jongyeop Kim, Chaeyeon Kim, Jeongwoo Park

**来源：** MICRO 2026，pp. 32–47；[DOI](https://doi.org/10.1109/MICRO67795.2026.00019)

## 英文摘要

The same large language model (LLM), quantized to the same Microscaling (MX) floating-point format, produces different inference results on NVIDIA Hopper and Blackwell GPUs. Using cross-architecture emulation, we demonstrate that the matrix multiply-accumulate (MMA) accumulation microarchitecture alone—all left as implementation-defined in the Open Compute Project (OCP) MX specification—is the sole source of these deterministic inference score discrepancies. Emulated MMA configurations on different physical GPUs produce bit-exact log-probabilities matching native execution across all evaluated LLM benchmarks. Low-precision inference results are therefore not reproducible across GPU platforms unless the MMA accumulation microarchitecture is specified. To isolate and characterize this effect, we construct a bit-accurate MMA emulation framework that reproduces the internal accumulation arithmetic of commercial MMA units on CUDA cores and integrates directly into the vLLM inference pipeline, enabling end-to-end evaluation of both language and vision-language models under arbitrary accumulation configurations. A sweep of the accumulation design space across FP8, MXFP4, and NVFP4 formats reveals that the model's iso-accuracy threshold lies well below commercially deployed precision levels. Hardware synthesis confirms that Pareto-optimal configurations within the iso-accuracy region yield 18.6-20.4% lower area and 16.3-16.7% lower energy relative to commercially deployed configurations. These results provide empirical grounds for standardizing MMA accumulation semantics in the OCP MX specification and offer concrete design-point targets for future low-precision MMA implementations. We release the emulation framework and evaluation infrastructure as open source to enable reproducible cross-platform inference evaluation.

## 中文摘要

同一个大语言模型（LLM）即使量化为相同的微缩放（Microscaling，MX）浮点格式，在 NVIDIA Hopper 与 Blackwell GPU 上也会产生不同的推理结果。通过跨架构仿真，我们证明：矩阵乘累加（MMA）的累加微架构是这些确定性推理评分差异的唯一来源，而开放计算项目（OCP）的 MX 规范将这些细节全部留给实现自行定义。对于所有评估的 LLM 基准，在不同物理 GPU 上仿真相应 MMA 配置，所得对数概率均与原生执行逐位一致。因此，除非明确 MMA 累加微架构，否则低精度推理结果无法跨 GPU 平台复现。为隔离和刻画这种影响，我们构建位精确 MMA 仿真框架，在 CUDA 核上重现商用 MMA 单元的内部累加运算，并直接集成到 vLLM 推理流水线，支持任意累加配置下语言模型与视觉语言模型的端到端评估。对 FP8、MXFP4、NVFP4 格式的累加设计空间扫描表明，模型维持相同精度所需的阈值明显低于商用配置采用的精度水平。硬件综合证实，在等精度区域中选择帕累托最优配置，相比商用配置可降低面积 18.6–20.4%、能耗 16.3–16.7%。这些结果为在 OCP MX 规范中标准化 MMA 累加语义提供了实证基础，也为未来低精度 MMA 实现给出了具体设计目标。我们开源了仿真框架与评估基础设施，以支持可复现的跨平台推理评估。

## 中文关键词

跨架构可复现性；设计空间探索；低精度大语言模型推理；矩阵乘累加

## 代码与研究制品

- 代码仓库：[https://github.com/IDSLab-SKKU/NADPE](https://github.com/IDSLab-SKKU/NADPE)
- 代码与复现实验仓库：[https://github.com/IDSLab-SKKU/micro26-ae](https://github.com/IDSLab-SKKU/micro26-ae)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21505180](https://doi.org/10.5281/zenodo.21505180)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
