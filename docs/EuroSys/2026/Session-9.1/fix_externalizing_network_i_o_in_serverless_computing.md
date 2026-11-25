---
title: "Fix: externalizing network I/O in serverless computing"
description: "EuroSys 2026 · Cloud · Yuhan Deng (Stanford University), Akshay Srivatsan (Stanford University), Sebast"
tags:
  - "EuroSys2026"
  - "Cloud"
---

# Fix: externalizing network I/O in serverless computing

**中文标题：** Fix：在无服务器计算中外部化网络I/O

**所属 Session：** [Session 9.1: Cloud](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud</p>
</div>

**作者**：Yuhan Deng (Stanford University), Akshay Srivatsan (Stanford University), Sebastian Ingino (Stanford University), Francis Chua (Stanford University), Yasmine Mitchell (Stanford University), Matthew Vilaysack (Stanford University), Keith Winstein (Stanford University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769387)

## 英文摘要

We describe a system for serverless computing where users, programs, and the underlying platform share a common representation of a computation: a deterministic procedure, run in an environment of well-specified data or the outputs of other computations. This representation externalizes I/O: data movement over the network is performed exclusively by the platform. Applications can describe the precise data needed at each stage, helping the provider schedule tasks and network transfers to reduce starvation. The design suggests an end-to-end argument for outsourced computing, shifting the service model from “pay-for-effort” to “pay-for-results.”

## 中文摘要

我们描述一个用于无服务器计算的系统，其中用户、程序和底层平台共享对计算的同一表示：一个确定性的过程，在由良定义的数据或其他计算输出构成的环境中运行。这一表示将I/O外部化：网络上的数据移动完全由平台执行。应用可以描述每个阶段所需的确切数据，从而帮助提供商调度任务和网络传输以减少饥饿。该设计为外包计算提出了一个端到端论证，将服务模式从“为努力付费”转向“为结果付费”。

**英文关键词：** serverless computing

**中文关键词：** 无服务器计算

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
