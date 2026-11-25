---
title: "PatternSketch: General and Runtime Reconfigurable Time-series Network Traffic Pattern Detection"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Yang Du (Soochow University, Suzhou, China), Dan Wang (Soochow University, Suzho"
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# PatternSketch: General and Runtime Reconfigurable Time-series Network Traffic Pattern Detection

**中文标题：** PatternSketch：通用且可运行时重构的时间序列网络流量模式检测

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Yang Du (Soochow University, Suzhou, China), Dan Wang (Soochow University, Suzhou, China), He Huang (Soochow University, Suzhou, China), Hanwen Zhang (Soochow University, Suzhou, China), Jianzhi Tang (Soochow University, Suzhou, China), Fu Xiao (Nanjing University of Posts and Telecommunications, Nanjing, China), Yu-E Sun (Soochow University, Suzhou, China)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769337)

## 英文摘要

Network traffic measurement is indispensable for many network management tasks. Time-series traffic pattern detection extends the benefits of traditional single-period flow measurement by revealing dynamic flow behaviors, but also yields higher complexity. When multiple patterns must be monitored simultaneously, building a separate sketch for each pattern is prohibitive since programmable switches typically allow only one resource-intensive sketch. In this paper, we propose PatternSketch, which enables general and dynamically reconfigurable time-series pattern detection within a single sketch. PatternSketch unifies the detection of diverse patterns with a Pattern Automaton and decomposes the pattern detection process into two phases in the data plane, while allowing operators to reconfigure the active set of monitoring patterns at runtime without taking the switch offline. Our implementation on an Intel Tofino switch demonstrates that PatternSketch can operate at line rate, detecting multiple patterns concurrently while using only tens of kilobytes of SRAM. This significantly reduces both computational and storage resource consumption compared to deploying multiple, pattern-specific sketches. Evaluations on four real-world datasets show that the hardware version of PatternSketch maintains over 90% F1 scores while simultaneously detecting six time-series patterns (three representative and three newly proposed) with as little as 200KB of memory.

## 中文摘要

网络流量测量对许多网络管理任务不可或缺。时间序列流量模式检测通过揭示动态流行为，扩展了传统单周期流测量的优势，但也带来了更高的复杂度。当需要同时监测多种模式时，为每种模式单独构建一个 sketch 是不可行的，因为可编程交换机通常只允许一个资源密集型的 sketch。本文提出 PatternSketch，它在单个 sketch 内实现了通用且可动态重构的时间序列模式检测。PatternSketch 用模式自动机统一了对多种模式的检测，并在数据面将模式检测过程分解为两个阶段，同时允许运维人员在运行时重构活跃的监测模式集合，而无需使交换机下线。我们在 Intel Tofino 交换机上的实现表明，PatternSketch 可以线速运行，仅使用数十 KB 的 SRAM 即可同时检测多种模式。与部署多个针对特定模式的 sketch 相比，这显著降低了计算和存储资源消耗。在四个真实数据集上的评估表明，PatternSketch 的硬件版本在同时检测六种时间序列模式（三种代表性模式与三种新提出的模式）时，仅需 200KB 内存即可保持 90% 以上的 F1 分数。

**英文关键词：** Sketch, Network Traffic Pattern Detection, Network Measurement

**中文关键词：** Sketch、网络流量模式检测、网络测量

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
