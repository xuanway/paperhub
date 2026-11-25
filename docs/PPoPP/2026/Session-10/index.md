---
title: "Session 10: ML Inference"
description: "PPoPP 2026 Session 10（ML Inference），2026 年 2 月 3 日 15:50–17:10，Balmoral，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-10"
  - "ML Inference"
---

# Session 10: ML Inference

**PPoPP 2026 · 2026 年 2 月 3 日 15:50–17:10 · Balmoral · Session Chair：Hailong Yang**

关注 ML 推理系统：视觉基础模型的显存平滑、多 SLO LLM 服务调度、混合分辨率扩散模型服务，以及数据特征感知的扩散模型服务。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [BEEMS: Boosting Machine Vision Efficiency via Computation Graph-Based Memory Smoothing](beems_boosting_machine_vision_efficiency_via_computation_graph_based_memory_smoothing.md) | Hanjing Shen 等 5 人 | 高峰算子降内存、低谷算子提延迟，峰值内存最多降 90% |
| 2 | [Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving](laser_unlocking_layer_level_scheduling_for_efficient_multi_slo_llm_serving.md) | Jianxiong Liao 等 5 人 | 层级调度突破迭代级限制，同 SLO 下吞吐提升逾 1.67× |
| 3 | [MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models](mixfusion_a_patch_level_parallel_serving_system_for_mixed_resolution_diffusion_models.md) | Desen Sun 等 3 人 | patch 级并行批处理混合分辨率请求，SLO 满足率 +30.1% |
| 4 | [ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models](chitudiffusion_a_data_characteristic_aware_serving_system_for_diffusion_models.md) | Chengzhang Wu 等 7 人 | 子图切分 + 多引擎协同，A100/H100 吞吐最高 2.13×/2.19× |

---

[← Session 9: Parallel Algorithms](../Session-9/index.md) · [PPoPP 2026 总览](../index.md) · [Session 11: Graphs and Graph Neural Networks →](../Session-11/index.md)
