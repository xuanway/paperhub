---
title: "FlexiWalker: Extensible GPU Framework for Efficient Dynamic Random Walks with Runtime Adaptation"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Seongyeon Park (Seoul National University), Jaeyong Song (Seoul National Univers"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# FlexiWalker: Extensible GPU Framework for Efficient Dynamic Random Walks with Runtime Adaptation

**中文标题：** FlexiWalker：面向高效动态随机游走并支持运行时自适应的可扩展GPU框架

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Seongyeon Park (Seoul National University), Jaeyong Song (Seoul National University), Changmin Shin (Seoul National University), Sukjin Kim (Seoul National University), Junguk Hong (Seoul National University), Jinho Lee (Seoul National University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769358)

## 英文摘要

Dynamic random walks are fundamental to various graph analysis applications, offering advantages by adapting to evolving graph properties. Their runtime-dependent transition probabilities break down the pre-computation strategy that underpins most existing CPU and GPU static random walk optimizations. This leaves practitioners suffering from suboptimal frameworks and having to write hand-tuned kernels that do not adapt to workload diversity. To handle this issue, we present FlexiWalker, the first GPU framework that delivers efficient, workload-generic support for dynamic random walks. Our design-space study shows that rejection sampling and reservoir sampling are more suitable than other sampling techniques under massive parallelism. Thus, we devise (i) new high-performance kernels for them that eliminate global reductions, redundant memory accesses, and random-number generation. Given the necessity of choosing the best-fitting sampling strategy at runtime, we adopt (ii) a lightweight first-order cost model that selects the faster kernel per node at runtime. To enhance usability, we introduce (iii) a compile-time component that automatically specializes user-supplied walk logic into optimized building blocks. On various dynamic random walk workloads with real-world graphs, FlexiWalker outperforms the best published CPU/GPU baselines by geometric means of 73.44× and 5.91×, respectively, while successfully executing workloads that prior systems cannot support. We open-source FlexiWalker in https://github.com/AIS-SNU/FlexiWalker.

## 中文摘要

动态随机游走是各类图分析应用的基础，其通过适应不断变化的图属性而具有优势。其取决于运行时的转移概率打破了支撑现有大多数CPU和GPU静态随机游走优化的预计算策略。这使得实践者不得不使用次优的框架，并编写无法适应工作负载多样性的手工调优内核。为解决这一问题，我们提出FlexiWalker，首个为动态随机游走提供高效、工作负载通用支持的GPU框架。我们的设计空间研究表明，在大规模并行下，拒绝采样和蓄水池采样比其他采样技术更为合适。因此，我们为它们设计了(i) 新的高性能内核，消除了全局归约、冗余内存访问和随机数生成。鉴于需要在运行时选择最合适的采样策略，我们采用(ii) 一个轻量级的一阶代价模型，在运行时为每个节点选择更快的内核。为提升易用性，我们引入(iii) 一个编译期组件，自动将用户提供的游走逻辑特化为优化的构建块。在多种使用真实世界图的动态随机游走工作负载上，FlexiWalker分别以73.44倍和5.91倍的几何平均值优于已发表的最佳CPU/GPU基线，并成功执行了先前系统无法支持的工作负载。我们将FlexiWalker开源在 https://github.com/AIS-SNU/FlexiWalker。

**英文关键词：** Dynamic Random Walks, GPU Optimization

**中文关键词：** 动态随机游走、GPU优化

## 代码与研究制品

- [代码](https://github.com/AIS-SNU/FlexiWalker)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
