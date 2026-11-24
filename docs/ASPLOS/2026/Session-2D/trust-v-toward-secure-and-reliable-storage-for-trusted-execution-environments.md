---
title: "Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments"
description: "ASPLOS 2026 · Session 2D · Trust-V：面向可信执行环境的安全可靠存储"
tags:
  - "ASPLOS2026"
  - "Session 2D"
  - "DRAM Reliability & Security"
---

# Trust-V: Toward Secure and Reliable Storage for Trusted Execution Environments

**中文标题：** Trust-V：面向可信执行环境的安全可靠存储

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2026](../index.md)

**作者：** SeungKyun Han (Chungnam National University), Jiyeon Yang (Chungnam National University), Jinsoo Jang (Chungnam National University)

**单位：** Chungnam National University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790242) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Trusted execution environments (TEEs) provide strong isolation for security-critical applications (enclaves) and their runtime data from potentially malicious operating systems. While TEEs also support secure storage by sealing data and storing it persistently on media, they do not ensure the integrity of sealed data, leaving it vulnerable to deletion or manipulation by an untrusted OS. In this work, we present Trusted Storage, a runtime storage isolation mechanism for TEEs that guarantees the integrity of TEE persistent data. The core design partitions storage into trusted and untrusted regions and enforces access control by locking MMIO regions and monitoring block I/O. To ensure portability, Trusted Storage requires no hardware modifications or additional hardware. We implemented a prototype, Trust-V, on the RISC-V platform. In particular, to support secure operation on legacy devices where security features are limited, Trust-V introduces a Virtual-M mode, a sandboxed privileged execution environment in machine mode, for securely hosting the monitor. Our evaluation demonstrates that, although Trust-V incurs up to 3.86× system overhead, it allows TEE software to reliably store and retrieve persistent data.

## 中文摘要

可信执行环境（Trusted Execution Environment，TEE）为安全攸关的应用（enclave）及其运行时数据提供与潜在恶意操作系统之间的强隔离。虽然 TEE 还通过封装数据并将其持久存储在介质上来支持安全存储，但它们并不保证封装数据的完整性，使其易被不可信操作系统删除或篡改。在本工作中，我们提出 Trusted Storage，这是一种面向 TEE 的运行时存储隔离机制，可保证 TEE 持久数据的完整性。其核心设计将存储划分为可信区域与不可信区域，并通过锁定 MMIO 区域和监控块 I/O 来实施访问控制。为保证可移植性，Trusted Storage 无需硬件修改或额外硬件。我们在 RISC-V 平台上实现了原型系统 Trust-V。特别地，为在安全特性有限的遗留设备上支持安全运行，Trust-V 引入了 Virtual-M 模式，即机器模式下的沙箱化特权执行环境，用于安全地承载监控器。我们的评估表明，尽管 Trust-V 带来最高 3.86× 的系统开销，但它使 TEE 软件能够可靠地存储和取回持久数据。

## 英文关键词

Trusted Execution Environment; Trusted Storage; Data Integrity Protection; Privilege Separation and Sandboxing

## 中文关键词

可信执行环境；可信存储；数据完整性保护；特权分离与沙箱

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790242)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2026](../index.md)
