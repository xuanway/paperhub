---
title: "NutCracker: A Compilation Framework for Hybrid DPU Architectures"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Yihan Yang (National University of Singapore), Haifeng Sun (National University "
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# NutCracker: A Compilation Framework for Hybrid DPU Architectures

**中文标题：** NutCracker：面向混合 DPU 架构的编译框架

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Yihan Yang (National University of Singapore), Haifeng Sun (National University of Singapore), Antoine Kaufmann (Max Planck Institute for Software Systems (MPI-SWS)), Jialin Li (National University of Singapore)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803618)

## 英文摘要

SoC-based SmartNICs, or data processing units (DPUs), are becoming a viable option for offloading infrastructure services. However, developers need deep hardware-level knowledge to fully utilize the available hardware accelerators on a target DPU. Hardware heterogeneity also makes porting across DPUs a formidable task. In this work, we propose a new compiler framework, NutCracker. Using NutCracker, programmers develop DPU applications using high-level target-independent languages. NutCracker applies a two-stage compilation process. It first performs progressive lowering to convert the source program to candidate intermediate representations (IRs) of the target DPU. Next, NutCracker applies cost-guided mapping optimization using equality saturation to select a final implementation on the target hardware with a configurable optimization goal. Evaluated on eight applications, NutCracker reduces developer effort by nearly 90% while delivering performance within 3% of handcrafted implementations for seven of the workloads. Moreover, its compilation time is comparable to standard toolchains such as GCC.

## 中文摘要

基于 SoC 的 SmartNIC（即数据处理单元，DPU）正成为卸载基础设施服务的可行选择。然而，开发者需要深入的硬件级知识才能充分利用目标 DPU 上可用的硬件加速器。硬件异构性也使跨 DPU 移植成为一项艰巨任务。本工作提出一个新的编译器框架 NutCracker。使用 NutCracker，程序员可以用高层、目标无关的语言开发 DPU 应用。NutCracker 采用两阶段编译过程。它首先执行渐进式下降，将源程序转换为目标 DPU 的候选中间表示（IR）。接着，NutCracker 利用等价饱和进行代价引导的映射优化，以可配置的优化目标在目标硬件上选择最终实现。在八个应用上评估，NutCracker 将开发者工作量减少近 90%，同时在七个工作负载上性能与手工实现相差 3% 以内。此外，其编译时间与 GCC 等标准工具链相当。

**英文关键词：** Data-plane programming language, In-network computation

**中文关键词：** 数据面编程语言、网内计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
