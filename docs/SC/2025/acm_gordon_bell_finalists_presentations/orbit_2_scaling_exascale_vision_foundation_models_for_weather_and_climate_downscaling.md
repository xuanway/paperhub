---
title: "ORBIT-2: Scaling Exascale Vision Foundation Models for Weather and Climate Downscaling"
description: "SC 2025 · ACM Gordon Bell Finalists Presentations · Xiao Wang; Jong-Youl Choi; Takuya Kurihaya; Isaac Lyngaas; Hong-Jun Yoon; Nasik "
tags:
  - "SC2025"
  - "ACM Gordon Bell Finalists Presentations"
---

# ORBIT-2: Scaling Exascale Vision Foundation Models for Weather and Climate Downscaling

**中文标题：** 扩展百亿亿次视觉基础模型以进行天气与气候降尺度

**所属 Session：** [ACM Gordon Bell Finalists Presentations](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：ACM Gordon Bell Finalists Presentations。</p>
<p class="paper-seo-summary__tags">SC 2025 · ACM Gordon Bell Finalists Presentations</p>
</div>

**作者**：Xiao Wang; Jong-Youl Choi; Takuya Kurihaya; Isaac Lyngaas; Hong-Jun Yoon; Nasik Muhammad Nafi; Aristeidis Tsaris; Fan Ming; Ashwin M Aji; Maliha Hossain; Mohamed Wahib; Dali Wang; Peter Thornton; Moetasim Ashfaq; Prasanna Balaprakash; Dan Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap875&sess=sess577)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Sparse observations and coarse-resolution climate models limit regional decision-making, underscoring the need for robust downscaling. However, existing AI methods struggle with generalization across variables and geographies and are constrained by the quadratic complexity of Vision Transformer (ViT) self-attention. We introduce ORBIT-2, a scalable foundation model for global, high-resolution climate downscaling. ORBIT-2 incorporates two key innovations: (1) Residual Slim ViT (Reslim), a lightweight architecture with residual learning and Bayesian regularization for efficient, robust prediction; and (2) TILES, a tile-wise sequence-scaling algorithm that reduces self-attention complexity from quadratic to linear, enabling long-sequence processing and massive parallelism. ORBIT-2 scales to 10 billion parameters across 32,768 GPUs, achieving up to 1.8 ExaFLOPS sustained throughput and 92%–98% strong scaling efficiency. It supports downscaling to 0.9 km global resolution and processes sequ

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
