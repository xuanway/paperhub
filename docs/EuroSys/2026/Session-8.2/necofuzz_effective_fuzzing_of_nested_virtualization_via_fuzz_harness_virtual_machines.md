---
title: "NecoFuzz: Effective Fuzzing of Nested Virtualization via Fuzz-Harness Virtual Machines"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Reima Ishii (The University of Tokyo), Takaaki Fukai (National Institute of Adva"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# NecoFuzz: Effective Fuzzing of Nested Virtualization via Fuzz-Harness Virtual Machines

**中文标题：** NecoFuzz：借助模糊测试载体虚拟机对嵌套虚拟化进行高效模糊测试

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Reima Ishii (The University of Tokyo), Takaaki Fukai (National Institute of Advanced Industrial Science and Technology), Takahiro Shinagawa (The University of Tokyo)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769347)

## 英文摘要

Nested virtualization is now widely supported by major cloud vendors, allowing users to leverage virtualization-based technologies in the cloud. However, supporting nested virtualization significantly increases host hypervisor complexity and introduces a new attack surface in cloud platforms. While many prior studies have explored hypervisor fuzzing, none has explicitly addressed nested virtualization due to the challenge of generating effective virtual machine (VM) instances with a vast state space as fuzzing inputs.

We present NecoFuzz, the first fuzzing framework that systematically targets nested virtualization-specific logic in hypervisors. NecoFuzz synthesizes executable fuzz-harness VMs with internal states near the boundary between valid and invalid, guided by an approximate model of hardware-assisted virtualization specifications. Since vulnerabilities in nested virtualization often stem from incorrect handling of unexpected VM states, this specification-guided, boundary-oriented generation significantly improves coverage of security-critical code across different hypervisors.

We implemented NecoFuzz on Intel VT-x and AMD-V by extending AFL++ to support fuzz-harness VMs. NecoFuzz achieved 84.7% and 74.2% code coverage for nested virtualization-specific code on Intel VT-x and AMD-V, respectively, and uncovered six previously unknown vulnerabilities across three hypervisors, including two assigned CVEs.

## 中文摘要

嵌套虚拟化目前已得到主要云厂商的广泛支持，使用户能够在云中利用基于虚拟化的技术。然而，支持嵌套虚拟化显著增加了宿主 hypervisor 的复杂度，并在云平台上引入了新的攻击面。尽管此前已有许多研究探索 hypervisor 模糊测试，但由于难以生成具有巨大状态空间的有效虚拟机（VM）实例作为模糊测试输入，尚无工作明确针对嵌套虚拟化。

我们提出 NecoFuzz，这是首个系统性针对 hypervisor 中嵌套虚拟化特有逻辑的模糊测试框架。NecoFuzz 在硬件辅助虚拟化规范的近似模型引导下，合成内部状态接近有效与无效边界的可执行模糊测试载体虚拟机。由于嵌套虚拟化中的漏洞往往源于对意外 VM 状态的错误处理，这种规范引导、面向边界的生成方式显著提升了对不同 hypervisor 中安全关键代码的覆盖。

我们通过扩展 AFL++ 以支持模糊测试载体虚拟机，在 Intel VT-x 与 AMD-V 上实现了 NecoFuzz。NecoFuzz 在 Intel VT-x 与 AMD-V 上分别对嵌套虚拟化特有代码达到 84.7% 与 74.2% 的代码覆盖率，并在三个 hypervisor 中发现了六个此前未知的漏洞，其中两个被分配了 CVE 编号。

**英文关键词：** Nested Virtualization, Fuzzing

**中文关键词：** 嵌套虚拟化、模糊测试

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
