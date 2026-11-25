---
title: "Merkle-Tree Weight Snapshot Deduplication for Provenance-Aware Auditing of Neural Network Training"
description: "HPDC 2026 · Session 8 — Storage & I/O for Data-Intensive Workloads"
tags:
  - "HPDC2026"
  - "Session 8"
  - "Storage & I/O for Data-Intensive Workloads"
---

# Merkle-Tree Weight Snapshot Deduplication for Provenance-Aware Auditing of Neural Network Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 8</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807587)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#NgATBHTMNT26](https://dblp.org/db/conf/hpdc/hpdc2026.html#NgATBHTMNT26)

**作者**：Kin Wai Ng, Francesco Antici, Nigel Tan, Befikir Bogale, Caleb Han, Florence Tama, Osamu Miyashita, Bogdan Nicolae, Michela Taufer

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）

---

## 英文摘要

Weight snapshots taken during neural network training provide a foundation for reproducibility and for understanding how models evolve during learning. They indicate whether networks progress toward higher accuracy or diverge toward poor generalization, yet their size and frequency impose severe storage and I/O burdens. As models scale, snapshots exhibit substantial cross-epoch redundancy, making them increasingly difficult to archive and analyze efficiently. We introduce a Merkle-tree deduplication pipeline that removes redundancy while exposing metadata about training dynamics. Chunking and deduplicating weights yields 70–80% storage savings across CIFAR-10/100 and protein diffraction datasets, outperforming list-based deduplication and per-snapshot compression baselines. Beyond space savings, Merkle-tree metadata categorizes chunks as fixed duplicates, shifted duplicates, or first occurrences. These signals predict validation accuracy with mean absolute error below 1% and provide an optional, metadata-driven signal to inform early stopping, enabling savings of 16–72% of the training epochs with negligible accuracy loss. Our work demonstrates that Merkle-tree deduplication provides a unified approach to reduce overhead, preserve reproducibility, and explain training dynamics within user-defined error tolerances, without disrupting the learning loop.

## 中文摘要

神经网络训练期间采集的权重快照为可复现性以及理解模型在学习过程中的演化提供了基础。它们指示网络是朝更高精度推进还是发散走向较差的泛化，但其大小与频率带来沉重的存储和 I/O 负担。随着模型规模增长，快照呈现显著的跨轮次冗余，使其越来越难以高效归档与分析。我们提出一条 Merkle 树去重流水线，在消除冗余的同时暴露有关训练动态的元数据。对权重分块并去重，在 CIFAR-10/100 和蛋白质衍射数据集上节省 70–80% 的存储，优于基于列表的去重和逐快照压缩基线。除节省空间外，Merkle 树元数据还将块归类为固定重复、偏移重复或首次出现。这些信号以低于 1% 的平均绝对误差预测验证精度，并提供可选的元数据驱动信号以指导早停，在精度损失可忽略的情况下节省 16–72% 的训练轮次。我们的工作表明，Merkle 树去重提供了一种统一方法，在用户定义的误差容限内降低开销、保持可复现性并解释训练动态，同时不干扰学习循环。

## 英文关键词

Checkpointing, Neural architecture search, Model evolution analysis, Metadata-driven monitoring, Cross-epoch redundancy

## 中文关键词

检查点，神经架构搜索，模型演化分析，元数据驱动监控，跨轮次冗余

---

[← 返回 Session 8 — Storage & I/O for Data-Intensive Workloads](index.md)
