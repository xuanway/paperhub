---
title: "FlowCheck: Decoupling Checkpointing and Training of Large-Scale Models"
description: "EuroSys 2025 · LLM Training · Zimeng Huang (Shanghai Jiao Tong University & Alibaba Cloud), Hao Nie (Alibaba C"
tags:
  - "EuroSys2025"
  - "LLM Training"
---

# FlowCheck: Decoupling Checkpointing and Training of Large-Scale Models

**中文标题：** 解耦大规模模型的检查点与训练

**所属 Session：** [Session 9.2: LLM Training](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Training。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Training</p>
</div>

**作者**：Zimeng Huang (Shanghai Jiao Tong University & Alibaba Cloud), Hao Nie (Alibaba Cloud & Peking University), Haonan Jia (Alibaba Cloud), Bo Jiang (Shanghai Jiao Tong University), Junchen Guo (Alibaba Cloud), Jianyuan Lu (Alibaba Cloud), Rong Wen (Alibaba Cloud), Biao Lyu (Zhejiang University & Alibaba Cloud), Shunmin Zhu (Hangzhou Feitian Cloud & Alibaba Cloud), Xinbing Wang (Shanghai Jiao Tong University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696088)

## 英文摘要

Checkpointing is becoming a hotspot of interest in both academia and industry as the primary fault-tolerance method for large model training. However, existing checkpoint designs are tightly coupled with the training process, leading to interruptions that reduce overall training efficiency. To reduce the impact of checkpoints on training, this paper presents FlowCheck, a novel checkpointing system that decouples checkpoint operations from the training process, enabling checkpoint saving without blocking the training. Specifically, FlowCheck updates the checkpoints by extracting complete gradient information from the network traffic of normal training. FlowCheck deploys a traffic-mirroring network to support this design. To utilize mirrored traffic for checkpointing operations, two key challenges need to be addressed. First, we need to achieve precise identification and extraction of gradient packets from training traffic. Second, the transmission on the mirror link is unreliable due to its inability to trigger retransmission upon packet loss. Through two key designs: (1) packet-counting-based traffic identification, and (2) packet redundancy recovery mechanism, FlowCheck implements an efficient checkpointing system using the existing training network and solves the above two challenges. Experiments and estimations verify that FlowCheck achieves checkpoint operations with zero impact on training, and demonstrate that FlowCheck achieves over 98% effective training time under practical fault conditions.

## 中文摘要

随着检查点成为大模型训练的主要容错方法，它正成为学术界和工业界关注的热点。然而，现有检查点设计与训练过程紧密耦合，导致中断并降低整体训练效率。为减少检查点对训练的影响，本文提出 FlowCheck，一种新颖的检查点系统，它将检查点操作与训练过程解耦，使检查点保存无需阻塞训练。具体而言，FlowCheck 通过从正常训练的网络流量中提取完整梯度信息来更新检查点。FlowCheck 部署一个流量镜像网络以支持该设计。为利用镜像流量执行检查点操作，需要解决两个关键挑战。第一，我们需要从训练流量中精确识别并提取梯度数据包。第二，由于镜像链路在丢包时无法触发重传，其传输是不可靠的。通过两项关键设计：(1) 基于数据包计数的流量识别；(2) 数据包冗余恢复机制，FlowCheck 利用现有训练网络实现了高效的检查点系统，并解决了上述两个挑战。实验和估算验证了 FlowCheck 实现了对训练零影响的检查点操作，并表明 FlowCheck 在实际故障条件下可达到超过 98% 的有效训练时间。

**英文关键词：** Distributed Training, Fault Tolerance, In-network Checkpoint

**中文关键词：** 分布式训练、容错、网内检查点

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
