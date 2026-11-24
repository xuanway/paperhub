---
title: "SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs"
description: "ASPLOS 2026 · Session 2B · SpeContext：在 LLM 中以投机式上下文稀疏性实现高效长上下文推理"
tags:
  - "ASPLOS2026"
  - "Session 2B"
  - "Speculative Decoding"
---

# SpeContext: Enabling Efficient Long-context Reasoning with Speculative Context Sparsity in LLMs

**中文标题：** SpeContext：在 LLM 中以投机式上下文稀疏性实现高效长上下文推理

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jiaming Xu (Shanghai Jiao Tong University; SII;), Jiayi Pan (Shanghai Jiao Tong University; Infinigence-AI;), Hanzhen Wang (Shanghai Jiao Tong University), Yongkang Zhou (Shanghai Jiao Tong University; SII;), Jiancai Ye (Shanghai Jiao Tong University), Yu Wang (Tsinghua University), Guohao Dai (Shanghai Jiao Tong University; Infinigence-AI; SII;)

**单位：** Shanghai Jiao Tong University; SII;；Shanghai Jiao Tong University; Infinigence-AI;；Shanghai Jiao Tong University；Tsinghua University；Shanghai Jiao Tong University; Infinigence-AI; SII;

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790224) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

As test-time scaling in large language model(LLM) reasoning has been proven effective in enhancing the model performance through step-by-step generation, this long-context generation incurs substantial Key-Value(KV) cache, posing a critical bottleneck for practical applications deployment(e.g., Agents). While recent KV cache optimizations perform well in the long-context input scenario, the following problems remain unsolved if directly applied to long-context reasoning. (1) Time-consuming layer-wise retrieval operation. The retrieval operation, which selects the important KV pairs in each layer, brings the synchronization overhead that scales with model depth due to the data dependency, resulting in up to 60% latency overhead. (2) Complete retention of the newly generated KV cache. Existing works designed for long-context input choose to retain the KV pair of newly generated tokens to avoid repeated, time-consuming processing on the KV cache, rendering them ineffective in long-context reasoning. (3) Performance degradation with a tiny increase in sequence length. Existing offloading strategies determined before inference cannot adapt to the increasing sequence length, resulting in > 80% performance degradation with a tiny increase in sequence length. In this paper, we point out that the objective of the retrieval algorithms is to align with the LLM, which is similar to the objective of knowledge distillation in LLMs. We analyze the similarity in information focus between the distilled language model(DLM) and the original LLM from the perspective of information theory, and thus propose a novel paradigm that leverages a DLM as the retrieval algorithm. Based on the insight, we present SpeContext, an algorithm and system co-design for long-context reasoning. (1) At the algorithm level, SpeContext proposes lightweight retrieval head based on the head-level attention weights of DLM, achieving > 90% parameters reduction by pruning the redundancy. (2) At the system level, SpeContext designs an asynchronous prefetch dataflow via the elastic loading strategy, effectively overlapping KV cache retrieval with the LLM computation. (3) At the compilation level, SpeContext constructs the theoretical memory model and implements an adaptive memory management system to achieve acceleration by maximizing GPU memory utilization. We deploy and evaluate SpeContext in two resource-constrained environments, cloud and edge. Extensive experiments show that, compared with the Huggingface and FlashInfer framework, SpeContext achieves up to 24.89× and 2.19× throughput improvement in cloud and 10.06× and 8.02× speedup in edge with negligible accuracy loss, pushing the Pareto frontier of accuracy and throughput.

## 中文摘要

随着大语言模型（LLM）推理中的测试时扩展（test-time scaling）被证明能通过逐步生成提升模型性能，这种长上下文生成会带来大量键值（KV）缓存，成为实际应用部署（例如 Agent）的关键瓶颈。尽管近期的 KV 缓存优化在长上下文输入场景中表现良好，但若直接应用于长上下文推理，以下问题仍未解决。(1) 逐层检索操作耗时。每层中挑选重要 KV 对的检索操作会因数据依赖而带来随模型深度增长的同步开销，导致最高 60% 的延迟开销。(2) 新生成的 KV 缓存被完整保留。为长上下文输入设计的现有工作选择保留新生成 token 的 KV 对，以避免对 KV 缓存进行重复且耗时的处理，这使得它们在长上下文推理中失效。(3) 序列长度稍有增加即导致性能下降。在推理前确定的现有卸载策略无法适应不断增长的序列长度，导致序列长度稍有增加时性能下降超过 80%。在本文中，我们指出检索算法的目标是与 LLM 对齐，这与 LLM 中知识蒸馏的目标相似。我们从信息论的角度分析了蒸馏语言模型（DLM）与原始 LLM 在信息关注上的相似性，并据此提出了一种利用 DLM 作为检索算法的新范式。基于这一洞见，我们提出 SpeContext，一种面向长上下文推理的算法与系统协同设计。(1) 在算法层面，SpeContext 提出基于 DLM 头级注意力权重的轻量级检索头，通过剪除冗余实现超过 90% 的参数削减。(2) 在系统层面，SpeContext 通过弹性加载策略设计了异步预取数据流，有效地将 KV 缓存检索与 LLM 计算重叠。(3) 在编译层面，SpeContext 构建了理论内存模型并实现了自适应内存管理系统，通过最大化 GPU 内存利用率来实现加速。我们在云和边缘两种资源受限环境中部署并评估了 SpeContext。大量实验表明，与 Huggingface 和 FlashInfer 框架相比，SpeContext 在云端实现最高 24.89× 和 2.19× 的吞吐提升，在边缘实现 10.06× 和 8.02× 的加速，且精度损失可忽略，推动了精度与吞吐的帕累托前沿。

## 英文关键词

Large Language Models, Long-context Reasoning, Sparse Attention, KV Cache Selection, GPU

## 中文关键词

大语言模型；长上下文推理；稀疏注意力；KV 缓存选择；GPU

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790224)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2026](../index.md)
