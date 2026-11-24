# SeaStore: Redesigning Ceph’s Storage Backend for CPU-Efficient NVMe Performance

**中文标题**：SeaStore：为 CPU 高效的 NVMe 性能重新设计 Ceph 存储后端

**所属 Session**：[Session 6: Storage and File Systems](index.md) · [ATC 2026](../index.md)

**作者**：Myoungwon Oh (Korea Aerospace University), Yingxin Cheng (DDN), Matan Breizman (IBM), Josh Durgin (IBM)

## 英文摘要
This paper presents SeaStore, a new CPU-efficient, NVMe-oriented storage backend for Ceph, a general-purpose distributed storage system. Over the past decade, Ceph has evolved alongside advancements in storage technology. However, it faces fundamental challenges in random I/O performance due to the structural limitations of its software stack that cannot be addressed via the modular changes adopted in the past. Addressing these limitations requires solving three design challenges: (1) the limitations of a heterogeneous and tightly coupled RocksDB-based architecture, (2) the lack of efficient per-core transaction processing, (3) maintaining high transaction concurrency without excessive contention. SeaStore efficiently overcomes these limitations by introducing three techniques: sharding with hybrid layout, cooperative optimistic pipeline processing, and contention reduction via structure-free updates. We have completely rebuilt the storage backend and integrated SeaStore into the Ceph mainline as a next generation storage backend. Our evaluation results show that SeaStore achieves up to 70% improvement in small random write performance, and scales IOPS with the number of cores. Furthermore, it offers at least 2x higher IOPS under mixed workloads and serves small random reads while reducing CPU usage by 25%.

## 中文摘要
本文提出 SeaStore，一个面向 Ceph（通用分布式存储系统）的新的 CPU 高效、面向 NVMe 的存储后端。过去十年间，Ceph 一直随着存储技术的进步而演进。然而，由于其软件栈的结构性限制无法通过过去所采用的模块化改动来消除，它在随机 I/O 性能上面临根本性挑战。要解决这些限制，需要应对三个设计挑战：（1）异构且紧耦合的基于 RocksDB 的架构的局限；（2）缺乏高效的每核事务处理；（3）在不过度争用的前提下保持高事务并发。SeaStore 通过引入三项技术有效克服了这些限制：混合布局的分片、协作式乐观流水线处理，以及通过无结构更新减少争用。我们完全重建了该存储后端，并将 SeaStore 作为下一代存储后端集成到 Ceph 主线中。评估结果表明，SeaStore 的小随机写性能最多提升 70%，并且 IOPS 随核数扩展。此外，它在混合工作负载下提供至少 2 倍的 IOPS，并在服务小随机读的同时将 CPU 使用率降低 25%。

## 英文关键词
Distributed storage system, storage backend, transaction processing, asynchronous I/O, sharding, NVMe storage, Ceph

## 中文关键词
分布式存储系统，存储后端，事务处理，异步 I/O，分片，NVMe 存储，Ceph

[返回 Session 6](index.md) · [返回 ATC 2026](../index.md)
