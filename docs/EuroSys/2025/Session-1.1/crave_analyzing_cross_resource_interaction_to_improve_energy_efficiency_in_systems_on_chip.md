---
title: "CRAVE: Analyzing Cross-Resource Interaction to Improve Energy Efficiency in Systems-on-Chip"
description: "EuroSys 2025 · Operating Systems · Dipayan Mukherjee (University of Illinois, Urbana-Champaign), Sam Hachem (Univer"
tags:
  - "EuroSys2025"
  - "Operating Systems"
---

# CRAVE: Analyzing Cross-Resource Interaction to Improve Energy Efficiency in Systems-on-Chip

**中文标题：** 分析片上系统中的跨资源交互以提高能效

**所属 Session：** [Session 1.1: Operating Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Operating Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Operating Systems</p>
</div>

**作者**：Dipayan Mukherjee (University of Illinois, Urbana-Champaign), Sam Hachem (University of Illinois, Urbana-Champaign), Jeremy Bao (University of Illinois, Urbana-Champaign), Curtis Madsen (Sandia National Labs), Tian Ma (Sandia National Labs), Saugata Ghose (University of Illinois Urbana-Champaign), Gul Agha (University of Illinois at Urbana-Champaign)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717498)

## 英文摘要

Mobile platforms make use of dynamic voltage and frequency scaling (DVFS) to trade off runtime performance and power consumption for their systems-on-chip (SoCs). State-of-the-art governors in the OS use application-based characteristics to control the SoC’s DVFS settings for CPU cores, as well as the GPU in some SoCs. Through experimental characterization of real-world mobile platforms, we find that key SoC components have a complex relationship with one another, which directly affects their performance and power usage. This relationship is dependent on the architecture of the SoC as it is caused by the interaction of processing elements such as the CPU and GPU through a shared main memory. Unfortunately, existing application-oriented governors do not explicitly capture this design-induced relationship.

We propose a new governor, called CRAVE, which uses learned design characteristics to control DVFS settings. At design time, CRAVE identifies optimal DVFS settings for the SoC by sampling points across a multivariate space of frequency settings for the three major mobile system components: CPU cores, GPU, and memory. At runtime, CRAVE monitors resource utilization, in a manner similar to that of the existing simple governors that are built into today’s OS kernels, and then applies the previously-learned optimal settings. We implement CRAVE on two real mobile platforms: the ODROID-XU4 and the NVIDIA Jetson TX2. Compared to the best built-in Linux governor, CRAVE improves performance by 20% while reducing energy usage by 16% on the TX2, with similar gains on the XU4. CRAVE also shows an improvement over a state-of-the-art application-driven governor, with performance gains of 16% and energy savings of 10%.

## 中文摘要

移动平台利用动态电压频率调节（DVFS）在片上系统（SoC）的运行时性能与功耗之间进行权衡。当前操作系统中最先进的调速器利用基于应用的特征来控制 CPU 核心乃至某些 SoC 中 GPU 的 DVFS 设置。通过对真实移动平台进行实验性刻画，我们发现 SoC 的关键组件之间存在复杂的关系，这直接影响它们的性能与功耗。这种关系取决于 SoC 的体系结构，因为它是由 CPU、GPU 等处理单元通过共享主存进行交互所引起的。遗憾的是，现有面向应用的调速器并未显式刻画这种由设计引起的关系。

我们提出了一种新的调速器 CRAVE，它利用学习到的设计特征来控制 DVFS 设置。在设计时，CRAVE 通过在三个主要移动系统组件（CPU 核心、GPU 和内存）的频率设置所构成的多变量空间中采样，为 SoC 确定最优的 DVFS 设置。在运行时，CRAVE 以类似于当今操作系统内核内置的简单调速器的方式监控资源利用率，然后应用先前学到的最优设置。我们在两个真实的移动平台上实现了 CRAVE：ODROID-XU4 和 NVIDIA Jetson TX2。与最佳的内置 Linux 调速器相比，CRAVE 在 TX2 上将性能提升 20%，同时将能耗降低 16%，在 XU4 上取得了类似的收益。CRAVE 相较于最先进的由应用驱动的调速器同样有所改进，性能提升 16%，节能 10%。

**英文关键词：** power management, DVFS, systems-on-chip

**中文关键词：** 功耗管理、DVFS、片上系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
