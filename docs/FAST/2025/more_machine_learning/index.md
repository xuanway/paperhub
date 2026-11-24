---
title: "More Machine Learning · FAST 2025"
description: "FAST 2025 · More Machine Learning · 4 篇论文"
tags:
  - "FAST2025"
  - "More Machine Learning"
---

# More Machine Learning · FAST 2025

**中文主题**：机器学习专题

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-26 09:00–10:20 · **Chair**：Ali R. Butt（Virginia Tech）

本 Session 的四项工作都把机器学习放进了存储系统的关键路径：缓存淘汰用学习模型预测对象复用，图训练把模型搬到特征一侧，索引则把学习模型落到 DPU 与 PIM 这类新硬件上。四条路线的共同约束不是模型精度，而是学习本身的代价——训练与预测的 CPU 开销、跨机特征传输、以及 DPU/PIM 的容量与算力上限，因此对策一致地指向把代价挪到更便宜的维度，例如用更粗的训练频率换开销、用更多内存访问换更少浮点运算。代表性结果显示这条路可行：淘汰开销较 HALP 降低 60.9%，GNN 训练相对 P3 最高加速 4.2 倍，DPU 索引内存最多省 92%，PIM 索引吞吐达基线 36.5 倍。

本 Session 共收录 **4** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches](3l_cache_low_overhead_and_precise_learning_based_eviction_policy_for_caches.md) ([code](https://github.com/optiq-lab/3L-Cache)) | 3L-Cache：低开销且精确的缓存学习型淘汰策略 | 三个 L 的关键不在模型更聪明，而在砍掉训练浪费与预测浪费：训练频率降一个量级，采样只挑冷对象。 | [页面](https://www.usenix.org/conference/fast25/presentation/zhou-wenbin) · [PDF](https://www.usenix.org/system/files/fast25-zhou-wenbin.pdf) |
| [LeapGNN: Accelerating Distributed GNN Training Leveraging Feature-Centric Model Migration](leapgnn_accelerating_distributed_gnn_training_leveraging_feature_centric_model_migration.md) ([code](https://github.com/ISCS-ZJU/LeapGNN-AE)) | LeapGNN：借助以特征为中心的模型迁移加速分布式 GNN 训练 | 模型参数远小于顶点特征，于是把模型搬到特征一侧，再用微图把一次迁移要取的特征压到最少。 | [页面](https://www.usenix.org/conference/fast25/presentation/chen-weijian-leap) · [PDF](https://www.usenix.org/system/files/fast25-chen-weijian-leap.pdf) |
| [HiDPU: A DPU-Oriented Hybrid Indexing Scheme for Disaggregated Storage Systems](hidpu_a_dpu_oriented_hybrid_indexing_scheme_for_disaggregated_storage_systems.md) | HiDPU：面向解耦存储系统的 DPU 导向混合索引方案 | 让 DPU 自己查地址映射：按地址连续性分段混合索引，把 DPU-host 交互压到一次。 | [页面](https://www.usenix.org/conference/fast25/presentation/zhu) · [PDF](https://www.usenix.org/system/files/fast25-zhu.pdf) |
| [PIMLex: A High-Performance Learned Index with Processing-in-Memory](pimlex_a_high_performance_learned_index_with_processing_in_memory.md) | PIMLex：基于存内计算的高性能学习型索引 | 按 PIM 的短板改索引结构：搜索层下沉到 PIM，数据层留在 DRAM，用查表代替浮点运算。 | [页面](https://www.usenix.org/conference/fast25/presentation/cui) · [PDF](https://www.usenix.org/system/files/fast25-cui.pdf) |

[返回 FAST 2025](../index.md)
