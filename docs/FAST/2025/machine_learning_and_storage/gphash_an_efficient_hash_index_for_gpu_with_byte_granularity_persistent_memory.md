---
title: "GPHash: An Efficient Hash Index for GPU with Byte-Granularity Persistent Memory"
description: "FAST 2025 · Machine Learning and Storage · GPU 直连持久内存上的无锁哈希索引，吞吐最高提升 27.62 倍"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
  - "persistent memory"
  - "GPU"
---

# GPHash: An Efficient Hash Index for GPU with Byte-Granularity Persistent Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">GPM 让 GPU 按字节直接读写持久内存，但 warp 无感知执行、日志式一致性开销与 900 GB/s 对 39.6 GB/s 的带宽差使哈希索引低效。GPHash 以 warp 协作的桶访问、CAS 加槽位状态与冻结式桶缓存应对，吞吐最高提升 27.62 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Machine Learning and Storage</p>
</div>

**中文标题**：GPHash：面向字节粒度持久内存 GPU 的高效哈希索引

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/chen-menglei](https://www.usenix.org/conference/fast25/presentation/chen-menglei)

**论文 PDF**：[fast25-chen-menglei.pdf](https://www.usenix.org/system/files/fast25-chen-menglei.pdf)

**作者**：Menglei Chen、Yu Hua、Zhangyu Chen、Ming Zhang、Gen Dong（Wuhan National Laboratory for Optoelectronics, School of Computer, Huazhong University of Science and Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 203–220 页

**Session**：Machine Learning and Storage · 2025-02-25 15:50–17:30 · Chair：Kan Wu（Google）

**所属 Session**：[Machine Learning and Storage](index.md) · [FAST 2025](../index.md)

**关键词**：persistent memory, GPU, hash index, crash consistency, warp-cooperative execution, bucket cache

---

## 英文摘要

GPU with persistent memory (GPM) enables GPU-powered applications to directly manage the data in persistent memory at the byte granularity. Hash indexes have been widely used to achieve efficient data management. However, conventional hash indexes become inefficient for GPM systems due to warp-agnostic execution manner, high-overhead consistency guarantee, and significant bandwidth gap between PM and GPU. In this paper, we propose GPHash, an efficient hash index for GPM systems with high performance and consistency guarantee. To fully exploit the parallelism of GPU, GPHash executes all index operations in a lock-free and warp-cooperative manner. Moreover, by using CAS primitive and slot states, GPHash ensures consistency guarantee with low overhead. To further bridge the bandwidth gap between PM and GPU, GPHash caches hot items in GPU memory while minimizing the overhead for cache management. Extensive evaluations on YCSB and real-world workloads show that GPHash outperforms state-of-the-art CPU-assisted data management approaches and GPM hash indexes by up to 27.62×.

## 中文摘要

GPU 直连持久内存（GPM）让 GPU 应用能以字节粒度直接管理持久内存中的数据，哈希索引是常用的高效数据管理手段。但传统哈希索引在 GPM 上效率低下：执行方式对 warp 无感知、一致性保障开销高、持久内存与 GPU 之间带宽差距显著。

GPHash 是兼顾性能与崩溃一致性的 GPM 哈希索引：让所有索引操作以无锁且 warp 协作的方式执行，借助 CAS 原语与槽位状态以低开销保证一致性，并在显存中缓存热数据、压低缓存管理开销以填补带宽鸿沟。在 YCSB 与真实负载上的评估显示，GPHash 相比最先进的 CPU 辅助数据管理方案与 GPM 哈希索引最高提升 27.62 倍。

## 一句话总结

> 把一次哈希操作交给整个 warp 协作完成、用 CAS 加槽位状态代替日志、再以冻结式桶缓存挡住 PM 带宽瓶颈。

## 研究背景与问题

- **数据规模超出显存**：GPU 应用的数据量持续膨胀，深度推荐系统的 embedding 向量将达数十 TB，而显存容量有限且易失，应用只能把数据放到大容量持久存储上并依赖 CPU 管理。
- **CPU 辅助路径代价高**：GPU 与 CPU 之间的数据搬运耗时，还额外消耗 CPU 并干扰其他 CPU 应用；GPUDirect Storage 虽建立了直达数据通路，却只提供块级接口，与哈希索引需要的字节粒度访问不匹配。
- **GPM 可用但缺少配套索引**：GPM 借助统一虚拟地址把 PM 映射进 GPU 地址空间，让 GPU 内核按字节直接访问 PM；但现有 PM 哈希索引对 GPU 体系结构无感知，现有 GPU 哈希表又面向易失显存、不保证崩溃一致性。
- **三个具体障碍**：线程各自为战的执行方式带来严重 warp 分歧与非合并访存；PM 原子写宽度受内存总线限制（64 位系统为 8 字节），超出部分的写可能只完成一半，而日志与写时复制又带来额外写放大；GPU 显存读带宽可达 900 GB/s，6 块 Intel Optane DC PMM 的读带宽仅 39.6 GB/s。

## 核心贡献

- **GPU 意识与 PM 友好的哈希表结构**：用 warp 内 32 个线程一次性并发访问桶实现 one-shot warp access，把 key 直接放进槽位以获得合并访存，并用槽位相联、层间共享与多哈希位置提升内存效率。
- **无锁且无日志的并发控制与一致性**：索引操作以 warp 协作方式通过 warp 级指令执行，用 compare-and-swap 原语加槽位状态（标识槽位是否正在插入）实现 log-free 操作，省掉日志带来的额外 PM 写。
- **冻结式桶缓存 BktCache**：以桶为粒度缓存热数据，周期性识别并加载热桶（loading 阶段），两个 loading 阶段之间缓存成员保持不变（frozen 阶段），并用并发加载方案压低缓存管理开销。
- **实现与评估**：开源实现并在 YCSB 与真实负载上评估，同时论证只要 GPM 系统能让 GPU 内核以 load/store 指令直接访问 PM，GPHash 同样适用于基于 CXL 的 GPM 系统。

## 方法与技术要点

- **持久化前提**：GPM 通过统一虚拟地址映射、system-scoped 的 threadfence 排序、关闭 DDIO 绕过 LLC 来保证持久性，GPHash 在这一层之上构建索引。
- **warp 协作执行**：把一次索引操作交给整个 warp 协作完成，减少分支造成的 warp 分歧，并让 32 个线程的访存尽量落在同一条 128 字节 cache line 上以便硬件合并。
- **无日志提交**：插入时先用槽位状态标记该槽位正在被插入，再用 CAS 完成提交；崩溃后依据槽位状态判断是否存在部分更新，无需重放日志。
- **缓存粒度选择**：BktCache 以桶（默认 384 字节）为单位驻留显存，用 LFU 计数（每桶仅 4 字节）挑选热桶，成员在 frozen 阶段固定，避免大量线程并发增删链表造成的争用。
- **字节粒度收益**：PM 的字节可寻址性让索引可以在 PM 上原地更新，不必像块设备那样做整块搬运，这也是 GPM 相对 CPU 辅助方案的根本优势。

## 评估与主要结果

- **总体提升**：在 YCSB 与真实负载上，GPHash 相比最先进的 CPU 辅助数据管理方案最高提升 27.62 倍，相比 GPM 哈希索引最高提升 17.42 倍。
- **调整与恢复**：resizing 时间随桶数从 4.3 ms 增加到 667.7 ms，恢复时间与 Clevel、Dash、SEPH 等索引对比（图 14）。
- **缓存加载开销**：在 5% 与 20% 两种数据规模下比较 BktCache 的并发加载与对照方案，给出吞吐、耗时与 stall 的变化（图 15）。
- **空间开销**：LFU 的每桶计数器只占 4 字节，相对 384 字节的默认桶大小可忽略，说明缓存管理本身不引入显著内存代价。

## 代码与研究制品

- [代码仓库](https://github.com/LighT-chenml/GPHash)

[返回 Machine Learning and Storage](index.md) · [返回 FAST 2025](../index.md)
