---
title: "Compile-Time QoS Scheme for Deep Learning Inferences"
description: "SC 2025 · Machine Learning: Inference and Serving · Sungin Hong; Hyunjun Kim; Hwansoo Han"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# Compile-Time QoS Scheme for Deep Learning Inferences

**中文标题：** 面向深度学习推理的编译时服务质量方案

**所属 Session：** [Machine Learning: Inference and Serving](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Sungin Hong; Hyunjun Kim; Hwansoo Han

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap568&sess=sess168)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

With the proliferation of deep learning technologies across various service domains, the sharing of accelerators such as GPUs, TPUs, and NPUs for inference processing has become increasingly common. These accelerators must efficiently handle multiple deep learning services operating concurrently. However, inference requests, characterized by sequences of short-duration kernels, create significant challenges for online schedulers attempting to maintain quality of service (QoS) guarantees. This paper presents QoSlicer, a novel compile-time QoS management framework that employs kernel slicing to relieve the burden on schedulers. By generating multiple pre-determined slicing plans, QoSlicer enables more efficient, lightweight QoS scheduling while ensuring target latency requirements are met. Our approach incorporates a heuristic search algorithm to identify optimal slicing plans and implements robust performance estimation models to validate these plans. Our experimental evaluation across

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
