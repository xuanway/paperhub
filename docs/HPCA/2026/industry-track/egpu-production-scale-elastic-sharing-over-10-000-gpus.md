---
title: "eGPU: Production-Scale Elastic Sharing over 10,000 GPUs"
description: "HPCA 2026 · Industry Track"
tags:
  - "HPCA2026"
  - "Industry Track"
---

# eGPU: Production-Scale Elastic Sharing over 10,000 GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Industry Track。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Industry Track</p>
</div>

**论文链接**：
**作者**：Xiaochuan Tang Alibaba Group , Hao Qi , Jianbo Dong Alibaba Group , Yinghao Yu Alibaba Group , Zhennan Xue Alibaba Group , Zhengyu Zhang Alibaba Group , Daocheng Ying Alibaba Group , Zheng Cao Alibaba Group , Xiaoyi Lu UC Merced
**会议**：HPCA 2026

---

## 中文标题

eGPU：超过 10000 块 GPU 上的生产级弹性共享

## 英文摘要

As the cost of GPUs continues to rise, GPU-sharing solutions have become increasingly important for improving efficiency and maximizing resource utilization. At the same time, large-scale operational deployments of such solutions remain relatively less explored, especially in heterogeneous production environments where workload dynamics and orchestration complexity introduce new practical considerations. In this paper, we introduce eGPU, an elastic, efficient, and scalable GPU-sharing framework tailored for production-scale concurrent machine learning (ML) training and inference. eGPU enables fine-grained, runtime-adjustable sharing of GPUs across multiple jobs, while preserving high resource utilization and fault isolation. To address communication bottlenecks, eGPU supports native NVLink/NCCL-based communication between shared GPU instances, capabilities that are limited or unavailable in many existing designs. Built with production deployment in mind, eGPU integrates with Kubernetes (K8s) to support large-scale orchestration. It has been deployed and running stably in production clusters with over 10,000 GPUs for five years. Our evaluation results show that eGPU achieves elastic and precise control over instance sizes, improves job efficiency by 21% to 31% than SOTA sharing solutions, saves the number of GPUs required by up to 8×, and improves cluster GPU utilization by more than 3×.

## 中文摘要

随着 GPU 成本持续上升，GPU 共享方案对提升效率、最大化资源利用率日益重要。与此同时，此类方案的大规模生产部署仍相对缺乏研究，尤其是在异构生产环境中，负载动态性与编排复杂性带来了新的实际问题。本文提出 eGPU，一个面向生产级并发机器学习（ML）训练与推理的弹性、高效、可扩展 GPU 共享框架。eGPU 支持跨多个任务的细粒度、运行时可调的 GPU 共享，同时保持高资源利用率与故障隔离。为缓解通信瓶颈，eGPU 支持共享 GPU 实例之间原生的 NVLink/NCCL 通信，而许多现有设计对此能力有限或不可用。eGPU 以生产部署为设计目标，与 Kubernetes（K8s）集成以支持大规模编排；它已在超过 10000 块 GPU 的生产集群中稳定运行五年。评测结果表明，eGPU 实现了对实例大小的弹性且精确的控制，相比 SOTA 共享方案将任务效率提升 21% 至 31%，节省所需 GPU 数量多达 8 倍，并将集群 GPU 利用率提升 3 倍以上。
