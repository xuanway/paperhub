# Make Graphs Great Again: Rethinking LLM Agent Architecture via Structure-Semantic Separation

**中文标题**：让图重新伟大：通过结构—语义分离重思 LLM 智能体架构

**所属 Session**：[Session 16: AI Agents](index.md) · [ATC 2026](../index.md)

**作者**：Jingyi Jia (Huazhong University of Science and Technology), Jiale Wang (Huazhong University of Science and Technology), Haoyi Zhang (Huazhong University of Science and Technology), Qinbin Li (Huazhong University of Science and Technology), Xiaofei Liao (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

## 英文摘要
LLM-centric agent architectures route each observation back to the model for the next decision, leaving control logic implicit in a growing prompt and forcing repeated reconstruction of task state and routine execution progress even when runtime evidence determines the next transition. We present structure–semantic separation as a control boundary for LLM agents, making recurring tool-use structure explicit and executable while reserving the model for semantic decisions that structure cannot resolve. MotifAgent realizes this boundary through executable motif graphs: the Structure Engine advances graph execution based on runtime evidence, while the Semantic Engine resolves semantic gaps through scoped LLM calls, making recurring tool-use structure executable runtime state rather than prompt guidance. Exposing motif progress to the serving backend additionally enables structure-aware scheduling and fine-grained KV-cache retention. Across APIBank, TauBench, and AppWorld, MotifAgent reduces LLM calls and token consumption while maintaining comparable task performance. Serving replay experiments further show reduced prefill-stage latency and improved admission-time KV reuse under the evaluated queueing and cache-pressure conditions.

## 中文摘要
以 LLM 为中心的智能体架构将每次观测都送回模型以做出下一个决策，使控制逻辑隐含在不断增长的提示之中，并且即便运行时证据已经确定了下一个转移，也不得不反复重建任务状态和常规执行进度。我们提出结构—语义分离作为 LLM 智能体的控制边界，让重复出现的工具使用结构显式化并且可执行，同时把模型保留给结构无法解决的语义决策。MotifAgent 通过可执行的 motif 图实现这一边界：结构引擎依据运行时证据推进图执行，语义引擎则通过有范围的 LLM 调用解决语义缺口，从而使重复出现的工具使用结构成为可执行的运行时状态，而非提示中的引导。将 motif 进度暴露给服务后端还可实现结构感知的调度和细粒度的 KV 缓存保留。在 APIBank、TauBench 和 AppWorld 上，MotifAgent 在保持任务性能相当的同时减少了 LLM 调用次数与 token 消耗。服务回放实验进一步表明，在所评估的排队与缓存压力条件下，预填充阶段延迟降低，准入时的 KV 复用得到改善。

## 英文关键词
LLM agents, agent runtime, LLM serving, KV cache

## 中文关键词
LLM 智能体，智能体运行时，LLM 服务，KV 缓存

[返回 Session 16](index.md) · [返回 ATC 2026](../index.md)
