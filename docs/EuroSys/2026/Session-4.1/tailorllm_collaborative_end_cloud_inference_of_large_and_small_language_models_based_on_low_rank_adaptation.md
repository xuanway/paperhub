---
title: "TailorLLM: Collaborative End-Cloud Inference of Large and Small Language Models Based on Low-Rank Adaptation"
description: "EuroSys 2026 · On-Device & Federated Learning · Zian Wang (Beijing University of Posts and Telecommunications), Ziyi Wang (Beiji"
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# TailorLLM: Collaborative End-Cloud Inference of Large and Small Language Models Based on Low-Rank Adaptation

**中文标题：** TailorLLM：基于低秩适配的大语言模型与小语言模型端云协同推理

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Zian Wang (Beijing University of Posts and Telecommunications), Ziyi Wang (Beijing University of Posts and Telecommunications), Haonan Jin (Beijing University of Posts and Telecommunications), Jie Xing (Beijing University of Posts and Telecommunications), Lanshan Zhang (Beijing University of Posts and Telecommunications)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769346)

## 英文摘要

With the rapid expansion of large language model inference service users, cloud computing resource costs have become a critical challenge for service providers. Although utilizing end-device resources for auxiliary inference provides new possibilities to reduce cloud computing costs, existing solutions struggle to achieve an ideal balance across multi-task accuracy, end-to-end latency, and cloud computing costs.

We present TailorLLM, a task-level collaborative end-cloud inference solution based on low-rank fine-tuning for large language models. This framework comprises two core algorithms that support offline and online optimization, respectively: (i) To reduce transmission overhead while maintaining model performance, Resource-Friendly Low-Rank Adaptation (RFLoRA) decouples pre-trained parameters into cold and hot modules, reducing trainable parameters. (ii) To ensure coverage of users’ common tasks, we introduce AdapterMgr, an imitation learning-based replacement strategy that enables near-optimal dynamic management of the on-device LoRA matrix library. Finally, we implemented the TailorLLM prototype system on NVIDIA 3090 and Tesla T4 servers and thoroughly evaluated it on public task datasets. Compared to a series of baselines, TailorLLM reduces cloud resource consumption by up to 69.8% and inference latency by up to 62% while maintaining high accuracy.

## 中文摘要

随着大语言模型推理服务用户的快速增长，云计算资源成本已成为服务提供商面临的关键挑战。尽管利用端设备资源进行辅助推理为降低云计算成本提供了新的可能，但现有方案难以在多任务精度、端到端时延和云计算成本之间取得理想平衡。

我们提出 TailorLLM，一种基于大语言模型低秩微调的任务级端云协同推理方案。该框架包含两个分别支持离线优化与在线优化的核心算法：(i) 为在保持模型性能的同时降低传输开销，资源友好型低秩适配（RFLoRA）将预训练参数解耦为冷模块与热模块，从而减少可训练参数；(ii) 为确保覆盖用户的常见任务，我们引入 AdapterMgr，一种基于模仿学习的替换策略，可对端侧 LoRA 矩阵库实现接近最优的动态管理。最后，我们在 NVIDIA 3090 和 Tesla T4 服务器上实现了 TailorLLM 原型系统，并在公开任务数据集上进行了充分评估。与一系列基线相比，TailorLLM 在保持高精度的同时，将云资源消耗最多降低 69.8%，推理时延最多降低 62%。

**英文关键词：** Large Language Models, Edge Computing, Collaborative Inference, Low Rank Adaptation, Scheduling

**中文关键词：** 大语言模型、边缘计算、协同推理、低秩适配、调度

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
