---
title: "BASK: Batch And SmartNIC-offloaded KSM"
description: "EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators · Chanshin Kwak (KAIST), Jaehyeon Lee (KAIST), Minkyu Jung (KAIST), Changjun Lee ("
tags:
  - "EuroSys2026"
  - "Programmable Networks, SmartNICs & Accelerators"
---

# BASK: Batch And SmartNIC-offloaded KSM

**中文标题：** BASK：批处理与 SmartNIC 卸载的 KSM

**所属 Session：** [Session 11.2: Programmable Networks, SmartNICs & Accelerators](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Programmable Networks, SmartNICs & Accelerators。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Programmable Networks, SmartNICs & Accelerators</p>
</div>

**作者**：Chanshin Kwak (KAIST), Jaehyeon Lee (KAIST), Minkyu Jung (KAIST), Changjun Lee (KAIST), Youngjin Kwon (KAIST)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769372)

## 英文摘要

Modern cloud servers are increasingly constrained by memory capacity and bandwidth, despite dramatic growth in CPU core counts. Kernel Same-page Merging (KSM) alleviates memory pressure by deduplicating redundant pages, but incurs significant CPU overhead and performance interference due to frequent comparisons and hashing. Prior work reduces this burden through stateless offloading to accelerators such as SmartNICs, but suffers from low deduplication throughput due to frequent communication overhead.

This paper presents BASK, a stateful SmartNIC-based framework for KSM that offloads both control-plane and data-plane deduplication tasks. BASK introduces a transactional offloading model with optimistic concurrency control and shadow metadata, enabling batched, self-contained page deduplication, significantly improving deduplication throughput by minimizing communication overhead between host and SmartNIC. It tolerates SmartNIC failures, ensures safety through validation and rollback, and maintains isolation using read-only memory exposure. Evaluation under realistic cloud workloads shows that BASK improves deduplication throughput by up to 3.68× over standard KSM, while reducing Redis tail latency impact to only 1.42×, compared to 10.02× under aggressive KSM settings.

## 中文摘要

尽管 CPU 核数大幅增长，现代云服务器仍日益受限于内存容量与带宽。内核同页合并（KSM）通过去重冗余页面缓解内存压力，但因频繁的比较与哈希操作而带来显著的 CPU 开销与性能干扰。已有工作通过无状态卸载到 SmartNIC 等加速器来减轻这一负担，但受频繁通信开销影响，去重吞吐偏低。

本文提出 BASK，一个基于 SmartNIC 的有状态 KSM 框架，同时卸载控制面与数据面的去重任务。BASK 引入带乐观并发控制与影子元数据的事务式卸载模型，实现批量的、自包含的页面去重，通过最小化主机与 SmartNIC 之间的通信开销显著提升去重吞吐。它可容忍 SmartNIC 故障，通过校验与回滚确保安全，并利用只读内存暴露维持隔离。在真实云负载下的评估表明，BASK 相比标准 KSM 将去重吞吐最多提升 3.68×，同时将 Redis 尾延迟影响降至仅 1.42×，而在激进的 KSM 设置下该影响为 10.02×。

**英文关键词：** Cloud Computing, SmartNIC, memory deduplication, optimistic concurrency control

**中文关键词：** 云计算、SmartNIC、内存去重、乐观并发控制

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
