# SwiftBaton: Dependency-Aware Staged Reconstruction for Live Migration of Stateful Containers

**中文标题**：SwiftBaton：面向有状态容器热迁移的依赖感知分阶段重建

**所属 Session**：[Session 5: VM, Containers and Migration](index.md) · [ATC 2026](../index.md)

**作者**：Xianzhi Zhu (University of Science and Technology of China), Gonggu Chen (University of Science and Technology of China), Yancan Mao (National University of Singapore), Richard Ma (National University of Singapore), Lulu Yao (Ningbo University), Yongkun Li (University of Science and Technology of China), Yinlong Xu (University of Science and Technology of China), John C.S. Lui (The Chinese University of Hong Kong)

## 英文摘要
Cloud platforms must move stateful containers between hosts without losing their running state. A good migration must meet two goals at once: a short service pause and fast recovery after resume. Existing systems struggle to meet both. They improve checkpoint/restore through transfer scheduling and pipelined restoration, but still leave costly structural reconstruction on the downtime path. They treat memory largely as a bulk stream or reactive fault service, even though different pages are needed at different times. Even with faster networks, reconstructing interdependent kernel state and completing missing pages remain costly. These systems thus trade pause length against recovery speed. We present SwiftBaton, a live migration system for stateful Linux containers. SwiftBaton treats migration as dependency-aware staged reconstruction: each part of the state is rebuilt when it is needed, not when checkpoint/restore order reaches it. SwiftBaton pre-builds stable structural state through placeholders before the pause, validates it at cutover, and rebuilds the small remainder in parallel. It completes memory per page in demand order: stable pages before the pause, hot pages first, and the rest on demand. On a 2 GB Redis container, SwiftBaton cuts downtime to 40 ms and recovers full throughput in 188 ms, improving over a strengthened hybrid-copy baseline by 14.2× and 6.3×, respectively.

## 中文摘要
云平台必须在不丢失运行状态的前提下将有状态容器在主机之间迁移。一次好的迁移必须同时达成两个目标：短暂的服务暂停和恢复后的快速回弹。现有系统难以同时满足这两点。它们通过传输调度和流水线式恢复来改进检查点/恢复过程，却仍然把代价高昂的结构重建留在停机路径上。它们大体上把内存当作一个批量数据流或一种被动故障服务来处理，尽管不同页面在不同时刻才会被需要。即使网络更快，重建相互依赖的内核状态、补齐缺失页面依然代价高昂。因此这些系统只能在暂停时长与恢复速度之间做权衡。我们提出 SwiftBaton，一个面向有状态 Linux 容器的热迁移系统。SwiftBaton 把迁移视为依赖感知的分阶段重建：状态的每一部分在被需要时才被重建，而不是等到检查点/恢复顺序轮到它。SwiftBaton 在暂停之前通过占位符预先构建稳定的结构状态，在切换（cutover）时对其加以校验，并并行重建剩余的少量部分。它按需求顺序逐页补齐内存：稳定页在暂停前完成，热页优先，其余页面按需补齐。在一个 2 GB 的 Redis 容器上，SwiftBaton 将停机时间缩短到 40 ms，并在 188 ms 内恢复到满吞吐，相比经过强化的混合拷贝（hybrid-copy）基线分别提升 14.2× 和 6.3×。

## 英文关键词
Live Migration, Stateful Containers, Checkpoint and Restore

## 中文关键词
热迁移，有状态容器，检查点与恢复

[返回 Session 5](index.md) · [返回 ATC 2026](../index.md)
