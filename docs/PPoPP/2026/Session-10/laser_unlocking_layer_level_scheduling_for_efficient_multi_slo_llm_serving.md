---
title: "Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving"
description: "PPoPP 2026 Session 10（ML Inference）：层级调度突破迭代级限制，同 SLO 下吞吐提升逾 1.67×"
tags:
  - "PPoPP2026"
  - "Session-10"
  - "ML Inference"
  - "LLM Serving"
  - "Layer-Level Scheduling"
  - "SLO"
authors:
  - "Jianxiong Liao"
  - "Quanxing Dong"
  - "Yunkai Liang"
  - "Zhi Zhou"
  - "Xu Chen"
session: "Session 10: ML Inference"
session_number: 10
session_chair: "Hailong Yang"
date: "2026-02-03"
time: "16:10–16:30"
room: "Balmoral"
doi: "10.1145/3774934.3786413"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Laser: Unlocking Layer-Level Scheduling for Efficient Multi-SLO LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Laser，把迭代级调度细化为层级调度的多 SLO LLM 服务系统，将实例间请求分发与实例内层级调度结合，同等 SLO 达成率下吞吐提升逾 1.67×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 10: ML Inference</p>
</div>

**作者**：Jianxiong Liao, Quanxing Dong, Yunkai Liang, Zhi Zhou, and Xu Chen — Sun Yat-sen University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:10–16:30 · Session 10: ML Inference（主席：Hailong Yang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786413) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Engaging applications with diverse SLO requirements has become indispensable for production-scale LLM serving systems. However, existing systems rely on iteration-level scheduling, which enforces inflexible, unified execution across multi-SLO workloads, significantly constraining the serving efficiency. In this paper, we introduce layer-level scheduling, a novel mechanism that advances beyond conventional iteration-level granularity. This mechanism decomposes per-iteration computation into fine-grained layer operations, enabling the tailored execution of requests with differing requirements. However, this increased granularity introduces new challenges in both intra-instance request execution and cross-instance coordination, posing significant barriers to practical deployment. To address these challenges, we introduce Laser, a system designed for efficient multi-SLO LLM serving. The key aspect lies in the seamless integration of inter-instance request dispatching with layer-level scheduling within instances, delivering high serving throughput with SLO guarantees. Evaluations with real-world applications reveal that Laser effectively improves throughput by over 1.67× while maintaining the same SLO attainment rate compared to state-of-the-art systems.

## 中文摘要

在生产规模的 LLM 服务系统中，承载具有多样化 SLO 需求的应用已成为不可或缺的能力。然而，现有系统依赖迭代级调度（iteration-level scheduling），这会在多 SLO 工作负载上强制实施不灵活的统一执行，显著制约了服务效率。本文提出层粒度调度（layer-level scheduling），一种超越传统迭代级粒度的新机制。该机制将每次迭代的计算分解为细粒度的层操作，从而能够对需求各异的请求进行定制化执行。然而，这种更细的粒度在实例内请求执行与跨实例协调两方面都带来了新挑战，对实际部署构成显著障碍。为应对这些挑战，我们提出 Laser，一个面向高效多 SLO LLM 服务的系统。其关键在于将实例间的请求分发与实例内的层粒度调度无缝集成，在提供 SLO 保证的同时实现高服务吞吐。基于真实应用的评估表明，与当前最先进的系统相比，Laser 在保持相同 SLO 达成率的前提下，有效将吞吐提升超过 1.67×。

## 英文关键词

Layer-level Scheduling, Multi-SLO Serving, Large Language Model

## 中文关键词

层粒度调度；多 SLO 服务；大语言模型

---

## 一句话总结

> 提出 Laser，把迭代级调度细化为层级调度的多 SLO LLM 服务系统，将实例间请求分发与实例内层级调度结合，同等 SLO 达成率下吞吐提升逾 1.67×。

## 研究问题

生产级 LLM 服务需同时服务 SLO 需求各异的应用，但现有系统依赖迭代级调度，对整个迭代强制统一执行，严重限制了多 SLO 负载的服务效率。

## 方法简述

- 提出层级调度机制，将每轮迭代的计算分解为细粒度层操作，使不同需求的请求可被差异化执行。
- 针对粒度细化带来的实例内请求执行与跨实例协调两类新挑战进行系统设计。
- 设计 Laser 系统，将实例间请求分发与实例内层级调度无缝集成，在保证 SLO 的同时提升吞吐。

## 主要结果

- 在真实应用负载下，相比最先进系统吞吐提升逾 1.67×。
- 在提升吞吐的同时保持相同的 SLO 达成率。

---

> 所属 Session：[Session 10: ML Inference](index.md) · 返回 [PPoPP 2026 总览](../index.md)
