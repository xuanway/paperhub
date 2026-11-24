---
title: "Empowering WebAssembly with Thin Kernel Interfaces"
description: "EuroSys 2025 · Operating Systems · Arjun Ramesh (Carnegie Mellon University), Tianshu Huang (Carnegie Mellon Univer"
tags:
  - "EuroSys2025"
  - "Operating Systems"
---

# Empowering WebAssembly with Thin Kernel Interfaces

**中文标题：** 通过轻量内核接口增强 WebAssembly

**所属 Session：** [Session 1.1: Operating Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Operating Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Operating Systems</p>
</div>

**作者**：Arjun Ramesh (Carnegie Mellon University), Tianshu Huang (Carnegie Mellon University), Ben Titzer (CMU), Anthony Rowe (Carnegie Mellon University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717470)

## 英文摘要

Wasm is gaining popularity outside the Web as a well-specified low-level binary format with ISA portability, low memory footprint and polyglot targetability, enabling efficient in-process sandboxing of untrusted code. Despite these advantages, Wasm adoption for new domains is often hindered by the lack of many standard system interfaces which precludes reusability of existing software and slows ecosystem growth.

This paper proposes thin kernel interfaces for Wasm, which directly expose OS userspace syscalls without breaking intra-process sandboxing, enabling a new class of virtualization with Wasm as a universal binary format. By virtualizing the bottom layer of userspace, kernel interfaces enable effortless application ISA portability, compiler backend reusability, and armor programs with Wasm’s built-in control flow integrity and arbitrary code execution protection. Furthermore, existing capability-based APIs for Wasm, such as WASI, can be implemented as a Wasm module over kernel interfaces, improving reuse, robustness, and portability through better layering. We present an implementation of this concept for two kernels – Linux and Zephyr – by extending a modern Wasm engine and evaluate our system’s performance on a number of sophisticated applications which can run for the first time on Wasm.

## 中文摘要

Wasm 作为一种规范完善的低层二进制格式，具备 ISA 可移植性、低内存占用以及多语言可编译等特性，能够高效地在进程内对不可信代码实施沙箱隔离，因而正在 Web 之外日益流行。尽管拥有这些优势，Wasm 在新领域的采用仍常常受制于诸多标准系统接口的缺失，这使现有软件难以复用，并拖慢了生态的发展。

本文为 Wasm 提出薄内核接口，在不破坏进程内沙箱隔离的前提下直接暴露操作系统用户态系统调用，从而以 Wasm 作为通用二进制格式开启一类新的虚拟化。通过虚拟化用户态的最底层，内核接口使应用能够轻松实现 ISA 可移植、编译器后端可复用，并以 Wasm 内建的控制流完整性和任意代码执行防护为程序提供保护。此外，Wasm 现有的基于能力的 API（如 WASI）可以在内核接口之上以 Wasm 模块的形式实现，通过更好的分层提升复用性、健壮性和可移植性。我们扩展了一个现代 Wasm 引擎，在两个内核——Linux 和 Zephyr——上实现了这一概念，并在若干此前无法在 Wasm 上运行的复杂应用上评估了系统的性能。

**英文关键词：** virtualization, operating systems, WebAssembly, Linux, Zephyr, compilers, interpreters, edge computing

**中文关键词：** 虚拟化、操作系统、WebAssembly、Linux、Zephyr、编译器、解释器、边缘计算

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
