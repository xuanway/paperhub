---
title: "Balanced and Elastic End-to-End Training of Dynamic LLMs"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Mohamed Wahib; Muhammed Abdullah Soyturk; Didem Unat"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# Balanced and Elastic End-to-End Training of Dynamic LLMs

**中文标题：** 动态大语言模型的均衡弹性端到端训练

**所属 Session：** [Machine Learning: Training at Scale 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Mohamed Wahib; Muhammed Abdullah Soyturk; Didem Unat

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap160&sess=sess302)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

To reduce computational and memory costs in large language models (LLMs), dynamic workload reduction schemes like Mixture of Experts (MoEs), parameter pruning, layer freezing, sparse attention, early token exit, and Mixture of Depths (MoDs) have emerged. However, these methods introduce severe workload imbalances, limiting their practicality for large-scale distributed training. We propose DynMo, an autonomous dynamic load-balancing solution that ensures optimal compute distribution when using pipeline parallelism in training dynamic models. DynMo adaptively balances workloads, dynamically packs tasks into fewer workers to free idle resources, and supports both multi-GPU single-node and multi-node systems. Compared to static training methods (Megatron-LM, DeepSpeed), DynMo accelerates training by up to 1.23x (MoEs), 3.18x (pruning), 2.23x (layer freezing), 4.02x (sparse attention), 4.52x (early exit), and 1.17x (MoDs).

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
