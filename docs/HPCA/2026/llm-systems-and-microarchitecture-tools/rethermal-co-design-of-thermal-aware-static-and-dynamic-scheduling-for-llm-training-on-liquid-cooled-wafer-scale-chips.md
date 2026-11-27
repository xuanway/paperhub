---
title: "ReThermal: Co-Design of Thermal-Aware Static and Dynamic Scheduling for LLM Training on Liquid-Cooled Wafer-Scale Chips"
description: "HPCA 2026 · LLM Systems and Microarchitecture Tools"
tags:
  - "HPCA2026"
  - "LLM Systems and Microarchitecture Tools"
---

# ReThermal: Co-Design of Thermal-Aware Static and Dynamic Scheduling for LLM Training on Liquid-Cooled Wafer-Scale Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Systems and Microarchitecture Tools。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Systems and Microarchitecture Tools</p>
</div>

**论文链接**：
**作者**：Chengran Li Tsinghua University , Huizheng Wang Tsinghua University , Jiaxin Liu Tsinghua University , Jingyao Liu Tsinghua University , Zhiheng Yue Tsinghua University , Xia Li Shanghai AI Lab , Shenfei Jiang Shanghai AI Lab , Jinyi Deng Tsinghua University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

ReThermal：液冷晶圆级芯片上 LLM 训练的热感知静态与动态调度协同设计

## 英文摘要

With the increasing demand for high computational power in Large Language Models, wafer-scale chips have emerged as a solution, providing the necessary integration and computing capability to meet these needs. However, their ultralarge area and extreme heat dissipation introduce critical thermal management challenges under liquid-cooling environments. In addressing this issue, we identify two key opportunities and three major challenges: the behavior–thermal black box, the wafer-scale simulation bottleneck, and the runtime heat–schedule drift. To tackle these challenges, we propose ReThermal, a holistic scheduling framework that integrates three innovations. First, we introduce behavior-driven thermal modeling to capture workload-induced compute, communication, and heat coupling patterns at the system level. Second, we develop a DNN-accelerated wafer-scale thermal simulator that enables fast and accurate temperature prediction, significantly reducing simulation time. Third, we implement an adaptive thermal-aware scheduling strategy that coordinates compile-time and runtime decisions to dynamically optimize task placement. Evaluations show that ReThermal reduces peak temperature by up to 8.0°C and improves throughput by up to 39.23%, providing a scalable and effective thermal control solution for future liquid-cooled wafer-scale systems.

## 中文摘要

随着大语言模型对高算力的需求不断上升，晶圆级芯片作为解决方案出现，提供了满足这些需求所需的集成度与计算能力。然而，其超大面积与极端散热在液冷环境下带来严峻的热管理挑战。针对该问题，我们识别出两个关键机遇与三大挑战：行为—热黑箱、晶圆级模拟瓶颈，以及运行时热—调度漂移。为应对这些挑战，我们提出 ReThermal，一个融合三项创新的整体调度框架。首先，我们引入行为驱动的热建模，在系统层面刻画负载引发的计算、通信与热的耦合模式。其次，我们开发 DNN 加速的晶圆级热模拟器，实现快速准确的温度预测，显著缩短模拟时间。第三，我们实现自适应的热感知调度策略，协同编译期与运行时决策以动态优化任务放置。评估表明，ReThermal 将峰值温度最多降低 8.0°C，并将吞吐最多提升 39.23%，为未来液冷晶圆级系统提供了可扩展且有效的热控制方案。
