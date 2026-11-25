---
title: "CofferOS: Hardening OS-level Virtualization with Rust"
description: "EuroSys 2026 · OS & Virtualization · Minkyu Jung (KAIST), Chanshin Kwak (School of Computing, KAIST), Junho Ahn (KAIS"
tags:
  - "EuroSys2026"
  - "OS & Virtualization"
---

# CofferOS: Hardening OS-level Virtualization with Rust

**中文标题：** CofferOS：用 Rust 加固操作系统级虚拟化

**所属 Session：** [Session 1.1: OS & Virtualization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：OS & Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · OS & Virtualization</p>
</div>

**作者**：Minkyu Jung (KAIST), Chanshin Kwak (School of Computing, KAIST), Junho Ahn (KAIST), Sunho Park (KAIST), Changjun Lee (KAIST), Jongyul Kim (University of Illinois Urbana-Champaign), Jeehoon Kang (FuriosaAI), Youngjin Kwon (KAIST)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803569)

## 英文摘要

OS-level virtualization (e.g., Linux containers) has become a cornerstone of modern cloud systems. While it offers the illusion of isolated kernels for processes, these processes share the same underlying kernel, raising critical concerns around security, fault isolation, and the inability to customize kernels. Existing solutions address the issues by employing virtual machines that isolate kernels. However, these approaches incur significant performance overhead.

To provide strong isolation and customizability, we propose CofferOS, a new kernel for OS-level virtualization. By combining structural encapsulation with Rust’s memory safety guarantees, CofferOS eliminates shared kernel states among containers. The container is implemented as a single class, called Coffer, which contains the entire state of a container. Each running container is instantiated as a separate instance of Coffer. As a result, each container operates in complete isolation, without sharing any state with other containers. Furthermore, CofferOS introduces the Personality mechanism, enabling kernel customization for individual containers through a modular and pluggable design. We implement CofferOS, achieving performance comparable to Linux containers in various workloads and demonstrating its improved security, fault isolation, and customizability, showcasing its practical applicability and flexibility.

## 中文摘要

操作系统级虚拟化（如 Linux 容器）已成为现代云系统的基石。尽管它为进程提供了隔离内核的假象，但这些进程共享同一个底层内核，由此引发了对安全性、故障隔离以及无法定制内核的关键担忧。现有解决方案通过采用隔离内核的虚拟机来应对这些问题，然而这些方法会带来显著的性能开销。

为提供强隔离性与可定制性，我们提出 CofferOS，一种面向操作系统级虚拟化的新型内核。通过将结构化封装与 Rust 的内存安全保证相结合，CofferOS 消除了容器之间的共享内核状态。容器被实现为一个名为 Coffer 的单一类，其中包含容器的全部状态。每个运行中的容器都被实例化为一个独立的 Coffer 实例。因此，每个容器完全隔离运行，不与其他容器共享任何状态。此外，CofferOS 引入 Personality 机制，通过模块化、可插拔的设计实现对单个容器的内核定制。我们实现了 CofferOS，在各种工作负载下取得与 Linux 容器相当的性能，并展示了其在安全性、故障隔离和可定制性方面的改进，体现了其实际适用性与灵活性。

**英文关键词：** OS-level virtualization, Memory safety, System hardening, Language-based security

**中文关键词：** 操作系统级虚拟化、内存安全、系统加固、基于语言的安全

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
