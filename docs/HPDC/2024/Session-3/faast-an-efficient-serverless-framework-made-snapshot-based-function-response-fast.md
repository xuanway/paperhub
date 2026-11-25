---
title: "Faast: An Efficient Serverless Framework Made Snapshot-based Function Response Fast"
description: "HPDC 2024 · Session 3 — Serverless Computing"
tags:
  - "HPDC2024"
  - "Session 3"
  - "Serverless Computing"
---

# Faast: An Efficient Serverless Framework Made Snapshot-based Function Response Fast

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 3</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658681)

**作者**：Yongshu Bai, Zhihui Yang, Feng Gao

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）

---

## 英文摘要

Recent years have seen the rapid popularity of serverless computing, benefiting from its seamless scalability and pay-as-you-go charg-ing model. Despite recent efforts to enhance function cold-start performance by utilizing snapshot and working set mechanisms, the existing methods still suffered considerable overheads in end-to-end response time as functions’ inputs varied. In this paper, we propose Faast, a novel solution designed to improve function response time by enhancing virtual machine snapshot-based startup while guaranteeing function execution performance. Our system introduces a preparation phase to generate a lightweight working set, which excludes stale pages that do not require loading from snapshot files for each function to expedite startup. Additionally, Faast facilitates network connectivity for the snapshot by implementing NAT within the virtio-net device model bypassing the time-consuming network namespace setup. To guarantee execution performance, a divergent page fault handling mechanism is designed to address page faults related to stale and non-stale pages separately, effectively mitigating sluggish disk I/O accesses. Faast also incrementally adapts the working set file across various function invocations to bolster functions’ resilience to diverse inputs. Extensive experiments demonstrate that Faast reduces function end-to-end time by up to 63% compared to the state-of-the-art.

## 中文摘要

近年来，无服务器计算凭借其无缝扩展性与按需付费的计费模式迅速普及。尽管近期有工作利用快照与工作集机制来提升函数冷启动性能，但现有方法在函数输入变化时，端到端响应时间仍存在可观开销。本文提出 Faast，一种新颖方案，通过增强基于虚拟机快照的启动来改善函数响应时间，同时保证函数执行性能。我们的系统引入准备阶段来生成轻量工作集，排除无需从快照文件加载的陈旧页面，从而为每个函数加速启动。此外，Faast 通过在 virtio-net 设备模型中实现 NAT 来为快照提供网络连通性，绕过了耗时的网络命名空间设置。为保证执行性能，设计了分化的缺页处理机制，分别处理与陈旧页面和非陈旧页面相关的缺页，有效缓解缓慢的磁盘 I/O 访问。Faast 还在不同函数调用间增量地调整工作集文件，以增强函数对多样输入的适应能力。大量实验表明，与最先进方案相比，Faast 将函数端到端时间最高降低 63%。

## 英文关键词

cloud computing, serverless computing, virtualization, snapshot, working set

## 中文关键词

云计算，无服务器计算，虚拟化，快照，工作集

---

[← 返回 Session 3 — Serverless Computing](index.md)
