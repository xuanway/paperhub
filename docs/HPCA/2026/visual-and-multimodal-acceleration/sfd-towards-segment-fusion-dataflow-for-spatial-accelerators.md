---
title: "SFD: Towards Segment Fusion Dataflow for Spatial Accelerators"
description: "HPCA 2026 · Visual and Multimodal Acceleration"
tags:
  - "HPCA2026"
  - "Visual and Multimodal Acceleration"
---

# SFD: Towards Segment Fusion Dataflow for Spatial Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Visual and Multimodal Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Visual and Multimodal Acceleration</p>
</div>

**论文链接**：
**作者**：Fuyu Wang Sun Yat-sen University , Minghua Shen Sun Yat-sen University , Yufei Ding UCSD , Nong Xiao National University of Defense Technology & Sun Yat-sen University , Yutong Lu Sun Yat-sen University
**会议**：HPCA 2026

---

## 中文标题

SFD：面向空间加速器的分段融合数据流

## 英文摘要

Spatial accelerators are promising to satiate the growing demands for performance and energy efficiency in deep neural networks (DNNs). Due to the speed gap between on-chip compute cores and off-chip memory bandwidth, common DNNs suffer from poor operational intensity and are increasingly memory-bound. While operator fusion has shown potential in alleviating this bottleneck, existing approaches suffer from two key limitations. They rely on predefined fusion templates before tensor mapping and impose tile constraints during mapping. As a result, they overlook the potential of fusing more operators and lead to sub-optimal performance. In this paper, we propose a segment fusion dataflow optimization framework called SFD. Central to this framework is the dataflow abstraction that enables template-free operator fusion after mapping and supports tile constraint relaxation through tile scheduling. Based on this abstraction, we first introduce a memory-centric mapper, which defines a design space and incorporates an algorithm to facilitate design space exploration (DSE). Then we propose an analytical network segmenter, which leverages mapping results to analyze tensor lifetimes and on-chip memory usage, fusing operators into variable-length segments. Finally, we introduce a dependency-aware tile scheduler, which develops a priority queue for each segment to ensure correct execution order. Extensive experiments with different DNNs demonstrate SFD achieves 1.4× to 2.2× speedup for spatial accelerators over state-of-the-art fusion frameworks.

## 中文摘要

空间加速器有望满足深度神经网络（DNN）对性能和能效日益增长的需求。由于片上计算核心与片外内存带宽之间的速度差距，常见 DNN 的计算强度偏低，且日益受限于内存。算子融合已在缓解这一瓶颈上显示出潜力，但现有方法存在两个关键局限：在张量映射之前依赖预定义的融合模板，并在映射过程中施加分块约束，因此忽视了融合更多算子的可能，导致性能次优。本文提出名为 SFD 的分段融合数据流优化框架。其核心是一种数据流抽象，支持在映射之后进行无模板的算子融合，并通过分块调度实现分块约束的松弛。基于该抽象，我们首先引入以内存为中心的映射器，它定义了设计空间并内置算法以辅助设计空间探索（DSE）；随后提出解析式网络分段器，利用映射结果分析张量生命周期与片上内存使用情况，将算子融合为长度可变的分段；最后引入依赖感知的分块调度器，为每个分段构建优先队列以确保正确的执行顺序。在不同 DNN 上的大量实验表明，相比最先进的融合框架，SFD 为空间加速器带来 1.4 倍至 2.2 倍的加速比。
