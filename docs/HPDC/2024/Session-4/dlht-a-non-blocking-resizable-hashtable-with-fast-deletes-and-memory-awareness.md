---
title: "DLHT: A Non-blocking Resizable Hashtable with Fast Deletes and Memory-awareness"
description: "HPDC 2024 · Session 4 — Software Systems & Workflows"
tags:
  - "HPDC2024"
  - "Session 4"
  - "Software Systems & Workflows"
---

# DLHT: A Non-blocking Resizable Hashtable with Fast Deletes and Memory-awareness

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 4</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658682)

**作者**：Antonios Katsarakis, Vasilis Gavrielatos, Nikos Ntarmos

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）

---

## 英文摘要

This paper presents DLHT, a concurrent in-memory hashtable. Despite efforts to optimize hashtables, that go as far as sacrificing core functionality, state-of-the-art designs still incur multiple memory accesses per request and block request processing in three cases. First, most hashtables block while waiting for data to be retrieved from memory. Second, open-addressing designs, which represent the current state-of-the-art, either cannot free index slots on deletes or must block all requests to do so. Third, index resizes block every request until all objects are copied to the new index. Defying folklore wisdom, DLHT forgoes open-addressing and adopts a fully-featured and memory-aware closed-addressing design based on bounded cache-line-chaining. This design offers 1 lock-free operations and deletes that free slots instantly, 2 completes most requests with a single memory access, 3 utilizes software prefetching to hide memory latencies, and 4 employs a novel non-blocking and parallel resizing. In a commodity server and a memory-resident workload, DLHT surpasses 1.6B requests per second and provides 3.5× (12×) the throughput of the state-of-the-art closed-addressing (open-addressing) resizable hashtable on Gets (Deletes).

## 中文摘要

本文提出 DLHT，一个并发内存哈希表。尽管为优化哈希表所做的努力甚至不惜牺牲核心功能，最先进的设计在每次请求时仍会产生多次内存访问，并在三种情况下阻塞请求处理。第一，大多数哈希表在等待从内存取回数据时阻塞。第二，代表当前最先进水平的开放寻址设计要么无法在删除时释放索引槽，要么必须阻塞所有请求才能释放。第三，索引扩容会在所有对象复制到新索引前阻塞每个请求。DLHT 一反常规认知，放弃开放寻址，采用基于有界缓存行链的、功能完备且内存感知的封闭寻址设计。该设计提供：1 无锁操作以及可即时释放槽位的删除；2 以单次内存访问完成大多数请求；3 利用软件预取隐藏内存延迟；4 采用新颖的非阻塞并行扩容。在商用服务器与内存驻留负载上，DLHT 每秒处理超过 16 亿次请求，在 Get（Delete）上吞吐分别达到最先进的封闭寻址（开放寻址）可扩容哈希表的 3.5 倍（12 倍）。

## 英文关键词

high throughput; in-memory; non-blocking; hastable; prefetching; consistency; memory-aware; deletes; resize; close-addressing

## 中文关键词

高吞吐；内存内；非阻塞；哈希表；预取；一致性；内存感知；删除；扩容；封闭寻址

---

[← 返回 Session 4 — Software Systems & Workflows](index.md)
