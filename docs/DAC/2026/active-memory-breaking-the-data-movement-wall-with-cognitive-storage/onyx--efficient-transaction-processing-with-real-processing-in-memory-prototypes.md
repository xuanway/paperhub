Onyx: Efficient Transaction Processing with Real Processing-in-Memory Prototypes
Authors：
[Menglei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0203814699425871419)，[Yixiao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0993542282136148486)，[Yu Hua](https://63dac.conference-program.com/?post_type=page&p=15&uid=647243)

## 中文标题

Onyx：基于真实存内处理原型的高效事务处理

## 英文摘要

A transaction ensures an all-or-nothing guarantee for a set of read/write operations. While modern transaction processing systems provide atomicity and consistency for data center applications, their performance is fundamentally limited by a critical memory bandwidth bottleneck, caused by massive numbers of read/write operations. Processing-in-memory (PIM) architectures offer a promising solution with their high aggregate bandwidth. However, directly applying PIM becomes inefficient in practice due to load imbalance and costly data transfers among PIM processors. To bridge the gap between transaction processing and PIM architectures, this paper presents Onyx, a high-throughput transaction processing system that efficiently executes transactions on a real UPMEM PIM prototype. To fully leverage the high parallelism and bandwidth of PIM, Onyx orchestrates the transaction execution workflow to maximize local accesses while maintaining load balance across PIM processors. It further employs rank-level asynchronous data transfer to reduce communication overhead. Extensive evaluation using real-world YCSB and TPC-C benchmarks shows that Onyx significantly outperforms state-of-the-art transaction processing systems.

## 中文摘要

事务为一组读/写操作提供全有或全无的保证。尽管现代事务处理系统为数据中心应用提供了原子性和一致性，但其性能从根本上受限于关键的内存带宽瓶颈，该瓶颈由大量读/写操作引起。存内处理（PIM）架构凭借其高聚合带宽提供了一种有前景的解决方案。然而，由于负载不均衡以及 PIM 处理器之间昂贵的数据传输，直接应用 PIM 在实践中效率不高。为弥合事务处理与 PIM 架构之间的差距，本文提出了 Onyx，一种在真实 UPMEM PIM 原型上高效执行事务的高吞吐量事务处理系统。为充分利用 PIM 的高并行性和带宽，Onyx 编排事务执行工作流，在保持 PIM 处理器间负载均衡的同时最大化本地访问。它进一步采用 rank 级异步数据传输来降低通信开销。使用真实 YCSB 和 TPC-C 基准的广泛评估表明，Onyx 显著优于当前最优的事务处理系统。

## 英文关键词

Architecture and System Design, Emerging Technologies, Compute/Storage Infrastructure

## 中文关键词

架构与系统设计、新兴技术、计算/存储基础设施
