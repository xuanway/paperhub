---
title: "Session 7: Cluster and Cloud Computing"
description: "PPoPP 2026 Session 7（Cluster and Cloud Computing），2026 年 2 月 3 日 11:30–12:50，Pyrmont，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-7"
  - "Cluster and Cloud Computing"
---

# Session 7: Cluster and Cloud Computing

**PPoPP 2026 · 2026 年 2 月 3 日 11:30–12:50 · Pyrmont · Session Chair：Ruslan Nikolaev**

关注集群与云计算：多租户云的最后一级缓存管理、零拷贝 RPC 序列化、GPU 到 CPU 的分布式迁移，以及 GPU 集群稀疏直接求解。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [Cacheman: A Comprehensive Last-Level Cache Management System for Multi-tenant Clouds](cacheman_a_comprehensive_last_level_cache_management_system_for_multi_tenant_clouds.md) | Xiaokang Hu 等 11 人 | 梯度式 LLC way 共享+秒级重分配，生产环境显著降低争用 SLA 违约 |
| 2 | [zBuffer: Zero-Copy and Metadata-Free Serialization for Fast RPC with Scatter-Gather Reflection](zbuffer_zero_copy_and_metadata_free_serialization_for_fast_rpc_with_scatter_gather_reflection.md) | Xiangyu Liu 等 5 人 | NIC scatter-gather+编译期静态反射，序列化快约 7×、P99 降 21% |
| 3 | [Scaling GPU-to-CPU Migration for Efficient Distributed Execution on CPU Clusters](scaling_gpu_to_cpu_migration_for_efficient_distributed_execution_on_cpu_clusters.md) | Ruobing Han 等 2 人 | 把 GPU 程序分布式迁移到 CPU 集群，集群吞吐平均比 GPU 高 2.59× |
| 4 | [🏆 Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters](trojan_horse_aggregate_and_batch_for_scaling_up_sparse_direct_solvers_on_gpu_clusters.md) | Yida Li 等 7 人 | 小任务聚合+批处理，A100 上 SuperLU_DIST 最高加速 418.79× |

### 获奖

- **Trojan Horse: Aggregate-and-Batch for Scaling Up Sparse Direct Solvers on GPU Clusters** —— Best Paper Nominee

---

[← Session 6: Mixed Precision and Quantization](../Session-6/index.md) · [PPoPP 2026 总览](../index.md) · [Session 8: Distributed Training →](../Session-8/index.md)
