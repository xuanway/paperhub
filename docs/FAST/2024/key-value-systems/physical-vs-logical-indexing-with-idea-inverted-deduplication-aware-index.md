---
title: "Physical vs. Logical Indexing with IDEA: Inverted Deduplication-Aware Index"
description: "FAST 2024 · Key-Value Systems · 第 243–258 页"
tags:
  - "FAST2024"
  - "Key-Value Systems"
---

# Physical vs. Logical Indexing with IDEA: Inverted Deduplication-Aware Index

**中文标题**：基于 IDEA 的物理索引与逻辑索引：倒排去重感知索引

**Session**：Key-Value Systems · 2024-02-28 14:00–15:40 · Chair：Angela Demke Brown（University of Toronto）

**作者**：Asaf Levi, Technion - Israel Institute of Technology; Philip Shilane, Dell Technologies; Sarai Sheinvald, Braude College of Engineering; Gala Yadgar, Technion - Israel Institute of Technology

**会议**：FAST 2024 · Santa Clara, CA · 第 243–258 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/levi](https://www.usenix.org/conference/fast24/presentation/levi)

**论文 PDF**：[fast24-levi.pdf](https://www.usenix.org/system/files/fast24-levi.pdf)

---

## 英文摘要

In the realm of information retrieval, the need to maintain reliable term-indexing has grown more acute in recent years, with vast amounts of ever-growing online data searched by a large number of search-engine users and used for data mining and natural language processing. At the same time, an increasing portion of primary storage systems employ data deduplication, where duplicate logical data chunks are replaced with references to a unique physical copy.

We show that indexing deduplicated data with deduplication-oblivious mechanisms might result in extreme inefficiencies: the index size would increase in proportion to the logical data size, regardless of its duplication ratio, consuming excessive storage and memory and slowing down lookups. In addition, the logically sequential accesses during index creation would be transformed into random and redundant accesses to the physical chunks. Indeed, to the best of our knowledge, term indexing is not supported by any deduplicating storage system.

In this paper, we propose the design of a deduplication-aware term-index that addresses these challenges. *IDEA* maps terms to the unique chunks that contain them, and maps each chunk to the files in which it is contained. This basic design concept improves the index performance and can support advanced functionalities such as inline indexing, result ranking, and proximity search. Our prototype implementation based on Lucene (the search engine at the core of Elasticsearch) shows that IDEA can reduce the index size and indexing time by up to 73% and 94%, respectively, and reduce term-lookup latency by up to 82% and 59% for single and multi-term queries, respectively.

## 中文摘要

在信息检索领域，近年来维护可靠词项索引的需求日益迫切：海量且不断增长的在线数据被大量搜索引擎用户检索，并用于数据挖掘和自然语言处理。与此同时，越来越多的主存储系统采用数据去重，即用指向唯一物理副本的引用来替代重复的逻辑数据块。

我们表明，使用对去重无感知的机制为去重数据建立索引可能导致极端低效：索引大小将随逻辑数据大小成比例增长，而与其重复率无关，从而消耗过多存储和内存并拖慢查找。此外，索引创建期间逻辑上顺序的访问会被转化为对物理块的随机且冗余的访问。事实上，据我们所知，目前没有任何去重存储系统支持词项索引。

本文提出一种去重感知词项索引的设计，以应对这些挑战。*IDEA* 将词项映射到包含它们的唯一块，并将每个块映射到包含它的文件。这一基本设计概念提升了索引性能，并可支持内联索引、结果排序和邻近搜索等高级功能。我们基于 Lucene（Elasticsearch 核心的搜索引擎）的原型实现表明，IDEA 可将索引大小和索引时间分别最多减少 73% 和 94%，并将单词项查询和多词项查询的查找延迟分别最多降低 82% 和 59%。
