Gwrite: Offloading Replication in Disaggregated Memory Systems
Authors：
[Jianglang Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=30128089790858352771)，[Mingxing ZHANG](https://63dac.conference-program.com/?post_type=page&p=15&uid=6600409225009972135)，[Yingdi Shan](https://63dac.conference-program.com/?post_type=page&p=15&uid=514397011352868318)，[Yongwei Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5017120961218593028)

## 中文标题

GWrite：解耦式内存系统中的复制卸载

## 英文摘要

Disaggregated memory architectures leverage RDMA to decouple compute and memory nodes. In write-intensive, strongly-consistent systems (e.g., distributed transactions, durable key-value stores), synchronous replication makes the compute node’s RDMA Network Interface Card (RNIC) a dominant bottleneck: each additional replica multiplies its I/O operations per second (IOPS) and bandwidth cost, quickly degrading write throughput. Meanwhile, memory-side RNICs support full-duplex communication but contribute little outbound traffic during replication, leaving valuable I/O capacity unused. We propose GWrite, a hardware-oriented RDMA primitive that enables CPU-free, autonomous replication on memory nodes, and GWrap, a co-designed software protocol. GWrite shifts replication fan-out from the compute node’s RNIC to memory-side RNICs, while GWrap builds hierarchical replication paths and batched confirmations to avoid new bottlenecks. A software prototype on commodity RNICs emulating the GWrite primitive achieves up to 2.18× higher throughput in a distributed transaction system and reduces replication-induced performance degradation from 46.7% to 19.7% in a disaggregated hash table, demonstrating that GWrite can substantially alleviate compute-side RNIC bottlenecks in write-intensive, durable disaggregated systems.

## 中文摘要

解耦式内存架构借助 RDMA 将计算节点与内存节点分离。在写密集的强一致系统（如分布式事务、持久化键值存储）中，同步复制使计算节点的 RDMA 网卡（RNIC）成为主要瓶颈：每增加一个副本，其每秒 I/O 操作数（IOPS）与带宽开销便成倍增加，写吞吐量迅速下降。与此同时，内存侧 RNIC 虽支持全双工通信，但在复制过程中几乎不产生出向流量，使宝贵的 I/O 能力处于闲置状态。我们提出 GWrite，一种面向硬件的 RDMA 原语，可在内存节点上实现无需 CPU 参与的自主复制，并配以协同设计的软件协议 GWrap。GWrite 将复制扇出从计算节点的 RNIC 转移到内存侧 RNIC，GWrap 则构建分层复制路径与批量确认机制，以避免产生新的瓶颈。在商用 RNIC 上模拟 GWrite 原语的软件原型在分布式事务系统中取得最高 2.18 倍的吞吐提升，并将解耦式哈希表中由复制引起的性能下降从 46.7% 降至 19.7%，表明 GWrite 能够显著缓解写密集、持久化解耦系统中的计算侧 RNIC 瓶颈。

## 英文关键词

disaggregated memory, RDMA, replication, hardware/software codesign

## 中文关键词

解耦式内存、RDMA、复制、软硬件协同设计
