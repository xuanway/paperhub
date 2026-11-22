---
title: "A Harmony of Ice and Fire: Mitigating Cold Last-Level Cache Effects in Serverless Computing on Commodity Hardware"
description: "MICRO 2026 · Session 9C · A Harmony of Ice and Fire：缓解商用硬件上无服务器计算的末级缓存冷启动影响"
tags:
  - "MICRO2026"
  - "Cache"
---

# A Harmony of Ice and Fire: Mitigating Cold Last-Level Cache Effects in Serverless Computing on Commodity Hardware

**中文标题：** A Harmony of Ice and Fire：缓解商用硬件上无服务器计算的末级缓存冷启动影响

**所属 Session：** [Session 9C](index.md) · [MICRO 2026](../index.md)

**作者：** Qi Ling, Ajay Rawat, Pedro Fonseca, Kazem Taram

**来源：** MICRO 2026，pp. 3395–3411；[DOI](https://doi.org/10.1109/MICRO67795.2026.00227)

## 英文摘要

Serverless computing has become a popular paradigm for deploying event-driven services, allowing developers to focus purely on their service logic and leave infrastructure management to cloud providers. However, serverless functions are short-lived and heavily interleaved, causing them to execute with cold microarchitectural state and lose much of the performance benefit normally delivered by modern caches. We show that ineffective management of the last-level cache (LLC) is a primary contributor to this overhead. This paper presents HarmoniCa, a dynamic, fine-grained LLC management system that requires no hardware or application changes. HarmoniCa introduces a slice-aware LLC partitioning mechanism that leverages the linear structure of Intel's slice-hashing function to construct lightweight set–slice partitions, improving partitioning granularity and reducing partitioning overheads by up to 7× compared to existing techniques. Building on a detailed characterization of serverless cache behavior and using our novel partitioning technique, HarmoniCa dynamically allocates shared and private LLC partitions, learns each function's sensitivity to cold LLC, and assigns cache resources accordingly. Across a range of serverless workloads, HarmoniCa improves the performance of cache-sensitive functions by 34.7%, without harming the performance of other co-located functions.

## 中文摘要

无服务器计算已成为部署事件驱动服务的流行范例，使开发人员能够完全专注于其服务逻辑，并将基础设施管理留给云提供商。然而，无服务器功能是短暂的并且严重交错，导致它们以冷微架构状态执行，并失去了现代缓存通常提供的大部分性能优势。我们表明，末级缓存 (LLC) 的无效管理是造成这种开销的主要原因。本文介绍了 HarmoniCa，这是一种动态、细粒度的 LLC 管理系统，无需更改硬件或应用程序。 HarmoniCa引入了切片感知的LLC分区机制，利用英特尔切片散列函数的线性结构构建轻量级的集合切片分区，与现有技术相比，提高了分区粒度，并将分区开销减少了7倍。基于无服务器缓存行为的详细特征并使用我们新颖的分区技术，HarmoniCa 动态分配共享和私有 LLC 分区，了解每个功能对冷 LLC 的敏感性，并相应地分配缓存资源。在一系列无服务器工作负载中，HarmoniCa 将缓存敏感功能的性能提高了 34.7%，而不会损害其他共置功能的性能。

## 中文关键词

无服务器计算；缓存分区；冷启动；末级缓存

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21548955](https://doi.org/10.5281/zenodo.21548955)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9C](index.md) · [MICRO 2026 主页](../index.md)
