---
title: "Fork: A Dual Congestion Control Loop for Small and Large Flows in Datacenters"
description: "EuroSys 2025 · Network/Network Congestion Control · Yuan Liu (Tianjin University), Wenxin Li (Tianjin University & Huaxiahaorui Tech"
tags:
  - "EuroSys2025"
  - "Network/Network Congestion Control"
---

# Fork: A Dual Congestion Control Loop for Small and Large Flows in Datacenters

**中文标题：** 面向数据中心大小流的双拥塞控制环路

**所属 Session：** [Session 3.2: Network/Network Congestion Control](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network/Network Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network/Network Congestion Control</p>
</div>

**作者**：Yuan Liu (Tianjin University), Wenxin Li (Tianjin University & Huaxiahaorui Technology (Tianjin) Co., Ltd.), Yulong Li (Tianjin University), Lide Suo (Tianjin University), Xuan Gao (Tianjin University), Xin Xie (Tianjin University), Sheng Chen (Tianjin University & Huaxiahaorui Technology (Tianjin) Co., Ltd.), Ziqi Fan (Tianjin University), Wenyu Qu (Tianjin University), Guyue Liu (Peking University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696101)

## 英文摘要

Many existing transport designs aim to deliver ultra-low latency and high bandwidth for applications in high-speed datacenter networks. However, almost all of them intertwine the control of small and large flows using the same control entity (e.g., sender or receiver) and congestion feedback signal (e.g., ECN or credit), thus bringing significant performance impairments. By contrast, we seek to decouple the rate control of small flows from that of large ones.

To this end, we present Fork, a new datacenter transport that relies on two parallel control loops. One sender-driven small flow control loop (SCP) runs at the highest priority with a multi-flow ACK clocking mechanism to achieve low latencies for small flows. Another receiver-driven low-priority large flow control loop (LCP) employs two simple yet effective mechanisms: ECN migration and AIMD credit control, to protect small flow transmission while gracefully utilizing the spare bandwidth left by SCP. We have implemented a Fork prototype based on DPDK, and shown, through both testbed experiments and simulations, that compared to Homa and Aeolus, Fork reduces the average FCT of small flows by up to 81.4% and 67.7%, respectively, while maintaining lower FCTs for large flows.

## 中文摘要

许多现有传输设计旨在为高速数据中心网络中的应用提供超低延迟和高带宽。然而，它们几乎都使用相同的控制实体（如发送方或接收方）和拥塞反馈信号（如 ECN 或信用）来交织控制小流和大流，从而带来显著的性能损害。相比之下，我们试图将小流的速率控制与大流的速率控制解耦。

为此，我们提出 Fork，一种依赖两个并行控制环路的新型数据中心传输方案。一个由发送方驱动的小流控制环路（SCP）以最高优先级运行，并采用多流 ACK 时钟机制，以实现小流的低延迟。另一个由接收方驱动的低优先级大流控制环路（LCP）采用两种简单而有效的机制：ECN 迁移和 AIMD 信用控制，以保护小流传输，同时优雅地利用 SCP 留下的空闲带宽。我们基于 DPDK 实现了 Fork 原型，并通过测试床实验和仿真表明，与 Homa 和 Aeolus 相比，Fork 分别将小流的平均 FCT 降低最多 81.4% 和 67.7%，同时为大流保持较低的 FCT。

**英文关键词：** datacenter networking, congestion control

**中文关键词：** 数据中心网络、拥塞控制

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
