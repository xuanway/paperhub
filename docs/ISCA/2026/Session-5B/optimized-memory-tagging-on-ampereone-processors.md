---
title: "Optimized Memory Tagging on AmpereOne® Processors"
description: "ISCA 2026 · Session 5B · Optimized Memory Tagging on AmpereOne® Processors"
tags:
  - "ISCA2026"
  - "Session 5B"
  - "Industry Track 2"
---

# Optimized Memory Tagging on AmpereOne® Processors

**中文标题：** AmpereOne® 处理器上的优化内存标记

**所属 Session：** [Session 5B](index.md) · [ISCA 2026](../index.md)

**作者：** Shivnandan Kaushik, Mahesh Madhav, Nagi Aboulenein, Jason Bessette, Sandeep Brahmadathan, Benjamin Chaffin, Matthew Erler, Stephan Jourdan, Thomas Maciukenas, Ramya Jayaram Masti, Jon Perry, Massimo Sutera, Scott Tetrick, Bret Toll, David Turley, Carl Worth, Atiq Bajwa

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory-safety escapes continue to form the launching pad for a wide range of security attacks, especially for the substantial base of deployed software that is coded in pointer-based languages such as C/C++. Although compiler and Instruction Set Architecture (ISA) extensions have been introduced to address elements of this issue, the overhead and/or comprehensive applicability have limited broad production deployment. The Memory Tagging Extension (MTE) to the ARM AArch64 Instruction Set Architecture is a valuable tool to address memory-safety escapes; when used in synchronous tag-checking mode, MTE provides deterministic detection and prevention of sequential buffer overflow attacks, and probabilistic detection and prevention of exploits resulting from temporal use-after-free pointer programming bugs. The AmpereOne® processor, launched in 2024, is the first datacenter processor to support MTE. Its optimized MTE implementation uniquely incurs no memory capacity overhead for tag storage and provides synchronous tag-checking with single-digit performance impact across a broad range of datacenter class workloads. This paper analyzes the complete hardware-software stack of those workloads, identifying application memory management as the primary remaining source of overhead and highlighting clear opportunities for software optimization. The combination of an efficient hardware foundation and a clear path for software improvement makes the MTE implementation of the AmpereOne® processor highly attractive for deployment in production cloud environments.

## 中文摘要

内存安全逃逸（memory-safety escapes）仍然是各类安全攻击的跳板，对于以 C/C++ 等基于指针的语言编写的大量已部署软件尤其如此。尽管已有编译器和指令集架构（ISA）扩展来处理该问题的部分环节，但其开销和／或普适性限制了大规模的生产部署。ARM AArch64 指令集架构的内存标记扩展（MTE）是应对内存安全逃逸的有力工具；在同步标记检查模式下使用时，MTE 能够确定性地检测并阻止顺序缓冲区溢出攻击，并能概率性地检测并阻止由时序上的释放后使用（use-after-free）指针编程缺陷所导致的利用行为。2024 年推出的 AmpereOne® 处理器是首款支持 MTE 的数据中心处理器。其优化的 MTE 实现独到地不为标记存储带来任何内存容量开销，并在广泛的数据中心级负载上以个位数的性能影响提供同步标记检查。本文分析了这些负载的完整软硬件栈，指出应用内存管理是剩余开销的主要来源，并揭示了明确的软件优化机会。高效的硬件基础与清晰的软件改进路径相结合，使 AmpereOne® 处理器的 MTE 实现对于在生产云环境中部署极具吸引力。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 5B](index.md) · [返回 ISCA 2026](../index.md)
