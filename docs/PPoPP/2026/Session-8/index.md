---
title: "Session 8: Distributed Training"
description: "PPoPP 2026 Session 8（Distributed Training），2026 年 2 月 3 日 14:10–15:30，Balmoral，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-8"
  - "Distributed Training"
---

# Session 8: Distributed Training

**PPoPP 2026 · 2026 年 2 月 3 日 14:10–15:30 · Balmoral · Session Chair：Bo Fang**

聚焦分布式训练系统：可定制的集合通信压缩库、弹性容错训练、长序列 Transformer 的注意力并行流水，以及训练慢/挂起异常诊断。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training](coccl_a_collective_communication_library_supporting_easy_integration_and_configuration_of_customized_compression_for_scalable_llm_training.md) | Xingchen Liu 等 14 人 | NCCL 之上的压缩集成通信库，3D 并行训练吞吐提升 1.24× |
| 2 | [Elastor: Elastic and Efficient Model Partitioning and Checkpointing for Fault-Tolerant Distributed Training](elastor_elastic_and_efficient_model_partitioning_and_checkpointing_for_fault_tolerant_distributed_training.md) | Xuanyu Wang 等 7 人 | 异构划分+划分无关细粒度检查点，任意 GPU 数弹性恢复 |
| 3 | [HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism](helixpipe_efficient_distributed_training_of_long_sequence_transformers_with_attention_parallel_pipeline_parallelism.md) | Geng Zhang 等 5 人 | 注意力并行流水+无注意力重算，7B/128k 序列提速 26% |
| 4 | [🏆 CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training](ccl_d_a_high_precision_diagnostic_system_for_slow_and_hang_anomalies_in_large_scale_model_training.md) | Yida Gu 等 20 人 | rank 级实时探针+自动根因定位，6 分钟内锁定故障 GPU 卡 |

### 获奖

- **CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training** —— Best Paper Nominee

---

[← Session 7: Cluster and Cloud Computing](../Session-7/index.md) · [PPoPP 2026 总览](../index.md) · [Session 9: Parallel Algorithms →](../Session-9/index.md)
