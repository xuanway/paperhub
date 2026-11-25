---
title: "Session 6: Mixed Precision and Quantization"
description: "PPoPP 2026 Session 6（Mixed Precision and Quantization），2026 年 2 月 3 日 11:30–12:50，Balmoral，共 4 篇论文。"
tags:
  - "PPoPP2026"
  - "Session-6"
  - "Mixed Precision and Quantization"
---

# Session 6: Mixed Precision and Quantization

**PPoPP 2026 · 2026 年 2 月 3 日 11:30–12:50 · Balmoral · Session Chair：Dingwen Tao**

围绕混合精度与量化：旋转混合精度量化、非均匀 3-bit LLM 推理、2-bit KV Cache 量化，以及分子动力学的 16-bit 混合精度。

本 Session 共收录 **4** 篇论文。

官方议程：[PPoPP 2026 Main Conference Papers](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [RoMeo: Mitigating Dual-dimensional Outliers with Rotated Mixed Precision Quantization](romeo_mitigating_dual_dimensional_outliers_with_rotated_mixed_precision_quantization.md) | Qihao Zhang 等 5 人 | 旋转把通道离群迁到 token 维，精度 +5.17%、2.10× |
| 2 | [High-Throughput Non-uniformly Quantized 3-bit LLM Inference](high_throughput_non_uniformly_quantized_3_bit_llm_inference.md) | YuAng Chen 等 3 人 | 融合反量化流水线，核级 4.82×、端到端 11.46× |
| 3 | [JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference](janusquant_accurate_and_efficient_2_bit_kv_cache_quantization_for_long_context_inference.md) | Chengyu Sun 等 6 人 | 2-bit KV cache 量化，省显存 5.3×、解码吞吐 4.45× |
| 4 | [🏆 HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff](hiercut_enabling_16_bit_format_mixed_precision_for_molecular_dynamics_through_hierarchical_cutoff.md) | Zeyu Song 等 8 人 | 按截断层分配 16-bit 精度，较 FP64 最高 3.75× |

### 获奖

- **HierCut: Enabling 16-bit Format Mixed Precision for Molecular Dynamics through Hierarchical Cutoff** —— Best Artifact Award

---

[← Session 5: Stencil and Sparse Matrix Computation](../Session-5/index.md) · [PPoPP 2026 总览](../index.md) · [Session 7: Cluster and Cloud Computing →](../Session-7/index.md)
