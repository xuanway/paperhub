---
title: "Gopher: Efficient Dynamic Graph Pattern Mining via DAG-Driven Execution"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Yi Zhang (Huazhong University of Science and Technology, China), Yu Huang (Huazh"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# Gopher: Efficient Dynamic Graph Pattern Mining via DAG-Driven Execution

**中文标题：** Gopher：通过DAG驱动执行的高效动态图模式挖掘

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Yi Zhang (Huazhong University of Science and Technology, China), Yu Huang (Huazhong University of Science and Technology, China), Chaoqiang Liu (Huazhong University of Science and Technology, China), Haifeng Liu (Huazhong University of Science and Technology, China), Juntao Chen (Huazhong University of Science and Technology, China), Jingrui Yuan (Huazhong University of Science and Technology, China), Jianhui Yue (Michigan Technological University, USA), XIAOFEI LIAO (Huazhong University of Science and Technology, China), Hai Jin (Huazhong University of Science and Technology, China), Jingling Xue (University of New South Wales, Australia)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769365)

## 英文摘要

Graph pattern mining is essential for analyzing dynamic networks, where graphs evolve over time. To accommodate these changes, existing solutions update match sets incrementally, avoiding the need to re-mine the entire graph and achieving significant performance improvements. However, these methods suffer from inefficiencies due to redundant set intersection operations across subgraph instances, causing performance degradation.

In this paper, we propose Gopher, a DAG-driven dynamic graph pattern mining system that leverages computation locality for enhanced performance. Gopher uses DAGs to represent set operations, identifying and merging common subexpressions at compile time. This reduces redundant computations during runtime. To maximize performance, we introduce a DAG-based mining engine with fine-grained parallelism to decouple data dependencies and a canonical expression-based restoration module to efficiently assemble the results. Evaluations on a multi-core CPU show that Gopher outperforms state-of-the-art solutions, achieving speedups of up to 75.58×, 35.99×, and 11.76× over Tesseract, Cheetah, and PSMiner, respectively.

## 中文摘要

图模式挖掘对于分析随时间演化的动态网络至关重要。为适应这些变化，现有方案增量地更新匹配集，避免重新挖掘整个图，从而实现显著的性能提升。然而，这些方法由于跨子图实例存在冗余的集合求交操作而效率低下，导致性能下降。

本文提出Gopher，一个DAG驱动的动态图模式挖掘系统，它利用计算局部性来提升性能。Gopher用DAG表示集合操作，在编译期识别并合并公共子表达式。这减少了运行时的冗余计算。为最大化性能，我们引入一个具有细粒度并行的基于DAG的挖掘引擎以解耦数据依赖，以及一个基于规范表达式的恢复模块以高效组装结果。在多核CPU上的评估表明，Gopher优于最先进方案，相较Tesseract、Cheetah和PSMiner分别取得最高75.58倍、35.99倍和11.76倍的加速。

**英文关键词：** Graph mining system, Dynamic graph, Incremental computing, Directed acyclic graphs (DAGs)

**中文关键词：** 图挖掘系统、动态图、增量计算、有向无环图（DAG）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
