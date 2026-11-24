---
title: "Moko: Marrying Python with Big Data Systems"
description: "EuroSys 2025 · Distributed Systems · Ke Meng (Alibaba Group), Tao He (Alibaba Group), Sijie Shen (Alibaba Group), Lei"
tags:
  - "EuroSys2025"
  - "Distributed Systems"
---

# Moko: Marrying Python with Big Data Systems

**中文标题：** 将 Python 与大数据系统结合

**所属 Session：** [Session 3.1: Distributed Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Distributed Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Distributed Systems</p>
</div>

**作者**：Ke Meng (Alibaba Group), Tao He (Alibaba Group), Sijie Shen (Alibaba Group), Lei Wang (Alibaba Group), Wenyuan Yu (Alibaba Group), Jingren Zhou (Alibaba Group)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696100)

## 英文摘要

Python stands as the preferred language for data science, thanks to its user-friendly syntax and a robust ecosystem that effortlessly accommodates a variety of data types and workloads, such as relational/tabular data, tensors, and graphs. While Python thrives in smaller data settings, it struggles to scale in distributed big data environments. MOKO is an IR-based execution framework designed to extend Python’s reach into the distributed big data domain by generating code that can utilize existing systems such as Spark, Dask, Torch, and GRAPE. MOKO preserves Python’s key features— interoperability, ease of use, and support for multi-model data types and workloads—while enabling efficient execution in a distributed setting. Our evaluation indicates that MOKO can accelerate Python applications by up to 11× across diverse systems, diminish data alignment overhead by 28×, and outperform hand-optimized solutions by 2.5×.

## 中文摘要

Python 凭借其易用的语法和强大的生态（可轻松容纳关系/表格数据、张量、图等多种数据类型与工作负载），成为数据科学的首选语言。尽管 Python 在较小数据规模下蓬勃发展，但在分布式大数据环境中却难以扩展。MOKO 是一个基于中间表示（IR）的执行框架，旨在通过生成可利用 Spark、Dask、Torch 和 GRAPE 等现有系统的代码，将 Python 的能力延伸到分布式大数据领域。MOKO 保留了 Python 的关键特性——互操作性、易用性以及对多模型数据类型和工作负载的支持——同时在分布式环境中实现高效执行。我们的评估表明，MOKO 可在多种系统上将 Python 应用加速至多 11 倍，将数据对齐开销降低 28 倍，并比手工优化的方案快 2.5 倍。

**英文关键词：** big-data, Python, scheduling

**中文关键词：** 大数据、Python、调度

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
