---
title: "Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism"
description: "ISCA 2026 · Session 6A · Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism"
tags:
  - "ISCA2026"
  - "Session 6A"
  - "LLM 4"
---

# Tetris: Efficient Long-context LLM Serving with Chunkwise Dynamic Sequence Parallelism

**中文标题：** Tetris: 基于分块动态序列并行的高效长上下文 LLM 服务

**所属 Session：** [Session 6A](index.md) · [ISCA 2026](../index.md)

**作者：** Cong Li, Yuzhe Yang, Xuegui Zheng, Qifan Yang, Yijin Guan, Size Zheng, Li-Wen Chang, Shufan Liu, Xin Liu, Guangyu Sun

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

With the advancement of large language models (LLMs), their context windows have rapidly expanded. To meet diverse demands from varying-length requests in online services, existing state-of-the-art systems adjust resource allocation by tuning the sequence parallelism (SP) allocation. However, current dynamic SP allocation lacks flexibility to (1) support stage-specific parallelism requirements in LLM inference, (2) mitigate the global latency degradation from excessive SP allocation, and (3) exploit resource fragments arising from SP size variation. To tackle this problem, we propose Chunkwise Dynamic Sequence Parallelism (CDSP), a fine-grained parallelism strategy that assigns SP sizes across intra-request token segments. Based on CDSP, we build Tetris, an LLM serving system that (1) efficiently integrates CDSP into disaggregated cluster architecture to satisfy parallelism heterogeneity, (2) dynamically regulates SP size expansion based on real-time load conditions, and (3) adaptively explores chunking plans to utilize fragmented resources while meeting per-request demands. Compared with state-of-the-art systems, Tetris achieves up to 4.35× lower time-to-first-token (TTFT) under max sustainable loads, reduces median time-between-tokens (TBT) by up to 40.1%, and increases the max request capacity by up to 45%.

## 中文摘要

随着大语言模型（LLM）的发展，其上下文窗口迅速扩大。为满足在线服务中不同长度请求的多样化需求，现有最先进系统通过调整序列并行（SP）分配来调节资源分配。然而，当前的动态 SP 分配缺乏灵活性，无法：(1) 支持 LLM 推理中各阶段不同的并行需求；(2) 缓解过度 SP 分配导致的全局延迟退化；(3) 利用 SP 规模变化产生的资源碎片。为解决这一问题，我们提出分块动态序列并行（CDSP），一种在请求内令牌分段之间分配 SP 规模的细粒度并行策略。基于 CDSP，我们构建了 Tetris，一个 LLM 服务系统，它 (1) 将 CDSP 高效集成到分离式集群架构中以满足并行异构性；(2) 根据实时负载状况动态调节 SP 规模的扩张；(3) 自适应地探索分块方案，在满足每个请求需求的同时利用碎片化资源。与最先进系统相比，Tetris 在最大可持续负载下将首令牌时间（TTFT）最多降低 4.35 倍，将令牌间时间（TBT）中位数最多降低 40.1%，并将最大请求容量提升最多 45%。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6A](index.md) · [返回 ISCA 2026](../index.md)
