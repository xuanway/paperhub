---
title: "MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models"
description: "PPoPP 2026 Session 10（ML Inference）：patch 级并行批处理混合分辨率请求，SLO 满足率 +30.1%"
tags:
  - "PPoPP2026"
  - "Session-10"
  - "ML Inference"
  - "Diffusion Models"
  - "Patch-Level Parallelism"
  - "Serving System"
authors:
  - "Desen Sun"
  - "Zepeng Zhao"
  - "Yuke Wang"
session: "Session 10: ML Inference"
session_number: 10
session_chair: "Hailong Yang"
date: "2026-02-03"
time: "16:30–16:50"
room: "Balmoral"
doi: "10.1145/3774934.3786420"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# MixFusion: A Patch-Level Parallel Serving System for Mixed-Resolution Diffusion Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 MixFusion，混合分辨率扩散模型的服务系统，用 patch 级并行批处理异构请求，配合 patch 定制缓存与 SLO 感知调度，SLO 满足率提升 30.1%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 10: ML Inference</p>
</div>

**作者**：Desen Sun, Zepeng Zhao, and Yuke Wang — University of Waterloo, Canada; Carnegie Mellon University, USA; Rice University, USA

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:30–16:50 · Session 10: ML Inference（主席：Hailong Yang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786420) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Text-to-Image (T2I) diffusion models have recently attracted significant attention due to their ability to synthesize high-fidelity photorealistic images. However, serving diffusion models would suffer from hardware underutilization in real-world settings due to highly variable request resolutions. To this end, we present MixFusion, a parallel serving System that exploits fine-grained patch-level parallelism to enable efficient batching of mixed-resolution requests. Specifically, MixFusion introduces a novel patch-based processing workflow, significantly enabling concurrent processing across heterogeneous requests. Furthermore, MixFusion incorporates a patch-tailored cache management policy to exploit the patch-level locality benefits. In addition, MixFusion features an SLO-aware scheduling strategy with lightweight online latency prediction. Extensive evaluation demonstrates that MixFusion achieves 30.1% higher SLO satisfaction compared to the state-of-the-art solutions on average. Our code is available at https://github.com/desenSunUBW/mixfusion.

## 中文摘要

文本到图像（Text-to-Image，T2I）扩散模型近期因其合成高保真、照片级真实图像的能力而受到广泛关注。然而在真实场景中，由于请求分辨率差异极大，扩散模型的服务会出现硬件利用率不足的问题。为此，我们提出 MixFusion，一个并行服务系统，它利用细粒度的图块级（patch-level）并行，实现混合分辨率请求的高效批处理。具体而言，MixFusion 引入了一种新颖的基于图块的处理流程，显著支持对异构请求的并发处理。此外，MixFusion 结合了面向图块定制的缓存管理策略，以利用图块级局部性带来的收益。同时，MixFusion 具备 SLO 感知的调度策略，并配有轻量级在线延迟预测。大量评估表明，与最先进的方案相比，MixFusion 平均将 SLO 满足率提升 30.1%。我们的代码见 https://github.com/desenSunUBW/mixfusion。

## 英文关键词

Patch Management, Diffusion Model Serving, Mixed-Resolution Batching

## 中文关键词

图块管理；扩散模型服务；混合分辨率批处理

---

## 一句话总结

> 提出 MixFusion，混合分辨率扩散模型的服务系统，用 patch 级并行批处理异构请求，配合 patch 定制缓存与 SLO 感知调度，SLO 满足率提升 30.1%。

## 研究问题

真实场景中 T2I 扩散模型的请求分辨率高度可变，导致批处理困难与硬件利用率不足，现有服务方案难以高效应对混合分辨率请求。

## 方法简述

- 提出基于 patch 的处理流程，使异构请求能够并发处理并高效批处理。
- 设计 patch 定制的缓存管理策略，充分利用 patch 级局部性收益。
- 采用 SLO 感知的调度策略，并结合轻量级在线延迟预测进行请求编排。

## 主要结果

- 相比最先进方案，平均 SLO 满足率提升 30.1%。
- 在混合分辨率请求负载下实现了异构请求的并发处理与高效批处理。

---

> 所属 Session：[Session 10: ML Inference](index.md) · 返回 [PPoPP 2026 总览](../index.md)
