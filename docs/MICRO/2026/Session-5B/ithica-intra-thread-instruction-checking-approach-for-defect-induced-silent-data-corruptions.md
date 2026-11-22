---
title: "ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions"
description: "MICRO 2026 · Session 5B · ITHICA：面向缺陷引发的静默数据损坏的线程内指令检查方法"
tags:
  - "MICRO2026"
---

# ITHICA: Intra-Thread Instruction Checking Approach for Defect-Induced Silent Data Corruptions

**中文标题：** ITHICA：面向缺陷引发的静默数据损坏的线程内指令检查方法

**所属 Session：** [Session 5B](index.md) · [MICRO 2026](../index.md)

**作者：** Ioanna Vavelidou, Subho Sankar Banerjee, Eric Xue Liu, Mike Fuller, Subhasish Mitra, Caroline Trippel

**来源：** MICRO 2026，pp. 1662–1681；[DOI](https://doi.org/10.1109/MICRO67795.2026.00120)

## 英文摘要

Hyperscalers are reporting silent data corruptions (SDCs), presumed to be caused by silicon manufacturing defects, as a threat to datacenter reliability. To support datacenter testing efforts to detect defective CPU servers, this paper presents ITHICA, an approach and tool for automatically generating functional tests for defect-induced errors from arbitrary programs by inserting intra-thread, instruction-level error checks, primarily leveraging instruction duplication and output comparison. Our key insight is that the most pernicious defects (those most likely to escape manufacturing testing) cause inconsistent errors: two executions of the same instruction given the same inputs within the same thread can produce different architectural outputs depending on the execution context in which they run. By exploiting this insight, ITHICA uniquely enables arbitrary programs to serve as tests and localizes affected instructions concurrently with error detection. We use ITHICA to transform industrial hyperscaler tests (our baseline), datacenter programs, and common libraries into functional tests, and evaluate them on over 3,000 CPU servers. ITHICA checks detect 39% more defective servers than baseline industrial checks and yield novel findings on defect behavior that challenge conclusions drawn by prior hyperscaler fleet studies.

## 中文摘要

超大规模企业报告称，静默数据损坏 (SDC) 是对数据中心可靠性的威胁，据推测这是由硅制造缺陷引起的。为了支持数据中心测试工作来检测有缺陷的 CPU 服务器，本文提出了 ITHICA，这是一种方法和工具，通过插入线程内指令级错误检查（主要利用指令复制和输出比较），自动生成针对任意程序中缺陷引起的错误的功能测试。我们的主要见解是，最有害的缺陷（最有可能逃脱制造测试的缺陷）会导致不一致的错误：在同一线程内给定相同输入的同一指令的两次执行可能会产生不同的架构输出，具体取决于它们运行的​​执行上下文。通过利用这种洞察力，ITHICA 独特地允许任意程序充当测试并在错误检测的同时本地化受影响的指令。我们使用 ITHICA 将工业超大规模测试（我们的基准）、数据中心程序和通用库转换为功能测试，并在 3,000 多个 CPU 服务器上对其进行评估。 ITHICA 检查发现的缺陷服务器比基准工业检查多 39%，并产生了有关缺陷行为的新颖发现，挑战了之前超大规模集群研究得出的结论。

## 中文关键词

可靠性；静默数据损坏；硬件故障；制造缺陷；功能测试；数据中心测试

## 代码与研究制品

- 代码仓库：[https://github.com/ioannavav/ithica](https://github.com/ioannavav/ithica)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21554153](https://doi.org/10.5281/zenodo.21554153)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5B](index.md) · [MICRO 2026 主页](../index.md)
