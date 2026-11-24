# CacheFS: Peer-to-Peer Cooperative Caching for LLM Weight Distribution at Cloud Scale

**中文标题**：CacheFS：面向云规模 LLM 权重分发的对等协同缓存

**所属 Session**：[Session 22: Large-scale AI](index.md) · [ATC 2026](../index.md)

**作者**：Zheng Liu (Zhejiang University, Alibaba Group), Eryu Guan (Alibaba Group), Shang Zhao (Alibaba Group), Chengkun Wei (Zhejiang University), Teng Ma (Alibaba Group), Jin Shi (Zhejiang University), Ye Cao (Alibaba Group), Chen Cao (Alibaba Group), Wenpeng Li (Alibaba Group), Tao He (Alibaba Group), Wenyuan Yu (Alibaba Group), Tao Ma (Alibaba Group), Wenzhi Chen (Zhejiang University)

## 英文摘要
Elastic LLM inference must bring new GPU instances online quickly, but burst scale-out makes many instances fetch the same large model from shared cloud storage. In our production environment, distributing Qwen2.5-72B from NFS to 50 instances takes 28 minutes. Model weights are immutable, read in full, loaded nearly sequentially, and identical across replicas. These properties allow inference nodes to use host memory and intra-cluster bandwidth as a cooperative cache without the write and consistency mechanisms of a general-purpose file system. We present CacheFS, a peer-to-peer cooperative caching file system. Its central mechanism is hash-aware cooperative eviction. Under memory pressure, each node preferentially retains blocks assigned to it by consistent hashing. When aggregate cache capacity covers the working set, the union of 𝑁partial caches converges toward full model coverage even if no node can hold the complete model. This requires neither centralized nor per-block retention coordination. CacheFS also provides a coroutine-based data plane, proactive preload, a pre-warmed CacheRoot tier, and a transparent FUSE interface for unmodified inference frameworks. After more than eighteen months of production operation across four cloud regions, CacheFS distributes Qwen2.5-72B to 50 instances in 30 seconds, 56× faster than NFS. For DeepSeek-R1, per-node loading from object storage decreases from 19 minutes to 200 seconds. Together with a companion fast-startup runtime, CacheFS saves more than 7,700 GPU card-hours per day.

## 中文摘要
弹性 LLM 推理必须让新的 GPU 实例快速上线，但突发性扩容会使许多实例同时从共享云存储获取同一个大模型。在我们的生产环境中，把 Qwen2.5-72B 从 NFS 分发到 50 个实例需要 28 分钟。模型权重不可变、被完整读取、近乎顺序加载，且各副本之间完全相同。这些特性使推理节点可以把主机内存与集群内带宽用作协同缓存，而无需通用文件系统的写入与一致性机制。我们提出 CacheFS，一个对等协同缓存文件系统。其核心机制是哈希感知的协同淘汰。在内存压力下，每个节点优先保留由一致性哈希分配给它的块。当聚合缓存容量覆盖工作集时，即使没有任何节点能容纳完整模型，N 个部分缓存的并集也会收敛到对模型的完整覆盖。这既不需要集中式协调，也不需要逐块的保留协调。CacheFS 还提供基于协程的数据平面、主动预加载、预热好的 CacheRoot 层，以及对未修改推理框架透明的 FUSE 接口。在四个云区域历经超过十八个月的生产运行后，CacheFS 将 Qwen2.5-72B 分发到 50 个实例仅需 30 秒，比 NFS 快 56×。对于 DeepSeek-R1，单节点从对象存储加载的时间从 19 分钟降至 200 秒。配合配套的快速启动运行时，CacheFS 每天节省超过 7,700 GPU 卡·小时。

## 英文关键词
peer-to-peer caching, distributed file systems, LLM inference, model distribution, elastic scaling, RDMA

## 中文关键词
对等缓存，分布式文件系统，LLM 推理，模型分发，弹性伸缩，RDMA

[返回 Session 22](index.md) · [返回 ATC 2026](../index.md)
