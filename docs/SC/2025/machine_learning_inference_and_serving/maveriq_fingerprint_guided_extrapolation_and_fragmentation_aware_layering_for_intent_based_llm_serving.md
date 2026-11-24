---
title: "MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving"
description: "SC 2025 · Machine Learning: Inference and Serving · Dimitrios Liakopoulos; Prasoon Sinha; Tianrui Hu; Myungjin Lee; Neeraja J. Yadwa"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving

**中文标题：** 面向意图驱动大语言模型服务的指纹引导外推与碎片感知分层

**所属 Session：** [Machine Learning: Inference and Serving](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Dimitrios Liakopoulos; Prasoon Sinha; Tianrui Hu; Myungjin Lee; Neeraja J. Yadwadkar

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap709&sess=sess168)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Large language models (LLMs) are becoming ubiquitous across industries, where applications demand diverse user intents. To meet those intents, developers must manually explore combinations of parallelism and compression techniques that affect resource usage, latency, cost, and accuracy. Prior works automate this process but incur high profiling costs, inefficient GPU use, or ignore diverse user-intents. We build MaverIQ, an automated intent-based LLM inference serving system that translates user-expressed intents into LLM deployment configurations and deploys the chosen configurations to improve operational cost for the provider. To reduce profiling costs, MaverIQ introduces and observes LLM fingerprint—a compact proxy of the LLM—under a few configurations, and uses novel analytical models to extrapolate the observed fingerprint data to the full LLM. To cut provider costs, we exploit our key observation that uneven LLM layer distribution minimally affects inference latency. MaverIQ cut

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
