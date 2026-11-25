---
title: "GICC: A High-Performance Runtime for GPU-Initiated Communication and Coordination in Modern HPC Systems"
description: "HPDC 2026 · Session 11 — Communication, Workflows & Sustainability"
tags:
  - "HPDC2026"
  - "Session 11"
  - "Communication, Workflows & Sustainability"
---

# GICC: A High-Performance Runtime for GPU-Initiated Communication and Coordination in Modern HPC Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 11</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807576)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ShanAC26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ShanAC26)

**作者**：Baodi Shan, Mauricio Araya-Polo, Barbara Chapman

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 11 — Communication, Workflows & Sustainability（2026年7月16日 13:30–14:30 · Session Chair：Mehmet Koyuturk）

---

## 英文摘要

An increasingly popular approach for distributed GPU applications is kernel-level, cross-node coordination to reduce launch overheads and improve compute–communication overlap. The reality is that such support is lacking. On one hand, on OFI-based interconnects such as HPE Slingshot—which powers six of the top ten systems in the November 2025 Top500, including the top three—GPU kernels cannot autonomously drive distributed coordination: existing runtimes rely on host-driven progress and do not provide a bounded mechanism for recycling pre-staged NIC work across repeated GPU-triggered operations. On the other hand, on InfiniBand, GPU-initiated communication is possible, but current implementations incur unnecessary synchronization and locking overheads. This paper presents GICC, a GPU-driven coordination framework that enables GPU kernels to issue coordination commands and directly trigger NIC-level operations without host involvement on the fast path. For example, in stencil computations, GPU threads can directly initiate halo exchanges with neighboring nodes as soon as boundary regions are computed, rather than waiting for the kernel to complete and relying on the host to orchestrate communication. This eliminates synchronization overhead and enables fine-grained overlap between interior computation and boundary data transfer. GICC decouples coordination semantics from data movement and introduces an asynchronous resource reclamation scheme: the NIC signals completion to both GPU and host memory, enabling a lightweight host thread to recycle NIC resources concurrently with GPU execution—without injecting latency into the coordination path. This design enables sustained GPU-driven coordination under finite NIC state, a capability absent from existing runtimes on OFI-based fabrics. We implement GICC on NVIDIA and AMD GPUs over both InfiniBand and Slingshot (OFI). On Slingshot, GICC reduces average per-coordination latency by up to 229× and improves weak scaling efficiency by up to 25%. On InfiniBand, GICC achieves up to 1.95× lower put latency than NVSHMEM by eliminating unnecessary locking and synchronization. For an industrial stencil-based proxy application on 64 AMD MI250X GCDs, GPU-aware MPI incurs over 52% higher communication time than GICC, and GICC achieves 42% parallel efficiency versus MPI’s 35.4%. These results demonstrate that GPU-driven, resource-aware coordination is both necessary and achievable across the dominant interconnects in modern HPC systems.

## 中文摘要

分布式 GPU 应用日益流行的一种方法是核级、跨节点协调，以降低启动开销并提升计算-通信重叠。现实情况是此类支持仍然缺乏。一方面，在 HPE Slingshot 等基于 OFI 的互连上——它为 2025 年 11 月 Top500 前十中的六套系统（包括前三名）提供支撑——GPU 核无法自主驱动分布式协调：现有运行时依赖主机驱动的推进，且未提供有界机制来在重复的 GPU 触发操作间回收预置的 NIC 工作。另一方面，在 InfiniBand 上可以实现 GPU 发起的通信，但当前实现带来不必要的同步与加锁开销。本文提出 GICC，一个 GPU 驱动的协调框架，使 GPU 核能够发出协调命令并直接触发 NIC 级操作，而无需主机参与快速路径。例如，在模板（stencil）计算中，GPU 线程可以在边界区域计算完成后立即直接与相邻节点发起 halo 交换，而无需等待核完成并依赖主机编排通信。这消除了同步开销，并实现内部计算与边界数据传输之间的细粒度重叠。GICC 将协调语义与数据搬运解耦，并引入异步资源回收方案：NIC 向 GPU 和主机内存同时发出完成信号，使轻量主机线程能够与 GPU 执行并发地回收 NIC 资源——且不向协调路径注入延迟。该设计使 GPU 驱动的协调能够在有限的 NIC 状态下持续进行，这是基于 OFI 网络的现有运行时并不具备的能力。我们在 NVIDIA 和 AMD GPU 上、通过 InfiniBand 和 Slingshot（OFI）实现了 GICC。在 Slingshot 上，GICC 将平均每次协调延迟最高降低 229 倍，并将弱扩展效率最高提升 25%。在 InfiniBand 上，GICC 通过消除不必要的加锁与同步，使 put 延迟比 NVSHMEM 最高低 1.95 倍。对于 64 个 AMD MI250X GCD 上的工业模板代理应用，GPU 感知 MPI 的通信时间比 GICC 高出 52% 以上，GICC 取得 42% 的并行效率，而 MPI 为 35.4%。这些结果表明，GPU 驱动、资源感知的协调在现代 HPC 系统的主流互连上既是必要的，也是可实现的。

## 英文关键词

RDMA, GPGPU, Libfabric, SHMEM, One-sided Communication

## 中文关键词

RDMA，GPGPU，Libfabric，SHMEM，单边通信

---

[← 返回 Session 11 — Communication, Workflows & Sustainability](index.md)
