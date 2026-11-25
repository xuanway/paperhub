Crystal-KV: Efficient KV Cache Management for Chain-of-Thought LLMs via Answer-First Principle
Authors：
[Zihan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=752843)，[Cheng Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9722161818012809504)，[Lei Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=852843)，[Cheng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=96570298800640399811)，[Chao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=952843)，[teng wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=652843)，[Wenqi Lou](https://63dac.conference-program.com/?post_type=page&p=15&uid=425843)，[Xuehai Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=513843)

## 中文标题

Crystal-KV：基于答案优先原则的思维链 LLM 高效 KV Cache 管理

## 英文摘要

Chain-of-Thought (CoT) reasoning in large language models (LLMs) significantly improves accuracy on complex tasks, yet incurs excessive memory overhead due to the long think-stage sequences stored in the Key-Value (KV) cache. Unlike traditional generation tasks where all tokens are uniformly important, CoT emphasizes the final answer, rendering conventional KV compression strategies ineffective. In this paper, we present Crystal-KV, an efficient KV cache management framework tailored for CoT reasoning. Our key insight is the answer-first principle. By mapping answer preferences into think-stage attention map, we distinguish between SlipKV, which mainly maintains the reasoning flow but may occasionally introduce misleading context, and CrystalKV, which truly contributes to the correctness of the final answer. We further propose an attention-based Least Recently Frequently Used algorithm that evicts expired SlipKV entries while preserving CrystalKV without disrupting reasoning flow. Finally, we introduce an adaptive cache budget allocation algorithm that dynamically allocates KV cache budgets across layers and heads according to the proportion of CrystalKV, improving utilization by prioritizing critical components. Results show that Crystal-KV achieves state-of-the-art KV cache compression, significantly improves throughput, and enables faster response time, while maintaining, or even improving, answer accuracy for CoT reasoning. The code is available at github.com/ZhW-loop/Crystal-KV.

## 中文摘要

大语言模型（LLM）中的思维链（CoT）推理显著提升了复杂任务的准确率，但由于 KV cache 中存储了较长的思考阶段序列，也带来了过高的内存开销。与所有 token 同等重要的传统生成任务不同，CoT 强调最终答案，使得常规 KV 压缩策略效果不佳。本文提出 Crystal-KV，一个面向 CoT 推理的高效 KV cache 管理框架。我们的核心洞察是答案优先原则。通过将答案偏好映射到思考阶段的注意力图，我们区分出 SlipKV 与 CrystalKV：前者主要维持推理流程，但可能偶尔引入误导性上下文；后者则真正对最终答案的正确性有所贡献。我们进一步提出基于注意力的最近最少频繁使用（Least Recently Frequently Used）算法，在驱逐过期 SlipKV 条目的同时保留 CrystalKV 而不破坏推理流程。最后，我们引入自适应缓存预算分配算法，依据 CrystalKV 所占比例在各层与各头之间动态分配 KV cache 预算，通过优先保障关键组件提升利用率。结果表明，Crystal-KV 实现了最优的 KV cache 压缩，显著提升吞吐并带来更快的响应时间，同时保持甚至提升 CoT 推理的答案准确率。代码已开源于 github.com/ZhW-loop/Crystal-KV。

## 英文关键词

KV Cache Compression, Efficient CoT Reasoning, LLM Inference

## 中文关键词

KV Cache 压缩、高效 CoT 推理、LLM 推理
