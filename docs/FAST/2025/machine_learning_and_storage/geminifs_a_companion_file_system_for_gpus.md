---
title: "GeminiFS: A Companion File System for GPUs"
description: "FAST 2025 · Machine Learning and Storage · GPU 绕过 CPU 按文件直读 NVMe 的伴生文件系统，训练卸载耗时降 94.5%"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
  - "GPU-centric storage"
  - "companion file system"
---

# GeminiFS: A Companion File System for GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">GPU 中心存储绕开 CPU 却丢掉了文件抽象，GNN、LLM 训练因此缺少隔离、共享与崩溃一致性。GeminiFS 与宿主文件系统伴生，靠嵌入文件的元数据、CPU/GPU 并行控制平面与软件定义页缓存按文件直读 NVMe，卸载激活的训练耗时比 GDS 低 91%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Machine Learning and Storage</p>
</div>

**中文标题**：GeminiFS：面向 GPU 的伴生文件系统

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/qiu](https://www.usenix.org/conference/fast25/presentation/qiu)

**论文 PDF**：[fast25-qiu.pdf](https://www.usenix.org/system/files/fast25-qiu.pdf)

**作者**：Shi Qiu、Weinan Liu、Yifan Hu、Jianqin Yan、Zhirong Shen（NICE Lab, Xiamen University）；Xin Yao、Renhai Chen、Gong Zhang（Huawei Theory Lab）；Yiming Zhang（NICE Lab, Xiamen University and Shanghai Jiao Tong University）

**会议**：FAST 2025 · Santa Clara, CA · 第 221–236 页

**Session**：Machine Learning and Storage · 2025-02-25 15:50–17:30 · Chair：Kan Wu（Google）

**所属 Session**：[Machine Learning and Storage](index.md) · [FAST 2025](../index.md)

**关键词**：GPU-centric storage, companion file system, NVMe, metadata synchronization, page cache, libGemini

---

## 英文摘要

GPU-centric storage solutions enable direct access from the GPU to the storage device via NVMe queues, completely bypassing the CPU. These solutions alleviate the problems of previous CPU-centric solutions that relied on the host CPU to initiate data storage access, such as high CPU-GPU synchronization overheads, I/O traffic amplification, and high CPU processing latency. However, the state-of-the-art GPU-centric solutions have no file abstraction or management functionalities (e.g., fine-grained isolation and access control) of traditional host file systems, and cannot satisfy the needs of GPU-accelerated machine learning (ML) applications like GNN and LLM which require fast file access and data sharing. Therefore, existing GPU-centric storage solutions are inefficient and inconvenient when being applied in practical ML scenarios.

This paper presents a companion file system (called GeminiFS) for GPUs. GeminiFS offers a file system interface to GPU programs that enables direct file-based access to NVMe storage, which is managed by the host file system. GeminiFS realizes metadata synchronization between the host and GPU file systems by embedding the metadata directly into the files. We extend the existing NVMe driver to allow the CPU and the GPU to set up their control planes in parallel for the storage device. Moreover, GeminiFS provides a GPU-friendly, software-defined page cache to fully utilize the internal bandwidth of the GPU. We further offer a convenient library (libGemini) tailored for GPU programmers, which abstracts away various underlying complexities thereby reducing programming complexity. Extensive evaluation shows that GeminiFS significantly outperforms the state-of-the-art storage solutions for large-scale ML workloads.

## 中文摘要

GPU 中心方案通过 NVMe 队列让 GPU 直接访问存储、绕开 CPU，缓解了 CPU 中心方案的同步开销、I/O 流量放大与处理延迟。但这类方案没有传统宿主文件系统的文件抽象与管理功能（如细粒度隔离与访问控制），无法满足 GNN、LLM 等 GPU 加速应用对快速文件访问与数据共享的需求。

GeminiFS 是为 GPU 设计的伴生文件系统：向 GPU 程序提供文件接口，使其能直接按文件访问宿主文件系统管理的 NVMe 存储；把元数据嵌入文件实现两侧文件系统的元数据同步；扩展 NVMe 驱动使 CPU 与 GPU 可并行建立控制平面；并提供 GPU 友好的软件定义页缓存。配套的 libGemini 库降低编程复杂度。大规模 ML 负载上它显著优于现有存储方案。

## 一句话总结

> 不另造通用 GPU 文件系统，而是让 GPU 侧的文件系统与宿主文件系统伴生，元数据随文件走、控制平面两侧并行。

## 研究背景与问题

- **显存缺口持续扩大**：GNN 与 LLM 的数据集和权重可达数十 TB 且仍在增长，用主机 DRAM 或多卡显存池做扩展在可预见期内都很昂贵，把 GPU 的触角延伸到存储更具性价比。
- **CPU 中心路径成为瓶颈**：Dragon、GDS 等方案依赖 CPU 显式发起或经 GPU 缺页隐式触发访问，在成百上千 GPU 线程并发读写时 CPU 与 CPU-GPU 同步成为瓶颈；GDS 还只提供非 POSIX 接口，其 cuFileBatchIOSubmit 一次最多处理 128 个操作。
- **GPU 中心方案缺少文件语义**：BaM 等把 NVMe 队列放进显存、由 GPU 线程直接下发 I/O，但没有文件抽象与管理功能，缺少数据与元数据完整性、崩溃一致性、持久性以及跨 GPU 设备管理存储资源的能力，访问宿主文件系统管理的文件仍要 CPU-GPU 拷贝。
- **通用 GPU 文件系统难以落地**：GPU 天生不适合运行需要复杂元数据维护的存储软件，直接照搬宿主文件系统结构不现实。

## 核心贡献

- **伴生文件系统定位**：与宿主文件系统共存，主机侧继续负责文件的创建、移动与删除，GPU 侧把元数据取到显存后向 GPU 程序提供文件系统抽象，既保留隔离与访问控制，又免去 CPU 发起 I/O。
- **GVDK 文件格式**：把文件大小、类型、偏移以及文件逻辑块到 NVMe 物理块的映射直接嵌入文件，据此实现 CPU/GPU 两侧文件系统的元数据同步，并支撑 GPU 程序所需的文件操作。
- **扩展 NVMe 驱动**：允许 CPU 与 GPU 并行建立各自的存储控制平面，共享驱动在两侧都保有 I/O 队列，使主机与 GPU 文件系统能并发向设备提交 NVMe 请求。
- **软件定义页缓存与 libGemini**：提供 GPU 友好的页缓存架构与灵活 API，可被多个 GPU 进程共享以降低显存占用；libGemini 封装元数据获取、同步、NVMe 队列控制与主机侧初始化等细节。

## 方法与技术要点

- **利用负载特征简化设计**：GPU 的存储 I/O 具有可预测性，访问信息可由模型设置提前得出；磁盘上多数数据生命周期内只读、写入只通过追加完成，因此元数据同样可预测且稳定。
- **元数据随文件走**：GVDK 让元数据内嵌于文件，GPU 侧高效取回并支持面向 GPU 存储访问的高并发文件操作，同时在同步过程中处理崩溃一致性与并发控制。
- **控制平面并行**：扩展后的驱动让 CPU 与 GPU 同时持有 I/O 队列，GPU 线程可直接向 NVMe 设备提交命令，从而缩短控制与数据通路。
- **页缓存设计**：软件定义的 GPU 页缓存利用可预测访问做局部性优化并控制数据放置，在多个 GPU 进程间共享以降低显存占用。
- **可编程性**：libGemini 把跨 CPU/GPU 的底层差异封装成简单抽象，系统已在近期发布的 GPU 上实现，关键组件已开源。

## 评估与主要结果

- **激活留在显存的训练**：GPT2-124M 训练（batch size 64，跑 3 步、每步写一次 checkpoint，页缓存 2 GB）下，GeminiFS 的系统总运行时间相比 native（memcpy 加 read/write）、DLRover-RM 与 GDS 分别下降 25%、12% 与 10%；checkpoint 写时间分别下降 85%、75% 与 59%。
- **卸载激活的训练**：把激活卸载到存储时，GeminiFS 的训练时间相比 native 与 GDS 分别下降 94.5% 与 91%；相比把所有激活都留在显存，训练时间只增加约 4 倍。
- **访问画像**：表 3 给出该训练负载的存储访问特征——模型权重 238 MB 读写、checkpoint 每步 713 MB 追加顺序写、激活 57.96 GB 读写，其中激活卸载产生大量小 I/O，正是 CPU 中心方案的软肋。
- **定性结论**：在 GPT2-124M 训练与大规模 ML 负载上，GeminiFS 显著优于 GDS、DLRover-RM 与 native 方案，说明绕过 CPU 与共享页缓存对 checkpoint 与激活卸载都有效。

[返回 Machine Learning and Storage](index.md) · [返回 FAST 2025](../index.md)
