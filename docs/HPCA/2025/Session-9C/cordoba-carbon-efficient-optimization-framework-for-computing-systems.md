---
title: "CORDOBA: Carbon-Efficient Optimization Framework for Computing Systems"
description: "HPCA 2025 · Finding the Best Table"
tags:
  - "HPCA2025"
  - "Finding the Best Table"
---

# CORDOBA: Carbon-Efficient Optimization Framework for Computing Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Finding the Best Table。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Finding the Best Table</p>
</div>

**论文链接**：
**作者**：Mariam Elgamal (Harvard University), Doug Carmean (Meta), Elnaz Ansari (Meta), Okay Zed (Meta), Ramesh Peri (Meta), Srilatha Manne (Meta), Udit Gupta (Meta), Gu-Yeon Wei (Harvard University), David Brooks (Harvard University), Gage Hills (Harvard University), Carole-Jean Wu (Meta)
**会议**：HPCA 2025

---

## 中文标题

CORDOBA：面向计算系统的碳高效优化框架

## 英文摘要

The world’s push toward an environmentally sustainable society is highly dependent on the semiconductor industry. Despite existing carbon modeling efforts to quantify carbon footprint of computing systems, optimizing carbon footprint in large design spaces—while also considering trade-offs in power, performance, and area—is especially challenging. To address this need, we present CORDOBA, a carbon-aware optimization framework that optimizes carbon efficiency. We quantify carbon efficiency using the total Carbon Delay Product metric (tCDP): the product of total carbon and application execution time. We justify why tCDP is an effective metric for quantifying carbon efficiency. We use CORDOBA to explore the large design space for carbon-efficient specialized hardware, and identify distinct carbon-efficient optimal designs across operational use (eliminating up to 98% of the design space) despite uncertainty in carbon footprint parameters. We quantify opportunities to improve tCDP for real system case studies: (a) optimizing hardware provisioning from 8 to 4 cores in real system CPUs improves tCDP by 1.25×; and (b) leveraging advanced three-dimensional (3D) integration techniques (3D stacking of separately-fabricated logic and memory chips) improves tCDP by 6.9× versus conventional systems.

## 中文摘要

世界迈向环境可持续社会的进程高度依赖半导体产业。尽管已有碳排放建模工作来量化计算系统的碳足迹，但在庞大设计空间中优化碳足迹、同时兼顾功耗、性能与面积（PPA）的折中，尤其具有挑战性。为满足这一需求，我们提出 CORDOBA，一个以碳效率为优化目标的碳感知优化框架。我们使用总碳时延积（tCDP）指标来量化碳效率，即总碳量与应用程序执行时间的乘积。我们论证了 tCDP 是量化碳效率的有效指标。我们使用 CORDOBA 探索面向碳高效专用硬件的大设计空间，并在碳足迹参数存在不确定性的情况下，识别出跨运行使用场景中各自不同的碳高效最优设计（消除了最多 98% 的设计空间）。我们针对真实系统案例研究量化了改善 tCDP 的机会：（a）将真实系统 CPU 的硬件配置从 8 核优化为 4 核可改善 tCDP 1.25×；（b）相较传统系统，利用先进的三维（3D）集成技术（分别制造的逻辑芯片与存储芯片的 3D 堆叠）可改善 tCDP 6.9×。
