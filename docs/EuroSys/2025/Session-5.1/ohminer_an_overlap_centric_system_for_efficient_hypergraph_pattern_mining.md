---
title: "OHMiner: An Overlap-centric System for Efficient Hypergraph Pattern Mining"
description: "EuroSys 2025 · Graph and Stream processing · Hao Qi (Huazhong University of Science and Technology), Kang Luo (Huazhong Unive"
tags:
  - "EuroSys2025"
  - "Graph and Stream processing"
---

# OHMiner: An Overlap-centric System for Efficient Hypergraph Pattern Mining

**中文标题：** 面向高效超图模式挖掘的重叠中心系统

**所属 Session：** [Session 5.1: Graph and Stream processing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Graph and Stream processing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Graph and Stream processing</p>
</div>

**作者**：Hao Qi (Huazhong University of Science and Technology), Kang Luo (Huazhong University of Science and Technology), Ligang He (University of Warwick), Yu Zhang (Huazhong University of Science and Technology), Minzhi Cai (Huazhong University of Science and Technology), Jingxin Dai (Huazhong University of Science and Technology), Bingsheng He (National University of Singapore), Hai Jin (Huazhong University of Science and Technology), Zhan Zhang (Zhejiang Lab, China), Jin Zhao (Huazhong University of Science and Technology), Hengshan Yue (Jilin University), Hui Yu (Huazhong University of Science and Technology), Xiaofei Liao (Huazhong University of Science and Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717474)

## 英文摘要

Hypergraph Pattern Mining (HPM) aims to identify all the instances of user-interested subhypergraphs (patterns) in hypergraphs, which has been widely used in various applications. However, existing solutions either need significant enumeration overhead because they extend subhypergraphs at the granularity of vertices, or suffer from massive redundant computations because they often need to repeatedly fetch and process the same incident hyperedges for different vertices. This paper presents an overlap-centric system named OHMiner to efficiently support HPM. OHMiner proposes an overlap-centric execution model to determine the subhypergraphs isomorphism through computing and comparing overlaps among hyperedges using set operations. This model aims to efficiently handle the vertices that collectively share the same incident hyperedges. To automatically and precisely retrieve an arbitrary pattern’s overlapping semantics without performing redundant set computations, OHMiner further proposes a redundancy-free compiler, which constructs an Overlap Intersection Graph (OIG) for the pattern, optimizes the OIG, and generates an overlap-centric execution plan to guide the procedure of HPM. Moreover, OHMiner designs an overlap-centric parallel execution engine, which adopts an incremental overlap-pruned approach to fast validate candidates for HPM. Additionally, it proposes a degree-aware data store to support efficient generation of candidates. Through evaluating OHMiner on a broad range of real-world hypergraphs with various patterns, our experimental results show that OHMiner outperforms the state-of-the-art HPM system by 5.4×–22.2×.

## 中文摘要

超图模式挖掘（HPM）旨在找出超图中所有用户感兴趣的子超图（模式）的实例，已被广泛应用于各类应用。然而，现有方案要么以顶点为粒度扩展子超图而需要大量枚举开销，要么由于常常需要为不同顶点反复获取和处理相同的关联超边而遭受大量冗余计算。本文提出一种以重叠为中心的系统 OHMiner，以高效支持 HPM。OHMiner 提出以重叠为中心的执行模型，通过使用集合运算计算和比较超边之间的重叠来确定子超图同构。该模型旨在高效处理共同共享相同关联超边的顶点。为在不执行冗余集合运算的情况下自动且精确地获取任意模式的重叠语义，OHMiner 进一步提出一种无冗余编译器，它为模式构建重叠交集图（OIG），优化该 OIG，并生成以重叠为中心的执行计划以指导 HPM 过程。此外，OHMiner 设计了以重叠为中心的并行执行引擎，采用增量式重叠剪枝方法快速验证 HPM 的候选。同时，它提出一种度数感知的数据存储以支持候选的高效生成。通过在大量具有各种模式的真实超图上评估 OHMiner，我们的实验结果表明，OHMiner 比最先进的 HPM 系统快 5.4×–22.2×。

**英文关键词：** Hypergraph pattern mining, Overlap, Compiler, Parallel execution engine

**中文关键词：** 超图模式挖掘、重叠、编译器、并行执行引擎

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
