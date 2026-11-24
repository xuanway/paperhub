---
title: "AlloyStack: A Library Operating System for Serverless Workflow Applications"
description: "EuroSys 2025 · Cloud and Serverless Computing · Jianing You (Tianjin University), Kang Chen (Tsinghua University), Laiping Zhao "
tags:
  - "EuroSys2025"
  - "Cloud and Serverless Computing"
---

# AlloyStack: A Library Operating System for Serverless Workflow Applications

**中文标题：** 面向无服务器工作流应用的库操作系统

**所属 Session：** [Session 7.1: Cloud and Serverless Computing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Serverless Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Serverless Computing</p>
</div>

**作者**：Jianing You (Tianjin University), Kang Chen (Tsinghua University), Laiping Zhao (Tianjin University), Yiming Li (Tianjin University), Yichi Chen (Tianjin University), Yuxuan Du (Tianjin University), Yanjie Wang (Tianjin University), Luhang Wen (Tianjin University), Keyang Hu (Tsinghua University), Keqiu Li (Tianjin University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717490)

## 英文摘要

Serverless workflow applications, composed of multiple serverless functions, are increasingly popular in production. However, inter-function communication and cold start latency remain key performance bottlenecks. This paper introduces AlloyStack, a library operating system (LibOS) tailored for serverless workflows. AlloyStack addresses two major challenges: (1) reducing cold start latency through on-demand OS component loading and (2) minimizing data transfer overhead by enabling functions within the same workflow to share a single address space, eliminating unnecessary data copying. To ensure secure isolation, AlloyStack uses Memory Protection Keys (MPK) to separate user functions from the LibOS while maintaining efficient data sharing. Our evaluation shows that AlloyStack reduces cold start times by 98.5% to just 1.3𝑚𝑠. Compared to SOTA systems, AlloyStack achieves a 7.3× to 38.7× speedup in Rust end-to-end latency and a 4.8× to 78.3× speedup in other languages for intermediate data-intensive workflows.

## 中文摘要

由多个无服务器函数组成的无服务器工作流应用在生产中日益流行。然而，函数间通信和冷启动延迟仍是关键性能瓶颈。本文提出 AlloyStack，一个为无服务器工作流量身定制的库操作系统（LibOS）。AlloyStack 解决两大挑战：（1）通过按需加载操作系统组件降低冷启动延迟；（2）通过使同一工作流内的函数共享单一地址空间、消除不必要的数据拷贝来最小化数据传输开销。为确保安全隔离，AlloyStack 使用内存保护键（MPK）将用户函数与 LibOS 分离，同时保持高效的数据共享。我们的评估表明，AlloyStack 将冷启动时间降低 98.5%，仅需 1.3 ms。与 SOTA 系统相比，AlloyStack 在 Rust 端到端延迟上实现 7.3 至 38.7 倍加速，在其他语言的中间数据密集型工作流上实现 4.8 至 78.3 倍加速。

**英文关键词：** Serverless Computing, Cold Start, Data Transfer

**中文关键词：** 无服务器计算、冷启动、数据传输

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
