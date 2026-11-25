---
title: "Session 12: Optimizing Transformers"
description: "PPoPP 2026 Session 12（Optimizing Transformers），2026 年 2 月 3 日 17:15–18:15，Pyrmont，共 3 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-12"
  - "Optimizing Transformers"
---

# Session 12: Optimizing Transformers

**PPoPP 2026 · 2026 年 2 月 3 日 17:15–18:15 · Pyrmont · Session Chair：Shaoshuai Zhang**

围绕 Transformer 优化：利用张量-向量并行的全张量化注意力、GPU 稀疏 Transformer 推理，以及跨硬件后端的统一注意力框架。

本 Session 共收录 **3** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [FlashAttention-T: Towards Fully Tensorized Attention by Exploiting Tensor-Vector Parallelism](flashattention_t_towards_fully_tensorized_attention_by_exploiting_tensor_vector_parallelism.md) | Jianxing Xu 等 11 人 | softmax 卸载至张量核，H100 空窗比例降至 2.7%，最高 1.17× |
| 2 | [Accelerating Sparse Transformer Inference on GPU](accelerating_sparse_transformer_inference_on_gpu.md) | Wenhao Dai 等 9 人 | 稀疏 Transformer 行/块核 + 两阶段融合搜索，MHA 6×、端到端 1.4× |
| 3 | [MetaAttention: A Unified and Performant Attention Framework across Hardware Backends](metaattention_a_unified_and_performant_attention_framework_across_hardware_backends.md) | Feiyang Chen 等 12 人 | 打分+聚合抽象跨后端自动调优，原不支持配置最高 10.4× |

---

[← Session 11: Graphs and Graph Neural Networks](../Session-11/index.md) · [PPoPP 2026 总览](../index.md) · [Session 13: Matrix and Linear Algebra Algorithms →](../Session-13/index.md)
