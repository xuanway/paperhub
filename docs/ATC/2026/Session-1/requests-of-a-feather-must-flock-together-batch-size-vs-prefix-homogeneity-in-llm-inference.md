# Requests of a Feather Must Flock Together: Batch Size vs. Prefix Homogeneity in LLM Inference

**中文标题**：同羽之请求当聚群：LLM 推理中批次大小与前缀同质性的权衡

**所属 Session**：[Session 1: LLM Inference I](index.md) · [ATC 2026](../index.md)

**作者**：Saksham Rathi (Indian Institute of Technology Bombay), Preeti (Indian Institute of Technology Bombay), Mythili Vutukuru (Indian Institute of Technology Bombay)

## 英文摘要
Auto-regressive token generation in large language models is memory-bound because it requires “attending to” key and value tensors (KV cache) of all previous tokens. Prior work aims to improve the efficiency of this decode process by batching multiple requests together, and maximizing batch size subject to GPU memory constraints. The key observation of our work is that with prefix-sharing workloads, smaller, prefix-homogeneous batches – where all requests share a common prefix – can achieve higher decode throughput than larger, heterogeneous batches, due to better spatial and temporal locality during KV cache accesses. However, current prefix-aware schedulers maximize prefix reuse within a batch only to reduce KV cache memory footprint, but do not stop batch formation at smaller homogeneous batches that could have performed better. Further, we show that shared prefix detection in existing schedulers relies on radix-tree traversals, incurring substantial CPU overhead that is often comparable to GPU execution time. This paper presents Feather, a prefix-aware scheduler that uses reinforcement learning (RL) to learn the optimal tradeoff between batch size and prefix homogeneity. We also introduce Chunked Hash Tree (CHT), a lightweight data structure that enables fast prefix detection and efficient request selection for the RL scheduler, avoiding expensive tree traversals. We integrate Feather into vLLM and SGLang, and our evaluation shows that Feather achieves 2–10× higher end-to-end throughput as compared to existing schedulers by reducing the total number of KV cache accesses, while doing no worse than the status quo when there is insufficient prefix sharing.

## 中文摘要
大语言模型中的自回归令牌生成受限于内存带宽，因为它需要对所有先前令牌的键值张量（KV 缓存）进行“关注”（attending to）操作。已有工作通过将多个请求合批，并在 GPU 显存约束下最大化批次大小，来提升这一解码过程的效率。我们工作的关键观察是：在前缀共享型负载下，更小的、前缀同质的批次（即所有请求共享同一前缀）由于在 KV 缓存访问过程中具有更好的空间与时间局部性，可以获得比更大的异构批次更高的解码吞吐。然而，当前的前缀感知调度器只是为了降低 KV 缓存内存占用而最大化批次内的前缀复用，却不会在可能表现更优的较小同质批次处停止批次构建。此外，我们表明现有调度器中的共享前缀检测依赖基数树遍历，带来可观的 CPU 开销，往往与 GPU 执行时间相当。本文提出 Feather，一个使用强化学习（RL）来学习批次大小与前缀同质性之间最优权衡的前缀感知调度器。我们还引入分块哈希树（Chunked Hash Tree，CHT），一种轻量级数据结构，它可为该 RL 调度器实现快速的前缀检测与高效的请求选择，从而避免昂贵的树遍历。我们将 Feather 集成到 vLLM 与 SGLang 中，评估表明，Feather 通过减少 KV 缓存访问总次数，相比现有调度器获得 2 倍至 10 倍更高的端到端吞吐，同时在前缀共享不足时不劣于现有水平。

## 英文关键词
LLM Inference, Prefix Sharing, Batching and Scheduling, Reinforcement Learning

## 中文关键词
LLM 推理，前缀共享，合批与调度，强化学习

[返回 Session 1](index.md) · [返回 ATC 2026](../index.md)
