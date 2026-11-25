---
title: "Session 4: GPU and Heterogeneous Computing"
description: "PPoPP 2026 Session 4（GPU and Heterogeneous Computing），2026 年 2 月 2 日 15:50–17:10，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-4"
  - "GPU and Heterogeneous Computing"
---

# Session 4: GPU and Heterogeneous Computing

**PPoPP 2026 · 2026 年 2 月 2 日 15:50–17:10 · Pyrmont · Session Chair：Frank Mueller**

关注 GPU 与异构计算：GPU 渐进式有损压缩、异构 OpenMP 数据映射的动态检测、GPU 极大团枚举，以及驯服细粒度不规则性的 APSP。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [🏆 PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation](prism_an_efficient_gpu_based_lossy_compression_framework_for_progressive_data_retrieval_with_multi_level_interpolation.md) | Bing Lu 等 9 人 | 多重插值+位平面+符号-绝对值编码，吞吐高 20.1× |
| 2 | [Dynamic Detection of Inefficient Data Mapping Patterns in Heterogeneous OpenMP Applications](dynamic_detection_of_inefficient_data_mapping_patterns_in_heterogeneous_openmp_applications.md) | Luke Marzen 等 3 人 | OMPT 动态检测低效数据映射，开销仅 5%，给出源码归因 |
| 3 | [Root-Down Exposure for Maximal Clique Enumeration on GPUs](root_down_exposure_for_maximal_clique_enumeration_on_gpus.md) | Zhe Pan 等 3 人 | 根下暴露免同步拉取，比 SOTA 快 1.25–5.38× |
| 4 | [ROME: Maximizing GPU Efficiency for All-Pairs Shortest Path via Taming Fine-Grained Irregularities](rome_maximizing_gpu_efficiency_for_all_pairs_shortest_path_via_taming_fine_grained_irregularities.md) | Weile Luo 等 7 人 | 空间重构+异步流水线驯服不规则，比 SOTA GPU 快 11.2–338× |

### 获奖

- **PRISM: An Efficient GPU-Based Lossy Compression Framework for Progressive Data Retrieval with Multi-Level Interpolation** —— Best Paper Nominee

---

[← Session 3: Concurrent Data Structures](../Session-3/index.md) · [PPoPP 2026 总览](../index.md) · [Session 5: Stencil and Sparse Matrix Computation →](../Session-5/index.md)
