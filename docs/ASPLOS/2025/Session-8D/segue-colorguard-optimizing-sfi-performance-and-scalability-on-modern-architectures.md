---
title: "Segue & ColorGuard: Optimizing SFI Performance and Scalability on Modern Architectures"
description: "ASPLOS 2025 · Session 8D · Segue 与 ColorGuard：在现代体系结构上优化 SFI 的性能与可扩展性"
tags:
  - "ASPLOS2025"
  - "Session 8D"
  - "Security"
---

# Segue & ColorGuard: Optimizing SFI Performance and Scalability on Modern Architectures

**中文标题：** Segue 与 ColorGuard：在现代体系结构上优化 SFI 的性能与可扩展性

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shravan Narayan (UT Austin), Tal Garfinkel (UC San Diego), Evan Johnson (UC San Diego), Zachary Yedidia (Stanford University), Yingchen Wang (UC Berkeley), Andrew Brown (Intel), Anjo Vahldiek-Oberwagner (Intel Labs), Michael LeMay (Intel Labs), Wenyong Huang (Intel), Xin Wang (Intel), Mingqiu Sun (Intel), Dean Tullsen (UC San Diego), Deian Stefan (UC San Diego)

**单位：** UT Austin；UC San Diego；Stanford University；UC Berkeley；Intel；Intel Labs

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707249) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Software-based fault isolation (SFI) enables in-process isolation through compiler instrumentation of memory accesses, and is a critical part of WebAssembly (Wasm). We present two optimizations that improve SFI performance and scalability: Segue uses x86-64 segmentation to reduce the cost of instrumentation on memory accesses, e.g., it eliminates 44.7% of Wasm's overhead on a Wasm-compatible subset of SPEC CPU 2006, and reduces overhead of Wasm-sandboxed font rendering in Firefox by 75%; ColorGuard leverages memory tagging (e.g., MPK), to enable up to a 15× increase in the number of Wasm instances that can run concurrently in a single address space, improving efficiency for high scale server-side workloads. We also explore the challenges of deploying these optimizations in three production toolchains: Wasm2c, WAMR and Wasmtime.

## 中文摘要

基于软件的故障隔离（SFI）通过编译器对内存访问进行插桩来实现进程内隔离，是 WebAssembly（Wasm）的关键组成部分。我们提出两项优化来提升 SFI 的性能与可扩展性：Segue 利用 x86-64 分段机制降低内存访问插桩的开销，例如，它在 SPEC CPU 2006 的 Wasm 兼容子集上消除了 Wasm 44.7% 的开销，并将 Firefox 中经 Wasm 沙箱化的字体渲染开销降低 75%；ColorGuard 借助内存标记（例如 MPK），使单个地址空间中可并发运行的 Wasm 实例数量最多提升 15×，从而提升大规模服务器端工作负载的效率。我们还探讨了在三种生产工具链 Wasm2c、WAMR 和 Wasmtime 中部署这些优化所面临的挑战。

## 英文关键词

SFI, Wasm, sandboxing, optimization

## 中文关键词

SFI；Wasm；沙箱化；优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707249)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2025](../index.md)
