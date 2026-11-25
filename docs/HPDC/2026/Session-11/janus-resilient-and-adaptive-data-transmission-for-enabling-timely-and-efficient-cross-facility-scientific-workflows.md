---
title: "JANUS: Resilient and Adaptive Data Transmission for Enabling Timely and Efficient Cross-Facility Scientific Workflows"
description: "HPDC 2026 · Session 11 — Communication, Workflows & Sustainability"
tags:
  - "HPDC2026"
  - "Session 11"
  - "Communication, Workflows & Sustainability"
---

# JANUS: Resilient and Adaptive Data Transmission for Enabling Timely and Efficient Cross-Facility Scientific Workflows

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 11</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807590)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#EsaulovCPSKBW26](https://dblp.org/db/conf/hpdc/hpdc2026.html#EsaulovCPSKBW26)

**作者**：Vladislav Esaulov, Jieyang Chen, Norbert Podhorszki, Fred Suter, Scott Klasky, Anu G. Bourgeois, Lipeng Wan

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）

---

## 英文摘要

In modern science, the growing complexity of large-scale scientific projects has led to an increasing reliance on cross-facility scientific workflows, where resources and expertise from multiple institutions and geographic locations are leveraged to accelerate scientific discovery. These workflows often require transmitting huge amounts of scientific data through wide-area networks. Although high-speed networks like ESnet and transfer services such as Globus have improved data mobility, several challenges remain. The sheer volume of data can overwhelm network bandwidth, widely used transport protocols such as TCP suffer from inefficiencies due to retransmissions triggered by packet loss, and existing fault-tolerance mechanisms like erasure coding introduce substantial overhead. In this paper, we propose Janus, a resilient and adaptable data transmission approach designed for cross-facility scientific workflows. Unlike traditional TCP-based methods, Janus leverages UDP, integrates erasure coding for fault tolerance, and combines it with error-bounded lossy compression to reduce overhead. This novel design allows users to balance data transmission time and accuracy, optimizing transfer performance based on specific scientific requirements. Additionally, Janus dynamically adjusts erasure coding parameters in response to real-time network conditions, ensuring efficient data transfers even in fluctuating environments. We develop optimization models for determining ideal configurations and implement adaptive data transfer protocols to enhance reliability. Through extensive simulations and real-network experiments, we demonstrate that Janus significantly improves transfer efficiency while maintaining data fidelity.

## 中文摘要

在现代科学中，大规模科学项目日益复杂，导致对跨设施科学工作流的依赖不断增加：利用来自多个机构和地理位置的资源与专业知识来加速科学发现。这些工作流常常需要通过广域网传输海量科学数据。尽管 ESnet 等高速网络和 Globus 等传输服务改善了数据移动性，仍存在若干挑战。数据量之大可能压垮网络带宽；TCP 等广泛使用的传输协议因丢包引发的重传而效率低下；纠删码等现有容错机制带来可观开销。本文提出 Janus，一种面向跨设施科学工作流的弹性、自适应数据传输方法。与传统的基于 TCP 的方法不同，Janus 利用 UDP，集成纠删码实现容错，并结合误差有界有损压缩以降低开销。这一新颖设计允许用户在数据传输时间与精度之间权衡，根据具体科学需求优化传输性能。此外，Janus 根据实时网络状况动态调整纠删码参数，确保在波动环境中也能高效传输数据。我们开发了用于确定理想配置的优化模型，并实现了自适应数据传输协议以增强可靠性。通过大量仿真与真实网络实验，我们证明 Janus 在保持数据保真度的同时显著提升了传输效率。

## 英文关键词

Scientific Data, Data Transfer, Error-Bounded Lossy Compression, Erasure Coding, Fault-Tolerance

## 中文关键词

科学数据，数据传输，误差有界有损压缩，纠删码，容错

---

[← 返回 Session 11 — Communication, Workflows & Sustainability](index.md)
