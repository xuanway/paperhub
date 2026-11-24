---
title: "TetriServe: Efficiently Serving Mixed DiT Workloads"
description: "ASPLOS 2026 · Session 5A · TetriServe：高效服务混合 DiT 工作负载"
tags:
  - "ASPLOS2026"
  - "Session 5A"
  - "Generative Model Serving"
---

# TetriServe: Efficiently Serving Mixed DiT Workloads

**中文标题：** TetriServe：高效服务混合 DiT 工作负载

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Runyu Lu (University of Michigan), Shiqi He (University of Michigan), Wenxuan Tan (UW-Madison), Shenggui Li (Nanyang Technological University), Ruofan Wu (University of Michigan), Jeff J. Ma (University of Michigan), Ang Chen (University of Michigan), Mosharaf Chowdhury (University of Michigan)

**单位：** University of Michigan；UW-Madison；Nanyang Technological University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790233) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Diffusion Transformer (DiT) models excel at generating highquality images through iterative denoising steps, but serving them under strict Service Level Objectives (SLOs) is challenging due to their high computational cost, particularly at larger resolutions. Existing serving systems use fixed-degree sequence parallelism, which is inefficient for heterogeneous workloads with mixed resolutions and deadlines, leading to poor GPU utilization and low SLO attainment. In this paper, we propose step-level sequence parallelism to dynamically adjust the degree of parallelism of individual requests according to their deadlines. We present TetriServe1, a DiT serving system that implements this strategy for highly efficient image generation. Specifically, TetriServe introduces a novel round-based scheduling mechanism that improves SLO attainment by (1) discretizing time into fixed rounds to make deadline-aware scheduling tractable, (2) adapting parallelism at the step level and minimizing GPU hour consumption, and (3) jointly packing requests to minimize late completions. Extensive evaluation on state-of-the-art DiT models shows that TetriServe achieves up to 32% higher SLO attainment compared to existing solutions without degrading image quality.

## 中文摘要

扩散 Transformer（DiT）模型通过迭代去噪步骤在高品质图像生成方面表现优异，但由于其计算成本高昂（在较大分辨率下尤为如此），在严格的服务等级目标（SLO）下对其进行服务具有挑战性。现有的服务系统采用固定并行度的序列并行，对于分辨率与截止时间混合的异构工作负载而言效率低下，导致 GPU 利用率不佳、SLO 达成率偏低。本文提出步级序列并行（step-level sequence parallelism），根据各个请求的截止时间动态调整其并行度。我们提出 TetriServe1，这是一个实现了该策略的 DiT 服务系统，可实现高效的图像生成。具体而言，TetriServe 引入了一种新颖的基于轮次的调度机制，通过以下方式提升 SLO 达成率：(1) 将时间离散化为固定轮次，使截止时间感知的调度变得可处理；(2) 在步级调整并行度并最小化 GPU 小时消耗；(3) 联合打包请求以最小化延迟完成。在先进 DiT 模型上的大量评估表明，与现有方案相比，TetriServe 在图像质量不下降的情况下实现了高达 32% 更高的 SLO 达成率。

## 英文关键词

diffusion transformer serving, gpu resource scheduling, sequence parallelism

## 中文关键词

扩散 Transformer 服务；GPU 资源调度；序列并行

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790233)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2026](../index.md)
