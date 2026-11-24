---
title: "Graph.hls: A Compiler Framework for Composable Graph Accelerator Design"
description: "ISCA 2026 · Session 4C · Graph.hls: A Compiler Framework for Composable Graph Accelerator Design"
tags:
  - "ISCA2026"
  - "Session 4C"
  - "Domain Specific Accelerators 1"
---

# Graph.hls: A Compiler Framework for Composable Graph Accelerator Design

**中文标题：** Graph.hls: 面向可组合图加速器设计的编译器框架

**所属 Session：** [Session 4C](index.md) · [ISCA 2026](../index.md)

**作者：** Feiyang Wu, Xuxiao Yang, Zhuohang Bian, Jing Wang, Ruifan Xu, Guangyu Sun, Yun Liang, Youwei Zhuo(卓有为)

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

FPGAs offer superior performance for graph processing, but existing High-Level Synthesis (HLS) frameworks face two critical bottlenecks: (1) optimization techniques scattered across incompatible frameworks cannot be composed—a simple 16-bit data type change requires modifying 200+ lines across 10+ files, and (2) developers lack systematic validation tools, forcing reliance on slow hardware emulation taking 50+ minutes per iteration. We present Graph.hls, a domain-specific compiler framework that addresses these challenges through hierarchical abstraction and automated workflows. Graph.hls organizes graph accelerator parameters into three levels by modification cost, enabling composition of multiple optimizations through unified configuration. Graph.hls’s GH-Architect automatically generates optimized hardware by propagating dependencies and performing resource-aware code generation, while GH-Scope provides rapid verification through IR-level simulation and baseline comparison, completing validation in under 1 second. Our DSL naturally expresses graph algorithms beyond the traditional GAS model, and the hierarchical abstraction enables composing optimizations across algorithms and FPGA platforms without manual code integration. Evaluation shows Graph.hls achieves 2.6× average speedup over ReGraph and 1.2× over ThunderGP with fair parameter-matched comparison, and up to 4.48× speedup with full multi-level design space exploration. GH-Scope accelerates simulation by 301.6× over vendor C-Sim and reduces debugging time by up to 455,000× over hardware emulation, enabling composable, high-performance graph accelerator design.


## 中文摘要

FPGA 为图处理提供了优越性能，但现有的高层次综合（HLS）框架面临两个关键瓶颈：(1) 分散在不兼容框架中的优化技术无法组合——仅将数据类型改为 16 位就需要跨 10+ 个文件修改 200+ 行代码；(2) 开发者缺乏系统化验证工具，只能依赖每次迭代耗时 50+ 分钟的缓慢硬件仿真。我们提出 Graph.hls，一个通过层次化抽象和自动化工作流应对这些挑战的领域专用编译器框架。Graph.hls 按修改成本将图加速器参数组织为三个层次，从而通过统一配置实现多种优化的组合。Graph.hls 的 GH-Architect 通过传播依赖关系并执行资源感知的代码生成，自动生成优化后的硬件；GH-Scope 则通过 IR 级仿真和基线比较提供快速验证，可在 1 秒内完成验证。我们的 DSL 能够自然表达超出传统 GAS 模型的图算法，而层次化抽象使得跨算法和 FPGA 平台组合优化无需手工代码集成。评估表明，在公平的参数匹配比较下，Graph.hls 相比 ReGraph 平均加速 2.6×，相比 ThunderGP 加速 1.2×；在完整的多层次设计空间探索下加速最高可达 4.48×。GH-Scope 相比厂商 C-Sim 将仿真加速 301.6×，相比硬件仿真将调试时间最多缩短 455,000×，从而实现可组合的高性能图加速器设计。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：pku-lemonade/Graph.hls](https://github.com/pku-lemonade/Graph.hls)
- [实验材料归档（Zenodo 19451706）](https://zenodo.org/records/19451706)（论文或公开检索提供；本次未能在线核实页面）

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2026](../index.md)
