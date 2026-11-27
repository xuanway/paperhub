---
title: "SpecMPK: Efficient In-Process Isolation with Speculative and Secure Permission Update Instruction"
description: "HPCA 2025 · Securing your Chips"
tags:
  - "HPCA2025"
  - "Securing your Chips"
---

# SpecMPK: Efficient In-Process Isolation with Speculative and Secure Permission Update Instruction

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Securing your Chips。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Securing your Chips</p>
</div>

**论文链接**：
**作者**：Debpratim Adak (North Carolina State University), Huiyang Zhou (North Carolina State University), Eric Rotenberg (North Carolina State University), Amro Awad (University of Oxford)
**会议**：HPCA 2025

---

## 中文标题

SpecMPK：基于推测且安全的权限更新指令的高效进程内隔离

## 英文摘要

In today’s digital landscape, software applications are susceptible to various threats arising from vulnerabilities in unsafe programming languages (C, C++) and speculative out-of-order cores in high-performance computers. Researchers recommended enhancements in both software and hardware for protection against such attacks. In-process isolation is a promising way to mitigate memory-related attacks. It compartmentalizes critical data and pointers in a separate memory region and enforces access control to this memory region. Any operation to such memory locations may require a permission adjustment before and after the operation, depending on the required access control. Memory Protection Keys, a recent architecture support, has been adopted by multiple processor vendors to allow access control changes in the user space, leading to lower performance overhead than the conventional system calls (e.g., mprotect). Still, this technology incurs significant performance overhead since the permission update instruction is serialized. Our research demonstrates significant performance improvement by allowing speculative permission updates. However, speculative execution of the permission update instruction may upgrade access permission transiently, leading to potential speculative execution attacks. To prevent such attacks, we propose Speculative Memory Protection Keys (SpecMPK), a lightweight microarchitecture enhancement to examine permission change and block transiently upgraded memory instructions until they become non-squashable. SpecMPK significantly improves performance compared to a serialized domain switch instruction. This work shows an average 12.21% performance improvement for selected SPEC workloads requiring frequent domain switches for various memory safety schemes using memory protection keys.

## 中文摘要

在当今的数字化环境中，软件应用容易受到源自不安全编程语言（C、C++）缺陷以及高性能计算机中推测式乱序核心的各类威胁。研究者建议在软件与硬件两方面进行增强以抵御此类攻击。进程内隔离是缓解内存相关攻击的一种有前景的方法。它将关键数据与指针分割到单独的内存区域，并对该内存区域实施访问控制。对此类内存位置的任何操作都可能需要在操作前后调整权限，具体取决于所需的访问控制。内存保护键（Memory Protection Keys）作为一项较新的架构支持，已被多家处理器厂商采用，使用户空间中的访问控制变更成为可能，相比传统系统调用（如 mprotect）带来更低的性能开销。然而，由于权限更新指令是串行化的，该技术仍产生显著的性能开销。我们的研究表明，允许推测式权限更新可带来显著的性能提升。不过，权限更新指令的推测执行可能瞬时提升访问权限，从而导致潜在的推测执行攻击。为防止此类攻击，我们提出推测式内存保护键（SpecMPK），一种轻量级微架构增强，用于检查权限变更并阻塞被瞬时提权的内存指令，直至它们不可被清除。与串行化的域切换指令相比，SpecMPK 显著提升了性能。本工作表明，对于使用内存保护键的各类内存安全方案中需要频繁域切换的选定 SPEC 负载，平均性能提升 12.21%。
