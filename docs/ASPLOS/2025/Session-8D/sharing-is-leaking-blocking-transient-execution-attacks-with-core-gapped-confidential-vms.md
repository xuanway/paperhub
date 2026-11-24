---
title: "Sharing is leaking: blocking transient-execution attacks with core-gapped confidential VMs"
description: "ASPLOS 2025 · Session 8D · 共享即泄漏：以核心隔离的机密虚拟机阻断瞬态执行攻击"
tags:
  - "ASPLOS2025"
  - "Session 8D"
  - "Security"
---

# Sharing is leaking: blocking transient-execution attacks with core-gapped confidential VMs

**中文标题：** 共享即泄漏：以核心隔离的机密虚拟机阻断瞬态执行攻击

**所属 Session：** [Session 8D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Charly Castes (EPFL,Google), Andrew Baumann (Google)

**单位：** EPFL,Google；Google

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674190) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Confidential VMs on platforms such as Intel TDX, AMD SEV and Arm CCA promise greater security for cloud users against even a hypervisor-level attacker, but this promise has been shattered by repeated transient-execution vulnerabilities and CPU bugs. At the root of this problem lies the need to multiplex CPU cores with all their complex microarchitectural state among distrusting entities, with an untrusted hypervisor in control of the multiplexing. We propose core-gapped confidential VMs, a set of softwareonly modifications that ensure that no distrusting code shares a core, thus removing all same-core side-channels and transient-execution vulnerabilities from the guest's TCB. We present an Arm-based prototype along with a performance evaluation showing that, not only does core-gapping offer performance competitive with non-confidential VMs, the greater locality achieved by avoiding shared cores can even improve performance for CPU-intensive workloads.

## 中文摘要

在 Intel TDX、AMD SEV 和 Arm CCA 等平台上，机密虚拟机承诺为云用户提供更高的安全性，甚至可抵御虚拟机监控器层级的攻击者，但这一承诺已被反复出现的瞬态执行漏洞和 CPU 缺陷所打破。该问题的根源在于，需要在互不信任的实体之间多路复用带有全部复杂微体系结构状态的 CPU 核心，而多路复用由不受信任的虚拟机监控器掌控。我们提出核心隔离的机密虚拟机，这是一组纯软件修改，确保互不信任的代码不会共享同一个核心，从而从客户机的 TCB 中消除所有同核侧信道与瞬态执行漏洞。我们给出了一个基于 Arm 的原型以及性能评估，结果表明，核心隔离不仅提供了与非机密虚拟机相当的性能，而且通过避免共享核心所获得的更高局部性，甚至能够提升 CPU 密集型工作负载的性能。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674190)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8D](index.md) · [返回 ASPLOS 2025](../index.md)
