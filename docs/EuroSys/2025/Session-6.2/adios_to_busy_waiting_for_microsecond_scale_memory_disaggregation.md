---
title: "Adios to Busy-Waiting for Microsecond-scale Memory Disaggregation"
description: "EuroSys 2025 · Memory Tiering and Disaggregation · Wonsup Yoon (KAIST), Jisu Ok (KAIST), Sue Moon (KAIST), Youngjin Kwon (KAIST)"
tags:
  - "EuroSys2025"
  - "Memory Tiering and Disaggregation"
---

# Adios to Busy-Waiting for Microsecond-scale Memory Disaggregation

**中文标题：** 告别微秒级解耦内存中的忙等待

**所属 Session：** [Session 6.2: Memory Tiering and Disaggregation](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Memory Tiering and Disaggregation。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Memory Tiering and Disaggregation</p>
</div>

**作者**：Wonsup Yoon (KAIST), Jisu Ok (KAIST), Sue Moon (KAIST), Youngjin Kwon (KAIST)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717475)

## 英文摘要

How fast and efficiently page faults are handled determines the performance of paging-based memory disaggregation (MD) systems. Recent MD systems employ busy-waiting in page fault handling to avoid costly interrupt handling and context switching. Upon a page fault, they issue a remote fetch request and busy-wait for the completion of the request rather than yield their execution to other tasks. While these attempts succeed to cut the latency of MD systems to microseconds, they suffer from head-of-line (HOL) blocking that leads to high tail latency and causes RDMA network underutilization.

To address the problems, we reload the yield-based mechanism into the page fault handling and propose a new MD system, Adios. While yielding involves the switching overhead, Adios minimizes it by putting the page fault handler and the execution scheduler into a single address space. Then we use newly designed lightweight user-level threads, namely unithread. We also devise a dispatching algorithm that alleviates the imbalance in RDMA queue pairs, assuring lessened queueing delays and improved RDMA network utilization. Our evaluation demonstrates that Adios outperforms an existing state-of-the-art busy-waiting MD system, DiLOS, by up to 1.07-1.64× in throughput and 1.99-10.89× in P99.9 latency on real-world applications.

## 中文摘要

缺页处理的速度和效率决定了基于分页的内存解耦（MD）系统的性能。近期的 MD 系统在缺页处理中采用忙等待，以避免昂贵的中断处理和上下文切换。一旦发生缺页，它们发出远程取页请求并忙等待该请求完成，而不是将执行让给其他任务。尽管这些尝试成功将 MD 系统的延迟降至微秒级，但它们遭受队头（HOL）阻塞，导致高尾延迟并造成 RDMA 网络利用不足。

为解决这些问题，我们在缺页处理中重新引入基于让出（yield）的机制，并提出新的 MD 系统 Adios。虽然让出涉及切换开销，但 Adios 通过将缺页处理程序和执行调度器置于同一地址空间来最小化该开销。接着我们使用新设计的轻量级用户级线程，即 unithread。我们还设计了一种调度算法，缓解 RDMA 队列对之间的不平衡，从而减少排队延迟并提升 RDMA 网络利用率。我们的评估表明，在真实应用上，Adios 的吞吐比现有最先进的忙等待 MD 系统 DiLOS 高 1.07–1.64 倍，P99.9 延迟低 1.99–10.89 倍。

**英文关键词：** memory disaggregation, disaggregated data center, unikernel, microsecond-scale

**中文关键词：** 内存解耦、解耦数据中心、unikernel、微秒级

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
