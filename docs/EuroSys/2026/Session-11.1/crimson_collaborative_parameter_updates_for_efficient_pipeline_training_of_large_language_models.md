---
title: "Crimson: Collaborative Parameter Updates for Efficient Pipeline Training of Large Language Models"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Yapeng Jiang (Sun Yat-sen University), Wuhui Chen (Sun Yat-sen University), Ganh"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# Crimson: Collaborative Parameter Updates for Efficient Pipeline Training of Large Language Models

**中文标题：** Crimson：面向大语言模型高效流水线训练的协同参数更新

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Yapeng Jiang (Sun Yat-sen University), Wuhui Chen (Sun Yat-sen University), Ganhong Huang (Sun Yat-sen University), Yuzhou Huang (Sun Yat-sen University), Zicong Hong (Hong Kong University of Science and Technology), Song Guo (Hong Kong University of Science and Technology), Yue Yu (Pengcheng Laboratory)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803606)

## 英文摘要

Large language models (LLMs) have driven significant progress in natural language processing, yet their training and finetuning remain limited by memory constraints, particularly the substantial memory footprints of optimizer states. Existing solutions address this challenge by offloading optimizer states and update tasks to the CPU, but this often leads to increased GPU idleness due to the CPU’s limited computational capabilities, especially in pipeline parallelism.

To address this, we present Crimson, an efficient system that optimizes parameter updates in pipeline parallelism. Crimson employs a collaborative parameter updates scheme that distributes each stage’s updates across its local GPU and CPU as well as the GPUs of subsequent stages. In addition, we design a multi-stage collaborative optimizer to coordinate computations and communications, together with a trapezoid bubble aware scheduling that formulates the process as an optimization problem to determine the optimal parameter update strategy. This approach maximizes GPU computational and memory efficiency. Experimental results across diverse model scales, parallelism configurations and state-of-the-art pipeline schedulings demonstrate that Crimson achieves throughput improvements exceeding 1.35× with ZeRO-Offload and ZeRO-Offload++, and up to 1.33× with Recomputation, along with increased GPU utilization.

## 中文摘要

大语言模型（LLM）推动了自然语言处理的显著进步，然而其训练与微调仍受限于内存约束，尤其是优化器状态所占的庞大内存。现有解决方案通过将优化器状态和更新任务卸载到CPU来应对这一挑战，但这往往因CPU有限的计算能力而导致GPU空闲增加，在流水线并行中尤为明显。

为解决这一问题，我们提出Crimson，一个优化流水线并行中参数更新的高效系统。Crimson采用协同参数更新方案，将每个阶段的更新分摊到其本地GPU与CPU以及后续阶段的GPU上。此外，我们设计了多阶段协同优化器来协调计算与通信，并结合梯形气泡感知调度，将该过程建模为优化问题，以确定最优的参数更新策略。该方法最大化了GPU的计算与内存效率。在多种模型规模、并行配置和最先进流水线调度下的实验结果表明，Crimson配合ZeRO-Offload和ZeRO-Offload++实现超过1.35倍的吞吐量提升，配合重计算（Recomputation）最高提升1.33倍，同时提高了GPU利用率。

**英文关键词：** Distributed Training, Pipeline Parallelism

**中文关键词：** 分布式训练、流水线并行

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
