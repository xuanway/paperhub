---
title: "Session 1: Graph Neural Networks"
description: "PPoPP 2025 Session 1（Graph Neural Networks），2025 年 3 月 3 日 10:00–11:00，Acacia D，共 3 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-1"
  - "Graph Neural Networks"
---

# Session 1: Graph Neural Networks

**PPoPP 2025 · 2025 年 3 月 3 日 10:00–11:00 · Acacia D · Session Chair：Miao Yin**

聚焦图神经网络的高效训练与推理：分布式动态图采样、利用稀疏张量核的图重排序，以及多 GPU 训练并行策略的自动选择。

本 Session 共收录 **3** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Helios: Efficient Distributed Dynamic Graph Sampling for Online GNN Inference](helios_efficient_distributed_dynamic_graph_sampling_for_online_gnn_inference.md) | Jie Sun 等 11 人 | 事件驱动预采样 + 查询感知缓存，吞吐最高 67×、P99 延迟最低 32× |
| 2 | [Accelerating GNNs on GPU Sparse Tensor Cores through N:M Sparsity-Oriented Graph Reordering](accelerating_gnns_on_gpu_sparse_tensor_cores_through_n_m_sparsity_oriented_graph_reordering.md) | Jou-An Chen 等 5 人 | 无损图重排序对齐 N:M 稀疏模式，SpMM 最高 43× 加速 |
| 3 | [Adaptive Parallel Training for Graph Neural Networks](adaptive_parallel_training_for_graph_neural_networks.md) | Kaihao Ma 等 8 人 | 代价模型自动选择多 GPU 并行策略，训练时间降低 2× 以上 |

---

[PPoPP 2025 总览](../index.md) · [Session 2: GPU I →](../Session-2/index.md)
