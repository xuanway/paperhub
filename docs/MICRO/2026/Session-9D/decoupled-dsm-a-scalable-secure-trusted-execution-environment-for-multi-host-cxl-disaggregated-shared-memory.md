---
title: "Decoupled-DSM: A Scalable Secure Trusted Execution Environment for Multi-Host CXL Disaggregated Shared Memory"
description: "MICRO 2026 · Session 9D · Decoupled-DSM：面向多主机 CXL 分离式共享内存的可扩展安全可信执行环境"
tags:
  - "MICRO2026"
  - "CXL"
---

# Decoupled-DSM: A Scalable Secure Trusted Execution Environment for Multi-Host CXL Disaggregated Shared Memory

**中文标题：** Decoupled-DSM：面向多主机 CXL 分离式共享内存的可扩展安全可信执行环境

**所属 Session：** [Session 9D](index.md) · [MICRO 2026](../index.md)

**作者：** Yuxin Yang, Yuanchao Xu

**来源：** MICRO 2026，pp. 3545–3559；[DOI](https://doi.org/10.1109/MICRO67795.2026.00236)

## 英文摘要

Confidential cloud computing based on Trusted Execution Environments (TEEs) has gained widespread adoption for protecting virtual machine (VM) memory from privileged software. Meanwhile, Compute Express Link (CXL) enables disaggregated shared memory (CXL-DSM), allowing hardware-coherent, in-place multi-host data sharing. However, existing CPU-centric TEEs are incompatible with CXL-DSM: they enforce memory ownership at the host level, enabling undetected cross-host access, and rely on encrypt-copy mechanisms that negate CXL-DSM performance benefits. This paper proposes Decoupled-DSM TEE, a scalable architecture for secure multi-host CXL-DSM. Decoupled-DSM retains memory allocation at the CXL device while offloading frequent permission checks to host-side TEEs, and introduces a host-CXL validation protocol that reuses reverse map table mechanisms to prevent forged mappings. Evaluation shows that Decoupled-DSM incurs only 7.3%–9.2% overhead over an insecure baseline.

## 中文摘要

基于可信执行环境 (TEE) 的机密云计算已被广泛采用，用于保护虚拟机 (VM) 内存免受特权软件的侵害。同时，Compute Express Link (CXL) 支持分解共享内存 (CXL-DSM)，从而实现硬件一致的就地多主机数据共享。然而，现有的以 CPU 为中心的 TEE 与 CXL-DSM 不兼容：它们在主机级别强制执行内存所有权，从而实现未检测到的跨主机访问，并依赖于否定 CXL-DSM 性能优势的加密复制机制。本文提出了 De Coupled-DSM TEE，这是一种用于安全多主机 CXL-DSM 的可扩展架构。解耦 DSM 保留 CXL 设备上的内存分配，同时将频繁的权限检查卸载到主机端 TEE，并引入了主机 CXL 验证协议，该协议重用反向映射表机制以防止伪造映射。评估表明，与不安全的基线相比，解耦 DSM 仅产生 7.3%–9.2% 的开销。

## 中文关键词

CXL；可信执行环境；内存访问控制；多主机共享内存；分离式内存

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9D](index.md) · [MICRO 2026 主页](../index.md)
