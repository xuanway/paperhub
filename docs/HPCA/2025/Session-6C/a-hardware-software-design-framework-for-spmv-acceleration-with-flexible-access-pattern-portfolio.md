---
title: "A Hardware-Software Design Framework for SpMV Acceleration with Flexible Access Pattern Portfolio"
description: "HPCA 2025 · Stacking the Layers (Sparsity)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Sparsity)"
---

# A Hardware-Software Design Framework for SpMV Acceleration with Flexible Access Pattern Portfolio

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Sparsity)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Sparsity)</p>
</div>

**论文链接**：
**作者**：Zhenyu Wu (The University of Hong Kong), Maolin Wang (The Hong Kong University of Science and Technology), Hayden So (University of Hong Kong)
**会议**：HPCA 2025

---

## 中文标题

支持灵活访问模式组合的 SpMV 加速软硬件设计框架

## 英文摘要

Sparse matrix-vector multiplications (SpMV) are notoriously challenging to accelerate due to their highly irregular data access pattern. Although a fully customized static accelerator design may be adequate for small problems that can fit entirely within an on-chip memory buffer, practical SpMV problems are large and have dynamic matrix structures that cannot easily be optimized at compile time. To address this need for trade-off between flexibility and performance, we present SPASM, a hardware-software framework that accelerates SpMV computation using a customizable portfolio of data access patterns as templates and a reconfigurable hardware to support their run-time execution. SPASM extracts local data access patterns of the input matrices and derives a set of template patterns to encode these inputs. Subsequently, a novel hardware computing structure is proposed to support vectorized computation and flexible switching between different template patterns for each tile computation. Furthermore, SPASM leverages the global compositions of input matrices to derive hardware configuration and workload schedules that improve load balancing among the parallel processing units. Importantly, although SPASM can optimize the pattern portfolio for a particular set of expected input matrices, the generated hardware can flexibly be used to accelerate SpMV of different input patterns albeit with reduced performance. Experimental results show that SPASM can achieve an average 2.81× speedup compared to the state-of-the-art SpMV accelerator while keeping a relatively low customization cost.

## 中文摘要

稀疏矩阵向量乘（SpMV）因其高度不规则的数据访问模式而极难加速。尽管完全定制的静态加速器设计对可完全驻留片上存储缓冲的小规模问题或许足够，但实际的 SpMV 问题规模庞大且矩阵结构动态变化，难以在编译期优化。为在灵活性与性能之间取得平衡，我们提出 SPASM，一个软硬件框架，它使用可定制的数据访问模式组合作为模板，并用可重构硬件支持其运行时执行。SPASM 提取输入矩阵的局部数据访问模式，并导出一组模板模式来编码这些输入。随后提出一种新颖的硬件计算结构，支持向量化计算以及在每个分块计算时于不同模板模式间灵活切换。此外，SPASM 利用输入矩阵的全局构成来导出硬件配置与负载调度，从而改善并行处理单元间的负载均衡。重要的是，尽管 SPASM 可针对特定预期输入矩阵集合优化模式组合，所生成的硬件仍可灵活用于加速不同输入模式的 SpMV，只是性能有所下降。实验结果表明，SPASM 相比最先进的 SpMV 加速器平均取得 2.81 倍加速，同时保持较低的定制成本。
