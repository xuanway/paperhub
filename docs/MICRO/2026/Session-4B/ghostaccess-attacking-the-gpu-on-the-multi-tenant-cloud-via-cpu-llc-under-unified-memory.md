---
title: "GhostAccess: Attacking the GPU on the Multi-Tenant Cloud via CPU LLC Under Unified Memory"
description: "MICRO 2026 · Session 4B · GhostAccess：在统一内存下通过 CPU 末级缓存攻击多租户云中的 GPU"
tags:
  - "MICRO2026"
  - "GPU"
---

# GhostAccess: Attacking the GPU on the Multi-Tenant Cloud via CPU LLC Under Unified Memory

**中文标题：** GhostAccess：在统一内存下通过 CPU 末级缓存攻击多租户云中的 GPU

**所属 Session：** [Session 4B](index.md) · [MICRO 2026](../index.md)

**作者：** Zihao Dan, Shinan Liu, Shuwen Deng, Yinqian Zhang, Dongsheng Wang, Yun Chen

**来源：** MICRO 2026，pp. 1459–1473；[DOI](https://doi.org/10.1109/MICRO67795.2026.00108)

## 英文摘要

The emergence of CUDA Unified Memory (UM) provides a unified virtual address space shared by CPUs and GPUs, simplifying programming and enabling memory oversubscription to mitigate GPU memory shortages. However, such technologies may involve a substantial number of CPU-side operations. Whether these behaviors introduce new security risks merits careful investigation. To answer this question, we reverse-engineered a UM performance API, cudaMemAdviseSetPreferredLocation, which enables the GPU to directly access system memory via the CPU page tables by establishing a mapping. Through this reverse engineering, we discover that when the GPU issues write operations to CPU memory through UM mapping, the data is loaded into the CPU last-level cache (LLC), thereby exposing a new attack surface to adversaries. Building on this observation, we propose GhostAccess, a cross-tenant GPU attack framework. GhostAccess can establish a high-bandwidth channel between a trojan residing on the victim tenant's GPU and a spy in another tenant, achieving a channel capacity of up to 1.02 Mbps with an error rate of 0.3%, which is 12.7x faster than the state-of-the-art GPU-assisted cross-tenant covert channel. In addition, we design a cross-tenant GPU side-channel attack for GhostAccess. We evaluate GhostAccess in four scenarios: fingerprinting six machine-learning applications, extracting parameters from K-means and CNN models, and fingerprinting LLM workloads. GhostAccess achieves accuracies of 99.6%, 99.8%, 99.6%, and 99.8%, respectively.

## 中文摘要

CUDA统一内存（UM）的出现提供了CPU和GPU共享的统一虚拟地址空间，简化了编程并实现内存超额使用，以缓解GPU内存短缺的问题。然而，此类技术可能涉及大量的CPU端操作。这些行为是否会带来新的安全风险值得仔细调查。为了回答这个问题，我们逆向设计了一个 UM 性能 API cudaMemAdviseSetPreferredLocation，它使 GPU 能够通过建立映射，通过 CPU 页表直接访问系统内存。通过这个逆向工程，我们发现，当GPU通过UM映射向CPU内存发出写操作时，数据被加载到CPU末级缓存（LLC）中，从而向对手暴露了新的攻击面。基于这一观察，我们提出了 GhostAccess，一种跨租户 GPU 攻击框架。 GhostAccess 可以在受害租户 GPU 上的木马与另一个租户中的间谍之间建立高带宽通道，通道容量高达 1.02 Mbps，错误率为 0.3%，比最先进的 GPU 辅助跨租户隐蔽通道快 12.7 倍。此外，我们还为 GhostAccess 设计了跨租户 GPU 侧通道攻击。我们在四种场景中评估 GhostAccess：对 6 个机器学习应用程序进行指纹识别、从 K 均值和 CNN 模型中提取参数以及对 LLM 工作负载进行指纹识别。 GhostAccess 的准确率分别为 99.6%、99.8%、99.6% 和 99.8%。

## 中文关键词

侧信道；图形处理器；末级缓存；跨租户攻击；统一内存

## 代码与研究制品

- 代码仓库：[https://github.com/ZihaoDan/GhostAccess](https://github.com/ZihaoDan/GhostAccess)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 4B](index.md) · [MICRO 2026 主页](../index.md)
