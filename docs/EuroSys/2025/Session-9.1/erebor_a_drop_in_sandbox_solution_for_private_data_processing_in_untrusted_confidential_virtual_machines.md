---
title: "Erebor: A Drop-In Sandbox Solution for Private Data Processing in Untrusted Confidential Virtual Machines"
description: "EuroSys 2025 · Security and Privacy · Chuqi Zhang (National University of Singapore), Rahul Priolkar (Arizona State Un"
tags:
  - "EuroSys2025"
  - "Security and Privacy"
---

# Erebor: A Drop-In Sandbox Solution for Private Data Processing in Untrusted Confidential Virtual Machines

**中文标题：** 面向不可信机密虚拟机中私有数据处理的即插即用沙箱

**所属 Session：** [Session 9.1: Security and Privacy](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Security and Privacy。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Security and Privacy</p>
</div>

**作者**：Chuqi Zhang (National University of Singapore), Rahul Priolkar (Arizona State University), Yuancheng Jiang (National University of Singapore), Yuan Xiao (Intel Labs), Mona Vij (Intel Labs), Zhenkai Liang (National University of Singapore), Adil Ahmad (Arizona State University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717464)

## 英文摘要

Confidential virtual machines (CVMs) are designed to protect data in cloud machines, but they fail in this task in common Software-as-a-Service (SaaS) cloud environments. In such settings, the software stack within a CVM, including service programs and the operating system, that receives and processes data may intentionally disclose it to attackers. We present Erebor, a sandboxing architecture for CVMs that processes client data in secure containers, where restrictions apply to both (a) access by all untrusted outside components and (b) the sandbox’s ability to communicate data through memory and software-controlled direct or covert exits. Erebor enables such restrictions through a security monitor design based on intra-kernel privilege isolation for CVM, fully compatible with emerging cloud deployments without requiring host modifications. Under realistic scenarios, such as large language model inference and private information retrieval, Erebor only adds a performance overhead of 4.5%–13.2%, demonstrating its practicality in terms of enabling strong data sandboxing in modern cloud machines.

## 中文摘要

机密虚拟机（CVM）旨在保护云主机中的数据，但在常见的软件即服务（SaaS）云环境中却无法完成这一任务。在此类环境中，CVM 内负责接收和处理数据的软件栈（包括服务程序和操作系统）可能故意将数据泄露给攻击者。我们提出 Erebor，一种面向 CVM 的沙箱架构，它在安全容器中处理客户端数据，并对两方面同时施加限制：（a）所有不可信外部组件的访问；（b）沙箱通过内存以及由软件控制的直接或隐蔽出口传递数据的能力。Erebor 通过一种基于 CVM 内核内特权隔离的安全监控器设计来实现这些限制，完全兼容新兴的云部署方式，且无需修改宿主机。在真实场景（如大语言模型推理和私有信息检索）下，Erebor 仅带来 4.5%–13.2% 的性能开销，表明其在现代云主机中实现强数据沙箱的实用性。

**英文关键词：** CVM, Sandboxed Container, OS Design

**中文关键词：** CVM、沙箱容器、操作系统设计

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
