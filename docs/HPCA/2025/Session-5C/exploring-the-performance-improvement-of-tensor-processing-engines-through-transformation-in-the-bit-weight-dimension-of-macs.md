---
title: "Exploring the Performance Improvement of Tensor Processing Engines through Transformation in the Bit-weight Dimension of MACs"
description: "HPCA 2025 · Stacking the Layers (Quantization)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Quantization)"
---

# Exploring the Performance Improvement of Tensor Processing Engines through Transformation in the Bit-weight Dimension of MACs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Quantization)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Quantization)</p>
</div>

**论文链接**：
**作者**：Qizhe Wu (University of Science and Technology of China), Huawen Liang (University of Science and Technology of China), Yuchen Gui (University of Science and Technology of China), Zhichen Zeng (University of Science and Technology of China), Zerong He (University of Science and Technology of China), Linfeng Tao (University of Science and Technology of China), Xiaotian Wang (University of Science and Technology of China), Letian Zhao (University of Science and Technology of China), Zhaoxi Zeng (University of Science and Technology of China), Wei Yuan (University of Science and Technology of China), Wei Wu (University of Science and Technology of China), Xi Jin (University of Science and Technology of China)
**会议**：HPCA 2025

---

## 中文标题

通过 MAC 位权维度变换探索张量处理引擎的性能提升

## 英文摘要

General matrix-matrix multiplication (GEMM), serving as a cornerstone of AI computations, has positioned tensor processing engines (TPEs) as increasingly critical components within existing GPUs and domain-specific architectures (DSA). Our analysis identifies that the prevailing architectures primarily focus on dataflow or operand reuse strategies, when considering the combination of matrix multiplication with multiply-accumulator (MAC) itself, it provides greater optimization space for the design of TPEs. This work introduces a novel perspective on matrix multiplication from a hardware standpoint, focusing on the bit-weight dimension of MACs. Through this lens, we propose a finer-grained TPE notation, using matrix triple loops as an example, introducing new methods and ideas for designing and optimizing PE microarchitecture. Based on the new notation and transformations, we propose four optimization techniques that achieve varying degrees of improvement in timing, area, and power consumption. We implement our design in RTL using the SMIC-28nm process. Applying our methods to four classic TPE architectures (include systolic array [20], 3D-Cube [27], multiplier-adder tree [48], and 2D-Matrix [30]), we achieved area efficiency improvements of 1.27×, 1.28×, 1.56×, and 1.44×, and 1.04×, 1.56×, 1.49×, and 1.20× for energy efficiency respectively. When applied to a bit-slice architecture, we achieved a 12.10× improvement in energy efficiency and 2.85× in area efficiency compared to Laconic [38]. Our Verilog HDL code, along with timing, area, and power reports for circuit synthesis in URL: https://github.com/wqzustc/High-Performance-Tensor-Processing-Engines.

## 中文摘要

通用矩阵乘法（GEMM）作为 AI 计算的基石，使张量处理引擎（TPE）在现有 GPU 与领域专用架构（DSA）中愈发关键。我们的分析发现，主流体系结构在考虑矩阵乘法与乘累加（MAC）本身的结合时，主要关注数据流或操作数复用策略，这为 TPE 设计提供了更大优化空间。本文从硬件角度为矩阵乘法引入新视角，聚焦 MAC 的位权维度，据此提出更细粒度的 TPE 记法，以矩阵三重循环为例，为设计与优化 PE 微架构引入新方法与思路。基于新记法与变换，我们提出四种优化技术，在时序、面积与功耗上取得不同程度的改善。我们用中芯国际 28nm 工艺以 RTL 实现设计。将其用于四种经典 TPE 架构（脉动阵列 [20]、3D-Cube [27]、乘加树 [48]、2D-Matrix [30]），面积效率分别提升 1.27×、1.28×、1.56× 与 1.44×，能效分别提升 1.04×、1.56×、1.49× 与 1.20×。用于位切片架构时，相比 Laconic [38] 能效提升 12.10×，面积效率提升 2.85×。我们的 Verilog HDL 代码以及电路综合的时序、面积与功耗报告见 https://github.com/wqzustc/High-Performance-Tensor-Processing-Engines。
