---
title: "RowScope: ML-Accelerated Reverse-Engineering for Precise Characterization of DRAM Internal Physical Organization"
description: "MICRO 2026 · Session 8B · RowScope：通过机器学习加速逆向工程，精确刻画 DRAM 内部物理组织"
tags:
  - "MICRO2026"
  - "DRAM"
---

# RowScope: ML-Accelerated Reverse-Engineering for Precise Characterization of DRAM Internal Physical Organization

**中文标题：** RowScope：通过机器学习加速逆向工程，精确刻画 DRAM 内部物理组织

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Zexi Meng, Longda Zhou, Fayong Liu, Haiyong Zheng, Zhigang Ji

**来源：** MICRO 2026，pp. 2895–2908；[DOI](https://doi.org/10.1109/MICRO67795.2026.00196)

## 英文摘要

Understanding DRAM physical row adjacency is critical for processing-in-memory (PIM) exploration and RowHammer mitigation. However, existing inference methods often yield ambiguous results, falsely identifying multiple victim rows per aggressor due to unmapped chip-level interleaving, tile-level partitioning, and confounding coupling effects. In this paper, we propose an FPGA-based reverse-engineering framework that isolates individual DRAM chips, performs fine-grained logical memory array tile (LMAT) partitioning, and employs bidirectional activation to distinguish true physical adjacency from coupling effects. Our characterization of 28 DDR4 DIMMs from three major vendors demonstrates that while conventional methods falsely report more than two adjacent rows in 21 DIMMs, our approach accurately isolates at most two truly adjacent physical rows per aggressor. Furthermore, because physical adjacency varies significantly across vendors, chips, and internal banks, exhaustive characterization is prohibitively time-consuming. We develop a machine learning-assisted prediction model that, using only four DIMMs for training, predicts the adjacency patterns of the remaining 24 modules with 95% accuracy, reducing overall testing time by up to 87%. Finally, leveraging the precise adjacency information extracted by our tool, we uncover that coupling rows persist in recently manufactured DRAMs and analyze their relationship with edge subarrays. This robust tool provides a new experimental pathway for understanding modern DRAM internal organization, laying the groundwork for future research in DRAM security analysis and microarchitectural model validation.

## 中文摘要

了解 DRAM 物理行邻接对于存内处理 (PIM) 探索和 RowHammer 缓解至关重要。然而，现有的推理方法经常产生不明确的结果，由于未映射的芯片级交织、分块级分区和混杂的耦合效应，错误地识别每个攻击者的多个受害者行。在本文中，我们提出了一种基于 FPGA 的逆向工程框架，该框架隔离各个 DRAM 芯片，执行细粒度逻辑内存阵列块 (LMAT) 分区，并采用双向激活来区分真实的物理邻接和耦合效应。我们对来自三个主要供应商的 28 个 DDR4 DIMM 的特征分析表明，虽然传统方法错误地报告了 21 个 DIMM 中两个以上相邻的行，但我们的方法准确地隔离了每个攻击者最多两个真正相邻的物理行。此外，由于供应商、芯片和内部银行之间的物理邻接性差异很大，因此详尽的特征描述非常耗时。我们开发了一种机器学习辅助预测模型，仅使用 4 个 DIMM 进行训练，即可以 95% 的准确率预测其余 24 个模块的邻接模式，从而将总体测试时间缩短高达 87%。最后，利用我们的工具提取的精确邻接信息，我们发现耦合行持续存在于最近制造的 DRAM 中，并分析了它们与边缘子阵列的关系。这个强大的工具为理解现代 DRAM 内部组织提供了新的实验途径，为 DRAM 安全分析和微架构模型验证的未来研究奠定了基础。

## 中文关键词

DRAM 微架构；逆向工程；物理行邻接关系；RowHammer；机器学习

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
