---
title: "Enhancing Large-Scale AI Training Efficiency: The C4 Solution for Real-Time Anomaly Detection and Communication Optimization"
description: "HPCA 2025 · Industry Session"
tags:
  - "HPCA2025"
  - "Industry Session"
---

# Enhancing Large-Scale AI Training Efficiency: The C4 Solution for Real-Time Anomaly Detection and Communication Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Industry Session。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Industry Session</p>
</div>

**论文链接**：
**作者**：Jianbo Dong (Alibaba Group, Bin Luo (Alibaba Group), Jun Zhang (Alibaba Group), Pengcheng Zhang (Alibaba Group), Fei Feng (Alibaba Group), Yikai Zhu (Alibaba Group), Ang Liu (Alibaba Group), Zian Chen (Alibaba Group), Yi Shi (Alibaba Group), Yang Liu (Alibaba Group), Hairong Jiao (Alibaba Group), Gang Lu (Alibaba Group), Yu Guan (Alibaba Group), Ennan Zhai (Alibaba Group), Wencong Xiao (Alibaba Group), Hanyu Zhao (Alibaba Group), Man Yuan (Alibaba Group), Siran Yang (Alibaba Group), Xiang Li (Alibaba Group), Jiamang Wang (Alibaba Group), Rui Men (Alibaba Group), Jianwei Zhang (Alibaba Group), Chang Zhou (Alibaba Group), Dennis Cai (Alibaba Group), Yuan Xie (Alibaba Group), Binzhang Fu (Alibaba Group)
**会议**：HPCA 2025

---

## 中文标题

提升大规模 AI 训练效率：面向实时异常检测与通信优化的 C4 方案

## 英文摘要

The emergence of Large Language Models (LLMs) has necessitated the adoption of distributed training techniques, involving the deployment of thousands of GPUs to train a single model. Unfortunately, the efficiency of large-scale distributed training systems is often suboptimal due to the increased likelihood of hardware errors in high-end GPU products and the heightened risk of network traffic collisions. Specifically, GPUs involved in the same job require periodic synchronization to exchange necessary data, such as gradients, parameters, or activations. As a result, any local hardware failure can disrupt training tasks, and the inability to swiftly identify faulty components leads to a significant waste of GPU resources. Moreover, prolonged communication due to traffic collisions can substantially increase GPU waiting times. To address these challenges, we propose a communication-driven solution, namely the C4. The key insights of C4 are twofold. First, the load in distributed training exhibits homogeneous characteristics and is divided into iterations through periodic synchronization, therefore hardware anomalies would incur certain syndrome in collective communication. By leveraging this feature, C4 can rapidly identify the faulty components, swiftly isolate the anomaly, and restart the task, thereby avoiding resource wastage caused by delays in anomaly detection. Second, the predictable communication model of collective communication, involving a limited number of long-lived flows, allows C4 to efficiently execute traffic planning, substantially reducing bandwidth competition among these flows. The C4 has been extensively deployed across real-world production systems in a hyperscale cloud provider, yielding a significant improvement in system efficiency, from 30% to 45%. This enhancement is attributed to a 30% reduction in error-induced overhead and a 15% reduction in communication costs.

## 中文摘要

大语言模型（LLM）的出现使得分布式训练技术成为必需，需要部署数千块 GPU 来训练单个模型。遗憾的是，由于高端 GPU 产品出现硬件错误的可能性增加，以及网络流量冲突风险升高，大规模分布式训练系统的效率往往欠佳。具体而言，同一作业中的 GPU 需要周期性同步以交换梯度、参数或激活等必要数据。因此，任何局部硬件故障都可能中断训练任务，而无法快速定位故障部件会导致 GPU 资源的大量浪费。此外，流量冲突引起的长时间通信会显著增加 GPU 等待时间。为应对这些挑战，我们提出一种通信驱动的解决方案 C4。C4 的关键洞见有两点。第一，分布式训练中的负载呈现同质特征，并通过周期性同步划分为迭代，因此硬件异常会在集合通信中表现出特定征兆。利用这一特性，C4 能够快速识别故障部件、迅速隔离异常并重启任务，从而避免因异常检测延迟造成的资源浪费。第二，集合通信的通信模式可预测，涉及数量有限的长生命周期流，这使 C4 能够高效执行流量规划，大幅减少这些流之间的带宽竞争。C4 已在某超大规模云服务商的真实生产系统中广泛部署，使系统效率从 30% 显著提升至 45%。这一提升归因于错误导致的开销降低 30% 以及通信成本降低 15%。
