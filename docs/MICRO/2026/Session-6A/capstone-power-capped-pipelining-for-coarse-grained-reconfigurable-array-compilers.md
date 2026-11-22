---
title: "Capstone: Power-Capped Pipelining for Coarse-Grained Reconfigurable Array Compilers"
description: "MICRO 2026 · Session 6A · Capstone：面向粗粒度可重构阵列编译器的功率受限流水线化"
tags:
  - "MICRO2026"
  - "Compiler"
  - "Energy Efficiency"
  - "Reconfigurable Computing"
---

# Capstone: Power-Capped Pipelining for Coarse-Grained Reconfigurable Array Compilers

**中文标题：** Capstone：面向粗粒度可重构阵列编译器的功率受限流水线化

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Sabrina Yarzada, Christopher Torng

**来源：** MICRO 2026，pp. 1879–1897；[DOI](https://doi.org/10.1109/MICRO67795.2026.00133)

## 英文摘要

Coarse-grained reconfigurable arrays (CGRAs) combine much of the performance and energy efficiency of ASICs with the flexibility of programmable hardware, making them attractive in power-constrained systems. However, modern CGRA compilers optimize primarily for performance and can create hardware configurations that exceed fixed power budgets. We empirically show that post-place-and-route (post-PnR) pipelining in Cascade, a prior state-of-the-art CGRA compiler, can monotonically increase power as it inserts registers to improve frequency. We present Capstone, a power-cap-aware extension of Cascade that integrates a fast, compiler-resident power model with uncertainty-aware controllers to guide bitstream selection. Capstone automatically learns energy costs for compiler-visible abstract events from hierarchical gate-level power supervision and achieves 16.8% MAPE, approaching a 14.8% oracle restricted to the same event abstraction, while adding less than 1% prediction overhead per post-PnR iteration. Capstone I applies a static guardband, Capstone II uses conformal calibration for probabilistic coverage under its calibration assumptions, and Capstone III uses event-level error bounds for a conditional deterministic guarantee. Across eight evaluated vector, matrix, and tensor kernels, all three modes achieve 100% cap compliance under the evaluated margins. Capstone I, II, and III retain 0.65×, 0.74×, and 0.81× of uncapped frequency on average while leaving median cap slack of 31.23%, 22.26%, and 13.85%, respectively. Capstone demonstrates that the compiler can proactively optimize the hardware configuration itself for a power constraint before deployment, rather than relying only on reactive run-time power management.

## 中文摘要

粗粒度可重构阵列 (CGRA) 将 ASIC 的大部分性能和能效与可编程硬件的灵活性相结合，使其在功耗受限的系统中具有吸引力。然而，现代 CGRA 编译器主要针对性能进行优化，并且可以创建超出固定功耗预算的硬件配置。我们凭经验表明，Cascade（一种先前最先进的 CGRA 编译器）中的后布局布线（后 PnR）流水线可以在插入寄存器以提高频率时单调增加功率。我们推出了 Capstone，它是 Cascade 的功率上限感知扩展，它将快速、编译器驻留的功率模型与不确定性感知控制器集成在一起，以指导比特流选择。 Capstone 自动从分层门级功耗监控中学习编译器可见抽象事件的能源成本，并实现 16.8% MAPE，接近限制于相同事件抽象的 14.8% 预言机，同时每次 PnR 迭代后增加的预测开销不到 1%。 Capstone I 应用静态保护带，Capstone II 在其校准假设下使用保角校准来实现概率覆盖，而 Capstone III 使用事件级误差界限来实现条件确定性保证。在八个评估的向量、矩阵和张量内核中，所有三种模式都在评估的裕度下实现了 100% 的上限合规性。 Capstone I、II 和 III 平均保留了 0.65×、0.74× 和 0.81× 的无上限频率，同时中位数上限分别为 31.23%、22.26% 和 13.85%。 Capstone 证明，编译器可以在部署之前针对功耗限制主动优化硬件配置本身，而不是仅依赖于反应性运行时功耗管理。

## 中文关键词

粗粒度可重构阵列；功耗感知编译；功耗建模；功耗封顶；领域专用编译器

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/usc-acorn/yarzada-capstone-micro2026](https://github.com/usc-acorn/yarzada-capstone-micro2026)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21880340](https://doi.org/10.5281/zenodo.21880340)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
