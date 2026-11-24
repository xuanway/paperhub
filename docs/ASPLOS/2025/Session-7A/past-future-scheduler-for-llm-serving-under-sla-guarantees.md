---
title: "Past-Future Scheduler for LLM Serving under SLA Guarantees"
description: "ASPLOS 2025 · Session 7A · 面向 SLA 保证下 LLM 服务的 Past-Future 调度器"
tags:
  - "ASPLOS2025"
  - "Session 7A"
  - "Serving LLMs"
---

# Past-Future Scheduler for LLM Serving under SLA Guarantees

**中文标题：** 面向 SLA 保证下 LLM 服务的 Past-Future 调度器

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ruihao Gong (Beihang University), Shihao Bai (SenseTime), Siyu Wu (Beihang University), Yunqian Fan (SenseTime), Zaijun Wang (SenseTime), Xiuhong Li (Peking University), Hailong Yang (Beihang University), Xianglong Liu (Beihang University)

**单位：** Beihang University；SenseTime；Peking University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716011) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The exploration and application of Large Language Models (LLMs) is thriving. To reduce deployment costs, continuous batching has become an essential feature in current service frameworks. The effectiveness of continuous batching relies on an accurate estimate of the memory requirements of requests. However, due to the diversity in request output lengths, existing frameworks tend to adopt aggressive or conservative schedulers, which often result in significant overestimation or underestimation of memory consumption. Consequently, they suffer from harmful request evictions or prolonged queuing times, failing to achieve satisfactory throughput under strict Service Level Agreement (SLA) guarantees (a.k.a. goodput), across various LLM application scenarios with differing input-output length distributions. To address this issue, we propose a novel Past-Future scheduler that precisely estimates the peak memory resources required by the running batch via considering the historical distribution of request output lengths and calculating memory occupancy at each future time point. It adapts to applications with all types of input-output length distributions, balancing the trade-off between request queuing and harmful evictions, thereby consistently achieving better goodput. Furthermore, to validate the effectiveness of the proposed scheduler, we developed a high-performance LLM serving framework, LightLLM, that implements the Past-Future scheduler. Compared to existing aggressive or conservative schedulers, LightLLM demonstrates superior goodput, achieving up to 2-3× higher goodput than other schedulers under heavy loads. LightLLM is open source to boost the research in such direction (

## 中文摘要

大语言模型（LLM）的探索与应用正蓬勃发展。为降低部署成本，连续批处理（continuous batching）已成为当前服务框架中的必备特性。连续批处理的有效性依赖于对请求内存需求的准确估计。然而，由于请求输出长度的多样性，现有框架往往采用激进或保守的调度器，常常导致对内存消耗的显著高估或低估。因此，它们会遭受有害的请求驱逐或漫长的排队时间，无法在具有不同输入-输出长度分布的各种 LLM 应用场景中，于严格的服务等级协议（SLA）保证下（即 goodput）取得令人满意的吞吐。为解决该问题，我们提出一种新颖的 Past-Future 调度器，它通过考虑请求输出长度的历史分布并计算未来每个时间点的内存占用，精确估计运行批次所需的峰值内存资源。它可适应具有各类输入-输出长度分布的应用，在请求排队与有害驱逐之间取得平衡，从而持续获得更好的 goodput。此外，为验证所提调度器的有效性，我们开发了实现 Past-Future 调度器的高性能 LLM 服务框架 LightLLM。与现有激进或保守的调度器相比，LightLLM 展现出更优的 goodput，在重负载下其 goodput 比其他调度器高出 2-3×。LightLLM 已开源以推动该方向的研究（

## 英文关键词

LLM Inference, Scheduling Optimization

## 中文关键词

LLM 推理；调度优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716011)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2025](../index.md)
