---
title: "Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context"
description: "ASPLOS 2026 · Session 4A · Triton-Sanitizer：一个面向 Triton 的快速、设备无关且具备丰富诊断上下文的内存检查器"
tags:
  - "ASPLOS2026"
  - "Session 4A"
  - "ML Training & Monitoring"
---

# Triton-Sanitizer: A Fast and Device-Agnostic Memory Sanitizer for Triton with Rich Diagnostic Context

**中文标题：** Triton-Sanitizer：一个面向 Triton 的快速、设备无关且具备丰富诊断上下文的内存检查器

**所属 Session：** [Session 4A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Hao Wu (George Mason University), Qidong Zhao (Google), Songqing Chen (George Mason University), Yang Chen (Meta), Yueming Hao (Meta), Tony CW Liu (Anthropic), Sijia Chen (Meta), Adnan Aziz (Meta), Keren Zhou (George Mason University)

**单位：** George Mason University；Google；Meta；Anthropic

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790241) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Memory access errors remain one of the most pervasive bugs in GPU programming. Existing GPU sanitizers such as compute-sanitizer detect memory access errors by instrumenting every memory instruction in low-level IRs or binaries, which imposes high overhead and provides minimal memory access error diagnostic context for fixing problems. We present Triton-Sanitizer, the first device-agnostic memory sanitizer designed for Triton, a domain-specific language for developing portable, efficient GPU kernels for deep learning workloads. Triton-Sanitizer leverages Triton's tile-oriented semantics to construct symbolic expressions for memory addresses and masks, verifies them with an SMT solver, and selectively falls back to eager simulation for indirect accesses. This hybrid analysis enables precise detection of memory access errors without false positives while avoiding the cost of per-access instrumentation. Beyond detection, Triton-Sanitizer generates rich diagnostic reports that attribute violations to the tensors nearest to the violated addresses, track the complete call path, and expose the symbolic operations responsible for incorrect addresses. Evaluated on seven widely used open-source repositories of Triton kernels, Triton-Sanitizer uncovered 24 previously unknown memory access errors, of which 8 have already been fixed and upstreamed by us. Compared to compute-sanitizer, Triton-Sanitizer achieves speedups ranging from 1.07× to 14.66×, with an average improvement of 1.62×, demonstrating its ability to enhance performance, precision, and usability in memory access error detection.

## 中文摘要

内存访问错误仍然是 GPU 编程中最普遍的一类缺陷。现有的 GPU 检查器（如 compute-sanitizer）通过插桩低层 IR 或二进制中的每一条内存指令来检测内存访问错误，这带来了很高的开销，并且为修复问题提供的内存访问错误诊断上下文极为有限。我们提出 Triton-Sanitizer，这是首个为 Triton 设计的设备无关内存检查器；Triton 是一种领域特定语言，用于为深度学习工作负载开发可移植、高效的 GPU 内核。Triton-Sanitizer 利用 Triton 面向图块（tile）的语义，为内存地址和掩码构建符号表达式，用 SMT 求解器对其进行验证，并对间接访问选择性地回退到急切模拟。这种混合分析能够精确检测内存访问错误且不产生假阳性，同时避免了逐次访问插桩的成本。除检测之外，Triton-Sanitizer 还生成丰富的诊断报告，将违规归因到最接近违规地址的张量，追踪完整的调用路径，并揭示导致错误地址的符号操作。在七个广泛使用的 Triton 内核开源仓库上进行评估，Triton-Sanitizer 发现了 24 个此前未知的内存访问错误，其中 8 个已由我们修复并上游合并。与 compute-sanitizer 相比，Triton-Sanitizer 实现了从 1.07× 到 14.66× 的加速，平均提升 1.62×，展现了其在内存访问错误检测中提升性能、精度与可用性的能力。

## 英文关键词

GPU, Debugging, Symbolic Execution, Memory Safety, Triton, Memory Access Errors

## 中文关键词

GPU；调试；符号执行；内存安全；Triton；内存访问错误

## 代码与研究制品

- [研究制品（Zenodo）](https://doi.org/10.5281/zenodo.17925531)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790241)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4A](index.md) · [返回 ASPLOS 2026](../index.md)
