---
title: "PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM"
description: "HPCA 2025 · Viva Las Learning Models (with PIM)"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models (with PIM)"
---

# PAISE: PIM-Accelerated Inference Scheduling Engine for Transformer-based LLM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models (with PIM)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models (with PIM)</p>
</div>

**论文链接**：
**作者**：Hyojung Lee (Samsung SDS), Daehyeon Baek (Samsung SDS), Jimyoung Son (Samsung SDS), Jieun Choi (Samsung SDS), Kihyo Moon (Samsung SDS), Minsung Jang (Samsung SDS)
**会议**：HPCA 2025

---

## 中文标题

PAISE：面向基于 Transformer 的 LLM 的 PIM 加速推理调度引擎

## 英文摘要

Transformer-based Large Language Models (LLMs) demand significant computational and memory resources due to the autoregressive token generation in decoder blocks. In particular, the attention layer in LLM models has low arithmetic intensity but high memory traffic, thus requiring frequent updates to the KV matrices with each decoder iteration. As a result, LLM inference becomes memory bound, leading to increased latency. To address this, we introduce PAISE, a framework leveraging Processing-In-Memory (PIM) technology to offload memory-intensive tasks. PAISE employs GPU-PIM heterogeneous computing resources to optimize inference operations in transformer-based LLMs. The framework comprises (i) a scheduling algorithm that decides which operations to offload to PIM based on model configuration and PIM hardware specifications and (ii) an enhanced PIM kernel that performs transaction-wise interleave-batched GEMM (General Matrix Multiplication) operations, maximizing data throughput via data layout adjustments. We implemented PAISE on the GPT-2 and Llama2-7B models using an AMD MI100 GPU with HBM-PIM devices. Our evaluations show that offloading the attention layer to PIM reduces execution time by up to 48.3% compared to GPU-only inference, demonstrating PAISE’s significant potential to enhance the efficiency of LLM inference, which could lead to faster and more efficient AI applications.

## 中文摘要

基于 Transformer 的大语言模型（LLM）因解码器模块中的自回归词元生成而需要大量计算与内存资源。特别地，LLM 模型中的注意力层算术强度低但访存流量高，因此每次解码器迭代都需频繁更新 KV 矩阵。结果 LLM 推理变为访存受限，导致时延增加。为此我们提出 PAISE，一个利用存内处理（PIM）技术卸载访存密集任务的框架。PAISE 采用 GPU-PIM 异构计算资源来优化基于 Transformer 的 LLM 的推理操作。该框架由两部分组成：（i）一个调度算法，它根据模型配置与 PIM 硬件规格决定将哪些操作卸载到 PIM；（ii）一个增强的 PIM 内核，它执行按事务交错的批处理 GEMM（通用矩阵乘法）操作，通过调整数据布局最大化数据吞吐。我们在配备 HBM-PIM 器件的 AMD MI100 GPU 上于 GPT-2 与 Llama2-7B 模型上实现了 PAISE。评估表明，与仅用 GPU 的推理相比，将注意力层卸载到 PIM 可使执行时间最多减少 48.3%，展现出 PAISE 在提升 LLM 推理效率方面的巨大潜力，有望带来更快、更高效的 AI 应用。
