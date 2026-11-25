---
title: "Session 9: Parallel Algorithms"
description: "PPoPP 2026 Session 9（Parallel Algorithms），2026 年 2 月 3 日 14:10–15:30，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-9"
  - "Parallel Algorithms"
---

# Session 9: Parallel Algorithms

**PPoPP 2026 · 2026 年 2 月 3 日 14:10–15:30 · Pyrmont · Session Chair：Kenjiro Taura**

涵盖并行算法与加速：GPU 端到端零知识证明生成、反向自动微分并行化、商用 CPU 序列比对，以及基于存内计算的空间索引。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Pipelonk: Accelerating End-to-End Zero-Knowledge Proof Generation on GPUs for PLONK-Based Protocols](pipelonk_accelerating_end_to_end_zero_knowledge_proof_generation_on_gpus_for_plonk_based_protocols.md) | Zhiyuan Zhang 等 7 人 | 8–80GB 显存均可运行，平均加速 10.7×、最高 19.4× |
| 2 | [ParDiff: Efficiently Parallelizing Reverse-Mode Automatic Differentiation with Direct Indexing](pardiff_efficiently_parallelizing_reverse_mode_automatic_differentiation_with_direct_indexing.md) | Shuhong Huang 等 11 人 | 直接索引磁带 + 求和感知循环变换，较 Enzyme 最高 483.21× |
| 3 | [Faster and Cheaper: Pushing the Sequence Alignment Throughput with Commercial CPUs](faster_and_cheaper_pushing_the_sequence_alignment_throughput_with_commercial_cpus.md) | Zhonghai Zhang 等 5 人 | 商用 CPU 上吞吐提升 2.27–3.28×、成本降低 2.54–5.65× |
| 4 | [PIM-zd-tree: A Fast Space-Partitioning Index Leveraging Processing-in-Memory](pim_zd_tree_a_fast_space_partitioning_index_leveraging_processing_in_memory.md) | Yiwei Zhao 等 8 人 | 首个真实 PIM 上的空间划分索引，吞吐最高 4.25×/99× |

---

[← Session 8: Distributed Training](../Session-8/index.md) · [PPoPP 2026 总览](../index.md) · [Session 10: ML Inference →](../Session-10/index.md)
