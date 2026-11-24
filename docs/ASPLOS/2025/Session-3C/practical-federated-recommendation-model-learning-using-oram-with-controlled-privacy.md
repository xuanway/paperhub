---
title: "Practical Federated Recommendation Model Learning Using ORAM with Controlled Privacy"
description: "ASPLOS 2025 · Session 3C · 基于可控隐私 ORAM 的实用联邦推荐模型学习"
tags:
  - "ASPLOS2025"
  - "Session 3C"
  - "ML Security"
---

# Practical Federated Recommendation Model Learning Using ORAM with Controlled Privacy

**中文标题：** 基于可控隐私 ORAM 的实用联邦推荐模型学习

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jinyu Liu (The Pennsylvania State University), Wenjie Xiong (Virginia Tech), G. Edward Suh (NVIDIA,Cornell University), Kiwan Maeng (The Pennsylvania State University)

**单位：** The Pennsylvania State University；Virginia Tech；NVIDIA,Cornell University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716014) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Training high-quality recommendation models requires collecting sensitive user data. The popular privacy-enhancing training method, federated learning (FL), cannot be used practically due to these models' large embedding tables. This paper introduces FEDORA, a system for training recommendation models with FL. FEDORA allows each user to only download, train, and upload a small subset of the large tables based on their private data, while hiding the access pattern using oblivious memory (ORAM). FEDORA reduces the ORAM's prohibitive latency and memory overheads by (1) introducing 𝜖-FDP, a formal way to balance the ORAM's privacy with performance, and (2) placing the large ORAM in a power- and cost-efficient SSD with SSD-friendly optimizations. Additionally, FEDORA is carefully designed to support (3) modern operation modes of FL. FEDORA achieves high model accuracy by using private features during training while achieving, on average, 5× latency and 158× SSD lifetime improvement over the baseline.

## 中文摘要

训练高质量的推荐模型需要收集敏感的用户数据。流行的隐私增强训练方法——联邦学习（FL）——由于这类模型拥有庞大的嵌入表而无法实际使用。本文提出 FEDORA，一个用 FL 训练推荐模型的系统。FEDORA 允许每个用户根据其私有数据，仅下载、训练并上传大表中的一小部分，同时使用不经意内存（ORAM）隐藏访问模式。FEDORA 通过以下方式降低 ORAM 高昂的延迟与内存开销：(1) 引入 𝜖-FDP，一种在 ORAM 隐私与性能之间取得平衡的形式化方法；(2) 将大型 ORAM 放置在能效与成本高效的 SSD 中，并配以面向 SSD 的优化。此外，FEDORA 经过精心设计以支持 (3) FL 的现代运行模式。FEDORA 通过在训练中使用私有特征实现了高模型精度，同时相比基线平均取得 5× 的延迟改善和 158× 的 SSD 寿命提升。

## 英文关键词

Federated Learning; Differential Privacy; Privacy Preserving Machine Learning; Trusted Execution Environment; Oblivious Memory; Solid State Drives

## 中文关键词

联邦学习；差分隐私；隐私保护机器学习；可信执行环境；不经意内存；固态硬盘

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716014)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2025](../index.md)
