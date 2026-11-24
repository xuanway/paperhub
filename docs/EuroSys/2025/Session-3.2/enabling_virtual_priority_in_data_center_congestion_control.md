---
title: "Enabling Virtual Priority in Data Center Congestion Control"
description: "EuroSys 2025 · Network/Network Congestion Control · Zhaochen Zhang (Nanjing University), Feiyang Xue (Nanjing University), Keqiang H"
tags:
  - "EuroSys2025"
  - "Network/Network Congestion Control"
---

# Enabling Virtual Priority in Data Center Congestion Control

**中文标题：** 在数据中心拥塞控制中引入虚拟优先级

**所属 Session：** [Session 3.2: Network/Network Congestion Control](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Network/Network Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Network/Network Congestion Control</p>
</div>

**作者**：Zhaochen Zhang (Nanjing University), Feiyang Xue (Nanjing University), Keqiang He (Shanghai Jiao Tong University), Zhimeng Yin (City University of Hong Kong), Gianni Antichi (Politecnico Milano & Queen Mary University of London), Jiaqi Gao (Unaffiliated), Yizhi Wang (Nanjing University), Rui Ning (Nanjing University), Haixin Nan (Nanjing University), Xu Zhang (Nanjing University), Peirui Cao (Nanjing University), Xiaoliang Wang (Nanjing University), Wanchun Dou (Nanjing University), Guihai Chen (Nanjing University), Chen Tian (Nanjing University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717463)

**获奖：** 最佳学生论文（秋季投稿）（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

In data center networks, various types of traffic with strict performance requirements operate simultaneously, necessitating effective isolation and scheduling through priority queues. However, most switches support only around ten priority queues. Virtual priority can address this limitation by emulating multi-priority queues on a single physical queue, but existing solutions often require complex switch-level scheduling and hardware changes. Our key insight is that virtual priority can be achieved by carefully managing bandwidth contention in a physical queue, which is traditionally handled by congestion control (CC) algorithms. Hence, the virtual priority mechanism needs to be tightly coupled with CC. In this paper, we propose PrioPlus, a CC enhancement algorithm that can be integrated with existing congestion control schemes to enable virtual priority transmission. PrioPlus assigns specific delay ranges to different priority levels, ensuring that flows transmit only when the delay is within the assigned range, effectively meeting virtual priority requirements. Compared to Swift CC with physical priority queues, PrioPlus provides strict priority for high-priority flows without impacting performance sensibly. Meanwhile, it benefits low-priority flows from 25% to 41% as its priority-aware design enhances CC’s ability to fully utilize available bandwidth once higher-priority traffic completes. As a result, in coflow and model training scenarios, PrioPlus improves job completion times by 21% and 33%, respectively, compared to Swift with physical priority queues.

## 中文摘要

在数据中心网络中，具有严格性能要求的各类流量同时运行，需要通过优先级队列进行有效的隔离与调度。然而，大多数交换机仅支持约十个优先级队列。虚拟优先级可通过在单个物理队列上模拟多优先级队列来缓解这一限制，但现有方案往往需要复杂的交换机级调度和硬件改动。我们的核心洞见是：虚拟优先级可以通过精细管理物理队列中的带宽竞争来实现，而这一竞争传统上由拥塞控制（CC）算法处理。因此，虚拟优先级机制需要与 CC 紧密耦合。本文提出 PrioPlus，一种可与现有拥塞控制方案集成以实现虚拟优先级传输的 CC 增强算法。PrioPlus 为不同优先级分配特定的延迟区间，确保流仅在延迟处于所分配区间内时发送，从而有效满足虚拟优先级需求。与使用物理优先级队列的 Swift CC 相比，PrioPlus 在不显著影响性能的前提下为高优先级流提供严格优先级。同时，由于其优先级感知设计增强了 CC 在更高优先级流量完成后充分利用可用带宽的能力，低优先级流可获得 25% 至 41% 的收益。因此，在 coflow 和模型训练场景中，与使用物理优先级队列的 Swift 相比，PrioPlus 分别将作业完成时间改善 21% 和 33%。

**英文关键词：** Congestion control algorithm, In-network priority, Data center network

**中文关键词：** 拥塞控制算法、网内优先级、数据中心网络

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
