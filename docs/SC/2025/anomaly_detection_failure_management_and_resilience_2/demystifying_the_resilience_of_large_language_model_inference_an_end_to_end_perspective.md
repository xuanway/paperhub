---
title: "Demystifying the Resilience of Large Language Model Inference: An End-to-End Perspective"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 2 · Yu Sun; Zachary Coalson; Shiyang Chen; Hang Liu; Zhao Zhang; Sanghyun Hong; Bo F"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 2"
---

# Demystifying the Resilience of Large Language Model Inference: An End-to-End Perspective

**中文标题：** 揭示大语言模型推理的弹性：端到端视角

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 2</p>
</div>

**作者**：Yu Sun; Zachary Coalson; Shiyang Chen; Hang Liu; Zhao Zhang; Sanghyun Hong; Bo Fang; Lishan Yang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap301&sess=sess178)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Deep neural networks are known to be resilient to random bitwise faults in their parameters. However, this resilience has primarily been established through evaluations on classification models. The extent to which this claim holds for large language models remains under-explored. In this work, we conduct an extensive measurement study on the impact of random bitwise faults in commercial-scale language model inference. We first expose that these language models are not truly resilient to random bit-flips. While aggregate metrics such as accuracy may suggest resilience, an in-depth inspection of the generated outputs shows significant degradation in text quality. Our analysis also shows that tasks requiring more complex reasoning suffer more from performance and quality degradation. Moreover, we extend our resilience analysis to models with augmented reasoning capabilities, such as Chain of Thought or Mixture of Experts architectures.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
