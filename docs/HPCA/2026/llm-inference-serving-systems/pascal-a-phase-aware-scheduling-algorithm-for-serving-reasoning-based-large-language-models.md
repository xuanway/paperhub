---
title: "PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models"
description: "HPCA 2026 · LLM Inference Serving Systems"
tags:
  - "HPCA2026"
  - "LLM Inference Serving Systems"
---

# PASCAL: A Phase-Aware Scheduling Algorithm for Serving Reasoning-based Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Inference Serving Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Inference Serving Systems</p>
</div>

**论文链接**：
**作者**：Eunyeong Cho KAIST , Jehyeon Bang KAIST , Ranggi Hwang UNIST , Minsoo Rhu KAIST
**会议**：HPCA 2026

---

## 中文标题

PASCAL：一种服务于基于推理的大语言模型的阶段感知调度算法

## 英文摘要

The emergence of reasoning-based LLMs leveraging Chain-of-Thought (CoT) inference introduces new serving challenges, as their extended reasoning phases delay user-visible output and inflate Time-To-First-Token (TTFT). Existing LLM serving frameworks fail to distinguish between reasoning and answering phases, leading to performance degradation under GPU memory constraints. We present PASCAL, a phase-aware scheduling algorithm that prioritizes reasoning to reduce TTFT while using controlled preemption and token pacing during answering to preserve Quality-of-Experience (QoE). Our hierarchical scheduler combines instance-level placement with intra-instance execution and enables dynamic migration at phase boundaries to balance load and reduce interference. Across benchmarks using DeepSeek-R1-Distill-Qwen-32B, PASCAL reduces tail TTFT by up to 72% while maintaining answering phase SLO attainment, demonstrating the importance of phase-aware scheduling for reasoning-based LLM deployment.

## 中文摘要

借助思维链（CoT）推理的基于推理的 LLM 的出现，带来了新的服务挑战：其冗长的推理阶段会推迟用户可见的输出，并抬高首个 Token 时延（TTFT）。现有 LLM 服务框架未能区分推理阶段与回答阶段，在 GPU 内存受限时导致性能下降。我们提出 PASCAL，一种阶段感知调度算法，它优先处理推理以降低 TTFT，同时在回答阶段采用受控抢占与 Token 节流以保持体验质量（QoE）。我们的分层调度器将实例级放置与实例内执行相结合，并支持在阶段边界进行动态迁移，以均衡负载并减少干扰。在使用 DeepSeek-R1-Distill-Qwen-32B 的多个基准上，PASCAL 将尾部 TTFT 最多降低 72%，同时保持回答阶段的 SLO 达成率，表明阶段感知调度对基于推理的 LLM 部署至关重要。
