---
title: "Marionette: A RowHammer Attack via Row Coupling"
description: "ASPLOS 2025 · Session 4B · Marionette：一种基于行耦合的 RowHammer 攻击"
tags:
  - "ASPLOS2025"
  - "Session 4B"
  - "Memory & Storage"
---

# Marionette: A RowHammer Attack via Row Coupling

**中文标题：** Marionette：一种基于行耦合的 RowHammer 攻击

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Seungmin Baek (Seoul National University), Minbok Wi (Seoul National University), Seonyong Park (Seoul National University), Hwayong Nam (Seoul National University), Michael Jaemin Kim (Seoul National University), Nam Sung Kim (University of Illinois), Jung Ho Ahn (Seoul National University)

**单位：** Seoul National University；University of Illinois

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707242) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

A body of recent work has revealed that two different rows in a DRAM bank, from the perspective of a processor-memory interface, are connected to the same wordline but two separate row buffers (bitline sense amplifiers) in certain DRAM chips. Such a pair of rows is referred to as a “coupled-row pair.” Coupled-row pairs pose a substantial security threat as RowHammer bitflips can be caused not only by the conventional, adjacent aggressor rows but also by their coupled rows that are distant in physical address. We investigate the impact of a coupled row on both FPGAbased infrastructure and server systems. In RowHammer attacks, coupled rows have hammering strength nearly identical to aggressor rows, with these attacks invisible to conventional, processor-side mitigation solutions. By exploiting these observations, we present Marionette, a new type of RowHammer attack that exploits coupled rows to extend the existing RowHammer attack surface. First, coupled rows enable an attacker to evade two types of existing software-based RowHammer defenses: trackingand isolation-based defenses. We induce RowHammer bitflips successfully against tracking-based RowHammer defenses by silently hammering coupled rows. We also identify the feasibility of RowHammer bitflips in an isolationbased inter-VM RowHammer defense by breaking DRAMsubarray-level isolation. Second, we successfully conduct an existing RowHammer exploit in a server under the trackingbased RowHammer defense. In a native server system, Marionette enhances the success rate of the RowHammer exploit Attribution International 4.0 License..66×. Lastly, we explore lightweight mitigation schemes for Marionette by exposing the coupled-row relationship to systems.

## 中文摘要

近期一系列工作揭示，在某些 DRAM 芯片中，从处理器-内存接口的视角看，同一个 DRAM bank 内两个不同的行连接到同一条字线，却连接到两个独立的行缓冲区（位线灵敏放大器）。这样的一对行被称为“耦合行对”（coupled-row pair）。耦合行对构成重大安全威胁，因为 RowHammer 位翻转不仅可以由传统的相邻攻击行引起，也可以由物理地址上相距较远的耦合行引起。我们研究了耦合行对基于 FPGA 的基础设施和服务器系统的影响。在 RowHammer 攻击中，耦合行的锤击强度与攻击行几乎相同，而这些攻击对传统的处理器侧缓解方案是不可见的。利用这些观察，我们提出 Marionette，一种新型 RowHammer 攻击，它利用耦合行扩展了现有的 RowHammer 攻击面。首先，耦合行使攻击者能够规避两类现有的基于软件的 RowHammer 防御：基于跟踪的防御和基于隔离的防御。我们通过静默地锤击耦合行，成功地在基于跟踪的 RowHammer 防御下引发了 RowHammer 位翻转。我们还通过打破 DRAM 子阵列级隔离，发现了在基于隔离的跨 VM RowHammer 防御中实现 RowHammer 位翻转的可行性。其次，我们在处于基于跟踪的 RowHammer 防御下的服务器中成功实施了一项已有的 RowHammer 漏洞利用。在原生服务器系统中，Marionette 将该 RowHammer 利用的成功率提升了 66 倍。最后，我们通过将耦合行关系暴露给系统，探索了针对 Marionette 的轻量级缓解方案。

## 英文关键词

DRAM, RowHammer, RowPress, Coupled row, Reliability, Security

## 中文关键词

DRAM；RowHammer；RowPress；耦合行；可靠性；安全性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707242)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2025](../index.md)
