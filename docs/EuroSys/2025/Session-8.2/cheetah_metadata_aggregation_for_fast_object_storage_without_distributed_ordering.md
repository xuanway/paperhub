---
title: "Cheetah: Metadata Aggregation for Fast Object Storage without Distributed Ordering"
description: "EuroSys 2025 · Storage · Yiming Zhang (SJTU & XMU), Li Wang (KylinSoft), Shengyun Liu (SJTU), Shun Gai (N"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Cheetah: Metadata Aggregation for Fast Object Storage without Distributed Ordering

**中文标题：** 无需分布式排序的快速对象存储元数据聚合

**所属 Session：** [Session 8.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Yiming Zhang (SJTU & XMU), Li Wang (KylinSoft), Shengyun Liu (SJTU), Shun Gai (NICE XLAB), Haonan Wang (NICE XLAB), Xin Yao (Huawei Theory Lab), Meiling Wang (Huawei Theory Lab), Kai Chen (HKUST), Dongsheng Li (NUDT), Jiwu Shu (Tsinghua University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696080)

## 英文摘要

Object stores usually maintain the mapping of objects to data servers’ disk volumes (referred to as volume metadata) in a central directory, while storing the object data’s in-volume offsets (referred to as offset metadata) together with the data on data servers. Unfortunately, the separation between volume/offset metadata complicates the processing of an object put: to ensure consistency, the multiple writes of the object’s volume/offset metadata and object data have to be orchestrated in a particular order, which severely lowers object I/O performance. We propose a write-optimal structure called MetaX that aggregates all metadata of a put, including both volume and offset metadata as well as other meta information such as data checksum and temporary meta-log. Based on MetaX, we design the Cheetah object store, which organizes object storage into rich metadata storage (on meta servers) and raw data storage (on data servers). Cheetah removes the distributed ordering constraint on the multiple metadata/data writes by enforcing local atomicity of writing MetaX, while still ensuring consistency. Evaluation shows that Cheetah significantly outperforms existing object stores.

## 中文摘要

对象存储通常将对象到数据服务器磁盘卷的映射（称为卷元数据）保存在中心目录中，而将对象数据的卷内偏移（称为偏移元数据）与数据一起存放在数据服务器上。遗憾的是，卷元数据与偏移元数据的分离使对象写入的处理变得复杂：为保证一致性，对象卷/偏移元数据与对象数据的多次写入必须按特定顺序编排，这严重降低了对象 I/O 性能。我们提出一种写最优的结构 MetaX，它将一次写入的所有元数据聚合在一起，包括卷元数据和偏移元数据，以及数据校验和、临时元日志等其他元信息。基于 MetaX，我们设计了 Cheetah 对象存储，它将对象存储组织为富元数据存储（位于元数据服务器）和原始数据存储（位于数据服务器）。Cheetah 通过强制写入 MetaX 的本地原子性，消除了对多次元数据/数据写入的分布式顺序约束，同时仍保证一致性。评估表明 Cheetah 显著优于现有对象存储。

**英文关键词：** Metadata aggregation, object storage, ordering

**中文关键词：** 元数据聚合、对象存储、排序

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
