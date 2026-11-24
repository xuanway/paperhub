---
title: "HPC-R1: Characterizing R1-Like Large Reasoning Models on HPC"
description: "SC 2025 · Machine Learning: Training at Scale 1 · Adam Weingram; Duo Zhang; Zhonghao Chen; Hao Qi; Xiaoyi Lu"
tags:
  - "SC2025"
  - "Machine Learning: Training at Scale 1"
---

# HPC-R1: Characterizing R1-Like Large Reasoning Models on HPC

**中文标题：** 在 HPC 上刻画 R1 类大型推理模型

**所属 Session：** [Machine Learning: Training at Scale 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Training at Scale 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Training at Scale 1</p>
</div>

**作者**：Adam Weingram; Duo Zhang; Zhonghao Chen; Hao Qi; Xiaoyi Lu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap456&sess=sess302)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Large reasoning models (LRMs) are becoming increasingly popular as they offer advanced capabilities in logical inference, mathematical reasoning, and knowledge synthesis, even beyond those of standard language models. However, their complex training workflows present significant challenges in reproducibility, efficiency, and system-level optimization. This paper introduces HPC-R1, a comprehensive characterization of LRM training on a modern HPC cluster. We analyze all major stages, including supervised fine-tuning (SFT), Group Relative Policy Optimization (GRPO)-based reinforcement learning (RL), autoregressive generation, and distillation using customized state-of-the-art frameworks. Our detailed performance analysis reveals key system scaling behaviors. We find that GRPO-based reinforcement learning training is heavily communication-bound, with over 90% of GPU time spent in non-compute operations, and that SFT achieves stable GPU throughput near 9.8 TFLOPs. We also observe inference

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
