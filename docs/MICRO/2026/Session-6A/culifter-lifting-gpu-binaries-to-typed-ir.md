---
title: "CuLifter: Lifting GPU Binaries to Typed IR"
description: "MICRO 2026 · Session 6A · CuLifter：将 GPU 二进制程序提升为带类型的中间表示"
tags:
  - "MICRO2026"
  - "GPU"
---

# CuLifter: Lifting GPU Binaries to Typed IR

**中文标题：** CuLifter：将 GPU 二进制程序提升为带类型的中间表示

**所属 Session：** [Session 6A](index.md) · [MICRO 2026](../index.md)

**作者：** Jisheng Zhao, Huanzhi Pu, Shinnung Jeong, Chihyo Ahn, Hyesoon Kim

**来源：** MICRO 2026，pp. 1848–1863；[DOI](https://doi.org/10.1109/MICRO67795.2026.00131)

## 英文摘要

GPU compilers merge all data types into a single unified register file, erasing the type information that binary-analysis tools rely on. We show that type recovery from this untyped register file is the central challenge of GPU binary lifting. We present CuLifter, a SASS-to-LLVM IR lifting framework that recovers register types via constraint propagation with conflict detection, reconstructs explicit control flow, and aggregates multi-instruction patterns. Across eight benchmark suites spanning open-source applications, vendor libraries, and optimized ML runtimes, CuLifter successfully lifts all 11,977 kernels to valid LLVM IR. Among the testable set, we achieve more than 90% execution correctness, verified via the CPU backend. An ablation study confirms that type recovery is the key mechanism to enable correct execution: disabling it causes 86.9% of kernels to execute incorrectly.

## 中文摘要

GPU 编译器将所有数据类型合并到一个统一的寄存器文件中，从而擦除二进制分析工具所依赖的类型信息。我们表明，从这个无类型寄存器文件中进行类型恢复是 GPU 二进制提升的核心挑战。我们提出了 CuLifter，一个 SASS 到 LLVM IR 提升框架，它通过冲突检测的约束传播来恢复寄存器类型，重建显式控制流，并聚合多指令模式。在涵盖开源应用程序、供应商库和优化的 ML 运行时的八个基准测试套件中，CuLifter 成功地将所有 11,977 个内核提升到有效的 LLVM IR。在可测试的集合中，我们通过 CPU 后端验证了超过 90% 的执行正确性。一项消融研究证实，类型恢复是实现正确执行的关键机制：禁用它会导致 86.9% 的内核执行不正确。

## 中文关键词

GPU 二进制提升；LLVM 中间表示；SASS 指令集；类型恢复；程序分析

## 代码与研究制品

- 代码仓库：[https://github.com/gthparch/CuLifter](https://github.com/gthparch/CuLifter)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6A](index.md) · [MICRO 2026 主页](../index.md)
