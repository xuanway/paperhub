---
title: "Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices"
description: "EuroSys 2026 · On-Device & Federated Learning · Fahao Chen (Shandong University, China, Xi'an Jiaotong University, China), Jie W"
tags:
  - "EuroSys2026"
  - "On-Device & Federated Learning"
---

# Federated Fine-Tuning of Sparsely-Activated Large Language Models on Resource-Constrained Devices

**中文标题：** 资源受限设备上稀疏激活大语言模型的联邦微调

**所属 Session：** [Session 4.1: On-Device & Federated Learning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：On-Device & Federated Learning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · On-Device & Federated Learning</p>
</div>

**作者**：Fahao Chen (Shandong University, China, Xi'an Jiaotong University, China), Jie Wan (Xi'an Jiaotong University, China), Peng Li (Xi'an Jiaotong University, China), Zhou Su (Xi'an Jiaotong University, China), Dongxiao Yu (Shandong University, China)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769329)

## 英文摘要

Federated fine-tuning of Mixture-of-Experts (MoE)-based large language models (LLMs) is challenging due to their massive computational requirements and the resource constraints of participants. Existing works attempt to fill this gap through model quantization, computation offloading, or expert pruning. However, they cannot achieve desired performance due to impractical system assumptions and a lack of consideration for MoE-specific characteristics. In this paper, we propose Flux, a system designed to enable federated fine-tuning of MoE-based LLMs across participants with constrained computing resources (e.g., consumer-grade GPUs), aiming to minimize time-to-accuracy. Flux introduces three key innovations: (1) quantization-based local profiling to estimate expert activation with minimal overhead, (2) adaptive layer-aware expert merging to reduce resource consumption while preserving accuracy, and (3) dynamic expert role assignment using an exploration-exploitation strategy to balance tuning and non-tuning experts. Extensive experiments on LLaMA-MoE and DeepSeek-MoE with multiple benchmark datasets demonstrate that Flux significantly outperforms existing methods, achieving up to 4.75× speedup in time-to-accuracy.

## 中文摘要

对基于专家混合（MoE）的大语言模型（LLM）进行联邦微调颇具挑战，因为其计算需求巨大，而参与者资源受限。已有工作尝试通过模型量化、计算卸载或专家剪枝来弥补这一差距。然而，由于系统假设不切实际且未考虑 MoE 特有的特性，它们无法达到理想性能。本文提出 Flux，一个旨在使 MoE 基座 LLM 能够在计算资源受限（如消费级 GPU）的参与者之间进行联邦微调的系统，目标是尽可能缩短达到目标精度所需的时间。Flux 引入三项关键创新：(1) 基于量化的本地剖析，以极低开销估计专家激活情况；(2) 自适应的层感知专家合并，在保持精度的同时降低资源消耗；(3) 采用探索-利用策略的动态专家角色分配，以平衡参与调优与不参与调优的专家。在 LLaMA-MoE 与 DeepSeek-MoE 上使用多个基准数据集的广泛实验表明，Flux 显著优于现有方法，达到目标精度所需时间最高加速 4.75 倍。

**英文关键词：** Federated Learning, Large Language Models, Mixture-of-Experts

**中文关键词：** 联邦学习、大语言模型、专家混合

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
