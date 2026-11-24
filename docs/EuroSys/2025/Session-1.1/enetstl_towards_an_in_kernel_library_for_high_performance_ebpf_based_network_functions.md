---
title: "eNetSTL: Towards an In-kernel Library for High-Performance eBPF-based Network Functions"
description: "EuroSys 2025 · Operating Systems · Bin Yang (Southeast University), Dian Shen (Southeast University), Junxue Zhang "
tags:
  - "EuroSys2025"
  - "Operating Systems"
---

# eNetSTL: Towards an In-kernel Library for High-Performance eBPF-based Network Functions

**中文标题：** 面向高性能 eBPF 网络功能的内核库

**所属 Session：** [Session 1.1: Operating Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Operating Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Operating Systems</p>
</div>

**作者**：Bin Yang (Southeast University), Dian Shen (Southeast University), Junxue Zhang (Hong Kong University of Science and Technology), Hanlin Yang (Southeast University), Lunqi Zhao (Southeast University), Beilun Wang (Southeast University), Guyue Liu (Peking Univeristy), Kai Chen (Hong Kong University of Science and Technology)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696094)

## 英文摘要

Using extended Berkeley Packet Filter (eBPF) to implement networking functions (NFs) has been a promising trend for modern network infrastructure. In this paper, we endeavor to implement 35 representative NFs with eBPF, but encounter inherent problems of either incomplete functionality or performance degradation of up to 49.2%. Conventional solutions like modifying the eBPF infrastructure or implementing functions directly in the kernel can lead to intrusive and unstable modifications.

To address these challenges, we present eNetSTL, the first in-kernel library for eBPF-based network functions. At its core, eNetSTL identifies shared performance-critical behaviors among the 35 NFs, and abstracts these behaviors into a minimal and stable set of in-kernel components (containing a memory wrapper, three algorithms, and two data structures). It reduces interaction overhead with eBPF and mitigate safety risks by using Rust and a metadata-assisted verifier. By doing so, eNetSTL minimizes intrusions into the kernel space, ensuring stability and compatibility with current and future requirements of eBPF-based NFs. We demonstrate the capabilities of eNetSTL by presenting three real-world use cases that leverage its comprehensive functionalities. Extensive testbed experiments on seven categories of NFs show that their implementation with eNetSTL outperforms the eBPF counterparts by up to 1.8×, in terms of packet processing rate.

## 中文摘要

使用扩展伯克利包过滤器（eBPF）实现网络功能（NF）已成为现代网络基础设施中一个有前景的趋势。在本文中，我们尝试用 eBPF 实现 35 个具有代表性的 NF，但遇到了功能不完整或性能下降高达 49.2% 的固有问题。修改 eBPF 基础设施或直接在内核中实现函数等传统方案会带来侵入性强且不稳定的修改。

为解决这些挑战，我们提出了 eNetSTL，这是首个面向基于 eBPF 的网络功能的内核内库。其核心在于，eNetSTL 识别出这 35 个 NF 之间共享的性能关键行为，并将这些行为抽象为一组最小且稳定的内核内组件（包含一个内存封装、三种算法和两种数据结构）。它通过使用 Rust 和元数据辅助的验证器，降低了与 eBPF 的交互开销并缓解了安全风险。通过这种方式，eNetSTL 最大限度地减少了对内核空间的侵入，确保其稳定性以及与基于 eBPF 的 NF 当前及未来需求的兼容性。我们通过三个利用其全面功能的真实用例展示了 eNetSTL 的能力。在七类 NF 上进行的大量测试床实验表明，使用 eNetSTL 实现的 NF 在包处理速率方面比对应的 eBPF 实现最高快 1.8 倍。

**英文关键词：** Network functions, eBPF, Performance profiling, In-kernel library

**中文关键词：** 网络功能、eBPF、性能剖析、内核内库

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
