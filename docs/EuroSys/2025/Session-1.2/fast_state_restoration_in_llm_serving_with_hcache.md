---
title: "Fast State Restoration in LLM Serving with HCache"
description: "EuroSys 2025 · LLM Serving · Shiwei Gao (Tsinghua University), Youmin Chen (Tsinghua University), Jiwu Shu (T"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# Fast State Restoration in LLM Serving with HCache

**中文标题：** 利用 HCache 快速恢复大语言模型服务状态

**所属 Session：** [Session 1.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Shiwei Gao (Tsinghua University), Youmin Chen (Tsinghua University), Jiwu Shu (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696072)

## 英文摘要

The growing complexity of LLM usage today, e.g., multi-round conversation and retrieval-augmented generation (RAG), makes contextual states (i.e., KV cache) reusable across user requests. Given the capacity constraints of GPU memory, only a limited number of contexts can be cached on GPU for reusing. Existing inference systems typically evict part of the KV cache and restore it by recomputing it from the original tokens or offloading it to host storage for later retrieval, both of which introduce substantial computational or I/O overheads.

We propose HCache, a novel LLM state restoration method. Its key idea is to restore LLM states from intermediate activations and thus utilize computational and I/O resources with low overhead. We enhance HCache with two techniques, including i) a bubble-free restoration scheduler that integrates resource-complementary methods to optimize the balance between computation and IO tasks; and ii) a chunk-based storage manager to address the layout mismatch issue (i.e., layer-before-token saving versus token-before-layer restoration). Our evaluations, conducted using real-world tasks, show that HCache reduces the TTFT by up to 1.93× compared to KV offload while consuming 1.92-2.40× less storage space; compared to token recomputation, HCache achieves up to 5.73× reduction in TTFT.

## 中文摘要

如今 LLM 的使用方式日益复杂，例如多轮对话和检索增强生成（RAG），使得上下文状态（即 KV cache）可以在不同用户请求之间复用。由于 GPU 显存容量的限制，只有有限数量的上下文能够缓存在 GPU 上以供复用。现有推理系统通常将部分 KV cache 驱逐，并通过从原始 token 重新计算或卸载到主机存储以便后续取回的方式进行恢复，这两者都会带来可观的计算或 I/O 开销。

我们提出 HCache，一种新颖的 LLM 状态恢复方法。其核心思想是从中间激活恢复 LLM 状态，从而以低开销利用计算和 I/O 资源。我们通过两项技术增强 HCache：i）无气泡恢复调度器，它整合资源互补的方法，优化计算任务与 I/O 任务之间的平衡；ii）基于块的存储管理器，解决布局不匹配问题（即按层优先保存与按 token 优先恢复之间的差异）。我们在真实任务上进行的评估表明，与 KV 卸载相比，HCache 将 TTFT 最多降低 1.93 倍，同时占用的存储空间减少 1.92–2.40 倍；与 token 重计算相比，HCache 的 TTFT 最多降低 5.73 倍。

**英文关键词：** LLM, machine learning system, state management

**中文关键词：** LLM、机器学习系统、状态管理

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
