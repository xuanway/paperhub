# KVLite: Efficient LLM Agent Scheduling via Head-Aware KV Sharing

**中文标题**：KVLite：基于头感知 KV 共享的高效 LLM 智能体调度

**所属 Session**：[Session 1: LLM Inference I](index.md) · [ATC 2026](../index.md)

**作者**：Jiaqi Si (National University of Defense Technology), Dezun Dong (National University of Defense Technology)

## 英文摘要
Large language models (LLMs) are increasingly being applied in agentic applications through complex prompting structures, including fixed system prompts and the reuse of historical messages. However, existing service systems suffer from severe inefficiency due to redundant computation caused by shared text segments. Existing KV reuse strategies often fall short due to either stringent application conditions or accuracy degradation resulting from the neglect of the dynamic nature of attention distributions. We propose KVLite, a service framework based on KV sharing for agentic applications. At the algorithm level, KVLite identifies the critical heads in each layer, recomputes the KV cache for these heads to achieve a balance between high accuracy and low recomputation overhead. At the system level, KVLite identifies and shortens the critical path in agentic workflows based on KV sharing. Experimental evaluations across multiple LLM and agent benchmarks show that KVLite can significantly outperform state-of-the-art baselines, achieving a 2.1×–3.9× speedup in prefill latency and 2.3× to 4.6× improvement in throughput, with negligible accuracy loss compared to the recomputation baseline.

## 中文摘要
大语言模型（LLM）正通过复杂的提示结构被越来越广泛地应用于智能体应用中，这些结构包括固定的系统提示以及对历史消息的复用。然而，由于共享文本片段所带来的冗余计算，现有服务系统存在严重的低效问题。已有的 KV 复用策略往往效果不佳，其原因要么是应用条件过于苛刻，要么是忽视了注意力分布的动态特性而导致精度下降。我们提出 KVLite，一个面向智能体应用的、基于 KV 共享的服务框架。在算法层面，KVLite 识别每一层中的关键注意力头，并为这些头重新计算 KV 缓存，从而在高精度与低重计算开销之间取得平衡。在系统层面，KVLite 基于 KV 共享识别并缩短智能体工作流中的关键路径。在多个 LLM 与智能体基准上的实验评估表明，KVLite 可显著优于最先进的基线，预填充延迟加速 2.1 倍至 3.9 倍，吞吐提升 2.3 倍至 4.6 倍，且相比重计算基线的精度损失可忽略不计。

## 英文关键词
LLM Agents, KV Cache Sharing, Request Scheduling

## 中文关键词
LLM 智能体，KV 缓存共享，请求调度

[返回 Session 1](index.md) · [返回 ATC 2026](../index.md)
