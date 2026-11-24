---
title: "Multiplexing Dynamic Deep Learning Workloads with SLO-awareness in GPU Clusters"
description: "EuroSys 2025 · GPU Systems · Wenyan Chen (University of Macau; Shenzhen Institute of Advanced Technology, Chi"
tags:
  - "EuroSys2025"
  - "GPU Systems"
---

# Multiplexing Dynamic Deep Learning Workloads with SLO-awareness in GPU Clusters

**中文标题：** 在 GPU 集群中以 SLO 感知方式复用动态深度学习工作负载

**所属 Session：** [Session 4.2: GPU Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：GPU Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · GPU Systems</p>
</div>

**作者**：Wenyan Chen (University of Macau; Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences), Chengzhi Lu (Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences; University of Macau), Huanle Xu (University of Macau, Macau SAR, China), Kejiang Ye (Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences), ChengZhong Xu (University of Macau)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696074)

## 英文摘要

Deep learning (DL) inference services are widely recognized as crucial workloads in large-scale cloud clusters. However, due to the stringent latency requirements, cloud providers often over-provision GPU resources, resulting in underutilization of the available GPU potential. Although co-locating tasks on the same device can enhance utilization, ensuring Service Level Objectives (SLOs) guarantees for multiplexing highly dynamic inference services becomes extremely challenging due to significant resource interference.

In this paper, we introduce Mudi, a new SLO-aware system designed to optimize the utilization of GPU resources within large-scale clusters. Mudi achieves this by efficiently multiplexing DL inference services with training tasks through spatial sharing. The fundamental concept behind Mudi involves profiling the latency of inference services using a piece-wise linear function that accurately captures resource interference. Leveraging this quantification of interference, Mudi designs a scalable cluster-wide co-location policy, determining the optimal multiplexing of training tasks and inference services to maximize resource efficiency. Furthermore, Mudi incorporates adaptive batching and resource scaling mechanisms to rapidly adapt to the dynamic workloads. Experimental results demonstrate that Mudi improves 42% of GPU resource utilization and achieves up to 2.27× higher training efficiency while satisfying inference SLOs, as compared to state-of-the-art multiplexing methods.

## 中文摘要

深度学习（DL）推理服务被广泛认为是大型云集群中的关键工作负载。然而，由于严格的延迟要求，云提供商常常过度配置 GPU 资源，导致可用 GPU 潜力利用不足。虽然在同一设备上共置任务可以提升利用率，但由于显著的资源干扰，为高度动态的推理服务复用确保服务等级目标（SLO）保证变得极具挑战性。

本文提出 Mudi，一种新的 SLO 感知系统，旨在优化大型集群内 GPU 资源的利用率。Mudi 通过空间共享将 DL 推理服务与训练任务高效复用，从而实现这一目标。Mudi 的基本思想是用分段线性函数刻画推理服务的延迟，以准确捕捉资源干扰。利用这种干扰量化，Mudi 设计了可扩展的集群级共置策略，确定训练任务与推理服务的最优复用方式，以最大化资源效率。此外，Mudi 还集成了自适应批处理和资源伸缩机制，以快速适应动态工作负载。实验结果表明，与最先进的复用方法相比，Mudi 在满足推理 SLO 的同时将 GPU 资源利用率提升 42%，并实现最高 2.27 倍的训练效率。

**英文关键词：** SLO-awareness, Dynamic workloads, Deep learning

**中文关键词：** SLO 感知、动态工作负载、深度学习

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
