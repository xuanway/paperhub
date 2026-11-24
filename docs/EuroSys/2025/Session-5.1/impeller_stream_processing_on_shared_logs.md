---
title: "Impeller: Stream Processing on Shared Logs"
description: "EuroSys 2025 · Graph and Stream processing · Zhiting Zhu (Lepton AI), Zhipeng Jia (Google), Newton Ni (University of Texas at"
tags:
  - "EuroSys2025"
  - "Graph and Stream processing"
---

# Impeller: Stream Processing on Shared Logs

**中文标题：** 基于共享日志的流处理

**所属 Session：** [Session 5.1: Graph and Stream processing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Graph and Stream processing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Graph and Stream processing</p>
</div>

**作者**：Zhiting Zhu (Lepton AI), Zhipeng Jia (Google), Newton Ni (University of Texas at Austin), Dixin Tang (UT Austin), Emmett Witchel (UT Austin)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717485)

## 英文摘要

Current stream processing systems provide exactly-once semantics using checkpointing or a combination of logging and checkpointing. These approaches can introduce high overhead, significantly increasing the latency for normal stream processing because maintaining exactly-once semantics requires coordination across distributed nodes and streams to capture a globally consistent state. We observe that modern distributed shared logs offer a promising solution for maintaining exactly-once semantics with a small overhead. We propose Impeller, a stream processing system that uses a distributed shared log for data storage and exactly-once processing. To maintain exactly-once semantics, Impeller includes a novel and efficient progress marking protocol based on string tags and selective reads in a shared log. The key idea is to leverage the log’s record-tagging feature to atomically mark progress across all streams. The experiments over the NEXMark benchmark show that Impeller achieves 1.3× to 5.4× lower p50 latency, or 1.3× to 5.0× higher saturation throughput than Kafka Streams.

## 中文摘要

当前的流处理系统使用检查点，或日志与检查点相结合的方式提供精确一次语义。这些方法会引入高开销，显著增加正常流处理的延迟，因为维护精确一次语义需要跨分布式节点和流进行协调，以捕获全局一致的状态。我们观察到，现代分布式共享日志为以较小开销维护精确一次语义提供了一种有前景的解决方案。我们提出 Impeller，一个使用分布式共享日志进行数据存储和精确一次处理的流处理系统。为维护精确一次语义，Impeller 包含一种新颖且高效的进度标记协议，基于字符串标签和共享日志中的选择性读取。其关键思想是利用日志的记录标签功能，原子地在所有流上标记进度。在 NEXMark 基准上的实验表明，与 Kafka Streams 相比，Impeller 的 p50 延迟低 1.3 倍至 5.4 倍，或在饱和吞吐量上高 1.3 倍至 5.0 倍。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
