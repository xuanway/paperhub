---
title: "MetaHG: Enhancing HGNN Systems Leveraging Advanced Metapath Graph Abstraction"
description: "EuroSys 2025 · ML Systems · Haiheng He (Huazhong University of Science and Technology), Haifeng Liu (Huazhon"
tags:
  - "EuroSys2025"
  - "ML Systems"
---

# MetaHG: Enhancing HGNN Systems Leveraging Advanced Metapath Graph Abstraction

**中文标题：** 利用先进元路径图抽象增强异构图神经网络系统

**所属 Session：** [Session 4.1: ML Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML Systems</p>
</div>

**作者**：Haiheng He (Huazhong University of Science and Technology), Haifeng Liu (Huazhong University of Science and Technology), Long Zheng (Huazhong University of Science and Technology), Yu Huang (Huazhong University of Science and Technology), Xinyang Shen (Huazhong University of Science and Technology), Wenkan Huang (Huazhong University of Science and Technology), Shuaihu Cao (Huazhong University of Science and Technology), XIAOFEI LIAO (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Jingling Xue (University of New South Wales)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717492)

## 英文摘要

Heterogeneous Graph Neural Networks (HGNNs) are pivotal for extracting semantic and structural information from heterogeneous graphs. Traditional HGNN implementations often grapple with the challenges of excessive metapath instances, requiring substantial storage or incurring high instance-matching overhead. These methods typically suffer from redundant instance encoding and costly semantic graph construction. Addressing these issues, we introduce an advanced Metapath Graph (MG) abstraction that encapsulates the structural information of all metapath instances within a compact representation. This approach significantly reduces storage demands, eliminates redundant instance encodings, and foregoes the need for constructing semantic graphs, thereby facilitating rapid HGNN inference. Our software-based system, MetaHG, leverages layerwise encoding and aggregation to avoid redundancies without the necessity of semantic graphs. It incorporates a fast, lightweight partitioning method to efficiently manage large graphs. Distinctively, MetaHG seamlessly integrates with both dynamic HGNNs and homogeneous GNNs, unlike conventional systems. Comparative evaluations demonstrate that MetaHG surpasses the state-of-the-art BFS- and DFS-based HGNN systems, MAGNN and the software implementation of MetaNMP, by 42.5× and 4.53×, respectively, on average.

## 中文摘要

异构图神经网络（HGNN）是从异构图提取语义与结构信息的关键技术。传统 HGNN 实现常常受困于元路径实例过多的问题，需要大量存储或带来高昂的实例匹配开销。这些方法通常存在冗余的实例编码和代价高昂的语义图构建。针对这些问题，我们提出一种先进的元路径图（MG）抽象，以紧凑表示封装所有元路径实例的结构信息。该方法显著降低了存储需求，消除了冗余的实例编码，并免去了构建语义图的需要，从而支持快速的 HGNN 推理。我们的软件系统 MetaHG 利用逐层编码与聚合，在无需语义图的情况下避免冗余。它采用一种快速轻量的划分方法来高效管理大图。与众不同的是，MetaHG 能同时无缝集成动态 HGNN 与同构 GNN，而传统系统则不能。对比评估表明，MetaHG 平均分别比最先进的基于 BFS 和 DFS 的 HGNN 系统 MAGNN 与 MetaNMP 的软件实现快 42.5 倍和 4.53 倍。

**英文关键词：** Heterogeneous Graph Neural Networks, Metapath Graph, Layerwise Encoding

**中文关键词：** 异构图神经网络、元路径图、逐层编码

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
