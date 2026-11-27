Cache Where It Counts: Towards Workload-Aware I/O Coordination for NUMA Storage Systems
Authors：
[Wenda Tang](https://63dac.conference-program.com/?post_type=page&p=15&uid=484690392633277988)，[Yanwen Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2797824632613930559)，[Yiduo Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=98238710491831130711)，[Jie Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=66025697494361779121)

## 中文标题

把缓存用在关键处：面向 NUMA 存储系统的工作负载感知 I/O 协同

## 英文摘要

Modern Non-Uniform Memory Access (NUMA) servers equipped with distributed Non-Volatile Memory Express (NVMe) storage present new challenges for I/O coordination. First, conventional page cache allocators ignore storage topology, resulting in inefficient cross-node cache placement and performance issues. Second, CPU schedulers overlook cache and storage locality, causing frequent cross-node cache accesses and further degrading performance. Third, the OS page cache employs a rigid eviction policy that fails to adapt to diverse application workloads, while even programmable alternatives often require complex manual tuning. To address these challenges, we propose Laelaps, a workload-aware I/O coordination framework for NUMA storage systems. Laelaps introduces three key techniques: (1) storage-topology-aware page cache placement, co-locating cache pages with their backing NVMe devices; (2) storage-topology-aware I/O thread scheduling that aligns thread placement with cache distribution to minimize cross-node accesses; and (3) workload-aware adaptive page caching that automatically selects eviction policies based on observed application access patterns. Evaluation shows that Laelaps achieves 1.41× geometric mean throughput improvement with 3.5% runtime overhead.

## 中文摘要

配备分布式 NVMe 存储的现代非统一内存访问（NUMA）服务器为 I/O 协同带来了新的挑战。首先，传统页缓存分配器忽略存储拓扑，导致低效的跨节点缓存放置和性能问题。其次，CPU 调度器忽视缓存与存储的局部性，造成频繁的跨节点缓存访问，进一步降低性能。第三，操作系统页缓存采用僵化的淘汰策略，无法适应多样的应用工作负载，而即便是可编程的替代方案也往往需要复杂的手动调优。为应对这些挑战，我们提出 Laelaps，一个面向 NUMA 存储系统的工作负载感知 I/O 协同框架。Laelaps 引入三项关键技术：(1) 存储拓扑感知的页缓存放置，将缓存页与其后端 NVMe 设备共置；(2) 存储拓扑感知的 I/O 线程调度，使线程放置与缓存分布对齐，以最小化跨节点访问；(3) 工作负载感知的自适应页缓存，根据观测到的应用访问模式自动选择淘汰策略。评估表明，Laelaps 实现了 1.41 倍的几何平均吞吐提升，运行时开销仅为 3.5%。

## 英文关键词

NUMA, Operating Systems, I/O Coordination, eBPF, Page Cache

## 中文关键词

NUMA、操作系统、I/O 协同、eBPF、页缓存
