---
title: "HyperHammer: Breaking Free from KVM-Enforced Isolation"
description: "ASPLOS 2025 · Session 4B · HyperHammer：突破 KVM 强制的隔离"
tags:
  - "ASPLOS2025"
  - "Session 4B"
  - "Memory & Storage"
---

# HyperHammer: Breaking Free from KVM-Enforced Isolation

**中文标题：** HyperHammer：突破 KVM 强制的隔离

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Wei Chen (Peking University), Zhi Zhang (University of Western Australia), Xin Zhang (Peking University), Qingni Shen (Peking University), Yuval Yarom (Ruhr University Bochum), Daniel Genkin (Georgia Institute of Technology), Chen Yan (Peking University), Zhe Wang (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Zhongguancun Laboratory)

**单位：** Peking University；University of Western Australia；Ruhr University Bochum；Georgia Institute of Technology；SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Zhongguancun Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716002) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Hardware-assisted virtualization is a key enabler of the modern cloud. It decouples virtual machine execution from the hardware it runs on, allowing increased flexibility through services such as dynamic hardware provisioning and live migration. Underlying this flexibility is the security promise that guest virtual machines are isolated from each other. However, due to the level of sharing between VMs, hardware vulnerabilities present a serious threat to this usage. One such vulnerability is Rowhammer, which allows attackers to modify the contents of memory to which they have no access. While the attack has been known for over a decade, published applications against such environments are limited, compromising only co-resident VMs, but not the hypervisor. Moreover, due to security concerns, a key component enabling their attack has been disabled. Hence, this attack is no longer applicable in a contemporary virtualized environment. In this paper, we examine how Rowhammer can affect virtualized systems. We present HyperHammer, a Rowhammer attack that breaks hypervisor-enforced memory isolation and further compromises the hypervisor. Due to the highly specific system requirements for leveraging Rowhammer bit flips, HyperHammer is demonstrated on a very particular system configuration. Therefore, as demonstrated, HyperHammer is more a proof-of-concept than an immediate threat to computer systems. Nonetheless, our work demonstrates that hardware-assisted virtualization does not fully protect the hypervisor, and that with sufficient engineering a determined attacker might achieve complete hypervisor compromise.

## 中文摘要

硬件辅助虚拟化是现代云的关键使能技术。它将虚拟机的执行与其所运行的硬件解耦，从而通过动态硬件供给、在线迁移等服务带来更高的灵活性。这种灵活性背后是这样一项安全承诺：客户虚拟机之间相互隔离。然而，由于虚拟机之间共享程度很高，硬件漏洞对这种使用方式构成了严重威胁。Rowhammer 就是其中一种漏洞，它允许攻击者修改其无权访问的内存内容。尽管该攻击已被知晓超过十年，但针对此类环境已发表的应用仍然有限，只能攻陷共驻的虚拟机，而无法攻陷 hypervisor。此外，出于安全考虑，使其攻击得以实施的一个关键组件已被禁用。因此，该攻击在当代虚拟化环境中不再适用。本文研究 Rowhammer 如何影响虚拟化系统。我们提出 HyperHammer，一种 Rowhammer 攻击，它打破了 hypervisor 强制的内存隔离，并进一步攻陷 hypervisor。由于利用 Rowhammer 位翻转需要非常特殊的系统条件，HyperHammer 是在一种非常特定的系统配置上进行演示的。因此，正如演示所示，HyperHammer 更像是一个概念验证，而非对计算机系统迫在眉睫的威胁。尽管如此，我们的工作表明，硬件辅助虚拟化并不能完全保护 hypervisor，并且只要工程投入足够，坚决的攻击者有可能实现彻底的 hypervisor 攻陷。

## 英文关键词

Hardware-assisted Virtualization, KVM, Memory Isolation, Rowhammer, Hypervisor Compromise

## 中文关键词

硬件辅助虚拟化；KVM；内存隔离；Rowhammer；Hypervisor 沦陷

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716002)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2025](../index.md)
