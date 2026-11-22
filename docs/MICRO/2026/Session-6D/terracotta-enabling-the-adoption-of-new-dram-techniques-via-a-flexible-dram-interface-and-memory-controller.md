---
title: "Terracotta: Enabling the Adoption of New DRAM Techniques via a Flexible DRAM Interface and Memory Controller"
description: "MICRO 2026 · Session 6D · Terracotta：通过灵活的 DRAM 接口与内存控制器促进新型 DRAM 技术应用"
tags:
  - "MICRO2026"
  - "DRAM"
---

# Terracotta: Enabling the Adoption of New DRAM Techniques via a Flexible DRAM Interface and Memory Controller

**中文标题：** Terracotta：通过灵活的 DRAM 接口与内存控制器促进新型 DRAM 技术应用

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Harsh Songara, Konstantinos Kanellopoulos, F. Nisa Bostancı, Konstantinos Marios Sgouras, Ataberk Olgun, İsmail Emir Yüksel, Andreas Kosmas Kakolyris, A. Giray Yağlıkçı, Onur Mutlu

**来源：** MICRO 2026，pp. 2162–2185；[DOI](https://doi.org/10.1109/MICRO67795.2026.00150)

## 英文摘要

DRAM is the dominant memory technology in modern systems, yet it continues to limit performance, energy efficiency, and system robustness. To mitigate such limitations, many prior works have proposed novel DRAM techniques that change how DRAM is operated to support in-DRAM computation, improve memory access latency and parallelism, and enhance DRAM maintenance and reliability. However, adopting these techniques one after another in current systems with rigid interfaces and memory controller hardware requires repeated and costly modifications to them, hindering the deployment of critical performance, energy-efficiency, and robustness improvements. Our goal is to reduce the repeated DRAM interface and memory controller modifications that hinder or slow down the deployment of diverse DRAM techniques. We observe that the DRAM commands and memory controller structures across several DRAM techniques are similar. Our key idea is to leverage these similarities to compose a set of primitives that DRAM vendors and system designers can use to implement a wide variety of DRAM techniques. To this end, we propose Terracotta, a new framework that consists of two flexible components: (i) custom command extensions that enable DRAM vendors to define new commands within a single, standardized interface, and (ii) a programmable memory controller that system designers can easily and flexibly program to support new DRAM techniques post-silicon fabrication. Together, these two components enable the deployment of new DRAM techniques via configuration of the memory controller rather than repeated interface and controller modifications. We design Terracotta for a DDR5-based system and comprehensively evaluate its performance, energy, and hardware complexity. We draw three key findings. First, for four DRAM techniques from four distinct domains including processing-using-DRAM, low-cost DRAM maintenance, subarray-level parallelism, and latency reduction, Terracotta retains almost all of the performance benefits (94–99.8%) that custom implementations provide over a baseline system without these techniques. Second, a Terracotta-based composition of two DRAM techniques from the domains of subarray-level parallelism and latency reduction outperforms the Terracotta-based implementations of the individual techniques, showing that Terracotta's flexibility can enable the benefits of multiple techniques via memory controller configuration rather than interface and controller modifications. Third, Terracotta's flexibility incurs low DRAM energy overheads (0.5–3.3%) and, low area and power overheads (0.03% and 0.56%, respectively) in a high-end server-grade processor. Terracotta's source code is freely available at https://github.com/CMU-SAFARI/Terracotta.

## 中文摘要

DRAM 是现代系统中占主导地位的内存技术，但它仍然限制着性能、能效和系统稳健性。为了缓解此类限制，许多先前的工作提出了新颖的 DRAM 技术，这些技术改变了 DRAM 的操作方式以支持 DRAM 内计算、改善内存访问时延和并行性，并增强 DRAM 维护和可靠性。然而，在当前具有严格接口和内存控制器硬件的系统中相继采用这些技术需要对它们进行重复且昂贵的修改，从而阻碍了关键性能、能效和鲁棒性改进的部署。我们的目标是减少阻碍或减慢不同 DRAM 技术部署的重复 DRAM 接口和内存控制器修改。我们观察到多种 DRAM 技术的 DRAM 命令和内存控制器结构是相似的。我们的主要想法是利用这些相似性来组成一组原语，DRAM 供应商和系统设计人员可以使用这些原语来实现各种 DRAM 技术。为此，我们提出了 Terracotta，这是一个由两个灵活组件组成的新框架：(i) 自定义命令扩展，使 DRAM 供应商能够在单个标准化接口中定义新命令，以及 (ii) 可编程内存控制器，系统设计人员可以轻松灵活地进行编程，以支持硅后制造的新 DRAM 技术。这两个组件一起支持通过内存控制器的配置来部署新的 DRAM 技术，而不是重复的接口和控制器修改。我们为基于 DDR5 的系统设计 Terracotta，并综合评估其性能、能耗和硬件复杂性。我们得出三个主要发现。首先，对于来自四个不同领域的四种 DRAM 技术，包括使用 DRAM 进行处理、低成本 DRAM 维护、子阵列级并行性和时延减少，Terracotta 保留了自定义实现相对于没有这些技术的基准系统提供的几乎所有性能优势 (94–99.8%)。其次，来自子阵列级并行性和时延减少领域的两种 DRAM 技术的基于 Terracotta 的组合优于单个技术的基于 Terracotta 的实现，这表明 Terracotta 的灵活性可以通过内存控制器配置而不是接口和控制器修改来实现多种技术的优势。第三，Terracotta 的灵活性在高端服务器级处理器中带来了低 DRAM 能源开销 (0.5–3.3%) 以及低面积和功耗开销（分别为 0.03% 和 0.56%）。 Terracotta 的源代码可在 https://github.com/CMU-SAFARI/Terracotta 免费获取。

## 中文关键词

DRAM 接口；内存控制器；可扩展架构；新型内存技术

## 代码与研究制品

- 代码仓库：[https://github.com/CMU-SAFARI/Terracotta](https://github.com/CMU-SAFARI/Terracotta)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21541650](https://doi.org/10.5281/zenodo.21541650)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
