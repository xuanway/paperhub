---
title: "coMulator: Coordinate Cross-Architecture Compilation and Emulation to Accelerate Dynamic Binary Translation"
description: "MICRO 2026 · Session 6A · coMulator：协调跨架构编译与仿真以加速动态二进制翻译"
tags:
  - "MICRO2026"
  - "Compiler"
---

# coMulator: Coordinate Cross-Architecture Compilation and Emulation to Accelerate Dynamic Binary Translation

**中文标题：** coMulator：协调跨架构编译与仿真以加速动态二进制翻译

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Yuhao Gu, Zhongchun Zheng, Nong Xiao, Yutong Lu, Xianwei Zhang

**来源：** MICRO 2026，pp. 1864–1878；[DOI](https://doi.org/10.1109/MICRO67795.2026.00132)

## 英文摘要

The rapid proliferation of diverse instruction set architectures (ISAs), such as x86, Arm, and RISC-V, has made cross-ISA execution a fundamental requirement for software portability and platform migration. Although dynamic binary translation (DBT) is the de facto solution, it incurs substantial performance overhead due to runtime interpretation and translation costs. Cross-compiling to the host ISA can avoid this penalty, but existing toolchains suffer from a binary dilemma, where any non-portable code or closed-source dependency forces full fallback to DBT. Recent hybrid approaches mitigate this by enabling partial native execution via function offloading or emulation-specific ABIs, but they remain limited: offloading requires manual engineering and cannot handle guest callbacks, while ABI-specific designs introduce tight coupling that reduces portability and scalability across ISA pairs. To bridge this critical gap, this paper presents coMulator, a source-guided, callback-capable, and ABI-bridging coordinated design that aims for dual generality across both diverse codebases and various guest/host ISA combinations. At its core, coMulator introduces gyhcall (guest yields host calls), an innovative target-neutral invocation mechanism that leverages compile-time assistance to fully automate function offloading while preserving ABI neutrality. Mechanistically, gyhcall bridges guest/host ABI structural discrepancies via collaborative stubs and handles complex control flows of guest callbacks through runtime emulation reentrancy. To further mitigate the boundary-crossing overhead inherent in gyhcall, coMulator incorporates four critical optimizations to eliminate unnecessary switches. We evaluate coMulator using the SPEC CPU 2017 benchmarks and real-world applications across nine guest/host combinations among x86_64, aarch64, and riscv64. The results demonstrate that coMulator consistently achieves an average speedup of over 7.90×, restoring over 75% of native execution performance. Further comparisons against representative state-of-the-arts including Risotto and Arm64EC demonstrates coMulator’s practicability and scalability for accelerating cross-ISA execution.

## 中文摘要

x86、Arm 和 RISC-V 等多种指令集架构 (ISA) 的快速增长使得跨 ISA 执行成为软件可移植性和平台迁移的基本要求。尽管动态二进制翻译 (DBT) 是事实上的解决方案，但由于运行时解释和翻译成本，它会产生大量的性能开销。交叉编译到主机 ISA 可以避免这种损失，但现有工具链面临二进制困境，任何不可移植代码或闭源依赖项都会迫使完全回退到 DBT。最近的混合方法通过函数卸载或特定于仿真的 ABI 启用部分原生执行来缓解这一问题，但它们仍然受到限制：卸载需要手动工程并且无法处理来宾回调，而特定于 ABI 的设计引入了紧密耦合，从而降低了 ISA 对之间的可移植性和可扩展性。为了弥补这一关键差距，本文提出了 coMulator，这是一种源引导、具有回调功能和 ABI 桥接协调设计，旨在实现跨不同代码库和各种来宾/主机 ISA 组合的双重通用性。 coMulator 的核心引入了 gyhcall（来宾产生主机调用），这是一种创新的目标中立调用机制，它利用编译时辅助来完全自动化函数卸载，同时保持 ABI 中立性。从机制上讲，gyhcall 通过协作存根弥合来宾/主机 ABI 结构差异，并通过运行时模拟重入处理来宾回调的复杂控制流。为了进一步减轻 gyhcall 固有的跨边界开销，coMulator 结合了四项关键优化来消除不必要的切换。我们使用 SPEC CPU 2017 基准测试和 x86_64、aarch64 和 riscv64 之间的九种来宾/主机组合的实际应用程序来评估 coMulator。结果表明，coMulator 始终实现超过 7.90 倍的平均加速，恢复了超过 75% 的原生执行性能。与 Risotto 和 Arm64EC 等代表性最先进技术的进一步比较证明了 coMulator 在加速跨 ISA 执行方面的实用性和可扩展性。

## 中文关键词

二进制翻译；模拟执行；交叉编译；函数卸载

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/yhgu2000/artifact-micro2026-comulator](https://github.com/yhgu2000/artifact-micro2026-comulator)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21530602](https://doi.org/10.5281/zenodo.21530602)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
