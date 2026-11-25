---
title: "Multipath Collective Communication Beyond Scale-up Networks in GPU Clouds"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Yuchen Xu (Peking University), Jianglong Nie (Peking University), Baojia Li (Ten"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# Multipath Collective Communication Beyond Scale-up Networks in GPU Clouds

**中文标题：** GPU 云中超越纵向扩展网络的多路径集合通信

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Yuchen Xu (Peking University), Jianglong Nie (Peking University), Baojia Li (Tencent), Mingzhuo Chen (Tencent), Hao Lu (Tencent), Guanyu Qu (Tencent), Zhenchuan Liu (Tencent), Shuangshaung Yin (Tencent), Xiaojie Huang (Tencent), Chunzhi He (Tencent), Yinben Xia (Tencent), Quan Wen (Tencent), Xiang Li (Tencent), Zekun He (Tencent), Yachen Wang (Tencent), Xianneng Zou (Tencent), Congcong Miao (Tencent), Wenfei Wu (Peking University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769330)

## 英文摘要

Hardware vendors introduce scale-up networks interconnecting accelerators to speed up communication in distributed training. We argue that in the context of GPU clouds, the scale-out network can be a good complement to the collective communication that is originally performed on scale-up networks. We build a system named MPCCS to enable multipath transmission of collectives on both networks. MPCCS essentially splits the traffic of collective flows to two networks. MPCCS overcomes three challenges caused by the progress of hardware-offloaded networks and the diversity of collective communication. First, it devises a dual-window protocol to enable the runtime traffic splitting over rigid hardware-offloaded interfaces. Second, it devises a bandwidth-delay product (BDP) estimation algorithm to enable bandwidth-adaptive traffic splitting, overcoming the difficulty of invisibility of transmission states (RTT and throughput) due to hardware encapsulation. Third, it devises coflow-synchronized multipath transmission for collective flows, which achieves universal applicability for diverse collectives in terms of correctness and performance optimality. We implement MPCCS and conduct extensive experiments both on the testbed and in simulation. MPCCS achieves a 23%~54% speedup compared with vanilla NCCL on communication microbenchmarks and above 10% acceleration for LLM training.

## 中文摘要

硬件厂商引入了互连加速器的纵向扩展网络，以加速分布式训练中的通信。我们认为，在 GPU 云的语境下，横向扩展网络可以成为原本在纵向扩展网络上执行的集合通信的良好补充。我们构建了名为 MPCCS 的系统，以在两个网络上实现集合通信的多路径传输。MPCCS 本质上是将集合通信流的流量拆分到两个网络。MPCCS 克服了硬件卸载网络的进展与集合通信的多样性所带来的三个挑战。第一，它设计了双窗口协议，以在刚性的硬件卸载接口之上实现运行时流量拆分。第二，它设计了带宽时延积（BDP）估计算法以实现带宽自适应的流量拆分，克服了硬件封装导致传输状态（RTT 与吞吐）不可见的困难。第三，它为集合通信流设计了共流同步的多路径传输，在正确性与性能最优性方面实现了对多种集合通信的普适性。我们实现了 MPCCS，并在测试床与仿真中开展了大量实验。在通信微基准上，MPCCS 相比原生 NCCL 实现了 23%~54% 的加速；在 LLM 训练中实现了 10% 以上的加速。

**英文关键词：** Multipath Collective Communication, Scale-up Networks, Scale-out Networks, GPU Clouds

**中文关键词：** 多路径集合通信、纵向扩展网络、横向扩展网络、GPU 云

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
