---
title: "AegonKV: A High Bandwidth, Low Tail Latency, and Low Storage Cost KV-Separated LSM Store with SmartSSD-based GC Offloading"
description: "FAST 2025 · Hardware Assist · 把 KV 分离的 GC 卸载到 SmartSSD，吞吐最高 3.3 倍、尾延迟降 66%"
tags:
  - "FAST2025"
  - "Hardware Assist"
  - "KV separation"
  - "LSM-tree"
---

# AegonKV: A High Bandwidth, Low Tail Latency, and Low Storage Cost KV-Separated LSM Store with SmartSSD-based GC Offloading

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">KV 分离压住了 LSM 写放大，但 Value 区 GC 要与前台读写争抢主机 CPU 与带宽，现有方案只能在三者间折中。AegonKV 把 GC 搬进 SmartSSD 的 FPGA，吞吐提升 1.28-3.3 倍、尾延迟降低 37%-66%、空间开销降低 15%-85%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Hardware Assist</p>
</div>

**中文标题**：AegonKV：基于 SmartSSD GC 卸载的高带宽、低尾延迟、低存储成本 KV 分离 LSM 存储

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/duan](https://www.usenix.org/conference/fast25/presentation/duan)

**论文 PDF**：[fast25-duan.pdf](https://www.usenix.org/system/files/fast25-duan.pdf)

**作者**：Zhuohui Duan、Hao Feng、Haikun Liu、Xiaofei Liao、Hai Jin、Bangyu Li（Huazhong University of Science and Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 321–335 页

**Session**：Hardware Assist · 2025-02-26 10:50–12:30 · Chair：Kiran Kumar Muniswamy Reddy（Amazon）

**所属 Session**：[Hardware Assist](index.md) · [FAST 2025](../index.md)

**关键词**：KV separation, LSM-tree, garbage collection, SmartSSD, near-data processing, tail latency

---

## 英文摘要

The key-value separation is renowned for its significant mitigation of the write amplification inherent in traditional LSM trees. However, KV separation potentially increases performance overhead in the management of Value region, especially for garbage collection (GC) operation that is used to reduce the redundant space occupation. In response, many efforts have been made to optimize the GC mechanism for KV separation. However, our analysis indicates that such solution based on trade-offs between CPU and I/O overheads cannot simultaneously satisfy the three requirements of KV separated systems in terms of throughput, tail latency, and space usage. This limitation hinders their real-world application.

In this paper, we introduce AegonKV, a “three-birds-one-stone” solution that comprehensively enhances the throughput, tail latency, and space usage of KV separated systems. AegonKV first proposes a SmartSSD-based GC offloading mechanism to enable asynchronous GC operations without competing with LSM read/write for bandwidth or CPU. AegonKV leverages offload-friendly data structures and hardware/software execution logic to address the challenges of GC offloading. Experiments demonstrate that AegonKV achieves the largest throughput improvement of 1.28-3.3 times, a significant reduction of 37%-66% in tail latency, and 15%-85% in space overhead compared to existing KV separated systems.

## 中文摘要

键值分离因能显著缓解传统 LSM 树固有的写放大而广受关注。然而，键值分离可能增加 Value 区管理的性能开销，尤其是用于减少冗余空间占用的垃圾回收（GC）操作。为此，已有许多工作优化键值分离的 GC 机制。但本文分析表明，这类在 CPU 与 I/O 开销之间取折中的方案，无法同时满足键值分离系统在吞吐、尾延迟与空间占用三方面的要求；这一局限阻碍了它们的实际应用。本文提出 AegonKV，一种“一石三鸟”的方案，全面提升键值分离系统的吞吐、尾延迟与空间占用。AegonKV 首先提出基于 SmartSSD 的 GC 卸载机制，使异步 GC 不与 LSM 读写争抢带宽或 CPU。AegonKV 利用面向卸载的数据结构与软硬件执行逻辑，解决 GC 卸载的挑战。实验表明，相比现有键值分离系统，AegonKV 取得最大 1.28–3.3 倍的吞吐提升、37%–66% 的尾延迟降低与 15%–85% 的空间开销降低。

## 一句话总结

> GC 本来就不该和前台读写抢带宽：把它整条流水线放进 SSD 的 FPGA，让吞吐、尾延迟、空间同时变好而不是互相交换。

## 研究背景与问题

- **KV 分离的收益与遗留问题**：把 value 从 LSM 里剥出来放进 vLog（Blob 文件），SSTable 只保留 key 与 value 地址，compaction 不再搬动无关的大 value，LSM 体积大幅缩小、写放大显著下降。
- **Value 区必须自己做 GC**：Blob 文件是日志结构，过期数据会不断堆积。direct GC 要扫描整个 Blob 文件，并在每个偏移处回查 LSM 判断该 value 是否仍然有效，这条路径既要额外 I/O 又要 LSM 侧的计算。
- **现有方案只是换折中位置**：DiffKV、BlobDB 等把单层 Blob 改造成多层 LSM，用 compaction 触发 GC 以减少回查与回写，代价是把开销转嫁给 compaction；基于 CPU/I/O 开销折中的各种设计无法同时满足吞吐、尾延迟、空间三项要求。
- **折中的后果**：缺少结构化调度会让吞吐间歇性受挫，而牺牲 GC 及时性或准确性换取性能，则会让冗余空间指数增长，或让 compaction 开销与写停顿显著上升。

## 核心贡献

- **SmartSSD 卸载 GC 的机制**：首次提出把 KV 分离系统的 GC 整体卸载到带 FPGA 的 SmartSSD 上，使 GC 的 I/O 走设备内部带宽、计算走设备内流水线，不再与 LSM 读写争抢主机资源。
- **FPGA 侧的 GC 流水线**：在设备内实现由 P2P 读写、文件解码/编码、过期数据过滤与合并组成的流水化 GC 流程，用硬件并行掩盖 GC 的处理时延。
- **卸载友好的数据结构**：把“value 是否失效”的判断从反复回查 LSM 改为在内存中细粒度跟踪失效状态的低开销结构，使设备侧无需执行 LSM 查询即可选中高收益的目标文件。
- **软硬件协同的卸载协议**：为非阻塞的 GC 任务数据准备与结果回传设计调度逻辑，在 FPGA 资源受限的前提下避免卸载单元过度部署引发的资源争抢。
- **完整实现**：基于代表性 KV 分离系统 Titan 构建 AegonKV，开源可用。

## 方法与技术要点

- **数据布局**：MemTable 与 Immutable MemTable 在内存中，落盘为 L0 到 Ln 的 SSTable；flush 时把 value 追加进 vLog 并把偏移写回 SSTable，于是 Key 区只存 <key, offset>，Value 区按追加写组织。
- **设备内执行路径**：SmartSSD 通过 PCIe Switch 在其 NVMe SSD 与 FPGA DRAM 之间建立 P2P 通道，GC 的数据搬运与处理绕开主机 I/O 栈与互连总线，只消耗设备内部带宽。
- **失效判定替代方案**：沿用“从 compaction 结果推算失效率”的思路并把粒度细化到具体位置，用内存友好的结构维护 value 的实时状态，既支撑目标文件选择，也让 GC 与硬件自适应地配合。
- **任务调度与回传**：GC 任务的数据准备与元数据反馈采用灵活的非阻塞策略，迁移与地址更新以批（batch）为单位回送 LSM，避免卸载单元争用导致系统不稳。
- **触发策略沿用 Titan**：仍以 garbage_ratio 阈值决定哪些文件进入 GC 队列，与 Titan 相同的触发方式使两者空间占用接近，但 AegonKV 把执行从关键路径上摘走。

## 评估与主要结果

- **平台与负载**：两颗 18 核 Intel Xeon Gold 5220 2.20GHz（双向超线程）、64GB DDR4-2666 内存、一块 Samsung SmartSSD；负载为 YCSB 与真实生产工作负载，基线是 Titan、DiffKV、BlobDB 与 RocksDB。
- **三项指标同时改善**：相对现有 KV 分离系统，吞吐最大提升 1.28-3.3 倍，尾延迟降低 37%-66%，空间开销降低 15%-85%。
- **对系统参数不敏感**：调整 garbage_ratio 时 AegonKV 的吞吐与尾延迟不变（Titan 在低垃圾比下依然很差）；GC 线程数增加不影响性能，4 个卸载线程已足够；batch_size 在 32MB 到 256MB 之间变化对性能与开销无影响。
- **对负载参数不敏感**：value 大小、数据集大小、读写比例、客户端线程数变化时，AegonKV 在三项指标上始终最优，且多线程冲突最小、扩展性最好；数据集增大时各系统吞吐与尾延迟都无显著变化。

## 代码与研究制品

- [代码仓库](https://github.com/CGCL-codes/AegonKV)

[返回 Hardware Assist](index.md) · [返回 FAST 2025](../index.md)
