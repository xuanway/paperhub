---
title: "Introspective Congestion Control for Consistent High Performance"
description: "EuroSys 2025 · Network/Network Congestion Control · Wanchun Jiang (School of Computer Science and Engineering, Central South Univers"
tags:
  - "EuroSys2025"
  - "Network/Network Congestion Control"
---

# Introspective Congestion Control for Consistent High Performance

**中文标题：** 面向持续高性能的内省式拥塞控制

**所属 Session：** [Session 3.2: Network/Network Congestion Control](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network/Network Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network/Network Congestion Control</p>
</div>

**作者**：Wanchun Jiang (School of Computer Science and Engineering, Central South University), Haoyang Li (School of Computer Science and Engineering, Central South University), Jia Wu (School of Computer Science and Engineering, Central South University), Kai Wang (School of Computer Science and Engineering, Central South University), Fengyuan Ren (Department of Computer Science and Technology, Tsinghua University), Jianxin Wang (School of Computer Science and Engineering, Central South University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696084)

## 英文摘要

The congestion control (CC) algorithm is expected to achieve consistent high performance under different network environments. Traditionally, classic CCs are designed with the methodology of inferring path conditions to guide the rate adjustment. However, this methodology suffers from wrong path condition inferences in certain cases, which mislead the rate adjustment and lead to performance degradation. To avoid wrong path condition inferences, we develop the projection-based introspective method and design the introspective congestion control (ICC) algorithm in this paper. Specifically, the rate adjustment rules are designed to possess a specialized profile such that the projection of the profile can be distinguished under unchanged path conditions. In this way, the projection, which can be distinguished from the time series of delay signals in the frequency domain, facilitates ICC to extract more information for path condition inferences. Consequently, with the introspection on the projection, ICC can avoid being misled by wrong path condition inferences and thus achieve consistent high performance under different conditions. The advantages of ICC are confirmed through extensive experiments conducted on various locally emulated scenarios, global testbeds over the Internet, and the Alipay platform.

## 中文摘要

拥塞控制（CC）算法被期望在不同网络环境下都能取得稳定的高性能。传统上，经典 CC 采用推断路径状况以指导速率调整的方法论来设计。然而，该方法论在某些情况下会出现路径状况误判，从而误导速率调整并导致性能下降。为避免路径状况误判，本文提出基于投影的内省方法，并设计了内省拥塞控制（ICC）算法。具体而言，速率调整规则被设计为具有一种特殊的剖面，使得在路径状况不变时该剖面的投影可被区分。这样，该投影可在频域中从延迟信号的时间序列里被辨识出来，从而帮助 ICC 提取更多信息用于路径状况推断。因此，通过对投影进行内省，ICC 能够避免被错误的路径状况推断所误导，从而在不同状况下取得稳定的高性能。我们在多种本地仿真场景、互联网上的全球测试床以及支付宝平台上开展了大量实验，验证了 ICC 的优势。

**英文关键词：** Congestion Control, Consistent High Performance, Path Condition Inferences, Introspective, Internet

**中文关键词：** 拥塞控制、稳定高性能、路径状况推断、内省、互联网

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
