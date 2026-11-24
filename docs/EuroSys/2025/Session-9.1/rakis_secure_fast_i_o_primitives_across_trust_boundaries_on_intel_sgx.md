---
title: "RAKIS: Secure Fast I/O Primitives Across Trust Boundaries on Intel SGX"
description: "EuroSys 2025 · Security and Privacy · Mansour Alharthi (Georgia Institute of Technology), Fan Sang (Georgia Institute "
tags:
  - "EuroSys2025"
  - "Security and Privacy"
---

# RAKIS: Secure Fast I/O Primitives Across Trust Boundaries on Intel SGX

**中文标题：** 在 Intel SGX 上跨信任边界提供安全快速 I/O 原语

**所属 Session：** [Session 9.1: Security and Privacy](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Security and Privacy。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Security and Privacy</p>
</div>

**作者**：Mansour Alharthi (Georgia Institute of Technology), Fan Sang (Georgia Institute of Technology), Dmitrii Kuvaiskii (Intel Labs), Mona Vij (Intel Labs), Taesoo Kim (Georgia Institute of Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696090)

## 英文摘要

The use of Intel® Software Guard Extensions (SGX) offers robust security measures for shielding applications in untrusted environments. However, the performance overhead experienced by IO-intensive applications within SGX limits widespread adoption. Prior approaches have proposed the use of userspace kernel-bypass libraries such as Data Plane Development Kit (DPDK) inside SGX enclaves to enable direct access to IO devices. However, these solutions often come at the cost of increasing the Trusted Computing Base (TCB) size, expanding the attack surface, and complicating deployment. In this paper, we introduce RAKIS, a comprehensive system that securely enables SGX enclave programs to leverage fast IO Linux kernel primitives without modifying user applications. RAKIS prioritizes the security of its TCB components by employing rigorous software testing and verification methods, embodying a security-by-design approach. Importantly, RAKIS achieves performance advantages without sacrificing TCB size or introducing deployment intricacies and demonstrates significant improvements in benchmark tests with a 4.6x increase in UDP network throughput compared to state-of-the-art SGX enclave LibOS (Gramine-SGX). To demonstrate the practical applicability of RAKIS, we evaluate its performance on four real-world programs showcasing an average performance improvement of 2.8x compared to Gramine-SGX across all workloads.

## 中文摘要

使用 Intel® Software Guard Extensions（SGX）为在不可信环境中保护应用提供了强健的安全措施。然而，SGX 内 I/O 密集型应用所经历的性能开销限制了其广泛采用。先前的方法提出在 SGX 飞地内使用用户态内核旁路库（如数据平面开发套件（DPDK））来实现对 I/O 设备的直接访问。然而，这些方案往往以增大可信计算基（TCB）规模、扩大攻击面并使部署复杂化为代价。在本文中，我们介绍 RAKIS，一个全面的系统，它安全地使 SGX 飞地程序能够利用快速的 Linux 内核 I/O 原语，而无需修改用户应用。RAKIS 通过采用严格的软件测试和验证方法，优先保障其 TCB 组件的安全性，体现了“安全源于设计”的理念。重要的是，RAKIS 在不牺牲 TCB 规模或引入部署复杂性的前提下获得性能优势，并在基准测试中展现出显著改进：与最先进的 SGX 飞地 LibOS（Gramine-SGX）相比，UDP 网络吞吐量提升 4.6 倍。为展示 RAKIS 的实际适用性，我们在四个真实程序上评估其性能，在所有工作负载上相比 Gramine-SGX 平均性能提升 2.8 倍。

**英文关键词：** Secure enclaves, express data path, iouring, trusted execution environments, system security, Intel SGX

**中文关键词：** 安全飞地、eXpress Data Path、io_uring、可信执行环境、系统安全、Intel SGX

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
