---
title: "Rearchitecting Programmable Networks For In-Network Computing: From Hardware To Language"
description: "EuroSys 2026 · Distributed Systems and Multicore · Haifeng Sun (National Key Laboratory for Multimedia Information Processing, Scho"
tags:
  - "EuroSys2026"
  - "Distributed Systems and Multicore"
---

# Rearchitecting Programmable Networks For In-Network Computing: From Hardware To Language

**中文标题：** 为网内计算重构可编程网络：从硬件到语言

**所属 Session：** [Session 10.1: Distributed Systems and Multicore](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Systems and Multicore。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Systems and Multicore</p>
</div>

**作者**：Haifeng Sun (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Bing Liu (Huawei Cloud Computing Technologies Co., Ltd.), Taixu Tian (Huawei Technologies Co., Ltd), Jinbo Sun (Institute of Computing Technology, CAS), Jintao He (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Qun Huang (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Luyou He (Huawei Cloud Computing Technologies Co., Ltd.), Xuan Wang (Huawei Technologies Co., Ltd), Feng Gao (Huawei Cloud Computing Technologies Co., Ltd.), Liguo Wang (Huawei Technologies Co., Ltd), Xiangcan Xu (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Junyi Guo (National Key Laboratory for Multimedia Information Processing, School of Computer Science, Peking University), Xiaoping Zhu (Huawei Cloud Computing Technologies Co., Ltd.), Yongqiang Yang (Huawei Cloud Computing Technologies Co., Ltd.)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769344)

## 英文摘要

In-network computing (INC) offers orders-of-magnitude performance gains for various applications. However, the existing pipeline-based switch architecture, though well-suited for stateless packet forwarding, imposes three constraints on stateful INC applications: (i) control-plane table management, (ii) scarce memory resources under per-stage layout, and (iii) a strict memory access model. To address these constraints, this paper provides a full-stack solution, covering a programmable chipset Solar-NP, a programming language NPC, and a complete toolchain XuanWu. First, Solar-NP adopts a run-to-completion-based (RTC-based) architecture with three new hardware features: data-plane table management, a hierarchical memory pool, and builtin data structures with atomic access guarantees. Second, to fully exploit the hardware features, our language NPC introduces a new abstraction, namely operation-action table (OAT), that allows table manipulations in the data plane. Finally, our XuanWu toolchain provides various utility software covering the complete workflow of developing, testing, debugging, and deployment. To show the power of our solution, we implement three types of INC cases, including in-network control, in-network telemetry, and in-network storage. Experimental results demonstrate that our solution allows more operations to be offloaded and achieves higher performance than today’s pipeline-based solutions.

## 中文摘要

网内计算（INC）为各类应用带来数量级的性能提升。然而，现有的基于流水线的交换机架构虽非常适合无状态报文转发，却对有状态 INC 应用施加了三项约束：(i) 控制平面表管理；(ii) 按阶段布局下稀缺的内存资源；(iii) 严格的内存访问模型。为应对这些约束，本文提供了一套全栈解决方案，涵盖可编程芯片组 Solar-NP、编程语言 NPC 和完整工具链 XuanWu。首先，Solar-NP 采用基于运行至完成（RTC）的架构，并具备三项新的硬件特性：数据平面表管理、分层内存池，以及具有原子访问保证的内置数据结构。其次，为充分利用这些硬件特性，我们的语言 NPC 引入了一种新抽象，即操作-动作表（OAT），允许在数据平面中进行表操作。最后，我们的 XuanWu 工具链提供多种实用软件，覆盖开发、测试、调试和部署的完整工作流。为展示方案的强大能力，我们实现了三类 INC 用例，包括网内控制、网内遥测和网内存储。实验结果表明，与当今基于流水线的方案相比，我们的方案可以卸载更多操作并取得更高性能。

**英文关键词：** RTC architecture, Data-plane programming language, In-network computation

**中文关键词：** RTC 架构、数据平面编程语言、网内计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
