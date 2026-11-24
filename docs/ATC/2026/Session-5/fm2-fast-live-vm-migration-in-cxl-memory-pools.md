# FM2: Fast Live VM Migration in CXL Memory Pools

**中文标题**：FM2：CXL 内存池中的快速虚拟机热迁移

**所属 Session**：[Session 5: VM, Containers and Migration](index.md) · [ATC 2026](../index.md)

**作者**：Zezhou Wang (University of Washington), Jonggyu Park (University of Washington), Shihang (Vic) Li (University of Washington), Pedro Henrique Penna (Microsoft Research), Thomas E. Anderson (University of Washington), Simon Peter (University of Washington)

## 英文摘要
Live virtual machine (VM) migration enables more efficient data center operation by relocating VMs across hosts without service interruption. Because many cloud applications are both memory-intensive and interactive, however, live VM migration has proven difficult to implement with acceptable performance. The emergence of Compute Express Link (CXL) offers a new lever: memory pools shared across multiple machines. We present FM2, a new CXL-based live VM migration framework that makes migration faster and less disruptive. Before migration is needed, FM2 proactively stores a copy of VM memory in a CXL memory pool, substantially reducing migration time and accelerating resource reclamation. FM2 also efficiently promotes performance-critical data from the CXL memory pool to the destination’s local memory, enabling rapid post-migration performance recovery. By decoupling live VM migration from memory transfer, FM2 reduces interference with application traffic while further shortening migration time. Across a range of memory-intensive workloads, FM2 reduces total migration time by up to 68× compared with QEMU’s hybrid migration across network and CXL interconnects, while keeping VM performance overheads below 2% and downtime under 150 ms.

## 中文摘要
虚拟机（VM）热迁移通过在不中断服务的情况下将 VM 在主机之间搬迁，使数据中心的运行更加高效。然而，由于许多云应用既内存密集又具有交互性，热迁移一直难以在可接受的性能下实现。Compute Express Link（CXL）的出现提供了一种新的手段：跨多台机器共享的内存池。我们提出 FM2，一个新的基于 CXL 的 VM 热迁移框架，它使迁移更快、干扰更小。在需要迁移之前，FM2 主动将 VM 内存的一份副本存放在 CXL 内存池中，从而大幅缩短迁移时间并加速资源回收。FM2 还能高效地把性能关键的数据从 CXL 内存池提升到目的端的本地内存，实现迁移后性能的快速恢复。通过将 VM 热迁移与内存传输解耦，FM2 在进一步缩短迁移时间的同时减少了对应用流量的干扰。在一系列内存密集型工作负载上，与 QEMU 跨网络和 CXL 互连的混合迁移相比，FM2 将总迁移时间最多缩短 68×，同时将 VM 性能开销保持在 2% 以下、停机时间控制在 150 ms 以内。

## 英文关键词
Live VM Migration, Compute Express Link (CXL), Memory Pooling

## 中文关键词
虚拟机热迁移，Compute Express Link（CXL），内存池化

[返回 Session 5](index.md) · [返回 ATC 2026](../index.md)
