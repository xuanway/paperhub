# MoE-Lego: A Plane-Grained System for Dynamic-Precision MoE Offloading

**中文标题**：MoE-Lego：面向动态精度 MoE 卸载的位平面粒度系统

**所属 Session**：[Session 10: LLM Inference II](index.md) · [ATC 2026](../index.md)

**作者**：Haozhe Wei (Shanghai Jiao Tong University), Xiaofeng Hou (Shanghai Jiao Tong University), Wenfeng Wang (Shanghai Jiao Tong University), Cheng Xu (Shanghai Jiao Tong University), Jiacheng Liu (Shanghai Jiao Tong University), Chao Li (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

## 英文摘要
Multi-precision inference balances serving efficiency and model quality for large MoE LLMs under limited memory. However, changing expert precision at runtime exposes a fundamental tradeoff in existing systems: they either waste GPU memory by storing multiple precision replicas, or incur high I/O overhead by reloading whole expert tensors. Thus, achieving both dynamic precision and efficient execution remains an open challenge. We present MoE-Lego, an end-to-end MoE inference system that uses bitplane representation as the substrate for dynamic multi-precision execution. MoE-Lego first constructs a single nested bitplane artifact with routing-aligned calibration, so all supported precisions share the same base planes. Its runtime scheduler changes precision by moving, retaining, and demoting only the required bitplanes, making the I/O cost approximately proportional to the bit-width delta instead of the full expert size. Its GPU executor treats target precision as an execution dimension: it builds precision buckets for routed FFN work and computes each bucket with grouped bitplane kernels, avoiding fragmented per-expert computation. Across Qwen1.5-MoE, Qwen3-MoE, and Phi-3.5-MoE on A100 and RTX 4090, MoE-Lego achieves geometric-mean speedups of 3.72× for prefill and 2.83× for decode over the baselines, while preserving near-16-bit model quality. An additional evaluation on Jetson Orin demonstrates its applicability to SSD-backed expert offloading.

## 中文摘要
多精度推理在有限内存下为大型 MoE LLM 权衡服务效率与模型质量。然而，在运行时改变专家精度暴露了现有系统中的一个根本性权衡：它们要么因存储多个精度副本而浪费 GPU 内存，要么因重新加载整个专家张量而带来高 I/O 开销。因此，同时实现动态精度与高效执行仍是一个开放挑战。我们提出 MoE-Lego，一个端到端 MoE 推理系统，它以位平面表示作为动态多精度执行的基底。MoE-Lego 首先通过路由对齐的校准构建单一的嵌套位平面产物，使所有支持的精度共享相同的基础平面。其运行时调度器仅通过移动、保留和降级所需的位平面来改变精度，使 I/O 开销大致正比于位宽差值而非完整的专家大小。其 GPU 执行器将目标精度视为一个执行维度：它为路由后的 FFN 工作构建精度桶，并用分组的位平面内核计算每个桶，避免碎片化的逐专家计算。在 A100 和 RTX 4090 上跨 Qwen1.5-MoE、Qwen3-MoE 和 Phi-3.5-MoE，MoE-Lego 相比基线取得预填充 3.72×、解码 2.83× 的几何平均加速，同时保持接近 16 位的模型质量。在 Jetson Orin 上的额外评估表明其适用于基于 SSD 的专家卸载。

## 英文关键词
Mixture-of-Experts, Expert Offloading, Dynamic Precision, Bitplane Representation

## 中文关键词
专家混合，专家卸载，动态精度，位平面表示

[返回 Session 10](index.md) · [返回 ATC 2026](../index.md)
