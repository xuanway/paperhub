# HYPIC: Position-Independent Caching for Hybrid-Attention LLM Serving

**中文标题**：HYPIC：面向混合注意力 LLM 服务的位置无关缓存

**所属 Session**：[Session 28: LLM Inference IV](index.md) · [ATC 2026](../index.md)

**作者**：Yifei Liu (Xiaohongshu Inc.), Juntong Wu (Peking University), Yang Liu (Shanghai Jiao Tong University), Junhao Hu (Peking University), Minghao Li (Xiaohongshu Inc.), Xiaoxu Chen (Xiaohongshu Inc.), Weihang Chen (Xiaohongshu Inc.)

## 英文摘要
In retrieval-augmented generation (RAG) and agentic LLM serving, prompts are assembled from multiple independent segments into long contexts, making prefill dominate the computation cost. To reduce this cost, position-independent caching (PIC) admits KV reuse for non-contiguous segments across requests, while hybrid-attention models reduce computational complexity using linear attention. However, existing PIC methods break down on hybrid-attention models because their per-token KV-cache reuse primitives do not transfer to per-request recurrent states. In this work, we present Hypic, the first system to accelerate hybrid-attention LLM serving with position-independent caching. For linear-attention layers, we identify the segment-cumulative transition operator as the missing algebraic primitive and cache it for each segment, enabling near-exact and constant-time state composition. For the remaining full-attention layers, we construct a small seam window to propagate hidden states through the linear-attention layers, so that cross-segment attention can be repaired by recomputation. Finally, Hypic introduces segment parallelism, which parallelizes cache-miss prefill across instances, turning long cold requests into an accelerable workload. Evaluated across four hybrid-attention models and five workloads, Hypic reduces time-to-first-token (TTFT) by 3.25× on average and improves QPS by 1.66× over Prefix Cache, while preserving task quality with a 1.71-point gap from Full Recompute.

## 中文摘要
在检索增强生成（RAG）与智能体 LLM 服务中，提示由多个相互独立的片段组装成长上下文，使预填充主导计算开销。为降低这一开销，位置无关缓存（PIC）允许跨请求对非连续片段进行 KV 复用，而混合注意力模型则利用线性注意力降低计算复杂度。然而，现有 PIC 方法在混合注意力模型上失效，因为其逐 token 的 KV 缓存复用原语无法迁移到逐请求的循环状态。在本工作中，我们提出 Hypic，首个以位置无关缓存加速混合注意力 LLM 服务的系统。对于线性注意力层，我们识别出片段累积转移算子（segment-cumulative transition operator）这一缺失的代数原语，并为每个片段缓存该算子，从而实现近乎精确且常数时间的状态组合。对于其余全注意力层，我们构造一个小的接缝窗口（seam window），使隐状态经由线性注意力层传播，从而可通过重计算修复跨片段注意力。最后，Hypic 引入片段并行，将缓存缺失的预填充跨实例并行化，把长冷请求转变为可加速的工作负载。在四种混合注意力模型与五个工作负载上的评估中，Hypic 相比前缀缓存平均将首 token 时延（TTFT）降低 3.25×，将 QPS 提升 1.66×，同时以与完全重计算相差 1.71 分的差距保持任务质量。

## 英文关键词
Large language model serving, Hybrid attention, Position-independent caching

## 中文关键词
大语言模型服务，混合注意力，位置无关缓存

[返回 Session 28](index.md) · [返回 ATC 2026](../index.md)
