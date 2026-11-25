---
title: "Mario: Near Zero-cost Activation Checkpointing in Pipeline Parallelism"
description: "PPoPP 2025 Session 5（Deep Neural Networks）：把重计算嵌入流水气泡，平均加速 1.16×–1.57×"
tags:
  - "PPoPP2025"
  - "Session-5"
  - "Deep Neural Networks"
  - "Pipeline Parallelism"
  - "Activation Checkpointing"
  - "LLM Training"
authors:
  - "Weijian Liu"
  - "Mingzhen Li"
  - "Guangming Tan"
  - "Weile Jia"
session: "Session 5: Deep Neural Networks"
session_number: 5
session_chair: "Wei Niu"
date: "2025-03-03"
time: "17:20–17:40"
room: "Acacia D"
doi: "10.1145/3710848.3710878"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Mario: Near Zero-cost Activation Checkpointing in Pipeline Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出流水优化器 Mario，将 activation checkpointing 自动切分并融入现有流水并行方案，通过重计算与气泡重叠、均衡显存占用，实现近零成本的检查点机制。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 5: Deep Neural Networks</p>
</div>

**作者**：Weijian Liu, Mingzhen Li, Guangming Tan, Weile Jia (Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 17:20–17:40 · Session 5: Deep Neural Networks（主席：Wei Niu）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710878) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出流水优化器 Mario，将 activation checkpointing 自动切分并融入现有流水并行方案，通过重计算与气泡重叠、均衡显存占用，实现近零成本的检查点机制。

## 研究问题

现有流水并行方案会产生额外且不均衡的显存占用，GPU 利用率仍有提升空间，限制了可训练模型规模与序列长度。

## 方法简述

- 把激活重计算提前到执行流程中，使其与流水气泡有效重叠。
- 借助 checkpointing 消除显存占用后，将更多前向计算前移，为重叠提供更大灵活度。
- 设计轻量流水模拟器，并实现自动调度器，在数分钟内搜索接近最优的 checkpointing 与流水配置组合。

## 主要结果

- 在 GPT-3 与 LLaMA2 上，相比 1F1B、Chimera、Interleave 等 SOTA 流水方案（不含/含 checkpointing）平均加速 1.16×/1.57×。
- 在更均衡的显存占用下支持更大模型或更长序列。

<details>
<summary>原文摘要（英文）</summary>

Large language models have to be trained in parallel due to their large number of parameters and significant memory footprint. Among various parallelism techniques, pipeline parallelism is widely adopted in inter-node scenarios with minimal communication overhead. However, state-of-the-art pipeline schemes lead to extra and imbalanced memory footprints, leaving room for further improvement. In this paper, we propose Mario, a pipeline optimizer that automatically tessellates activation checkpointing to existing pipeline schemes, enabling training larger models (or longer sequences) with less and balanced memory footprint across GPUs and improved GPU utilization. First, the activation recomputation can be effectively overlapped in the bubbles by moving it earlier in the execution process, thereby improving overall efficiency. With eliminated memory footprint through checkpointing, Mario allows for preposing more forward computation into the pipeline bubbles, making more room for further overlapping with greater flexibility, and thus exploiting the bubbles. Then we design a lightweight pipeline simulator to model execution behavior w/o|w/ Mario. Finally, we introduce an automatic pipeline scheduler specifically for Mario, capable of searching for near optimal combination of checkpointing and pipeline configurations within minutes. Experimental results on GPT3 and LLaMA2 models show that Mario can speed up existing state-of-the-art pipeline schemes (w/o|w/ checkpointing) including 1F1B, Chimera, and Interleave by 1.16×|1.57× on average. This work paves a new direction for effective low-cost pipeline training.

</details>

---

> 所属 Session：[Session 5: Deep Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
