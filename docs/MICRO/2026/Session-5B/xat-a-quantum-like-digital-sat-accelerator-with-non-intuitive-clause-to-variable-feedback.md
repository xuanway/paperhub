---
title: "XAT: A Quantum-Like Digital SAT Accelerator with Non-Intuitive Clause-to-Variable Feedback"
description: "MICRO 2026 · Session 5B · XAT：采用非直觉子句到变量反馈的类量子数字 SAT 加速器"
tags:
  - "MICRO2026"
  - "Quantum Computing"
---

# XAT: A Quantum-Like Digital SAT Accelerator with Non-Intuitive Clause-to-Variable Feedback

**中文标题：** XAT：采用非直觉子句到变量反馈的类量子数字 SAT 加速器

**所属 Session：** [Session 5B](index.md) · [MICRO 2026](../index.md)

**作者：** Zhezheng Ren, Shiyu Su

**来源：** MICRO 2026，pp. 1699–1713；[DOI](https://doi.org/10.1109/MICRO67795.2026.00122)

## 英文摘要

The Boolean Satisfiability (SAT) problem underpins critical applications across formal verification, AI planning, and cryptanalysis. Existing hardware accelerators for SAT remain fundamentally limited. Sequential or partially-parallel solvers are limited by inherently serial search procedures, restricting the solution time. In contrast, quantum-inspired analog/mixed-signal approaches enable fully parallel acceleration but suffer from limited scalability and solvability as the problem size increases. This paper presents XAT, a quantum-like digital accelerator for finding satisfying assignments of hard 3-SAT instances. XAT uses digital counters as spins and a reconfigurable digital crossbar to evaluate all clauses in parallel. It further introduces (i) fine-grained clause-satisfaction feedback, which distinguishes unsatisfied, weakly satisfied, moderately satisfied, and strongly satisfied clauses, and (ii) an offline pre-searched LUT mapping, where "pre-searched" means that the LUT entries are optimized before deployment on a small training set and then fixed during solving. We implement XAT on FPGA and as ASIC designs in 12~nm, 22~nm, and 65~nm, and evaluate it on SATLIB random 3-SAT benchmarks with 50–250 variables and generated random 3-SAT instances beyond 250 variables. XAT is a heuristic parallel SAT-assignment engine: it reports a solution when a satisfying assignment is found, but it does not provide UNSAT proofs as complete CDCL/DPLL solvers do. On satisfiable random 3-SAT instances, XAT achieves 215 times solution-time improvement over the Baseline at 250 variables and maintains 100% empirical solvability on all tested instances. The 12~nm implementation provides an additional 4.7 times speedup over the FPGA design. Furthermore, XAT maintains 100% solvability on generated hard random 3-SAT instances with 500 variables, extending the scalability frontier of hardware SAT solvers by 10 times compared to prior arts.

## 中文摘要

布尔可满足性 (SAT) 问题支撑着形式验证、人工智能规划和密码分析等关键应用。现有的 SAT 硬件加速器仍然受到根本限制。顺序或部分并行求解器受到固有的串行搜索过程的限制，从而限制了求解时间。相比之下，受量子启发的模拟/混合信号方法可以实现完全并行加速，但随着问题规模的增加，可扩展性和可解决性受到限制。本文介绍了 XAT，这是一种类量子数字加速器，用于寻找令人满意的硬 3-SAT 实例分配。 XAT 使用数字计数器作为旋转和可重新配置的数字交叉开关来并行评估所有条款。它还引入了（i）细粒度子句满意度反馈，区分不满意、弱满足、中等满意和强烈满足的子句，以及（ii）离线预搜索LUT映射，其中“预搜索”意味着LUT条目在部署到小型训练集之前进行优化，然后在求解过程中进行修复。我们在 FPGA 上实现 XAT，并将其作为 12~nm、22~nm 和 65~nm 的 ASIC 设计，并在具有 50-250 个变量的 SATLIB 随机 3-SAT 基准测试上对其进行评估，并生成超过 250 个变量的随机 3-SAT 实例。 XAT 是一种启发式并行 SAT 分配引擎：当找到令人满意的分配时，它会报告解决方案，但它不像完整的 CDCL/DPLL 求解器那样提供 UNSAT 证明。在可满足的随机 3-SAT 实例上，XAT 在 250 个变量下实现了比基线提高 215 倍的求解时间，并在所有测试实例上保持 100% 的经验可解性。 12~nm 实现比 FPGA 设计额外提供 4.7 倍的加速。此外，XAT 在生成的具有 500 个变量的硬随机 3-SAT 实例上保持 100% 的可解性，与现有技术相比，将硬件 SAT 求解器的可扩展性前沿扩展了 10 倍。

## 中文关键词

布尔可满足性；数字加速器；量子启发；计数器振荡器；子句满足反馈

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5B](index.md) · [MICRO 2026 主页](../index.md)
