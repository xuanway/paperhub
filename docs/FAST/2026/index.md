---
title: "FAST 2026 论文集"
description: "USENIX 文件与存储技术大会 FAST 2026，Santa Clara, CA"
tags:
  - "FAST2026"
  - "Storage Systems"
---

# FAST 2026

**FAST 2026** · 2026年2月24日 - 2月26日 · Santa Clara, CA

本目录按 [USENIX 官方技术议程](https://www.usenix.org/conference/fast26/technical-sessions)整理 **10 个主题、44 篇论文**。全文见 [FAST '26 论文集 PDF](https://www.usenix.org/system/files/fast26_full_proceedings.pdf)。

**论文演示文稿（Slides）**：可在 [FAST '26 官方主议程（Main Program）](https://www.usenix.org/conference/fast26/technical-sessions#tueam)中找到对应论文，点击 Slides 图标或进入论文页面查看；是否提供以官方页面为准。

点击主题名称可查看该场次的论文目录；下方按主题列出论文的中英文标题。单篇论文页面包含作者、官方链接及中英文摘要。

## 主题导航

| 主题 | 中文主题 | 论文数 | Session Chair |
| --- | --- | ---: | --- |
| [Cloud Technologies I](cloud-technologies-i/index.md) | 云技术 I | 4 | Ming Zhao（Arizona State University） |
| [AI and LLMs I](ai-and-llms-i/index.md) | 人工智能与大语言模型 I | 4 | Bingzhe Li（The University of Texas at Dallas） |
| [Indexing](indexing/index.md) | 索引 | 5 | Zhichao Cao（Arizona State University） |
| [AI and LLMs II](ai-and-llms-ii/index.md) | 人工智能与大语言模型 II | 5 | Jian Zhang（The Hong Kong University of Science and Technology） |
| [SSDs and CXL](ssds-and-cxl/index.md) | 固态硬盘与 CXL | 5 | Ethan Miller（University of California, Santa Cruz, and Pure Storage） |
| [Virtualization](virtualization/index.md) | 虚拟化 | 4 | Mai Zheng（Iowa State University） |
| [Cloud Technologies II](cloud-technologies-ii/index.md) | 云技术 II | 4 | Uday Kiran Jonnala（Dell Technologies） |
| [Tiering, Mobile, and SSDs](tiering-mobile-and-ssds/index.md) | 存储分层、移动设备与固态硬盘 | 5 | Vasily Tarasov（IBM Research） |
| [Integrity](integrity/index.md) | 数据完整性 | 4 | Gala Yadgar（Technion—Israel Institute of Technology） |
| [OS](os/index.md) | 操作系统 | 4 | Yu Liang（ETH Zurich） |

**最佳论文**：Here, There and Everywhere、SYSSPEC；**杰出工件奖**：DMTree、GPU Checkpoint/Restore、SYSSPEC。

## Cloud Technologies I

| 英文标题 | 中文标题 |
| --- | --- |
| **最佳论文** · [Here, There and Everywhere: The Past, the Present and the Future of Local Storage in Cloud](cloud-technologies-i/here-there-and-everywhere-the-past-the-present-and-the-future-of-local-storage-in-cloud.md) | 无处不在：云中本地存储的过去、现在与未来 |
| [Cost-efficient Archive Cloud Storage with Tape: Design and Deployment](cloud-technologies-i/cost-efficient-archive-cloud-storage-with-tape-design-and-deployment.md) | 基于磁带的高性价比归档云存储：设计与部署 |
| [Towards Condensed and Efficient Read-Only File System via Sort-Enhanced Compression](cloud-technologies-i/towards-condensed-and-efficient-read-only-file-system-via-sort-enhanced-compression.md) | 基于排序增强压缩的紧凑高效只读文件系统 |
| [ACOS: Apple’s Geo-Distributed Object Store at Exabyte Scale](cloud-technologies-i/acos-apples-geo-distributed-object-store-at-exabyte-scale.md) | ACOS：Apple 的 EB 级地理分布式对象存储 |

## AI and LLMs I

| 英文标题 | 中文标题 |
| --- | --- |
| [SolidAttention: Low-Latency SSD-based Serving on Memory-Constrained PCs](ai-and-llms-i/solidattention-low-latency-ssd-based-serving-on-memory-constrained-pcs.md) | SolidAttention：内存受限 PC 上的低延迟 SSD 服务 |
| [CacheSlide: Unlocking Cross Position-Aware KV Cache Reuse for Accelerating LLM Serving](ai-and-llms-i/cacheslide-unlocking-cross-position-aware-kv-cache-reuse-for-accelerating-llm-serving.md) | CacheSlide：解锁跨位置感知的 KV 缓存复用，加速 LLM 服务 |
| [Bidaw: Enhancing Key-Value Caching for Interactive LLM Serving via Bidirectional Computation–Storage Awareness](ai-and-llms-i/bidaw-enhancing-key-value-caching-for-interactive-llm-serving-via-bidirectional-computation-storage-awareness.md) | Bidaw：通过计算—存储双向感知增强交互式 LLM 服务的 KV 缓存 |
| [Accelerating Model Loading in LLM Inference by Programmable Page Cache](ai-and-llms-i/accelerating-model-loading-in-llm-inference-by-programmable-page-cache.md) | 利用可编程页缓存加速 LLM 推理中的模型加载 |

## Indexing

| 英文标题 | 中文标题 |
| --- | --- |
| [OdinANN: Direct Insert for Consistently Stable Performance in Billion-Scale Graph-Based Vector Search](indexing/odinann-direct-insert-for-consistently-stable-performance-in-billion-scale-graph-based-vector-search.md) | OdinANN：直接插入以实现十亿级图向量检索的一致稳定性能 |
| **杰出工件奖** · [DMTree: Towards Efficient Tree Indexing on Disaggregated Memory via Compute-side Collaborative Design](indexing/dmtree-towards-efficient-tree-indexing-on-disaggregated-memory-via-compute-side-collaborative-design.md) | DMTree：通过计算侧协同设计实现分离式内存上的高效树索引 |
| [An Efficient Cloud Storage Model with Compacted Metadata Management for Performance Monitoring Timeseries Systems](indexing/an-efficient-cloud-storage-model-with-compacted-metadata-management-for-performance-monitoring-timeseries-systems.md) | 面向性能监控时序系统的高效云存储模型与紧凑元数据管理 |
| ["Range as a Key" is the Key! Fast and Compact Cloud Block Store Index with RASK](indexing/range-as-a-key-is-the-key-fast-and-compact-cloud-block-store-index-with-rask.md) | “以范围为键”才是关键！基于 RASK 的快速紧凑云块存储索引 |
| [Holistic and Automated Task Scheduling for Distributed LSM-tree-based Storage](indexing/holistic-and-automated-task-scheduling-for-distributed-lsm-tree-based-storage.md) | 面向分布式 LSM-tree 存储的整体自动化任务调度 |

## AI and LLMs II

| 英文标题 | 中文标题 |
| --- | --- |
| [Preparation Meets Opportunity: Enhancing Data Preprocessing for ML Training With Seneca](ai-and-llms-ii/preparation-meets-opportunity-enhancing-data-preprocessing-for-ml-training-with-seneca.md) | 准备与机遇相遇：利用 Seneca 增强机器学习训练的数据预处理 |
| **杰出工件奖** · [GPU Checkpoint/Restore Made Fast and Lightweight](ai-and-llms-ii/gpu-checkpoint-restore-made-fast-and-lightweight.md) | 快速轻量的 GPU 检查点/恢复 |
| [Fast Cloud Storage for AI Jobs via Grouped I/O API with Transparent Read/Write Optimizations](ai-and-llms-ii/fast-cloud-storage-for-ai-jobs-via-grouped-i-o-api-with-transparent-read-write-optimizations.md) | 通过分组 I/O API 与透明读写优化为 AI 作业提供快速云存储 |
| [AdaCheck: An Adaptive Checkpointing System for Efficient LLM Training with Redundancy Utilization](ai-and-llms-ii/adacheck-an-adaptive-checkpointing-system-for-efficient-llm-training-with-redundancy-utilization.md) | AdaCheck：利用冗余实现高效 LLM 训练的自适应检查点系统 |
| **最佳论文**、**杰出工件奖** · [Sharpen the Spec, Cut the Code: A Case for Generative File System with SYSSPEC](ai-and-llms-ii/sharpen-the-spec-cut-the-code-a-case-for-generative-file-system-with-sysspec.md) | 磨利规范，精简代码：论基于 SYSSPEC 的生成式文件系统 |

## SSDs and CXL

| 英文标题 | 中文标题 |
| --- | --- |
| [Cylon: Fast and Accurate Full-System Emulation of CXL-SSDs](ssds-and-cxl/cylon-fast-and-accurate-full-system-emulation-of-cxl-ssds.md) | Cylon：快速准确的全系统 CXL-SSD 仿真 |
| [Xerxes: Extensive Exploration of Scalable Hardware Systems with CXL-Based Simulation Framework](ssds-and-cxl/xerxes-extensive-exploration-of-scalable-hardware-systems-with-cxl-based-simulation-framework.md) | Xerxes：利用基于 CXL 的仿真框架广泛探索可扩展硬件系统 |
| [Characterizing and Emulating FDP SSDs with WARP](ssds-and-cxl/characterizing-and-emulating-fdp-ssds-with-warp.md) | 基于 WARP 的 FDP SSD 表征与仿真 |
| [ScaleSwap: A Scalable OS Swap System for All-Flash Swap Arrays](ssds-and-cxl/scaleswap-a-scalable-os-swap-system-for-all-flash-swap-arrays.md) | ScaleSwap：面向全闪存交换阵列的可扩展操作系统交换系统 |
| [DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs](ssds-and-cxl/dpas-a-prompt-accurate-and-safe-i-o-completion-method-for-ssds.md) | DPAS：一种及时、准确且安全的 SSD I/O 完成方法 |

## Virtualization

| 英文标题 | 中文标题 |
| --- | --- |
| [How Soon is Now? Preloading Images for Virtual Disks with ThinkAhead](virtualization/how-soon-is-now-preloading-images-for-virtual-disks-with-thinkahead.md) | 还要等多久？利用 ThinkAhead 为虚拟磁盘预加载镜像 |
| [CoFS: A Filesystem for Fast Container Startup](virtualization/cofs-a-filesystem-for-fast-container-startup.md) | CoFS：面向快速容器启动的文件系统 |
| [RosenBridge: A Framework for Enabling Express I/O Paths Across the Virtualization Boundary](virtualization/rosenbridge-a-framework-for-enabling-express-i-o-paths-across-the-virtualization-boundary.md) | RosenBridge：跨越虚拟化边界启用快速 I/O 路径的框架 |
| [MlsDisk: Trusted Block Storage for TEEs Based on Layered Secure Logging](virtualization/mlsdisk-trusted-block-storage-for-tees-based-on-layered-secure-logging.md) | MlsDisk：基于分层安全日志的 TEE 可信块存储 |

## Cloud Technologies II

| 英文标题 | 中文标题 |
| --- | --- |
| [SkySync: Accelerating File Synchronization with Collaborative Delta Generation](cloud-technologies-ii/skysync-accelerating-file-synchronization-with-collaborative-delta-generation.md) | SkySync：通过协同增量生成加速文件同步 |
| [ParaSync: Exploiting Fine-Grained Parallelism for Efficient File Synchronization](cloud-technologies-ii/parasync-exploiting-fine-grained-parallelism-for-efficient-file-synchronization.md) | ParaSync：利用细粒度并行实现高效文件同步 |
| [Discard-Based Garbage Collection for Distributed Log-Structured Storage Systems in ByteDance](cloud-technologies-ii/discard-based-garbage-collection-for-distributed-log-structured-storage-systems-in-bytedance.md) | 字节跳动分布式日志结构存储系统中基于 Discard 的垃圾回收 |
| [PolarStore: High-Performance Data Compression for Large-Scale Cloud-Native Databases](cloud-technologies-ii/polarstore-high-performance-data-compression-for-large-scale-cloud-native-databases.md) | PolarStore：面向大规模云原生数据库的高性能数据压缩 |

## Tiering, Mobile, and SSDs

| 英文标题 | 中文标题 |
| --- | --- |
| [Unleashing Zoned UFS: Cross-Layer Optimizations for Next-Generation Mobile Storage](tiering-mobile-and-ssds/unleashing-zoned-ufs-cross-layer-optimizations-for-next-generation-mobile-storage.md) | 释放分区 UFS 的潜力：面向下一代移动存储的跨层优化 |
| [DOGI: Data Placement with Oracle-Guided Insights for Log-Structured Systems](tiering-mobile-and-ssds/dogi-data-placement-with-oracle-guided-insights-for-log-structured-systems.md) | DOGI：基于 Oracle 指导洞见的日志结构系统数据放置 |
| [Getting the MOST out of your Storage Hierarchy with Mirror-Optimized Storage Tiering](tiering-mobile-and-ssds/getting-the-most-out-of-your-storage-hierarchy-with-mirror-optimized-storage-tiering.md) | 借助镜像优化分层（MOST）充分利用存储层次结构 |
| [Rearchitecting Buffered I/O in the Era of High-Bandwidth SSDs](tiering-mobile-and-ssds/rearchitecting-buffered-i-o-in-the-era-of-high-bandwidth-ssds.md) | 高带宽 SSD 时代下缓冲 I/O 的重新架构 |
| [FailureMiner: A Joint Key Decision Mining Scheme for Practical SSD Failure Prediction and Analysis](tiering-mobile-and-ssds/failureminer-a-joint-key-decision-mining-scheme-for-practical-ssd-failure-prediction-and-analysis.md) | FailureMiner：面向实用 SSD 故障预测与分析的联合关键决策挖掘方案 |

## Integrity

| 英文标题 | 中文标题 |
| --- | --- |
| [DRBoost: Boosting Degraded Read Performance in MSR-Coded Storage Clusters](integrity/drboost-boosting-degraded-read-performance-in-msr-coded-storage-clusters.md) | DRBoost：提升 MSR 编码存储集群的降级读性能 |
| [LESS is More for I/O-Efficient Repairs in Erasure-Coded Storage](integrity/less-is-more-for-i-o-efficient-repairs-in-erasure-coded-storage.md) | LESS：面向纠删码存储 I/O 高效修复的少即是多方案 |
| [Advancing Data Integrity in Linux](integrity/advancing-data-integrity-in-linux.md) | 提升 Linux 中的数据完整性 |
| [CETOFS: A High-Performance File System with Host-Server Collaboration for Remote Storage](integrity/cetofs-a-high-performance-file-system-with-host-server-collaboration-for-remote-storage.md) | CETOFS：面向远程存储、主机—服务器协同的高性能文件系统 |

## OS

| 英文标题 | 中文标题 |
| --- | --- |
| [Cache-Centric Multi-Resource Allocation for Storage Services](os/cache-centric-multi-resource-allocation-for-storage-services.md) | 面向存储服务的以缓存为中心的多资源分配 |
| [Lockify: Understanding Linux Distributed Lock Management Overheads in Shared Storage](os/lockify-understanding-linux-distributed-lock-management-overheads-in-shared-storage.md) | Lockify：理解共享存储中 Linux 分布式锁管理的开销 |
| [uCache: A Customizable Unikernel-based IO Cache](os/ucache-a-customizable-unikernel-based-io-cache.md) | uCache：可定制的基于 Unikernel 的 IO 缓存 |
| [UnICom: A Universally High-Performant I/O Completion Mechanism for Modern Computer Systems](os/unicom-a-universally-high-performant-i-o-completion-mechanism-for-modern-computer-systems.md) | UnICom：面向现代计算机系统的通用高性能 I/O 完成机制 |
