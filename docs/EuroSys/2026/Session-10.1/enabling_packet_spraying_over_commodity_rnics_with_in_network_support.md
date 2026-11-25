---
title: "Enabling Packet Spraying over Commodity RNICs with In-Network Support"
description: "EuroSys 2026 · Distributed Systems and Multicore · Xiangzhou Liu (Hong Kong University of Science and Technology), Wenxue Li (Hong "
tags:
  - "EuroSys2026"
  - "Distributed Systems and Multicore"
---

# Enabling Packet Spraying over Commodity RNICs with In-Network Support

**中文标题：** 借助网内支持在商用 RNIC 上实现数据包喷洒

**所属 Session：** [Session 10.1: Distributed Systems and Multicore](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Systems and Multicore。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Systems and Multicore</p>
</div>

**作者**：Xiangzhou Liu (Hong Kong University of Science and Technology), Wenxue Li (Hong Kong University of Science and Technology), Zihao Wang (Hong Kong University of Science and Technology), Kai Chen (Hong Kong University of Science and Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803588)

## 英文摘要

AI training workloads exhibit unique traffic patterns that mismatch the ECMP load balancing of RDMA networks, leading to severe throughput degradation. While packet-level load balancing (e.g., random packet spraying, adaptive routing, etc.) offers a promising alternative to ECMP by providing fine-grained traffic distribution, it introduces out-of-order (OOO) packet arrivals. The reliable transport mechanism of current commodity RDMA NICs (RNICs) misinterprets these OOO arrivals as packet loss, causing spurious retransmissions and unnecessary slow starts.

We propose Themis, a lightweight middleware deployed on programmable switches, that eliminates the incompatibility between packet spraying and reliable transport in commodity RNICs without requiring any modifications to them. At its core, Themis applies PSN-based packet spraying at the source ToR switch, enabling it to infer whether an OOO packet and the expected packet traverse the same path. Building on this capability, Themis at the destination ToR analyzes NACKs triggered by OOO arrivals to determine whether they result from actual packet loss. It then blocks invalid NACKs while allowing valid ones to pass through. We implement a fully functional prototype of Themis using Tofino2. Experiments demonstrate that Themis reduces the communication completion time of Allreduce and Alltoall by 22.7%∼35.4% and 29.3%∼47.3%, respectively, compared to directly combining commodity RNICs and adaptive routing.

## 中文摘要

AI 训练工作负载呈现出独特的流量模式，与 RDMA 网络的 ECMP 负载均衡不匹配，导致吞吐量严重下降。数据包级负载均衡（如随机数据包喷洒、自适应路由等）通过提供细粒度的流量分发，成为 ECMP 的有前景替代方案，但它会引入数据包乱序（OOO）到达。当前商用 RDMA 网卡（RNIC）的可靠传输机制会将这些乱序到达误判为丢包，从而引发虚假重传和不必要的慢启动。

我们提出 Themis，一种部署在可编程交换机上的轻量级中间件，它在无需对商用 RNIC 做任何修改的情况下消除了数据包喷洒与可靠传输之间的不兼容性。其核心是，Themis 在源端 ToR 交换机上应用基于 PSN 的数据包喷洒，使其能够推断某个乱序数据包与期望数据包是否经过同一路径。在此基础上，目的端 ToR 的 Themis 分析由乱序到达触发的 NACK，以判定它们是否由真实丢包引起，随后阻塞无效的 NACK，而允许有效的 NACK 通过。我们使用 Tofino2 实现了 Themis 的完整功能原型。实验表明，与直接组合商用 RNIC 和自适应路由相比，Themis 将 Allreduce 和 Alltoall 的通信完成时间分别降低 22.7%～35.4% 和 29.3%～47.3%。

**英文关键词：** Datacenter networks, Load balancing

**中文关键词：** 数据中心网络、负载均衡

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
