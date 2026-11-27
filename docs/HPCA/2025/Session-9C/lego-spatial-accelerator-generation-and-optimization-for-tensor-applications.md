---
title: "LEGO: Spatial Accelerator Generation and Optimization for Tensor Applications"
description: "HPCA 2025 · Finding the Best Table"
tags:
  - "HPCA2025"
  - "Finding the Best Table"
---

# LEGO: Spatial Accelerator Generation and Optimization for Tensor Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Finding the Best Table。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Finding the Best Table</p>
</div>

**论文链接**：
**作者**：Yujun Lin (MIT), Zhekai Zhang (MIT), Song Han (MIT)
**会议**：HPCA 2025

---

## 中文标题

LEGO：面向张量应用的空间加速器生成与优化

## 英文摘要

Modern tensor applications, especially foundation models and generative AI applications require multiple input modalities (both vision and language), which increases the demand for flexible accelerator architecture. Existing frameworks suffer from the trade-off between design flexibility and productivity of RTL generation: either limited to very few hand-written templates or cannot automatically generate the RTL. To address this challenge, we propose the LEGO framework, which targets tensor applications and automatically generates spatial architecture design and outputs synthesizable RTL code without handwritten RTL design templates. Leveraging the affine-transformation-based architecture representation, LEGO front end finds interconnections between function units, synthesizes the memory system, and fuses different spatial dataflow designs based on data reuse analysis. LEGO back end then translates the hardware in a primitive-level graph to perform lower-level optimizations, and applies a set of linear-programming algorithms to optimally insert pipeline registers and reduce the overhead of unused logic when switching spatial dataflows. Our evaluation demonstrates that LEGO can achieve 3.2× speedup and 2.4× energy efficiency compared to previous work Gemmini, and can generate one architecture for diverse modern foundation models in generative AI applications.

## 中文摘要

现代张量应用，尤其是基础模型与生成式 AI 应用，需要视觉与语言等多种输入模态，从而提升了对灵活加速器架构的需求。现有框架在设计灵活性与 RTL 生成生产率之间难以兼顾：要么局限于极少数手写模板，要么无法自动生成 RTL。为此我们提出 LEGO 框架，它面向张量应用，可自动生成空间架构设计，并在无需手写 RTL 模板的情况下输出可综合的 RTL 代码。借助基于仿射变换的架构表示，LEGO 前端发现功能单元间的互连、综合存储系统，并基于数据复用分析融合不同的空间数据流设计；LEGO 后端将硬件翻译为原语级图以进行更低层次优化，并应用一系列线性规划算法最优地插入流水线寄存器、降低切换空间数据流时未用逻辑的开销。评估表明，与先前工作 Gemmini 相比，LEGO 可实现 3.2× 加速比与 2.4× 能效，并能为生成式 AI 中的多种现代基础模型生成同一套架构。
