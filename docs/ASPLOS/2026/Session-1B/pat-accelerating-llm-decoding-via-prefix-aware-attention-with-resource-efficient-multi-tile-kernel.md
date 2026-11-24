---
title: "PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel"
description: "ASPLOS 2026 · Session 1B · PAT：通过前缀感知注意力与资源高效的多 Tile 内核加速 LLM 解码"
tags:
  - "ASPLOS2026"
  - "Session 1B"
  - "LLM Serving: Latency & Scheduling"
---

# PAT: Accelerating LLM Decoding via Prefix-Aware Attention with Resource Efficient Multi-Tile Kernel

**中文标题：** PAT：通过前缀感知注意力与资源高效的多 Tile 内核加速 LLM 解码

**所属 Session：** [Session 1B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jinjun Yi (Tianjin University), Zhixin Zhao (Tianjin University), Yitao Hu (Tianjin University), Ke Yan (Tianjin University), Weiwei Sun (Tianjin University), Hao Wang (Stevens Institue of Technology), Laiping Zhao (Tianjin University), Yuhao Zhang (Tianjin University), Wenxin Li (Tianjin University), Keqiu Li (Tianjin University)

**单位：** Tianjin University；Stevens Institue of Technology

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790200) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

LLM serving is increasingly dominated by decode attention, which is a memory-bound operation due to massive KV cache loading from global memory. Meanwhile, real-world workloads exhibit substantial, hierarchical shared prefixes across requests (e.g., system prompts, tools/templates, RAG). Existing attention implementations fail to fully exploit prefix sharing: one-query-per-CTA execution repeatedly loads shared prefix KV cache, while one-size-fits-all tiling leaves on-chip resources idle and exacerbates bubbles for uneven KV lengths. These choices amplify memory bandwidth pressure and stall memory-bound decode attention. This paper introduces PAT, a prefix-aware attention kernel implementation for LLM decoding that organizes execution with a pack-forward-merge paradigm. PAT packs queries by shared prefix to reduce repeated memory accesses, runs a customized multi-tile kernel to achieve high resource efficiency. It further applies practical multi-stream forwarding and KV splitting to reduce resource bubbles. The final merge performs online softmax with negligible overhead. We implement PAT as an off-the-shelf plugin for vLLM. Evaluation on both real-world and synthetic workloads shows that PAT reduces attention latency by 53.5% on average and TPOT by 17.0-93.1% under the same configurations against state-of-the-art attention kernels. PAT's source code is publicly

## 中文摘要

LLM 服务正日益由解码注意力主导，由于需要从全局内存大量加载 KV 缓存，它是一项内存受限的操作。与此同时，真实工作负载在请求之间呈现出大量分层的共享前缀（例如系统提示、工具/模板、RAG）。现有注意力实现未能充分利用前缀共享：每 CTA 单查询的执行方式反复加载共享前缀 KV 缓存，而一刀切的分块方式使片上资源闲置，并加剧了 KV 长度不均带来的气泡。这些选择放大了内存带宽压力，并拖慢内存受限的解码注意力。本文提出 PAT，一种面向 LLM 解码的前缀感知注意力内核实现，它以打包-前送-合并（pack-forward-merge）范式组织执行。PAT 按共享前缀打包查询以减少重复内存访问，并运行定制的多 Tile 内核以实现高资源效率。它进一步采用实用的多流前送与 KV 切分来减少资源气泡。最后的合并以可忽略的开销执行在线 softmax。我们将 PAT 实现为 vLLM 的即插即用插件。在真实与合成工作负载上的评估表明，在相同配置下，与最先进的注意力内核相比，PAT 平均降低注意力延迟 53.5%，并将 TPOT 降低 17.0-93.1%。PAT 的源代码已公开

## 英文关键词

Large Language Models; LLM Inference; Prefix Aware Attention; GPU Kernel Scheduling

## 中文关键词

大语言模型；LLM 推理；前缀感知注意力；GPU 内核调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790200)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1B](index.md) · [返回 ASPLOS 2026](../index.md)
