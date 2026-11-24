---
title: "DOGI: Data Placement with Oracle-Guided Insights for Log-Structured Systems"
description: "FAST 2026 · Tiering, Mobile, and SSDs · 第 543–560 页"
tags:
  - "FAST2026"
  - "Tiering, Mobile, and SSDs"
---

# DOGI: Data Placement with Oracle-Guided Insights for Log-Structured Systems

**中文标题**：DOGI：基于 Oracle 指导洞见的日志结构系统数据放置

**Session**：Tiering, Mobile, and SSDs · 2026-02-26 10:50–12:30 · Chair：Vasily Tarasov（IBM Research）

**作者**：Jeeyun Kim, Pohang University of Science and Technology (POSTECH); Seonggyun Oh and Jungwoo Kim, Daegu Gyeongbuk Institute of Science and Technology; Jisung Park, Pohang University of Science and Technology (POSTECH); Jaeho Kim, Gyeongsang National University; Sungjin Lee, Pohang University of Science and Technology (POSTECH); Sam H. Noh, Virginia Tech

**会议**：FAST 2026 · Santa Clara, CA · 第 543–560 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/kim-jeeyun](https://www.usenix.org/conference/fast26/presentation/kim-jeeyun)

**论文 PDF**：[fast26-kim-jeeyun.pdf](https://www.usenix.org/system/files/fast26-kim-jeeyun.pdf)

---

## 英文摘要

Log-structured systems have become the backbone of modern data-intensive applications thanks to their high write throughput. Their efficiency, however, is deteriorated by the write amplification factor (WAF) induced by garbage collection. Despite extensive studies, there still exists a wide gap between practice and optimality. In this paper, we bridge this gap with two key contributions. We first design NoDaP, a near-optimal oracle baseline that sets the upper bound for WAF reduction. Then, guided by insights from NoDaP, we propose DOGI, an oracle-inspired data placement technique that combines simple yet effective heuristics with lightweight machine learning. DOGI predicts invalidation times for data blocks with high accuracy, dynamically tunes group configurations, and finds the sweet spot between fine-grained data placement and misprediction penalty. Our experiments, using simulations and a prototype on a zoned device, show that DOGI reduces WAF by up to 23.2% while improving write throughput by up to 13.3% over the best-performing baseline.

## 中文摘要

日志结构系统凭借高写吞吐量，已成为现代数据密集型应用的支柱。然而，垃圾回收引起的写放大因子（WAF）会削弱其效率。尽管已有大量研究，实践与最优性之间仍存在很大差距。本文通过两项关键贡献弥合这一差距。我们首先设计 NoDaP，一个接近最优的 Oracle 基线，为 WAF 降低设定上界。然后，在 NoDaP 洞见的指导下，我们提出 DOGI，一种受 Oracle 启发的数据放置技术，它将简单而有效的启发式方法与轻量级机器学习相结合。DOGI 能够高精度预测数据块的失效时间，动态调整组配置，并在细粒度数据放置与误预测代价之间找到最佳平衡点。我们使用仿真和分区设备上的原型进行实验，结果表明，与表现最佳的基线相比，DOGI 将 WAF 最多降低 23.2%，同时将写吞吐量最多提升 13.3%。
