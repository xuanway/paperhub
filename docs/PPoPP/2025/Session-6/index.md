---
title: "Session 6: Large Language Models"
description: "PPoPP 2025 Session 6（Large Language Models），2025 年 3 月 4 日 10:00–11:00，Acacia D，共 3 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-6"
  - "Large Language Models"
---

# Session 6: Large Language Models

**PPoPP 2025 · 2025 年 3 月 4 日 10:00–11:00 · Acacia D · Session Chair：Minjia Zhang**

围绕大语言模型的训练与推理：量化批量推理 kernel、长上下文训练的权重流水并行，以及注意力机制的算法级容错。

本 Session 共收录 **3** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models](marlin_mixed_precision_auto_regressive_parallel_inference_on_large_language_models.md) | Elias Frantar 等 5 人 | 批量量化推理 kernel，batch 16–32 近 4× 加速，端到端 2.8× |
| 2 | [WeiPipe: Weight Pipeline Parallelism for Communication-Effective Long-Context Large Model Training](weipipe_weight_pipeline_parallelism_for_communication_effective_long_context_large_model_training.md) | Junfeng Lin 等 6 人 | 由传激活改为传权重，降低长上下文训练通信量 |
| 3 | [ATTNChecker: Highly-Optimized Fault Tolerant Attention for Large Language Model Training](attnchecker_highly_optimized_fault_tolerant_attention_for_large_language_model_training.md) | Yuhang Liang 等 6 人 | 首个注意力 ABFT，训练开销 7%，恢复开销降 49× |

---

[← Session 5: Deep Neural Networks](../Session-5/index.md) · [PPoPP 2025 总览](../index.md) · [Session 7: Scheduling and Resource Management →](../Session-7/index.md)
