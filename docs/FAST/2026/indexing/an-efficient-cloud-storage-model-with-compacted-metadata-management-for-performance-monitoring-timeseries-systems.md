---
title: "An Efficient Cloud Storage Model with Compacted Metadata Management for Performance Monitoring Timeseries Systems"
description: "FAST 2026 · Indexing · 第 167–182 页"
tags:
  - "FAST2026"
  - "Indexing"
---

# An Efficient Cloud Storage Model with Compacted Metadata Management for Performance Monitoring Timeseries Systems

**中文标题**：面向性能监控时序系统的高效云存储模型与紧凑元数据管理

**Session**：Indexing · 2026-02-24 14:00–15:40 · Chair：Zhichao Cao（Arizona State University）

**作者**：Kai Zhang, The Chinese University of Hong Kong; Tianyu Wang, Shenzhen University; Zili Shao, The Chinese University of Hong Kong

**会议**：FAST 2026 · Santa Clara, CA · 第 167–182 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zhang-kai](https://www.usenix.org/conference/fast26/presentation/zhang-kai)

**论文 PDF**：[fast26-zhang-kai.pdf](https://www.usenix.org/system/files/fast26-zhang-kai.pdf)

---

## 英文摘要

Cloud-based performance monitoring timeseries systems are emerging due to their flexibility and pay-as-you-go capabilities. However, these systems encounter a major bottleneck in query performance, mainly attributed to the prolonged access latency of cloud storage and metadata redundancy of large number of timeseries. Thus, it is critical to optimize query performance within cloud environment and reduce metadata redundancy.

In this paper, we propose CloudTS, which is a novel timeseries data storage model with query optimization for cloud storage. CloudTS separately manages metadata and data, and introduces an efficient global metadata management for both space saving and query speedup. CloudTS also transparently supports the time-partitioned tag-based query model in performance monitoring timeseries systems. For metadata, a global tag dictionary is built to reduce metadata redundancy and a novel timeseries-tag mapping technique with a two-dimension bitmap is designed so the mapping of timeseries and tags can be efficiently accomplished to support tag-based queries. For data, the compressed data chunks are put into objects by timeseries group. We have implemented a fully functional prototype of CloudTS and evaluated it with production timeseries data and synthetic workloads based on Amazon S3. In comparison, Cortex, a cloud-based timeseries system widely adopted by industries, and Apache Parquet and JSON Time Series, two representative cloud storage formats, are utilized in the evaluation. Experimental results show that CloudTS can improve query performance by 1.37x on average compared with Cortex, and outperforms Apache Parquet and JSON Time Series as well.

## 中文摘要

基于云的性能监控时序系统因其灵活性和按需付费能力而不断涌现。然而，这类系统在查询性能上遇到重大瓶颈，主要归因于云存储的访问延迟较长以及大量时序数据的元数据冗余。因此，在云环境中优化查询性能并减少元数据冗余至关重要。

本文提出 CloudTS，一种面向云存储的新型时序数据存储模型，并带有查询优化。CloudTS 将元数据与数据分开管理，并引入高效的全局元数据管理，以同时节省空间和加速查询。CloudTS 还透明地支持性能监控时序系统中按时间分区的标签查询模型。在元数据方面，构建全局标签字典以减少元数据冗余，并设计一种基于二维位图的新型时序—标签映射技术，从而能够高效完成时序与标签的映射，以支持基于标签的查询。在数据方面，压缩后的数据块按时序组放入对象中。我们实现了 CloudTS 的完整功能原型，并使用生产时序数据和基于 Amazon S3 的合成负载对其进行了评估。在对比中，我们采用了 Cortex（一种被业界广泛采用的云时序系统）以及 Apache Parquet 和 JSON Time Series（两种具有代表性的云存储格式）进行评估。实验结果表明，与 Cortex 相比，CloudTS 平均可将查询性能提升 1.37 倍，并且优于 Apache Parquet 和 JSON Time Series。
