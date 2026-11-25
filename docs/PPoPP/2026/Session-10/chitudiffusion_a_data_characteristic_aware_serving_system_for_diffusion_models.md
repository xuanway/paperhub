---
title: "ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models"
description: "PPoPP 2026 Session 10（ML Inference）：子图切分 + 多引擎协同，A100/H100 吞吐最高 2.13×/2.19×"
tags:
  - "PPoPP2026"
  - "Session-10"
  - "ML Inference"
  - "Diffusion Models"
  - "Serving System"
  - "Compilation"
authors:
  - "Chengzhang Wu"
  - "Liyan Zheng"
  - "Haojie Wang"
  - "Kezhao Huang"
  - "Zixuan Ma"
  - "Dong Dong"
  - "Jidong Zhai"
session: "Session 10: ML Inference"
session_number: 10
session_chair: "Hailong Yang"
date: "2026-02-03"
time: "16:50–17:10"
room: "Balmoral"
doi: "10.1145/3774934.3786424"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# ChituDiffusion: A Data-Characteristic-Aware Serving System for Diffusion Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 ChituDiffusion，按请求数据属性局部性把扩散流水线重组为共享优化机会的子图，编译期生成多个专用执行引擎、运行期细粒度批处理，吞吐最高提升 2.13×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 10: ML Inference</p>
</div>

**作者**：Chengzhang Wu, Liyan Zheng, Haojie Wang, Kezhao Huang, Zixuan Ma, Dong Dong, and Jidong Zhai — Tsinghua University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 16:50–17:10 · Session 10: ML Inference（主席：Hailong Yang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786424) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Diffusion models have become the dominant approach for generative tasks in images, videos, and other domains. However, diverse data properties in generation requests, which are critical for efficient serving, remain underexploited. To address this issue, we propose a diffusion model serving system ChituDiffusion. ChituDiffusion leverages the locality of data properties to recompose a diffusion pipeline into subgraphs with shared optimization opportunities, enabling thorough compile-time and runtime co-optimizations. During compilation, ChituDiffusion compiles each subgraph into multiple execution engines optimized for specific data properties. At runtime, heterogeneous requests are elaborately reorganized into fine-grained batching tasks with similar properties and then efficiently executed by matched engines. Evaluation on five diffusion applications shows that ChituDiffusion improves the throughput by up to 2.13× (1.58× on average) on A100 and 2.19× (1.51× on average) on H100 compared with existing frameworks. The code for ChituDiffusion and the production traces have been made open-source at https://github.com/thu-pacman/chitu/tree/ Diffusion.

## 中文摘要

扩散模型已成为图像、视频及其他领域生成任务的主导方法。然而，生成请求中多样化的数据属性对高效服务至关重要，却仍未得到充分利用。为解决这一问题，我们提出扩散模型服务系统 ChituDiffusion。ChituDiffusion 利用数据属性的局部性，将扩散流水线重组为具有共享优化机会的子图，从而实现编译期与运行期的充分协同优化。在编译期，ChituDiffusion 将每个子图编译为多个针对特定数据属性优化的执行引擎。在运行期，异构请求被精细地重组为属性相似的细粒度批处理任务，随后由匹配的引擎高效执行。在五个扩散应用上的评估表明，与现有框架相比，ChituDiffusion 在 A100 上将吞吐提升最高 2.13×（平均 1.58×），在 H100 上提升最高 2.19×（平均 1.51×）。ChituDiffusion 的代码与生产环境 trace 已开源，地址为 https://github.com/thu-pacman/chitu/tree/Diffusion。

## 英文关键词

Deep learining serving system, Diffusion models, Data-characteristic-aware optimization, Compiler

## 中文关键词

深度学习服务系统；扩散模型；数据特征感知优化；编译器

---

## 一句话总结

> 提出 ChituDiffusion，按请求数据属性局部性把扩散流水线重组为共享优化机会的子图，编译期生成多个专用执行引擎、运行期细粒度批处理，吞吐最高提升 2.13×。

## 研究问题

生成请求的数据属性多样，而这些属性对高效服务至关重要，现有系统并未充分挖掘利用，导致扩散模型服务效率受限。

## 方法简述

- 利用数据属性局部性，将扩散流水线重组为具有共享优化机会的子图。
- 编译期为每个子图编译多个针对特定数据属性优化的执行引擎。
- 运行期将异构请求重组为属性相近的细粒度批处理任务，交由匹配的引擎执行，实现编译期与运行期协同优化。

## 主要结果

- 在 A100 上相比现有框架吞吐最高提升 2.13×，平均 1.58×。
- 在 H100 上最高提升 2.19×，平均 1.51×，覆盖五个扩散应用。

---

> 所属 Session：[Session 10: ML Inference](index.md) · 返回 [PPoPP 2026 总览](../index.md)
