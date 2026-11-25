---
title: "Session 4: Memory"
description: "PPoPP 2025 Session 4（Memory），2025 年 3 月 3 日 15:40–16:40，Acacia D，共 3 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-4"
  - "Memory"
---

# Session 4: Memory

**PPoPP 2025 · 2025 年 3 月 3 日 15:40–16:40 · Acacia D · Session Chair：Dong Li**

关注内存系统与数据移动：小对象 KV 缓存、虚拟机页预取，以及面向 MoE 的跨 GPU 共享内存通信融合。

本 Session 共收录 **3** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [AC-Cache: A Memory-Efficient Caching System for Small Objects via Exploiting Access Correlations](ac_cache_a_memory_efficient_caching_system_for_small_objects_via_exploiting_access_correlations.md) | Fulin Nan 等 8 人 | 面向小对象的访问相关性缓存，尾延迟降 5.1%–80.2% |
| 2 | [Effectively Virtual Page Prefetching via Spatial-Temporal Patterns for Memory-intensive Cloud Applications](effectively_virtual_page_prefetching_via_spatial_temporal_patterns_for_memory_intensive_cloud_applications.md) | Yun Wang 等 9 人 | 面向 VM 的时空模式页预取，性能损失降低 45% |
| 3 | [Harnessing Inter-GPU Shared Memory for Seamless MoE Communication-Computation Fusion](harnessing_inter_gpu_shared_memory_for_seamless_moe_communication_computation_fusion.md) | Hulin Wang 等 5 人 | 共享内存替代 All2All，平均比 FasterMoE 快 2.48× |

---

[← Session 3: Concurrent Data Structures and Synchronization I](../Session-3/index.md) · [PPoPP 2025 总览](../index.md) · [Session 5: Deep Neural Networks →](../Session-5/index.md)
