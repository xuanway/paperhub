---
title: "CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving"
description: "FAST 2026 · AI and LLMs I · 第 83–100 页"
tags:
  - "FAST2026"
  - "AI and LLMs I"
---

# CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving

**中文标题**：CacheSlide：解锁跨位置感知的 KV 缓存复用，加速 LLM 服务

**Session**：AI and LLMs I · 2026-02-24 11:05–12:25 · Chair：Bingzhe Li（The University of Texas at Dallas）

**作者**：Yang Liu and Yunfei Gu, Shanghai Jiao Tong University; Liqiang Zhang, Jinan Inspur Data Technology Co., Ltd; Chentao Wu, Guangtao Xue, Jie Li, and Minyi Guo, Shanghai Jiao Tong University; Junhao Hu, Peking University; Jie Meng, Huawei Cloud

**会议**：FAST 2026 · Santa Clara, CA · 第 83–100 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/liu-yang](https://www.usenix.org/conference/fast26/presentation/liu-yang)

**论文 PDF**：[fast26-liu-yang.pdf](https://www.usenix.org/system/files/fast26-liu-yang.pdf)

---

## 英文摘要

Large Language Models (LLMs) are increasingly deployed in agent-based applications with complex prompt structures comprising both invariant and dynamic segments. Existing KV cache reuse strategies—PositionDependent Caching (PDC) and Position-Independent Caching (PIC)—inadequately address these scenarios, imposing either strict positional constraints or introducing significant computational overhead due to Positionally Misaligned KV Drift (PMKD) and window padding problems. We identify a distinct pattern in agent workflows termed Relative-Position-Dependent Caching (RPDC), where reusable segments maintain consistent relative ordering despite absolute position shifts. To address this pattern, we propose CacheSlide, a novel KV cache management system that enhances positional-encoding similarity for fixed segments, computes attention for only a minimal subset of tokens, combines new and cached KVs using learned weights, and implements layer-wise and spill-aware KV-cache optimizations. Our implementation extends vLLM’s KV cache management with Chunked Contextual Position Encoding and Weighted Correction Attention. Experimental evaluation across multiple LLMs and agent benchmarks demonstrates that CacheSlide significantly outperforms state-of-the-art baselines, achieving 3.11-4.3× reduction in latency and 3.5-5.8× improvement in throughput, establishing a new efficiency frontier for agent-based LLM applications.

## 中文摘要

大语言模型（LLM）正越来越多地部署在基于智能体的应用中，这类应用的提示结构复杂，同时包含不变段和动态段。现有的 KV 缓存复用策略——位置相关缓存（PDC）和位置无关缓存（PIC）——无法充分应对这些场景：它们要么施加严格的位置约束，要么因位置失配的 KV 漂移（PMKD）和窗口填充问题而引入显著的计算开销。我们识别出智能体工作流中一种独特的模式，称为相对位置相关缓存（RPDC）：尽管绝对位置发生偏移，可复用段仍保持一致的相对顺序。针对这一模式，我们提出 CacheSlide，一种新颖的 KV 缓存管理系统。它增强固定段的位置编码相似性，仅对极少数 token 子集计算注意力，使用学习到的权重融合新 KV 与缓存 KV，并实现逐层与溢出感知的 KV 缓存优化。我们的实现通过分块上下文位置编码（Chunked Contextual Position Encoding）和加权校正注意力（Weighted Correction Attention）扩展了 vLLM 的 KV 缓存管理。在多个 LLM 和智能体基准上的实验评估表明，CacheSlide 显著优于最先进的基线，将延迟降低 3.11–4.3 倍，将吞吐量提升 3.5–5.8 倍，为基于智能体的 LLM 应用确立了新的效率前沿。
