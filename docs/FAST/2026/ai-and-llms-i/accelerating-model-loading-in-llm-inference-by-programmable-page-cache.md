---
title: "Accelerating Model Loading in LLM Inference by Programmable Page Cache"
description: "FAST 2026 · AI and LLMs I · 第 117–132 页"
tags:
  - "FAST2026"
  - "AI and LLMs I"
---

# Accelerating Model Loading in LLM Inference by Programmable Page Cache

**中文标题**：利用可编程页缓存加速 LLM 推理中的模型加载

**Session**：AI and LLMs I · 2026-02-24 11:05–12:25 · Chair：Bingzhe Li（The University of Texas at Dallas）

**作者**：Yubo Liu, Hongbo Li, Xiaojia Huang, Yongfeng Wang, Hanjun Guo, Hui Chen, Yuxin Ren, and Ning Jia, Huawei Technologies Co., Ltd.

**会议**：FAST 2026 · Santa Clara, CA · 第 117–132 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/liu-yubo](https://www.usenix.org/conference/fast26/presentation/liu-yubo)

**论文 PDF**：[fast26-liu-yubo.pdf](https://www.usenix.org/system/files/fast26-liu-yubo.pdf)

---

## 英文摘要

This paper examines the model loading bottleneck during the LLM inference startup. Existing solutions often optimize model loading performance at the expense of compatibility. However, compatibility is a crucial factor determining whether a technology can be widely applied in real-world scenarios. This work achieves both high performance and strong compatibility by optimizing the cache policy of the kernel file system. We design PPC, a programmable page cache framework that allows users to customize page cache policies in a non-intrusive, flexible, and lightweight manner. Furthermore, we design MAIO, a cache policy implemented based on PPC, to optimize model loading. MAIO introduces an I/O template-based mechanism to fully utilize SSD bandwidth, XPU affinity, and data locality to enhance the efficiency of prefetching and eviction. Our evaluation shows that MAIO reduces the model loading latency by up to 79% compared to existing optimizations. In a real-world application, MAIO achieves up to 36% improvement in inference throughput over other tested solutions in the elastic deployment scenario.

## 中文摘要

本文研究了 LLM 推理启动过程中的模型加载瓶颈。现有方案往往以牺牲兼容性为代价来优化模型加载性能。然而，兼容性是决定一项技术能否在真实场景中广泛应用的关键因素。本工作通过优化内核文件系统的缓存策略，同时实现了高性能与强兼容性。我们设计了 PPC，一个可编程页缓存框架，使用户能够以非侵入、灵活且轻量的方式自定义页缓存策略。此外，我们设计了 MAIO，一种基于 PPC 实现的缓存策略，用于优化模型加载。MAIO 引入基于 I/O 模板的机制，充分利用 SSD 带宽、XPU 亲和性和数据局部性，以提升预取和逐出的效率。评估表明，与现有优化相比，MAIO 将模型加载延迟最多降低 79%。在真实应用中，MAIO 在弹性部署场景下相较其他测试方案将推理吞吐量最多提升 36%。
