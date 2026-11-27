---
title: "Characterizing Cloud-Native LLM Inference at ByteDance and Exposing Optimization Challenges and Opportunities for Future AI Accelerators"
description: "HPCA 2026 · Industry Track"
tags:
  - "HPCA2026"
  - "Industry Track"
---

# Characterizing Cloud-Native LLM Inference at ByteDance and Exposing Optimization Challenges and Opportunities for Future AI Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Industry Track。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Industry Track</p>
</div>

**论文链接**：
**作者**：Jingwei Cai ByteDance Seed , Dehao Kong , Huang Hantao ByteDance Seed , Zishan Jiang ByteDance Seed , Zixuan Ma ByteDance Seed , Qingyu Guo ByteDance Seed , Zhenxing Zhang ByteDance Seed , Guiming Shi Tsinghua University , Mingyu Gao Tsinghua University , Kaisheng Ma Tsinghua University , Minghui Yu ByteDance Seed
**会议**：HPCA 2026

---

## 中文标题

剖析字节跳动的云原生 LLM 推理：揭示未来 AI 加速器面临的优化挑战与机遇

## 英文摘要

As a major provider of LLM inference services, ByteDance has continuously explored diverse accelerator options to meet the rapidly growing inference demands of various heterogeneous LLM scenarios with higher cost-effectiveness, thereby enabling LLMs to serve more people worldwide. However, during this process, we have found that the complexity and opacity of cloud scenarios and corresponding cloud accelerators make it difficult for academia and many innovative chip startups to fully understand the real demands and challenges of these scenarios, which in turn severely restricts innovation and application potential in this field. To bridge this gap, we first present and analyze the data and characteristics of the ByteDance Doubao LLM app across multiple dimensions, helping the community understand real-world cloud scenarios, and detail the challenges and opportunities we have identified. Second, we propose and plan to open-source our multi-level evaluation framework, XPU-Perf, which includes benchmarks spanning instructions, operators, and models. This framework improves interpretability and trustworthiness, and helps promising new accelerator architectures gain wider adoption and development. Finally, we present comparative results of four typical accelerators, summarize their shortcomings and challenges, conduct in-depth analysis, and highlight numerous architectural and scheduling innovation opportunities we have observed.

## 中文摘要

作为主要的 LLM 推理服务提供商，字节跳动持续探索多样化加速器选项，以满足各类异构 LLM 场景快速增长的推理需求并提升性价比，从而让 LLM 服务全球更多用户。然而在此过程中，我们发现云场景及相应云加速器的复杂性与不透明性，使学术界和众多创新型芯片初创企业难以充分理解这些场景的真实需求与挑战，进而严重制约了该领域的创新与应用潜力。为弥合这一鸿沟，我们首先从多个维度呈现并分析字节跳动豆包 LLM 应用的数据与特征，帮助社区理解真实的云场景，并详述我们识别出的挑战与机遇。其次，我们提出并计划开源多层级评测框架 XPU-Perf，其包含覆盖指令、算子与模型的基准测试；该框架提升了可解释性与可信度，有助于有前景的新型加速器架构获得更广泛的采用与发展。最后，我们给出四种典型加速器的对比结果，总结其不足与挑战并深入分析，强调我们观察到的众多架构与调度创新机会。
