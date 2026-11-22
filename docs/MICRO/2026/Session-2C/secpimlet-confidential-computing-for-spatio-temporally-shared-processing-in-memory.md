---
title: "SecPIMlet: Confidential Computing for Spatio-Temporally Shared Processing-in-Memory"
description: "MICRO 2026 · Session 2C · SecPIMlet：面向时空共享存内处理的机密计算"
tags:
  - "MICRO2026"
  - "Processing-in-Memory"
---

# SecPIMlet: Confidential Computing for Spatio-Temporally Shared Processing-in-Memory

**中文标题：** SecPIMlet：面向时空共享存内处理的机密计算

**所属 Session：** [Session 2C](index.md) · [MICRO 2026](../index.md)

**作者：** Sunho Lee, Minwoo Noh, Jeongwon Choi, Kwanghoon Choi, Igjae Kim, Chang Hyun Park, Jaehyuk Huh

**来源：** MICRO 2026，pp. 753–769；[DOI](https://doi.org/10.1109/MICRO67795.2026.00064)

## 英文摘要

As memory-intensive applications, particularly language models, continue to grow, processing-in-memory (PIM) has emerged as a promising architecture to alleviate memory bandwidth limitations. We find that PIM systems need to support both spatio and temporal sharing between domains to extract the maximal performance. However, current PIM systems lack the necessary protection to securely support such sharing. To address these issues, we introduce SecPIMlet, a trusted multi-domain PIM that enables efficient spatio-temporal sharing. For fast and confidential spatio-temporal sharing, SecPIMlet protects both PIM-resident data and execution contexts, while also securing in-transit data between the CPU and PIM. Our evaluation shows that SecPIMlet achieves at least 175.4% higher throughput than state-of-the-art approaches that support only spatial or temporal sharing, while providing stronger security protection.

## 中文摘要

随着内存密集型应用程序（尤其是语言模型）的不断增长，存内处理 (PIM) 已成为缓解内存带宽限制的一种有前景的架构。我们发现 PIM 系统需要支持域之间的空间和时间共享，以获取最大性能。然而，当前的 PIM 系统缺乏必要的保护来安全地支持此类共享。为了解决这些问题，我们引入了 SecPIMlet，这是一种可信的多域 PIM，可以实现高效的时空共享。为了实现快速、保密的时空共享，SecPIMlet 可以保护 PIM 驻留数据和执行上下文，同时还可以保护 CPU 和 PIM 之间传输的数据。我们的评估表明，与仅支持空间或时间共享的最先进方法相比，SecPIMlet 的吞吐量至少高出 175.4%，同时提供更强的安全保护。

## 中文关键词

存内处理；机密计算；时空共享；内存隔离；安全架构

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2C](index.md) · [MICRO 2026 主页](../index.md)
