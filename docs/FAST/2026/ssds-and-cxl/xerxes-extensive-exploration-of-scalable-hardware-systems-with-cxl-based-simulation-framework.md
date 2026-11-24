---
title: "Xerxes: Extensive Exploration of Scalable Hardware Systems with CXL-Based Simulation Framework"
description: "FAST 2026 · SSDs and CXL · 第 329–346 页"
tags:
  - "FAST2026"
  - "SSDs and CXL"
---

# Xerxes: Extensive Exploration of Scalable Hardware Systems with CXL-Based Simulation Framework

**中文标题**：Xerxes：利用基于 CXL 的仿真框架广泛探索可扩展硬件系统

**Session**：SSDs and CXL · 2026-02-25 14:00–15:40 · Chair：Ethan Miller（University of California, Santa Cruz, and Pure Storage）

**作者**：Yuda An and Shushu Yi, Peking University; Bo Mao, Xiamen University; Qiao Li, Mohamed bin Zayed University of Artificial Intelligence; Mingzhe Zhang, Institute of Information Engineering, Chinese Academy of Sciences; Diyu Zhou, Peking University; Ke Zhou, Huazhong University of Science and Technology (HUST); Nong Xiao, Sun Yat-sen University; Guangyu Sun, Yingwei Luo, and Jie Zhang, Peking University

**会议**：FAST 2026 · Santa Clara, CA · 第 329–346 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/an](https://www.usenix.org/conference/fast26/presentation/an)

**论文 PDF**：[fast26-an.pdf](https://www.usenix.org/system/files/fast26-an.pdf)

---

## 英文摘要

Compute Express Link (CXL) is an emerging industry standard that offers high-performance cache-coherent interconnects to heterogeneous devices, including host CPUs, computation accelerators, and memory devices. It aims to support high system scalability, peer-to-peer communication, and high-speed data transmission. To this end, the latest version of the CXL protocol introduces several new features, including port-based routing, device-managed coherence, and PCIe 6.0 support. However, the absence of CXL hardware and the methodological limitations of existing simulators hinder the exploration of these new architectures. To bridge this gap, we propose *Xerxes*, a novel simulation framework designed from the ground up to faithfully model the emerging features in the latest CXL protocol. It employs a dedicated interconnect layer to support interconnection within diverse system topologies. It also implements important components to conduct specific functions required by these features. Utilizing Xerxes, we comprehensively explore multiple aspects of CXL systems, including system topologies, device-managed coherences, and impacts of PCIe characteristics, and derive key observations that can inspire new designs of high-performance CXL systems. The codes of Xerxes are open-sourced and available at [https://github.com/ChaseLab-PKU/Xerxes](https://github.com/ChaseLab-PKU/Xerxes).

## 中文摘要

Compute Express Link（CXL）是一种新兴行业标准，为包括主机 CPU、计算加速器和内存设备在内的异构设备提供高性能缓存一致性互连。它旨在支持高系统可扩展性、对等通信和高速数据传输。为此，最新版本的 CXL 协议引入了若干新特性，包括基于端口的路由、设备管理的一致性和 PCIe 6.0 支持。然而，CXL 硬件的缺乏以及现有仿真器的方法学局限，阻碍了对这些新架构的探索。为弥合这一差距，我们提出 Xerxes，一个从零开始设计、旨在忠实建模最新 CXL 协议中新兴特性的新型仿真框架。它采用专用互连层来支持多种系统拓扑内的互连。它还实现了重要组件，以执行这些特性所需的特定功能。利用 Xerxes，我们全面探索了 CXL 系统的多个方面，包括系统拓扑、设备管理的一致性和 PCIe 特性的影响，并得出了可启发高性能 CXL 系统新设计的关键观察。Xerxes 的代码已开源，见 [https://github.com/ChaseLab-PKU/Xerxes](https://github.com/ChaseLab-PKU/Xerxes)。
