---
title: "GreenMix: Energy-Efficient Serverless Computing via Randomized Sketching on Asymmetric Multi-Cores"
description: "SC 2025 · System Software and Cloud Computing: Resource Utilization · Rohan Basu Roy; Tirthak Patel; Baolin Li; Sid Samsi; Vijay Gadepally; Devesh Tiw"
tags:
  - "SC2025"
  - "System Software and Cloud Computing: Resource Utilization"
---

# GreenMix: Energy-Efficient Serverless Computing via Randomized Sketching on Asymmetric Multi-Cores

**中文标题：** 通过非对称多核上的随机草图计算实现节能无服务器计算

**所属 Session：** [System Software and Cloud Computing: Resource Utilization](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：System Software and Cloud Computing: Resource Utilization。</p>
<p class="paper-seo-summary__tags">SC 2025 · System Software and Cloud Computing: Resource Utilization</p>
</div>

**作者**：Rohan Basu Roy; Tirthak Patel; Baolin Li; Sid Samsi; Vijay Gadepally; Devesh Tiwari

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap662&sess=sess370)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

GreenMix is motivated by the renewed interest in asymmetric multi-core processors and the emergence of the serverless computing model. Asymmetric multi-cores offer better energy and performance trade-offs by placing different core types on the same die. However, existing serverless scheduling techniques do not leverage these benefits. GreenMix is the first serverless work to reduce energy and serverless keep-alive costs while meeting QoS targets by leveraging asymmetric multi-cores. GreenMix employs randomized sketching, tailored for serverless function execution and keep-alive, and leverages processor asymmetry, to perform within 10% of the optimal solution in terms of energy efficiency and keep-alive cost reduction. GreenMix’s effectiveness is demonstrated through evaluations with production-grade serverless function invocation traces on different clusters made up of ARM big.LITTLE and Intel Alder asymmetric multi-core processors. GreenMix outperforms competing serverless frameworks

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
