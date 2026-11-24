---
title: "MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models"
description: "ASPLOS 2026 · Session 3B · MoDM：基于扩散模型混合的高效图像生成服务"
tags:
  - "ASPLOS2026"
  - "Session 3B"
  - "Mixture-of-Experts & Efficient Inference"
---

# MoDM: Efficient Serving for Image Generation via Mixture-of-Diffusion Models

**中文标题：** MoDM：基于扩散模型混合的高效图像生成服务

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yuchen Xia (University of Michigan), Divyam Sharma (University of Michigan), Yichao Yuan (University of Michigan), Souvik Kundu (Intel Labs), Nishil Talati (University of Michigan)

**单位：** University of Michigan；Intel Labs

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762220) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Diffusion-based text-to-image generation models trade latency for quality: small models are fast but generate lower quality images, while large models produce better images but are slow. We present MoDM, a novel caching-based serving system for diffusion models that dynamically balances latency and quality through a mixture of diffusion models. Unlike prior approaches that rely on model-specific internal features, MoDM caches final images, allowing seamless retrieval and reuse across multiple diffusion model families. This design enables adaptive serving by dynamically balancing latency and image quality: using smaller models for cache-hit requests to reduce latency while reserving larger models for cache-miss requests to maintain quality. Small model image quality is preserved using retrieved cached images. We design a global monitor that optimally allocates GPU resources and balances inference workload, ensuring high throughput while meeting Service-Level Objectives (SLOs) under varying request rates. Our evaluations show that MoDM significantly reduces an average serving time by 2.5× while retaining image quality, making it a practical solution for scalable and resource-efficient model deployment.

## 中文摘要

基于扩散的文本到图像生成模型以延迟换取质量：小模型速度快，但生成的图像质量较低；大模型生成的图像更好，但速度较慢。我们提出 MoDM，一个新颖的基于缓存的扩散模型服务系统，它通过混合多种扩散模型来动态平衡延迟与质量。与依赖模型特定内部特征的已有方法不同，MoDM 缓存最终图像，从而可在多个扩散模型家族之间无缝检索与复用。该设计通过动态平衡延迟与图像质量来实现自适应服务：对缓存命中的请求使用较小的模型以降低延迟，同时为缓存未命中的请求保留较大的模型以维持质量。小模型的图像质量通过检索到的缓存图像得以保持。我们设计了一个全局监控器，它最优地分配 GPU 资源并平衡推理负载，在变化的请求速率下确保高吞吐同时满足服务等级目标（SLO）。我们的评估表明，MoDM 在保持图像质量的同时将平均服务时间显著降低了 2.5×，使其成为可扩展且资源高效的模型部署的实用解决方案。

## 英文关键词

Model serving; Image generation; Caching

## 中文关键词

模型服务；图像生成；缓存

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762220)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2026](../index.md)
