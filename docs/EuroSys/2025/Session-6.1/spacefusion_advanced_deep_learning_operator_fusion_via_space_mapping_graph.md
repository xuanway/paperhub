---
title: "SpaceFusion: Advanced Deep Learning Operator Fusion via Space-Mapping Graph"
description: "EuroSys 2025 · ML systems · Liang Zhu (Shanghai Jiao Tong University), Jianguo Yao (Shanghai Jiao Tong Unive"
tags:
  - "EuroSys2025"
  - "ML systems"
---

# SpaceFusion: Advanced Deep Learning Operator Fusion via Space-Mapping Graph

**中文标题：** 通过空间映射图实现高级深度学习算子融合

**所属 Session：** [Session 6.1: ML systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML systems</p>
</div>

**作者**：Liang Zhu (Shanghai Jiao Tong University), Jianguo Yao (Shanghai Jiao Tong University), Haibing Guan (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696087)

## 英文摘要

This work proposes SpaceFusion, an advanced scheduler for efficient deep learning operator fusion. First, we develop a novel abstraction, the Space-Mapping Graph (SMG), to holistically model the spatial information of both inter- and intra-operator dependencies. Subsequently, we introduce the spatial and temporal slicers to decompose the fused spaces defined in SMGs, generating fusion schedules by analyzing and transforming dependencies. Finally, we present auto-scheduling methods that use the slicers to automatically create high-performance fusion schedules tailored to specific hardware resource configurations. End-to-end performance evaluations reveal that SpaceFusion achieves up to 8.79x speedup (3.54x on average) over baseline implementations from Huggingface for Transformer models, and a maximum of 2.21x speedup compared to the state-of-the-art manually-tuned implementations powered by FlashAttention.

## 中文摘要

本文提出 SpaceFusion，一个用于高效深度学习算子融合的先进调度器。首先，我们开发了一种新颖的抽象——空间映射图（SMG），以整体建模算子间和算子内依赖的空间信息。随后，我们引入空间切片器和时间切片器，对 SMG 中定义的融合空间进行分解，通过分析和变换依赖关系生成融合调度方案。最后，我们提出自动调度方法，利用这些切片器自动创建针对特定硬件资源配置的高性能融合调度方案。端到端性能评估表明，对于 Transformer 模型，SpaceFusion 相比 HuggingFace 的基线实现最高获得 8.79 倍加速（平均 3.54 倍），相比由 FlashAttention 支持的最先进手工调优实现最高获得 2.21 倍加速。

**英文关键词：** Machine Learning, Operator Fusion, Deep Learning Compilation

**中文关键词：** 机器学习、算子融合、深度学习编译

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
