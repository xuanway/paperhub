---
title: "A Hardware-Software Co-Design for Efficient Secure Containers"
description: "EuroSys 2025 · Security and Privacy · Jiacheng Shi (Shanghai Jiao Tong University), Yang Yu (Shanghai Jiao Tong Univer"
tags:
  - "EuroSys2025"
  - "Security and Privacy"
---

# A Hardware-Software Co-Design for Efficient Secure Containers

**中文标题：** 面向高效安全容器的软硬件协同设计

**所属 Session：** [Session 9.1: Security and Privacy](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Security and Privacy。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Security and Privacy</p>
</div>

**作者**：Jiacheng Shi (Shanghai Jiao Tong University), Yang Yu (Shanghai Jiao Tong University), Jinyu Gu (Shanghai Jiao Tong University), Yubin Xia (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717473)

## 英文摘要

VM-level containers provide strong isolation by running each container with its own kernel in a VM. However, they rely on virtualization hardware designed for general-purpose VMs, causing non-negligible performance overhead compared to OS-level containers. This performance gap widens dramatically in nested virtualization scenarios, where secure containers run inside a VM.

This paper proposes CKI (Container Kernel Isolation), a hardware-software co-design for efficient secure containers, based on two insights. First, Protection Keys for Supervisor (PKS) facilitates constructing a new privilege level for securely collocating multiple container kernels within the host kernel, without involving non-root ring-0. Second, the general-purpose virtualization mechanisms used by secure containers provide unnecessary features that exceed the actual isolation requirements of containers, especially the two-stage address translation, which is not required for container isolation, introducing avoidable performance overhead.

Thus, CKI avoids using the virtualization hardware for running container kernels and removes the unnecessary virtualization mechanism like two-stage address translation. Instead, it uses PKS to construct a new privilege level for isolating multiple container kernels, which allows more efficient cross-privilege interaction; it also uses single-stage address translation for each container while monitoring the page table updates in a lightweight way to ensure cross-container memory isolation.

Our experiments on real-world applications demonstrate the efficiency of CKI, reducing the latency of memory-intensive applications by up to 72% and 47% compared with state-of-the-art hardware-assisted virtualization (HVM) and software-based virtualization (PVM), respectively.

## 中文摘要

VM 级容器通过在 VM 中为每个容器运行各自的内核来提供强隔离。然而，它们依赖为通用 VM 设计的虚拟化硬件，与操作系统级容器相比带来不可忽视的性能开销。在嵌套虚拟化场景中（安全容器运行在 VM 内），这一性能差距急剧扩大。

本文提出 CKI（容器内核隔离），一种面向高效安全容器的软硬件协同设计，基于两点见解。第一，特权级保护密钥（PKS）有助于为主机内核内的多个容器内核安全共置构建新的特权级，而无需涉及非 root 的 ring-0。第二，安全容器所使用的通用虚拟化机制提供了超出容器实际隔离需求的多余特性，尤其是两阶段地址转换，它对容器隔离并非必需，却引入了可避免的性能开销。

因此，CKI 避免使用虚拟化硬件来运行容器内核，并移除诸如两阶段地址转换之类的非必要虚拟化机制。取而代之，它使用 PKS 构建新的特权级以隔离多个容器内核，从而实现更高效的跨特权级交互；它还为每个容器使用单阶段地址转换，同时以轻量方式监控页表更新，以确保跨容器的内存隔离。

我们在真实应用上的实验证明了 CKI 的高效性：与最先进的硬件辅助虚拟化（HVM）和基于软件的虚拟化（PVM）相比，CKI 分别将内存密集型应用的延迟降低最多 72% 和 47%。

**英文关键词：** Containers, Secure Containers, Memory Protection Keys, Operating Systems, Virtualization

**中文关键词：** 容器、安全容器、内存保护密钥、操作系统、虚拟化

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
