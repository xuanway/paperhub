---
title: "UniNDP: A Unified Compilation and Simulation Tool for Near DRAM Processing Architectures"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# UniNDP: A Unified Compilation and Simulation Tool for Near DRAM Processing Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Tongxin Xie (Tsinghua University), Zhenhua Zhu (Tsinghua University; HKUST), Bing Li (Institute of Microelectronics, Chinese Academy of Sciences), Yukai He (Capital Normal University), Cong Li (Peking University), Guangyu Sun (Peking University), Huazhong Yang (Tsinghua University), Yuan Xie (HKUST), Yu Wang (Tsinghua University)
**会议**：HPCA 2025

---

## 中文标题

UniNDP：面向近 DRAM 处理架构的统一编译与仿真工具

## 英文摘要

Near DRAM Processing (NDP) architectures have emerged to be a promising solution for commercializing in-memory computing and addressing the “memory wall” problem, especially for the memory-intensive machine learning (ML) workloads. In NDP architectures, the Processing Units (PUs) are distributed next to different memory units to exploit the high internal bandwidth. Therefore, in order to fully utilize the bandwidth advantage of NDP architectures for ML applications, meticulous evaluations and optimizations of data placement in DRAM and workload scheduling among different PUs are required. However, existing simulation and compilation tools face two insuperable obstacles to achieving these targets. On the one hand, tools for traditional von Neumann architectures only focus on the data access behaviors between the host and DRAM and treat DRAM as a whole part, which cannot support NDP architectures with multiple independent processing and memory units working simultaneously. On the other hand, existing NDP simulators and compilers are designed for specific DRAM technology and NDP architecture, lacking compatibility for various NDP architectures. In order to overcome these challenges and optimize data mapping and workload scheduling for different NDP architectures, we propose UniNDP, a unified NDP compilation and simulation tool for ML applications. Firstly, we propose a unified tree-based NDP hardware abstraction and the corresponding instruction set, enabling the support for various NDP architectures based on different DRAM technologies. Secondly, we design a cycle-accurate and instruction-driven NDP simulator to evaluate hardware performance by accurately tracking the working status of memory elements and PUs. The accurate simulation can provide effective guidance for compilation. Thirdly, we design an NDP compiler that optimizes data partition, mapping, and workload scheduling in different DRAM hierarchies. Furthermore, to enhance the compilation efficiency, we propose a hardware status-guided search space pruning strategy and a fast performance predictor using DRAM timing parameters. Extensive experimental results show that, compared to existing mapping and compilation methods, UniNDP can achieve 1.05-3.43× speedup across multiple NDP architectures and different ML workloads. Furthermore, based on the results of UniNDP, we provide insights for the future NDP architecture design and deployment in ML applications.

## 中文摘要

近 DRAM 处理（NDP）架构可将近存计算商业化并缓解“内存墙”问题，尤其适合访存密集的机器学习（ML）负载。其处理单元（PU）分散布置在各内存单元旁以利用高内部带宽，因而需细致评估与优化 DRAM 中的数据放置及 PU 间的负载调度。但现有工具存在两大障碍：传统冯·诺依曼架构的仿真与编译工具只关注主机与 DRAM 之间的访问行为，并把 DRAM 视为整体，无法支持多个独立处理与内存单元并行的 NDP 架构；现有 NDP 仿真器与编译器又绑定特定 DRAM 技术与架构，缺乏通用性。为此我们提出 UniNDP，一个面向 ML 应用的统一 NDP 编译与仿真工具。它首先给出统一的树状 NDP 硬件抽象及配套指令集，支持基于不同 DRAM 技术的多种 NDP 架构；其次设计周期精确、指令驱动的 NDP 仿真器，通过精确跟踪存储元件与 PU 的状态评估硬件性能，为编译提供有效指导；第三设计 NDP 编译器，在不同 DRAM 层次上优化数据划分、映射与负载调度，并提出由硬件状态引导的搜索空间剪枝与基于 DRAM 时序参数的快速性能预测器以提升编译效率。大量实验表明，相较现有映射与编译方法，UniNDP 在多种 NDP 架构与不同 ML 负载上取得 1.05-3.43× 加速。基于这些结果，我们还为未来 ML 应用中的 NDP 架构设计与部署提供了见解。
