---
title: "Handling Network Faults in Distributed AI Training: Failover is Now an Option"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Xin Zhe Khooi (National University of Singapore), Zhuo Jiang (ByteDance), Pan Xi"
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# Handling Network Faults in Distributed AI Training: Failover is Now an Option

**中文标题：** 应对分布式 AI 训练中的网络故障：故障切换已是一种可行选择

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Xin Zhe Khooi (National University of Singapore), Zhuo Jiang (ByteDance), Pan Xie (ByteDance), Zhigang Cui (ByteDance), Meng Wang (ByteDance), Yuze Jin (National University of Singapore), Pengfei Huo (ByteDance), Dongyang Wang (ByteDance), Lulu Chen (ByteDance), Lei Wang (ByteDance), Liaoyuan Feng (ByteDance), Xiaodong Liu (ByteDance), Peng Li (ByteDance), Qinlong Wang (ByteDance), Yang Bai (ByteDance), Yongcan Wang (ByteDance), Hao Jin (ByteDance), Jinshuai Sun (ByteDance), Shan Lu (ByteDance), Xiang Shi (ByteDance), Yingkai Zhao (ByteDance), Haiquan Chen (ByteDance), Yi Li (ByteDance), Jianxi Ye (ByteDance), Mun Choon Chan (National University of Singapore)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769322)

## 英文摘要

Distributed AI training often suffers from network faults. Network faults, especially at the last hop between a switch and a host, result in loss of connectivity, resulting in training job stalls and eventual failure. This is typically managed through a fail-stop mechanism, followed by a restart, incurring significant inefficiencies. We present ReCCL, the first network fault-tolerant collective communication library (CCL) that allows training progress to be preserved by seamlessly failing over to alternate paths when a network fault occurs. During failover, ReCCL keeps communication states synchronized while using dynamic channel load balancing and intra-host GPU routing to improve communication performance. Our evaluations demonstrate that ReCCL can perform failover seamlessly with minimal performance losses. Additionally, our simulations also demonstrate that failover can be effectively used to achieve significant savings in GPU hours for large-scale distributed AI training workloads.

## 中文摘要

分布式 AI 训练常常遭受网络故障的影响。网络故障，尤其是交换机与主机之间最后一跳的故障，会导致连接丢失，进而使训练作业停滞并最终失败。通常的做法是通过故障停止（fail-stop）机制继而重启来处理，这会造成显著的效率损失。我们提出 ReCCL，首个网络容错的集合通信库（CCL），它能够在发生网络故障时无缝切换到备用路径，从而保持训练进度。在故障切换期间，ReCCL 保持通信状态同步，同时利用动态通道负载均衡与主机内 GPU 路由来提升通信性能。我们的评估表明，ReCCL 能够以极小的性能损失完成无缝故障切换。此外，我们的模拟还表明，故障切换可被有效地用于为大规模分布式 AI 训练工作负载节省大量 GPU 机时。

**英文关键词：** distributed AI training, collective communication libraries, NCCL, failover, restart, RDMA

**中文关键词：** 分布式 AI 训练、集合通信库、NCCL、故障切换、重启、RDMA

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
