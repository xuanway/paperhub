---
title: "Silhouette: Leveraging Consistency Mechanisms to Detect Bugs in Persistent Memory-Based File Systems"
description: "FAST 2025 · Security, Integrity, and Consistency · 用持久化不变量剪掉受保护写，把 PM 文件系统测试提速 10 倍"
tags:
  - "FAST2025"
  - "Security, Integrity, and Consistency"
  - "persistent memory"
  - "crash consistency"
---

# Silhouette: Leveraging Consistency Mechanisms to Detect Bugs in Persistent Memory-Based File Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PM 文件系统崩溃一致性测试要枚举 in-flight 写的重排，穷举不可行。Silhouette 用静态插桩加类型分析，用 journaling、复制的持久化不变量判定受保护的写，只对剩余写生成两种镜像，找齐 Vinter 与 Chipmunk 全部 bug 且快 10 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Security, Integrity, and Consistency</p>
</div>

**中文标题**：Silhouette：利用一致性机制检测持久内存文件系统中的缺陷

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/jiao](https://www.usenix.org/conference/fast25/presentation/jiao)

**论文 PDF**：[fast25-jiao.pdf](https://www.usenix.org/system/files/fast25-jiao.pdf)

**作者**：Bing Jiao（Florida State University）；Ashvin Goel（University of Toronto）；An-I Andy Wang（Florida State University）

**会议**：FAST 2025 · Santa Clara, CA · 第 407–423 页

**Session**：Security, Integrity, and Consistency · 2025-02-26 14:00–15:40 · Chair：Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

**所属 Session**：[Security, Integrity, and Consistency](index.md) · [FAST 2025](../index.md)

**关键词**：persistent memory, crash consistency, bug detection, journaling, file systems, static instrumentation

---

## 英文摘要

The emergence of persistent memory (PM), with its non-volatile and byte-addressable characteristics, has led to a novel storage programming paradigm. However, PM programs need to flush stores from CPU caches and correctly order them to avoid inconsistencies after a crash. As a result, many bug-detection tools have been developed for checking crash-consistency bugs in PM software. These bug detectors focus on reordering in-flight stores, crashing the system, and then checking for crash consistency during recovery. However, large-scale systems such as file systems have many in-flight stores, resulting in a large exploration space that makes exhaustive testing prohibitive.

This paper presents Silhouette, a bug-detection framework that targets PM-based file systems. These file systems use standard crash-consistency mechanisms such as journaling and replication. Silhouette uses a novel combination of static instrumentation and data-type-based dynamic analysis to check whether these file systems implement their consistency mechanisms correctly. If these checks pass, then all stores associated with the consistency mechanism (e.g., logging and checkpointing stores for journaling) are considered protected and only the unprotected stores are reordered during exploration. Our evaluation shows that Silhouette dramatically reduces the exploration space, finds all bugs found by existing tools 10x faster, and finds several new bugs in various PM file systems.

## 中文摘要

持久内存（PM）兼具非易失与字节可寻址特性，但程序必须显式 flush 并保证 store 顺序，否则崩溃后会出现不一致，于是出现一批检测工具：它们重排 in-flight store、制造崩溃、再检查恢复结果。文件系统这类大型系统的 in-flight store 极多，探索空间大到无法穷举。Silhouette 针对使用 journaling、复制等标准一致性机制的 PM 文件系统：先用静态插桩与基于数据类型的动态分析，检验这些机制是否实现正确；通过后，与机制相关的 store（如日志与 checkpoint 写）视为受保护，只对不受保护的 store 做重排探索。评估显示它大幅压缩探索空间，比现有工具快 10 倍找齐全部已知 bug，并发现若干新 bug。

## 一句话总结

> PM 文件系统普遍靠 journaling 或复制保证崩溃一致性；先证明机制实现正确，绝大部分写就不必参与重排枚举。

## 研究背景与问题

- **PM 编程的持久化负担**：持久内存可按字节寻址且非易失，但 store 先落在易失的 CPU cache，需要 flush 加 fence 才能持久化；编译器与处理器还会重排指令，崩溃点落在中间就产生不一致。
- **穷举不可行**：Yat 在 fence 前注入故障并持久化 in-flight store 的所有子集，n 个 in-flight store 就会产生 2 的 n 次方个崩溃镜像；作者用它跑 PMFS 时，某些测试需要数年才能完成。
- **剪枝仍有缺口**：Vinter 只探索恢复期间会被读到的地址，但要先跑一遍恢复、开销大，还可能漏掉“崩溃后无需恢复”的 bug；Chipmunk 在 cacheline 粒度插桩，会漏掉未被 flush 的 temporal store。
- **本文的观察**：被检查的 PM 文件系统都在使用少数几种标准一致性机制（journaling、replication），机制本身的实现正确性可以用不变量来检查，从而把与之相关的 store 整体标记为受保护。

## 核心贡献

- **以一致性机制为中心的框架 Silhouette**：先验证文件系统是否把 journaling、复制这类机制实现正确，再只对不受保护的 store 做重排探索。
- **持久化不变量的形式化**：按顺序（ordering）、位置（location）、数据（data）三类不变量描述机制应满足的持久化性质，并用每条 store 的 update time 与 persist time 做判定。
- **轻量注解**：只需声明与机制相关的结构体与字段（例如 NOVA inode 的 log tail），不必编写代码级的检查规则，注解还可以增量补充。
- **2CP 重排启发式**：对每个不受保护的 store 只生成两个崩溃镜像，把组合枚举降为线性数量，同时保持对现有工具所发现 bug 的覆盖。

## 方法与技术要点

- **轨迹分析**：在文件系统执行轨迹上工作，用 store、flush、fence 指令确定每条 store 的 update time（发出时刻）与 persist time（持久化时刻），不变量检查就建立在这两个时间之上。
- **静态插桩加动态类型分析**：用 LLVM 插桩把地址区间映射到数据类型，运行时把一条 store 解析成 nova_inode.log_tail = new_tail 这样的字段级写入，让逻辑不变量能落在具体的数据结构上。
- **不变量检查示例**：journaling 要求“先记日志、再原地改”，即日志 store 的 persist time 必须早于原地 store 的 update time；检查通过后，logging 与 checkpointing 的 store 全部视为受保护。
- **2CP 探索**：对每个不受保护的 store 分别构造“只持久化它”与“持久化其余全部、唯独不持久化它”两个崩溃镜像，覆盖现有工具能够发现的全部 bug 形态。
- **实现与适配**：在 x86 持久化模型上实现，支持 PMFS、NOVA-fortis 与 WineFS；从 NOVA 迁到 PMFS 时，一名研究生约 30 分钟就完成了注解。

## 评估与主要结果

- **测试对象与基线**：PMFS、NOVA-fortis（NOVA）、WineFS，使用 ACE Seq-3 的系统调用序列轨迹；对比对象是 Vinter 与 Chipmunk。
- **搜索空间**：同一轨迹下 NOVA、PMFS、WineFS 的排序点分别为 13,743、2,702、582 个；NOVA 有 80% 的排序点 in-flight store 少于 8 个但长尾很长，Silhouette 只探索其中不受保护的部分。
- **bug 发现**：找齐 Vinter 与 Chipmunk 报告的全部崩溃一致性 bug，速度快 10 倍，并在多个 PM 文件系统中发现十余个新 bug。
- **局限**：2CP 一次只测一个关键 store，无法覆盖 (A, B) 到 (C, D) 这类成对顺序（在基于校验和的复制中遇到），可扩展为成对测试；误报可按数据类型批量排除。

## 代码与研究制品

- [代码仓库](https://github.com/iaoing/Silhouette)

[返回 Security, Integrity, and Consistency](index.md) · [返回 FAST 2025](../index.md)
