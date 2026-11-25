---
title: "PowerQuant: Architecture-Agnostic GPU Power Estimation via Quantile Regression"
description: "HPDC 2026 · Session 11 — Communication, Workflows & Sustainability"
tags:
  - "HPDC2026"
  - "Session 11"
  - "Communication, Workflows & Sustainability"
---

# PowerQuant: Architecture-Agnostic GPU Power Estimation via Quantile Regression

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 11</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807591)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ChallaDPSS26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ChallaDPSS26)

**作者**：Aditya Challa, Tanish Desai, Gargi Alavani Prabhu, Snehanshu Saha, Santonu Sarkar

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）

---

## 英文摘要

Accurate prediction of NVIDIA GPU power consumption remains challenging due to rapid architectural evolution. Existing machinelearning–based power models are tightly coupled to specific GPU architectures and degrade sharply on unseen platforms, requiring retraining and extensive power measurements, which hinder scalability. This paper presents a quantile-regression–based GPU power prediction framework that enables architecture-agnostic power estimation using static analysis-based compile-time CUDA kernel features. The key insight is that architectural changes primarily induce systematic shifts in power scale, while the relative ordering of kernel power demands remains preserved. By learning power quantiles that capture this ordering and mapping them to new GPUs through one-time calibration, the proposed approach mitigates cross-architecture distribution shift. Extensive evaluation across multiple NVIDIA GPU generations shows that, on unseen architectures, the proposed method improves prediction accuracy by up to 30–50% over existing regression models, while maintaining comparable accuracy in in-distribution settings. The resulting low-overhead, generalizable power estimates make the approach practical for power-aware scheduling, energy budgeting, and sustainability-oriented resource management in large HPC systems.

## 中文摘要

由于架构的快速演进，准确预测 NVIDIA GPU 功耗仍具挑战性。现有基于机器学习的功耗模型与特定 GPU 架构紧密耦合，在未见过的平台上性能急剧下降，需要重新训练和大量功耗测量，阻碍了可扩展性。本文提出一个基于分位数回归的 GPU 功耗预测框架，利用基于静态分析的编译期 CUDA 核特征，实现架构无关的功耗估计。其核心洞见是：架构变化主要引起功耗尺度的系统性偏移，而核功耗需求的相对顺序得以保持。通过学习刻画该顺序的功耗分位数，并通过一次性校准将其映射到新 GPU，该方法缓解了跨架构的分布偏移。跨多个 NVIDIA GPU 世代的大量评估表明，在未见架构上，所提方法相比现有回归模型将预测精度最高提升 30–50%，同时在分布内场景中保持相当的精度。由此得到的低开销、可泛化的功耗估计，使该方法适用于大型 HPC 系统中的功耗感知调度、能耗预算和面向可持续性的资源管理。

---

[← 返回 Session 11 — Communication, Workflows & Sustainability](index.md)
