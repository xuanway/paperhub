---
title: "Security, Integrity, and Consistency · FAST 2025"
description: "FAST 2025 · Security, Integrity, and Consistency · 5 篇论文"
tags:
  - "FAST2025"
  - "Security, Integrity, and Consistency"
---

# Security, Integrity, and Consistency · FAST 2025

**中文主题**：安全、完整性与一致性

**所属会议**：[FAST 2025](../index.md)

**Session**：2025-02-26 14:00–15:40 · **Chair**：Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

这五篇论文面对同一个结构性矛盾：顺序、原子性、一致性这类语义原本由单一层保证，如今却要在主机软件、块层、设备 FTL 与 TEE 之间重新分配，一旦跨层传递失配就会变成开销或漏洞。技术路线的分歧在于把责任放在哪一层——有的重排主机侧的数据结构与提交时机，有的改设备侧的映射表更新与命令队列，有的干脆把一致性机制本身当作被测对象来剪枝。结果同样分层：完整性校验的吞吐与延迟最多改善 2.2 倍，多队列 IO 栈的吞吐提升 2.9 倍，AWUPF 让随机写快 3.6 倍，而基于不变量的测试把同类 bug 的发现速度提高 10 倍。

本 Session 共收录 **5** 篇论文。

| 英文标题 | 中文标题 | 一句话总结 | 资源 |
| --- | --- | --- | --- |
| [On Scalable Integrity Checking for Secure Cloud Disks](on_scalable_integrity_checking_for_secure_cloud_disks.md) | 面向安全云盘的可扩展完整性校验 | 哈希树的主要开销是 CPU 哈希而不是元数据 I/O；把树做成随热块自调整的 splay 结构，开销就会随负载偏斜一起降下来。 | [页面](https://www.usenix.org/conference/fast25/presentation/burke) · [PDF](https://www.usenix.org/system/files/fast25-burke.pdf) |
| [Silhouette: Leveraging Consistency Mechanisms to Detect Bugs in Persistent Memory-Based File Systems](silhouette_leveraging_consistency_mechanisms_to_detect_bugs_in_persistent_memory_based_file_systems.md) ([code](https://github.com/iaoing/Silhouette)) | Silhouette：利用一致性机制检测持久内存文件系统中的缺陷 | PM 文件系统普遍靠 journaling 或复制保证崩溃一致性；先证明机制实现正确，绝大部分写就不必参与重排枚举。 | [页面](https://www.usenix.org/conference/fast25/presentation/jiao) · [PDF](https://www.usenix.org/system/files/fast25-jiao.pdf) |
| [OPIMQ: Order Preserving IO stack for Multi-Queue Block Device](opimq_order_preserving_io_stack_for_multi_queue_block_device.md) ([code](https://github.com/ESOS-Lab/OPIMQ)) | OPIMQ：面向多队列块设备的保序 I/O 栈 | 存储顺序不必靠等数据落地来保证：把 cache barrier 下沉到 FTL 的映射表更新顺序里，多队列的并行度就能保住。 | [页面](https://www.usenix.org/conference/fast25/presentation/kim-jieun) · [PDF](https://www.usenix.org/system/files/fast25-kim-jieun.pdf) |
| [AWUPF Rediscovered: Atomic Writes to Unleash Pivotal Fault-Tolerance in SSDs](awupf_rediscovered_atomic_writes_to_unleash_pivotal_fault_tolerance_in_ssds.md) | 重新发现 AWUPF：以原子写释放 SSD 的关键容错能力 | SSD 本来就保证 flash page 级原子写；把不超过 AWUPF 的映射更新从日志里改为直写，就省掉了 journal 的重复写。 | [页面](https://www.usenix.org/conference/fast25/presentation/jeon) · [PDF](https://www.usenix.org/system/files/fast25-jeon.pdf) |
| [AtomicDisk: A Secure Virtual Disk for TEEs against Eviction Attacks](atomicdisk_a_secure_virtual_disk_for_tees_against_eviction_attacks.md) | AtomicDisk：面向 TEE 的抵御逐出攻击的安全虚拟磁盘 | CIFC 还不够：TEE 分不清用户 sync 出的磁盘状态与 cache 逐出留下的瞬态快照，所以还需要一条 sync 原子性。 | [页面](https://www.usenix.org/conference/fast25/presentation/tian-hongliang) · [PDF](https://www.usenix.org/system/files/fast25-tian-hongliang.pdf) |

[返回 FAST 2025](../index.md)
