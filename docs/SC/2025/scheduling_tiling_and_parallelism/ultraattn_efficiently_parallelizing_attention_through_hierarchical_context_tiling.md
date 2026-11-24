---
title: "UltraAttn: Efficiently Parallelizing Attention Through Hierarchical Context-Tiling"
description: "SC 2025 · Scheduling, Tiling, and Parallelism · Haoyu Yang; Zan Zong; Yuyang Jin; Kinman Lei; Jiaao He; Qigang Yang; Jidong Zhai"
tags:
  - "SC2025"
  - "Scheduling, Tiling, and Parallelism"
---

# UltraAttn: Efficiently Parallelizing Attention Through Hierarchical Context-Tiling

**中文标题：** 通过分层上下文分块高效并行化注意力

**所属 Session：** [Scheduling, Tiling, and Parallelism](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Scheduling, Tiling, and Parallelism。</p>
<p class="paper-seo-summary__tags">SC 2025 · Scheduling, Tiling, and Parallelism</p>
</div>

**作者**：Haoyu Yang; Zan Zong; Yuyang Jin; Kinman Lei; Jiaao He; Qigang Yang; Jidong Zhai

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap916&sess=sess286)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Long-context comprehension is a crucial capability for LLM. Context parallelism and irregular block sparse attention are two key technologies to accelerate long contextual training and inference. Existing context parallelism techniques for attention suffer from poor scalability, owing to their common characteristics: the striped-like partition pattern. The striped-like partition pattern causes high communication traffic and inflexible kernel granularity, which in turn results in low single-kernel device utilization. To address these problems, we propose UltraAttn, a novel context parallelism solution for irregular attention. UltraAttn hierarchically tiles the context to reduce communication cost. UltraAttn also performs context-tiling at the kernel level to adjust the granularity of kernels to trade off between kernel overlap and single-kernel device utilization. UltraAttn executes distributed attention with an ILP-based runtime to optimize latency. We evaluate UltraAttn on 64 GPUs. Ul

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
