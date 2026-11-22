---
title: "Potluck: High-Level Synthesis for Architectural Design via Automated Module Extraction and Sharing"
description: "MICRO 2026 · Session 5A · Potluck：通过自动化模块提取与共享实现架构设计的高层次综合"
tags:
  - "MICRO2026"
---

# Potluck: High-Level Synthesis for Architectural Design via Automated Module Extraction and Sharing

**中文标题：** Potluck：通过自动化模块提取与共享实现架构设计的高层次综合

**所属 Session：** [Session 5A](index.md) · [MICRO 2026](../index.md)

**作者：** Hanqiu Chen, Cong Hao

**来源：** MICRO 2026，pp. 1595–1613；[DOI](https://doi.org/10.1109/MICRO67795.2026.00116)

## 英文摘要

With the rapid growth of Artificial Intelligence (AI) and Machine Learning (ML), architectural design has become more essential: accelerators tailored to specific algorithms quickly become obsolete, whereas architectural designs can support a wider range of workloads. However, fully automated architectural design generation still faces two key challenges: (1) it requires substantial expertise and manual effort, with limited support from existing High-Level Synthesis (HLS)-based solutions; and (2) existing HLS tools generate fixed dataflow and control logic, limiting flexible algorithm-to-architecture mapping. To address these challenges, we propose Potluck, a highly automated, template-free HLS-based framework for architectural design generation. Potluck enables flexible dataflow and control, functional module reuse, and introduces fully automated architecture generation with instruction compilation. Across eight real-world HLS benchmarks, Potluck reduces hardware resource usage by up to 67% through module reuse compared with naive merging, while maintaining frequencies comparable to manually designed architectures using Vitis HLS and reducing latency by up to 45%. We also analyze the trade-offs to determine when merging accelerators into a unified architecture is beneficial. Our code is in https://github.com/sharc-lab/Potluck.

## 中文摘要

随着人工智能 (AI) 和机器学习 (ML) 的快速发展，架构设计变得更加重要：针对特定算法定制的加速器很快就会过时，而架构设计可以支持更广泛的工作负载。然而，完全自动化的架构设计生成仍然面临两个关键挑战：（1）它需要大量的专业知识和手动工作，而现有的基于高级综合（HLS）的解决方案的支持有限； (2) 现有的 HLS 工具生成固定的数据流和控制逻辑，限制了灵活的算法到架构的映射。为了应对这些挑战，我们提出了 Potluck，一种高度自动化、基于无模板 HLS 的架构设计生成框架。 Potluck 实现了灵活的数据流和控制、功能模块重用，并引入了带有指令编译的全自动架构生成。在八个现实世界的 HLS 基准测试中，与简单合并相比，Potluck 通过模块重用将硬件资源使用量减少了高达 67%，同时保持了与使用 Vitis HLS 手动设计的架构相当的频率，并将时延减少了高达 45%。我们还分析了权衡，以确定何时将加速器合并到统一架构中是有利的。我们的代码位于 https://github.com/sharc-lab/Potluck。

## 中文关键词

高层次综合；机器学习；电子设计自动化工具；架构与加速器设计；模块共享

## 代码与研究制品

- 代码仓库：[https://github.com/sharc-lab/Potluck](https://github.com/sharc-lab/Potluck)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21542987](https://doi.org/10.5281/zenodo.21542987)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5A](index.md) · [MICRO 2026 主页](../index.md)
