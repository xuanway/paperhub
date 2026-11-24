# Zswap Boost: Accelerating Transparent Memory Compression in the Cloud

**中文标题**：Zswap Boost：加速云中的透明内存压缩

**所属 Session**：[Session 9: Memory Tiering and Management](index.md) · [ATC 2026](../index.md)

**作者**：Zheng Liu (Zhejiang University, Alibaba Group), Teng Ma (Alibaba Group), Chengkun Wei (Zhejiang University), Ning Zhang (Alibaba Group), Xingyu Liu (Zhejiang University), Gang Deng (Alibaba Group), Shangming Cai (Alibaba Group), Wenzhi Chen (Zhejiang University)

## 英文摘要
Memory is one of the most expensive and underutilized resources in cloud datacenters. Transparent memory compression reclaims overcommitted memory without additional hardware or application changes. Yet our production deployment of Linux zswap reveals substantial overhead for latency-sensitive workloads. Although compressed pages remain in memory, zswap retains disk-oriented swap indexing, red-black-tree lookup, swap-cache management, and slot allocation. Consequently, roughly 40% of swap-in critical-path CPU cycles are spent on bookkeeping rather than decompression. To eliminate this disk-centric tax, we present Zswap Boost, which encodes the compressed-page metadata location in the page-table entry. It reduces zswap’s three-level lookup to two and removes swap-slot, red-black-tree, and swap-cache operations from the critical path. We also integrate Intel IAA using batched compression and asynchronous decompression. Zswap Boost is implemented in our commercial Linux distribution and has run in production for nearly two years. In controlled experiments, Zswap Boost reduces swap-in latency from 6.6 ∼19.9 𝜇𝑠to 2.5 ∼4.3 𝜇𝑠, cuts Flink kernel-mode CPU time from 54.3% to 19.0%, and saves 12.5% of memory at a 2.13% performance cost. It also reduces Redis P99 latency by up to 18.5% compared with vanilla zswap. In our Flink cluster, the broader memory-overcommit pipeline enabled 130 physical machines to be retired.

## 中文摘要
内存是云数据中心中最昂贵且利用率最低的资源之一。透明内存压缩无需额外硬件或应用改动即可回收超额分配的内存。然而，我们在生产环境中部署 Linux zswap 时发现，它对延迟敏感型工作负载存在相当大的开销。尽管压缩页仍保留在内存中，zswap 却保留了面向磁盘的交换索引、红黑树查找、交换缓存管理以及槽位分配。因此，交换入（swap-in）关键路径上约 40% 的 CPU 周期被用于簿记工作而非解压缩。为消除这种以磁盘为中心的开销，我们提出 Zswap Boost，它将压缩页元数据的位置编码在页表项中。它把 zswap 的三级查找减少为两级，并从关键路径中移除交换槽位、红黑树和交换缓存操作。我们还使用批量压缩和异步解压缩集成 Intel IAA。Zswap Boost 已在我们的商业 Linux 发行版中实现，并已在生产环境中运行近两年。在受控实验中，Zswap Boost 将交换入延迟从 6.6∼19.9 微秒降至 2.5∼4.3 微秒，将 Flink 的内核态 CPU 时间从 54.3% 降至 19.0%，并以 2.13% 的性能代价节省 12.5% 的内存。与原版 zswap 相比，它还将 Redis 的 P99 延迟降低最多 18.5%。在我们的 Flink 集群中，更广泛的内存超额分配流水线使 130 台物理机得以退役。

## 英文关键词
transparent memory compression, zswap, memory swapping, page table, operating systems, cloud computing, memory management

## 中文关键词
透明内存压缩，zswap，内存交换，页表，操作系统，云计算，内存管理

[返回 Session 9](index.md) · [返回 ATC 2026](../index.md)
