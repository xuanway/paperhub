---
title: "CogSys: Efficient and Scalable Neurosymbolic Cognition System via Algorithm-Hardware Co-Design"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# CogSys: Efficient and Scalable Neurosymbolic Cognition System via Algorithm-Hardware Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Zishen Wan (Georgia Tech), Hanchen Yang (Georgia Tech), Ritik Raj (Georgia Tech), Che-Kai Liu (Georgia Tech), Ananda Samajdar (IBM), Arijit Raychowdhury (Georgia Tech), Tushar Krishna (Georgia Tech)
**会议**：HPCA 2025

---

## 中文标题

CogSys：通过算法—硬件协同设计的高效可扩展神经符号认知系统

## 英文摘要

Neurosymbolic AI is an emerging compositional paradigm that fuses neural learning with symbolic reasoning to enhance the transparency, interpretability, and trustworthiness of AI. It also exhibits higher data efficiency making it promising for edge deployments. Despite the algorithmic promises and demonstrations, unfortunately executing neurosymbolic workloads on current hardware (CPU/GPU/TPU) is challenging due to higher memory intensity, greater compute heterogeneity and access pattern irregularity, leading to severe hardware underutilization. This work proposes CogSys, a characterization and co-design framework dedicated to neurosymbolic AI system acceleration, aiming to win both reasoning efficiency and scalability. On the algorithm side, CogSys proposes an efficient factorization technique to alleviate compute and memory overhead. On the hardware side, CogSys proposes a scalable neurosymbolic architecture with reconfigurable neuro/symbolic processing elements (nsPE) and bubble streaming (BS) dataflow with spatial-temporal (ST) mapping for highly parallel and efficient neurosymbolic computation. On the system side, CogSys features an adaptive workload-aware scheduler (adSCH) to orchestrate heterogeneous kernels and enhance resource utilization. Evaluated across cognitive workloads, CogSys enables reconfigurable support for neural and symbolic kernels and exhibits >75× speedup over TPU-like systolic array with only <5% area overhead, as benchmarked under the TSMC 28nm technology node. CogSys achieves 4×- 96× speedup compared to desktop and edge GPUs. For the first time, CogSys enables real-time abduction reasoning towards human fluid intelligence, requiring only 0.3 s per reasoning task with 4 mm² area and 1.48 W power consumption.

## 中文摘要

神经符号 AI 是一种新兴的组合式范式，将神经学习与符号推理融合，以提升 AI 的透明度、可解释性与可信度。它还展现出更高的数据效率，使其在边缘部署中颇具前景。尽管在算法上已有诸多承诺与演示，但在当前硬件（CPU/GPU/TPU）上执行神经符号负载仍然困难，原因是更高的内存强度、更强的计算异构性与访问模式的不规则性，导致硬件严重利用不足。本文提出 CogSys，一个专用于神经符号 AI 系统加速的刻画与协同设计框架，致力于同时赢得推理效率与可扩展性。在算法侧，CogSys 提出一种高效的因子分解技术，以缓解计算与内存开销。在硬件侧，CogSys 提出一种可扩展的神经符号架构，具备可重构的神经/符号处理单元（nsPE），以及采用时空（ST）映射的冒泡流式（BS）数据流，实现高度并行且高效的神经符号计算。在系统侧，CogSys 具备自适应负载感知调度器（adSCH），以编排异构内核并提升资源利用率。在认知负载上的评估表明，CogSys 可对神经与符号内核提供可重构支持，在 TSMC 28nm 工艺节点下相比类 TPU 的脉动阵列实现了超过 75 倍加速，而面积开销不足 5%。与桌面和边缘 GPU 相比，CogSys 实现 4 倍至 96 倍加速。CogSys 首次使面向人类流体智力的实时溯因推理成为可能，每个推理任务仅需 0.3 秒，面积 4 mm²、功耗 1.48 W。
