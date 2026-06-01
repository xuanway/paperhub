---
title: "ACTINA: Adapting Circuit-Switching Techniques for AI Networking Architectures"
description: "SC 2025 · Architectures and Networks: Networking · Zhenguo Wu; Benjamin Klenk; Larry Dennison; Keren Bergman"
tags:
  - "SC2025"
  - "Architectures and Networks: Networking"
---

# ACTINA: Adapting Circuit-Switching Techniques for AI Networking Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Architectures and Networks: Networking。</p>
<p class="paper-seo-summary__tags">SC 2025 · Architectures and Networks: Networking</p>
</div>

**作者**：Zhenguo Wu; Benjamin Klenk; Larry Dennison; Keren Bergman

**会议**：SC 2025 · St. Louis, MO

## 摘要

While traditional datacenters rely on static, electrically switched fabrics, Optical Circuit Switch (OCS)-enabled reconfigurable networks offer dynamic bandwidth allocation and lower power consumption. This work introduces a quantitative framework for evaluating reconfigurable networks in large-scale AI systems, guiding the adoption of various OCS and link technologies by analyzing trade-offs in reconfiguration latency, link bandwidth provisioning, and OCS placement. Using this framework, we develop two in-workload reconfiguration strategies and propose an OCS-enabled, multi-dimensional all-to-all topology that supports hybrid parallelism with improved energy efficiency. Our evaluation demonstrates that with state-of-the-art per-GPU bandwidth, the optimal in-workload strategy achieves up to 2.3x improvement over the commonly used one-shot approach when reconfiguration latency is low (<100μs). However, with sufficiently high bandwidth, one-shot reconfiguration can achieve comparable per

---

## 一句话总结

> 该工作属于 Architectures and Networks: Networking 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Architectures and Networks: Networking 领域贡献新的设计范式或评估框架。
