---
title: "Jupiter: Pushing the Speed and Scalability Limitations for Subgraph Matching on Multi-GPUs"
description: "EuroSys 2025 · GPU Systems · Zhiheng Lin (Institute of Computing Technology, Chinese Academy of Sciences), Ke"
tags:
  - "EuroSys2025"
  - "GPU Systems"
---

# Jupiter: Pushing the Speed and Scalability Limitations for Subgraph Matching on Multi-GPUs

**中文标题：** 突破多 GPU 子图匹配的速度与可扩展性限制

**所属 Session：** [Session 4.2: GPU Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：GPU Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · GPU Systems</p>
</div>

**作者**：Zhiheng Lin (Institute of Computing Technology, Chinese Academy of Sciences), Ke Meng (Institute of Computing Technology), Changjie Xu (Institute of Computing Technology, Chinese Academy of Sciences), Weichen Cao (Institute of Computing Technology, Chinese Academy of Sciences), Guangming Tan (Institute of Computing Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717491)

**论文集标题：** Jupiter: Pushing Speed and Scalability Limitations for Subgraph Matching on Multi-GPUs（官方议程标题如上）

## 英文摘要

Graph pattern matching (GPM) aims to find subgraphs isomorphic to user-specified patterns within a large graph. Due to its ability to reveal potential relationships among entities in complex networks, it is widely applied in various fields, such as mining molecular structures in bioinformatics, detecting fraud in cloud-based e-commerce, and querying knowledge graphs in large language model. The explosion of data brought by the AI era has rendered traditional GPM systems inadequate for real-world needs. Due to the intricate data dependencies of GPM tasks, most SOTA GPM systems currently have limited scalability and performance, they perform well in small graph mining with single node but cannot scale to modern clusters with GPU acceleration. This paper introduces JUPITER, the first system capable of matching patterns on large graph across multi-node GPU clusters, which can handle graphs 10 times larger than SOTAs with the same memory resources. Its core principle is to delegate computation to the data-residing processing unit rather than pulling data to the computation location, which greatly improves communication efficiency. Experimental results show that JUPITER can reduce communication volume by two orders of magnitude compared to SOTA subgraph matching systems, achieving up to 120× speedup and an average of 21.5× speedup.

## 中文摘要

图模式匹配（GPM）旨在在大图中寻找与用户指定模式同构的子图。由于能够揭示复杂网络中实体之间的潜在关系，它被广泛应用于多个领域，例如生物信息学中的分子结构挖掘、云上电子商务中的欺诈检测，以及大语言模型中的知识图谱查询。AI 时代带来的数据爆炸使传统 GPM 系统难以满足现实需求。由于 GPM 任务复杂的数据依赖，目前大多数最先进的 GPM 系统可扩展性和性能有限，它们在单节点的小图挖掘中表现良好，却无法扩展到具备 GPU 加速的现代集群。本文提出 JUPITER，首个能够在多节点 GPU 集群上对大规模图进行模式匹配的系统，在相同内存资源下可处理比 SOTA 大 10 倍的图。其核心原理是将计算委托给数据所在的处理单元，而非将数据拉取到计算所在位置，从而大幅提升通信效率。实验结果表明，与 SOTA 子图匹配系统相比，JUPITER 可将通信量降低两个数量级，实现最高 120 倍、平均 21.5 倍的加速。

**英文关键词：** GPU, Subgraph Matching, Delegation

**中文关键词：** GPU、子图匹配、委托计算

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
