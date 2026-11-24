---
title: "Enabling fast networking in the public cloud"
description: "ASPLOS 2026 · Session 8B · 在公有云中实现快速网络"
tags:
  - "ASPLOS2026"
  - "Session 8B"
  - "Serverless & Cloud Networking"
---

# Enabling fast networking in the public cloud

**中文标题：** 在公有云中实现快速网络

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Alireza Sanaee (University of Cambridge & Huawei), Vahab Jabrayilov (Columbia University), Ilias Marinos (NVIDIA), Farbod Shahinfar (Politecnico di Milano), Divyanshu Saxena (The University of Texas at Austin), Kostis Kaffes (Columbia University), Gianni Antichi (Politecnico di Milano & Queen Mary University of London)

**单位：** University of Cambridge & Huawei；Columbia University；NVIDIA；Politecnico di Milano；The University of Texas at Austin；Politecnico di Milano & Queen Mary University of London

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790158) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Despite a decade of research, most high-performance userspace network stacks remain impractical for public cloud tenants developing their applications atop Virtual Machines (VMs). We identify two root causes: (1) reliance on specialized NIC features (e.g., flow steering, deep buffers) absent in commodity cloud vNICs, and (2) rigid execution models ill-suited to diverse application needs. We present Machnet, a high-performance and flexible userspace network stack designed for public cloud VMs. Machnet uses only a minimal set of vNIC features that any major cloud provider supports. It also relies on a microkernel architecture to enable flexible application execution. We evaluate Machnet across three major public clouds and on production-grade applications, including a key-value store, an HTTP server, and a state-machine replication system. We release Machnet at https: //github.com/microsoft/machnet.

## 中文摘要

尽管经过十年的研究，大多数高性能用户态网络栈对于那些在虚拟机（VM）之上开发应用的公有云租户而言仍不实用。我们指出两个根本原因：(1) 依赖专用网卡特性（例如流导向、深缓冲），而这些特性在商用云 vNIC 中并不存在；(2) 僵化的执行模型难以适配多样化的应用需求。我们提出 Machnet，一个为公有云 VM 设计的高性能且灵活的用户态网络栈。Machnet 只使用任何主流云厂商都支持的最小集合的 vNIC 特性。它还依靠微内核架构来实现灵活的应用执行。我们在三大公有云以及生产级应用上评估 Machnet，包括键值存储、HTTP 服务器和状态机复制系统。我们在 https: //github.com/microsoft/machnet 发布 Machnet。

## 英文关键词

User-level networking, DPDK, Remote Procedure Call (RPC), Low-latency systems, Network stack optimization, Cloud infrastructure, Virtualization

## 中文关键词

用户态网络；DPDK；远程过程调用（RPC）；低延迟系统；网络栈优化；云基础设施；虚拟化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790158)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2026](../index.md)
