# Building Memory Efficient Key-Value Stores in the CXL Era

**中文标题**：在 CXL 时代构建内存高效的键值存储

**所属 Session**：[Session 9: Memory Tiering and Management](index.md) · [ATC 2026](../index.md)

**作者**：Theodore Michailidis (University of California, San Diego), Steven Swanson (UCSD), Jishen Zhao (UCSD)

## 英文摘要
Key-value (KV) stores are utilized in a wide range of modern applications, with in-memory KV stores being popular for their low-latency and high throughput. In-memory KV stores, like redis and memcached, use hashtable-based indices that offer on average constant insert, lookup and delete times. However, these indices impose a high memory overhead and reduced memory and cache performance by design. While the index itself is compact in memory, accesses to data and metadata (e.g., key sizes, value sizes) lead to significant memory overhead. Moreover, traditional memory tiering mechanisms for heterogeneous memory architectures struggle to efficiently manage KV stores, leading to significant performance degradation. To solve these issues, we introduce CBC (Channel-Billed Cuckoo), a keyless, compact, memory-efficient and tiering-aware key-value index. CBC uses a 2 MiB-backed cuckoo hashing scheme that significantly extends TLB reach and improves cache locality, while also reducing the index memory overhead. Furthermore, we introduce a new KV-specific memory tiering mechanism that improves memory tiering performance by reducing profiling overhead and avoiding unnecessary page migrations. Our results show that CBC minimizes TLB and cache pollution, while it achieves up to 62% end-to-end lower memory overhead and one-to-two orders of magnitude better throughput over redis. Last, our evaluation also shows that CBC’s tiering mechanism outperforms previous memory tiering mechanisms by up to 30%.

## 中文摘要
键值（KV）存储被广泛应用于各类现代应用中，其中内存键值存储因其低延迟和高吞吐而广受欢迎。像 redis 和 memcached 这样的内存键值存储使用基于哈希表的索引，平均提供常数时间的插入、查找和删除。然而，这些索引在设计上带来高内存开销并降低了内存与缓存性能。虽然索引本身在内存中很紧凑，但对数据和元数据（例如键大小、值大小）的访问会导致显著的内存开销。此外，面向异构内存架构的传统内存分层机制难以高效地管理键值存储，导致显著的性能退化。为解决这些问题，我们提出 CBC（Channel-Billed Cuckoo），一种无键（keyless）、紧凑、内存高效且感知分层的键值索引。CBC 使用基于 2 MiB 的布谷鸟哈希方案，显著扩展了 TLB 的覆盖范围并改善了缓存局部性，同时降低了索引的内存开销。此外，我们提出一种新的键值专用内存分层机制，通过降低剖析开销和避免不必要的页迁移来提升内存分层性能。我们的结果表明，CBC 最大限度地减少了 TLB 与缓存污染，同时实现最多 62% 的端到端更低内存开销，以及相比 redis 高出一到两个数量级的吞吐。最后，我们的评估还表明，CBC 的分层机制比先前的内存分层机制性能高出最多 30%。

## 英文关键词
Key-value stores, cuckoo hashing, memory tiering, CXL, heterogeneous memory, huge pages, TLB

## 中文关键词
键值存储，布谷鸟哈希，内存分层，CXL，异构内存，大页，TLB

[返回 Session 9](index.md) · [返回 ATC 2026](../index.md)
