# Starfish: Fault-Tolerant Far Memory with Low Resource and Performance Overhead

**中文标题**：Starfish：低资源与性能开销的容错远端内存

**所属 Session**：[Session 9: Memory Tiering and Management](index.md) · [ATC 2026](../index.md)

**作者**：Yanwen Xia (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Benyong Deng (Huazhong University of Science and Technology), Hong Huang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Yuzheng Wang (Peking University), Quanxi Li (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Xingda Wei (Shanghai Jiao Tong University), Xiaobing Feng (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Huimin Cui (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences), Chenxi Wang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences)

## 英文摘要
Fault-tolerant (FT) far memory systems protect remote state against memory node failures. Existing designs optimize erasure coding (EC) around coarse memory units, forcing objects to fit those units and causing redundant protection work and amplified remote accesses. Starfish is object-first: it first reuses valid recovery paths, through retained remote backups and recomputation, and then uses object behavior to choose the protection method, granularity, and layout for the remaining remote object states. Across 6 applications and 8 workloads, Starfish improves performance by 2.1× over Hydra and 1.9× over Carbink on average. It reaches 88.3% of the performance of the same system without FT. Starfish also reduces network traffic by 8.5× and lowers memory node CPU usage by 7.5× over Carbink with no extra remote memory cost, while preserving efficient recovery.

## 中文摘要
容错（FT）远端内存系统保护远程状态免受内存节点故障的影响。现有设计围绕粗粒度的内存单元来优化纠删码（EC），迫使对象必须适配这些单元，从而导致冗余的保护工作和被放大的远程访问。Starfish 以对象为先：它首先通过保留的远程备份与重计算复用有效的恢复路径，然后利用对象行为为剩余的远程对象状态选择保护方法、粒度和布局。在 6 个应用和 8 种工作负载上，Starfish 相比 Hydra 平均提升性能 2.1×，相比 Carbink 提升 1.9×。它达到同一系统在无 FT 时性能的 88.3%。与 Carbink 相比，Starfish 还将网络流量降低 8.5×，将内存节点的 CPU 使用率降低 7.5×，且不增加额外的远程内存开销，同时保持高效的恢复。

## 英文关键词
Far memory, Fault tolerance, Runtime systems

## 中文关键词
远端内存，容错，运行时系统

[返回 Session 9](index.md) · [返回 ATC 2026](../index.md)
