---
title: "X-MoE: Enabling Scalable Training for Emerging Mixture-of-Experts Architectures on HPC Platforms"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Yueming Yuan; Ahan Gupta; Jianping Li; Sajal Dash; Feiyi Wang; Minjia Zhang"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# X-MoE: Enabling Scalable Training for Emerging Mixture-of-Experts Architectures on HPC Platforms

**中文标题：** 在 HPC 平台上实现新兴混合专家架构的可扩展训练

**所属 Session：** [Machine Learning: Training at Scale 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Yueming Yuan; Ahan Gupta; Jianping Li; Sajal Dash; Feiyi Wang; Minjia Zhang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap841&sess=sess302)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Emerging expert-specialized Mixture-of-Experts (MoE) architectures, such as DeepSeek-MoE, deliver strong model quality through fine-grained expert segmentation and large top-k routing. However, their scalability is limited by substantial activation memory overhead and costly all-to-all communication. Furthermore, current MoE training systems—primarily optimized for NVIDIA GPUs—perform suboptimally on non-NVIDIA platforms, leaving significant computational potential untapped. In this work, we present X-MoE, a novel MoE training system designed to deliver scalable training performance for next-generation MoE architectures. X-MoE achieves this via several novel techniques, including efficient padding-free MoE training with cross-platform kernels, redundancy-bypassing dispatch, and hybrid parallelism with sequence-sharded MoE blocks. Our evaluation on the Frontier supercomputer, powered by AMD MI250X GPUs, shows that X-MoE scales DeepSeek-style MoEs up to 545 billion parameters across 1,02

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
