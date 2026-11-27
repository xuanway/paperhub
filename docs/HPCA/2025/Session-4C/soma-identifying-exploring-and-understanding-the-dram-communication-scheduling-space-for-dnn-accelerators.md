---
title: "SoMA: Identifying, Exploring, and Understanding the DRAM Communication Scheduling Space for DNN Accelerators"
description: "HPCA 2025 · Stacking the Layers"
tags:
  - "HPCA2025"
  - "Stacking the Layers"
---

# SoMA: Identifying, Exploring, and Understanding the DRAM Communication Scheduling Space for DNN Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers</p>
</div>

**论文链接**：
**作者**：Jingwei Cai (Tsinghua University), Xuan Wang (Xi’an Jiaotong Uiversity), Mingyu Gao (Tsinghua University), Sen Peng (Xi’an Jiaotong University), Zijian Zhu (Tsinghua University), Yuchen Wei (Tsinghua University), Zuotong Wu (Xi’an Jiaotong University), Kaisheng Ma (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

SoMA：识别、探索与理解 DNN 加速器的 DRAM 通信调度空间

## 英文摘要

Modern Deep Neural Network (DNN) accelerators are equipped with increasingly larger on-chip buffers to provide more opportunities to alleviate the increasingly severe DRAM bandwidth pressure. However, most existing research on buffer utilization still primarily focuses on single-layer dataflow scheduling optimization. As buffers grow large enough to accommodate most single-layer weights in most networks, the impact of single-layer dataflow optimization on DRAM communication diminishes significantly. Therefore, developing new paradigms that fuse multiple layers to fully leverage the increasingly abundant on-chip buffer resources to reduce DRAM accesses has become particularly important, yet remains an open challenge. To address this challenge, we first identify the optimization opportunities in DRAM communication scheduling by analyzing the drawbacks of existing works on the layer fusion paradigm and recognizing the vast optimization potential in scheduling the timing of data prefetching from and storing to DRAM. To fully exploit these optimization opportunities, we develop a Tensor-centric Notation and its corresponding parsing method to represent different DRAM communication scheduling schemes and depict the overall space of DRAM communication scheduling. Then, to thoroughly and efficiently explore the space of DRAM communication scheduling for diverse accelerators and workloads, we develop an end-to-end scheduling framework, SoMa, which has already been developed into a compiler for our commercial accelerator product. Compared with the state-of-the-art (SOTA) Cocco framework, SoMa achieves, on average, a 2.11× performance improvement and a 37.3% reduction in energy cost simultaneously. Then, we leverage SoMa to study optimizations for LLM, perform design space exploration (DSE), and analyze the DRAM communication scheduling space through a practical example, yielding some interesting insights. Moreover, SoMa has been open-sourced at https://github.com/SET-Scheduling-Project/SoMa-HPCA2025.

## 中文摘要

现代 DNN 加速器的片上缓冲越来越大，为缓解日益严峻的 DRAM 带宽压力提供了更多机会。但现有缓冲利用研究仍主要聚焦单层数据流调度优化。当缓冲足以容纳大多数网络中大多数单层权重时，单层数据流优化对 DRAM 通信的影响显著减弱。因此，发展融合多层、充分利用丰富片上缓冲资源以减少 DRAM 访问的新范式尤为重要，却仍是开放挑战。为此我们首先分析现有层融合工作的不足，识别 DRAM 通信调度中的优化机会，并认识到在从 DRAM 预取数据与向 DRAM 写回数据的时机调度上存在巨大优化潜力。为充分利用这些机会，我们提出以张量为中心的记法及其解析方法，用以表示不同 DRAM 通信调度方案并刻画其整体空间。随后，为对多样加速器与负载彻底高效地探索该空间，我们开发了端到端调度框架 SoMa，它已成为我方商用加速器产品的编译器。与最先进的 Cocco 框架相比，SoMa 平均同时取得 2.11× 性能提升与 37.3% 能耗降低。我们还用 SoMa 研究 LLM 优化、进行设计空间探索（DSE），并通过实例分析该调度空间，得到若干有趣见解。SoMa 已开源于 https://github.com/SET-Scheduling-Project/SoMa-HPCA2025。
