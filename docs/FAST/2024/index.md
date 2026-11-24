---
title: "FAST 2024 论文集"
description: "USENIX 文件与存储技术大会 FAST 2024，Santa Clara, CA"
tags:
  - "FAST2024"
  - "Storage Systems"
---

# FAST 2024

**FAST 2024** · 2024年2月27日 - 2月29日 · Santa Clara, CA

本目录按 [USENIX 官方技术议程](https://www.usenix.org/conference/fast24/technical-sessions)整理 **7 个主题、22 篇论文**。全文见 [FAST '24 论文集 PDF](https://www.usenix.org/system/files/fast24-full_proceedings.pdf)。

**论文演示文稿（Slides）**：可在 [FAST '24 官方主议程（Main Program）](https://www.usenix.org/conference/fast24/technical-sessions#tue)中找到对应论文，点击 Slides 图标或进入论文页面查看；是否提供以官方页面为准。

点击主题名称可查看该场次的论文目录；下方按主题列出论文的中英文标题。单篇论文页面包含作者、官方链接及中英文摘要。

## 主题导航

| 主题 | 中文主题 | 论文数 | Session Chair |
| --- | --- | ---: | --- |
| [Distributed Storage](distributed-storage/index.md) | 分布式存储 | 3 | Raju Rangaswami（Florida International University） |
| [Caching](caching/index.md) | 缓存 | 3 | Carl Waldspurger（Carl Waldspurger Consulting） |
| [File Systems](file-systems/index.md) | 文件系统 | 3 | Peter Macko（MongoDB） |
| [Flash Storage](flash-storage/index.md) | 闪存存储 | 3 | Jooyoung Hwang（Samsung Electronics） |
| [Key-Value Systems](key-value-systems/index.md) | 键值系统 | 4 | Angela Demke Brown（University of Toronto） |
| [Cloud Storage](cloud-storage/index.md) | 云存储 | 3 | Young-ri Choi（UNIST (Ulsan National Institute of Science and Technology)） |
| [AI and Storage](ai-and-storage/index.md) | 人工智能与存储 | 3 | Patrick P. C. Lee（The Chinese University of Hong Kong (CUHK)） |

**最佳论文**：We Ain't Afraid of No File Fragmentation、What's the Story in EBS Glory。

## Distributed Storage

| 英文标题 | 中文标题 |
| --- | --- |
| [TeRM: Extending RDMA-Attached Memory with SSD](distributed-storage/term-extending-rdma-attached-memory-with-ssd.md) | TeRM：用 SSD 扩展 RDMA 附加内存 |
| [Combining Buffered I/O and Direct I/O in Distributed File Systems](distributed-storage/combining-buffered-i-o-and-direct-i-o-in-distributed-file-systems.md) | 在分布式文件系统中结合缓冲 I/O 与直接 I/O |
| [OmniCache: Collaborative Caching for Near-storage Accelerators](distributed-storage/omnicache-collaborative-caching-for-near-storage-accelerators.md) | OmniCache：面向近存储加速器的协同缓存 |

## Caching

| 英文标题 | 中文标题 |
| --- | --- |
| [Symbiosis: The Art of Application and Kernel Cache Cooperation](caching/symbiosis-the-art-of-application-and-kernel-cache-cooperation.md) | Symbiosis：应用与内核缓存协作的艺术 |
| [Optimizing File Systems on Heterogeneous Memory by Integrating DRAM Cache with Virtual Memory Management](caching/optimizing-file-systems-on-heterogeneous-memory-by-integrating-dram-cache-with-virtual-memory-management.md) | 通过将 DRAM 缓存与虚拟内存管理集成来优化异构内存上的文件系统 |
| [Kosmo: Efficient Online Miss Ratio Curve Generation for Eviction Policy Evaluation](caching/kosmo-efficient-online-miss-ratio-curve-generation-for-eviction-policy-evaluation.md) | Kosmo：面向逐出策略评估的高效在线缺失率曲线生成 |

## File Systems

| 英文标题 | 中文标题 |
| --- | --- |
| [I/O Passthru: Upstreaming a flexible and efficient I/O Path in Linux](file-systems/i-o-passthru-upstreaming-a-flexible-and-efficient-i-o-path-in-linux.md) | I/O Passthru：向 Linux 上游贡献灵活高效的 I/O 路径 |
| [Metis: File System Model Checking via Versatile Input and State Exploration](file-systems/metis-file-system-model-checking-via-versatile-input-and-state-exploration.md) | Metis：通过多样化输入与状态探索进行文件系统模型检查 |
| [RFUSE: Modernizing Userspace Filesystem Framework through Scalable Kernel-Userspace Communication](file-systems/rfuse-modernizing-userspace-filesystem-framework-through-scalable-kernel-userspace-communication.md) | RFUSE：通过可扩展的内核—用户态通信实现用户态文件系统框架现代化 |

## Flash Storage

| 英文标题 | 中文标题 |
| --- | --- |
| [The Design and Implementation of a Capacity-Variant Storage System](flash-storage/the-design-and-implementation-of-a-capacity-variant-storage-system.md) | 容量可变存储系统的设计与实现 |
| [I/O in a Flash: Evolution of ONTAP to Low-Latency SSDs](flash-storage/i-o-in-a-flash-evolution-of-ontap-to-low-latency-ssds.md) | 闪存中的 I/O：ONTAP 向低延迟 SSD 的演进 |
| **最佳论文** · [We Ain't Afraid of No File Fragmentation: Causes and Prevention of Its Performance Impact on Modern Flash SSDs](flash-storage/we-aint-afraid-of-no-file-fragmentation-causes-and-prevention-of-its-performance-impact-on-modern-flash-ssds.md) | 我们不惧怕文件碎片化：现代闪存 SSD 上碎片化性能影响的原因与预防 |

## Key-Value Systems

| 英文标题 | 中文标题 |
| --- | --- |
| [In-Memory Key-Value Store Live Migration with NetMigrate](key-value-systems/in-memory-key-value-store-live-migration-with-netmigrate.md) | 使用 NetMigrate 的内存键值存储在线迁移 |
| [IONIA: High-Performance Replication for Modern Disk-based KV Stores](key-value-systems/ionia-high-performance-replication-for-modern-disk-based-kv-stores.md) | IONIA：面向现代基于磁盘的 KV 存储的高性能复制 |
| [Physical vs. Logical Indexing with IDEA: Inverted Deduplication-Aware Index](key-value-systems/physical-vs-logical-indexing-with-idea-inverted-deduplication-aware-index.md) | 基于 IDEA 的物理索引与逻辑索引：倒排去重感知索引 |
| [MIDAS: Minimizing Write Amplification in Log-Structured Systems through Adaptive Group Number and Size Configuration](key-value-systems/midas-minimizing-write-amplification-in-log-structured-systems-through-adaptive-group-number-and-size-configuration.md) | MIDAS：通过自适应组数量与大小配置最小化日志结构系统中的写放大 |

## Cloud Storage

| 英文标题 | 中文标题 |
| --- | --- |
| **最佳论文** · [What's the Story in EBS Glory: Evolutions and Lessons in Building Cloud Block Store](cloud-storage/whats-the-story-in-ebs-glory-evolutions-and-lessons-in-building-cloud-block-store.md) | EBS 荣耀背后的故事：构建云块存储的演进与经验 |
| [ELECT: Enabling Erasure Coding Tiering for LSM-tree-based Storage](cloud-storage/elect-enabling-erasure-coding-tiering-for-lsm-tree-based-storage.md) | ELECT：为基于 LSM-tree 的存储启用纠删码分层 |
| [MinFlow: High-performance and Cost-efficient Data Passing for I/O-intensive Stateful Serverless Analytics](cloud-storage/minflow-high-performance-and-cost-efficient-data-passing-for-i-o-intensive-stateful-serverless-analytics.md) | MinFlow：面向 I/O 密集型有状态无服务器分析的高性能低成本数据传递 |

## AI and Storage

| 英文标题 | 中文标题 |
| --- | --- |
| [COLE: A Column-based Learned Storage for Blockchain Systems](ai-and-storage/cole-a-column-based-learned-storage-for-blockchain-systems.md) | COLE：面向区块链系统的基于列的学习型存储 |
| [Baleen: ML Admission & Prefetching for Flash Caches](ai-and-storage/baleen-ml-admission-prefetching-for-flash-caches.md) | Baleen：面向闪存缓存的机器学习准入与预取 |
| [Seraph: Towards Scalable and Efficient Fully-external Graph Computation via On-demand Processing](ai-and-storage/seraph-towards-scalable-and-efficient-fully-external-graph-computation-via-on-demand-processing.md) | Seraph：通过按需处理实现可扩展且高效的全外存图计算 |
