---
title: "DP-HLS: A High-Level Synthesis Framework for Accelerating Dynamic Programming Algorithms in Bioinformatics"
description: "HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing"
tags:
  - "HPCA2026"
  - "FPGA, SmartNIC, and Reconfigurable Computing"
---

# DP-HLS: A High-Level Synthesis Framework for Accelerating Dynamic Programming Algorithms in Bioinformatics

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: FPGA, SmartNIC, and Reconfigurable Computing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · FPGA, SmartNIC, and Reconfigurable Computing</p>
</div>

**论文链接**：
**作者**：Anshu Gupta UC San Diego , Yingqi Cao UC San Diego , Jason Liang UC San Diego , Yatish Turakhia UC San Diego
**会议**：HPCA 2026

---

## 中文标题

DP-HLS：加速生物信息学中动态规划算法的高层次综合框架

## 英文摘要

Dynamic programming (DP) is a widely used algorithmic paradigm, particularly in bioinformatics, finding applications in a wide spectrum of tasks, including read assembly, homology search, gene annotation, basecalling, and phylogenetic inference. Due to its computationally intensive nature, many ASIC- and FPGA-based accelerators have been proposed in recent years to accelerate specific tasks. However, DP algorithms in bioinformatics can vary considerably, and most existing solutions are customized for a single application, representing just one design point within the broader DP space. These implementations typically rely on low-level hardware description languages (HDLs), often requiring months of manual implementation effort. This paper introduces DP-HLS, a novel framework based on High-Level Synthesis (HLS) that simplifies and accelerates the development of a vast set of bioinformatically relevant 2-D DP algorithms in hardware. DP-HLS achieves this by introducing a new abstraction layer that decouples the front-end specification from predefined HLS-based back-end optimizations, enabling users to efficiently develop new 2-D DP kernels in C++ and deploy them on FPGAs without needing any expertise in hardware design or HLS. In our experience, DP-HLS significantly reduced the development time of new kernels (months to days) and produced designs with comparable resource utilization to open-source hand-coded HDL-based implementations and performance within 7.7–16.8% margin. DP-HLS is compatible with AWS® EC2 F1 FPGA instances. To showcase its versatility, we implemented 15 diverse 2-D DP kernels using the DP-HLS framework, achieving 1.38–41× improved cost-efficiency over state-of-the-art GPU and CPU baselines and providing the first open-source FPGA implementation for several of them. The DP-HLS codebase is available freely under the MIT license at https://github.com/TurakhiaLab/DP-HLS.

## 中文摘要

动态规划（DP）是一种广泛使用的算法范式，尤其在生物信息学中应用于读段组装、同源搜索、基因注释、碱基识别和系统发育推断等诸多任务。由于其计算密集，近年提出许多基于 ASIC 与 FPGA 的加速器以加速特定任务。然而生物信息学中的 DP 算法差异很大，多数现有方案仅针对单一应用定制，只对应整个 DP 设计空间中的一个设计点，且通常依赖底层硬件描述语言（HDL），往往需要数月的人工实现。本文提出 DP-HLS，一个基于高层次综合（HLS）的新框架，可简化并加速大量生物信息学相关二维 DP 算法的硬件开发。DP-HLS 通过引入新的抽象层，将前端描述与预定义的基于 HLS 的后端优化解耦，使用户能用 C++ 高效开发新的二维 DP 内核并部署到 FPGA，而无需硬件设计或 HLS 专业知识。在我们的实践中，DP-HLS 显著缩短了新内核的开发时间（从数月缩短到数天），所生成设计的资源利用率与开源手工 HDL 实现相当，性能差距在 7.7–16.8% 以内。DP-HLS 兼容 AWS® EC2 F1 FPGA 实例。为展示其通用性，我们使用 DP-HLS 实现了 15 个不同的二维 DP 内核，相比最先进的 GPU 和 CPU 基线，成本效率提升 1.38–41 倍，并为其中多个内核提供了首个开源 FPGA 实现。DP-HLS 代码以 MIT 许可证在 https://github.com/TurakhiaLab/DP-HLS 免费提供。
