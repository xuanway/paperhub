---
title: "Compute eXpress Leak: New Cache Attacks Using CXL Devices"
description: "MICRO 2026 · Session 4B · Compute eXpress Leak：利用 CXL 设备的新型缓存攻击"
tags:
  - "MICRO2026"
  - "CXL"
  - "Cache"
---

# Compute eXpress Leak: New Cache Attacks Using CXL Devices

**中文标题：** Compute eXpress Leak：利用 CXL 设备的新型缓存攻击

**所属 Session：** [Session 4B](index.md) · [MICRO 2026](../index.md)

**作者：** Ali Aqdas, Zheng Zhang, Yue Pan, Zixuan Wang, Tajana Rosing, Jishen Zhao, Kazem Taram

**来源：** MICRO 2026，pp. 1397–1412；[DOI](https://doi.org/10.1109/MICRO67795.2026.00104)

## 英文摘要

This paper presents the first systematic study of timing channels introduced by Compute eXpress Link (CXL) protocols and implementations. We show that CXL coherence operations expose new attack surfaces that allow untrusted devices and hosts to infer the memory access patterns across trust boundaries. We demonstrate that non-cacheable push writes can be exploited by a device to both inject cache lines into the host's last-level cache, and detect their residency through timing, enabling a new Prime+Probe-style attack from the device. This attack, dubbed PUSH+PUSH, does not require access to a host timer, and can bypass partitioning-based defenses that rely on Intel CAT. Furthermore, we analyze the security implications of cross-host memory sharing introduced in CXL 3.0. In particular, we study timing leakage arising from back-invalidation snoops and snoop-filter-based coherence tracking and simulate the vulnerability in CXLMemSim. We then present SnoopDog, a forward-looking cross-host timing attack that distinguishes whether a cache line is privately owned by another host based on access latency. We demonstrate end-to-end cross-host side-channel attacks, including recovery of tokens from large language model inference when model weights are shared across hosts on a CXL memory device.

## 中文摘要

本文首次对由 Compute eXpress Link (CXL) 协议和实现引入的定时通道进行系统研究。我们表明，CXL 一致性操作暴露了新的攻击面，允许不受信任的设备和主机跨信任边界推断内存访问模式。我们演示了设备可以利用不可缓存的推送写入将缓存行注入主机的末级缓存，并通过计时检测它们的驻留情况，从而从设备启用新的 Prime+Probe 式攻击。这种攻击被称为 PUSH+PUSH，不需要访问主机计时器，并且可以绕过依赖于 Intel CAT 的基于分区的防御。此外，我们分析了 CXL 3.0 中引入的跨主机内存共享的安全隐患。特别是，我们研究了由反向失效监听和基于监听过滤器的一致性跟踪引起的时序泄漏，并在 CXLMemSim 中模拟了该漏洞。然后，我们提出了 SnoopDog，这是一种前瞻性的跨主机定时攻击，它根据访问时延来区分缓存线是否为另一台主机私有。我们演示了端到端跨主机侧通道攻击，包括当模型权重在 CXL 内存设备上的主机之间共享时从大语言模型推理中恢复词元。

## 中文关键词

CXL；微架构安全；缓存攻击；侧信道

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21549983](https://doi.org/10.5281/zenodo.21549983)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 4B](index.md) · [MICRO 2026 主页](../index.md)
