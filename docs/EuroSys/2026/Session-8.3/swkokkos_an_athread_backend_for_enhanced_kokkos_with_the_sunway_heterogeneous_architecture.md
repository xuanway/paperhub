---
title: "swKokkos: An Athread Backend for Enhanced Kokkos with the Sunway Heterogeneous Architecture"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · Junlin Wei (Computer Network Information Center, Chinese Academy of Science; Pen"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# swKokkos: An Athread Backend for Enhanced Kokkos with the Sunway Heterogeneous Architecture

**中文标题：** swKokkos：为 Kokkos 提供神威异构架构支持的 Athread 后端

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：Junlin Wei (Computer Network Information Center, Chinese Academy of Science; Pengcheng Laboratory; University of Chinese Academy of Sciences), Jinrong Jiang (Computer Network Information Center, Chinese Academy of Sciences; University of Chinese Academy of Sciences), Wu Wang (Computer Network Information Center, Chinese Academy of Science), Chen Li (Computer Network Information Center, Chinese Academy of Science), Yehong Zhang (Pengcheng Laboratory), Yue Yu (Pengcheng Laboratory), Lian Zhao (Computer Network Information Center, Chinese Academy of Science), Xiang Han (Computer Network Information Center, Chinese Academy of Science), Zhenjia Li (Computer Network Information Center, Chinese Academy of Science), Feng Zhang (Computer Network Information Center, Chinese Academy of Science), Haoyuan Zhang (Computer Network Information Center, Chinese Academy of Science), Yidi Bai (Computer Network Information Center, Chinese Academy of Science), Maoxue Yu (Laoshan Laboratory), Kaixu (Laoshan Laboratory), Hailong Liu (Laoshan Laboratory), Xuebin Chi (Computer Network Information Center, Chinese Academy of Sciences; University of Chinese Academy of Sciences)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803604)

## 英文摘要

Performance portability is crucial for enabling the efficient execution of high-performance applications across evolving heterogeneous architectures. The Kokkos library offers an abstraction layer that decouples algorithmic logic from hardware-specific details. However, Kokkos lacks support for the Sunway processor, which is an essential heterogeneous architecture. We present swKokkos, an Athread backend that enables Kokkos on the Sunway many-core architecture. It introduces a compile-time kernel registration and runtime callback mechanism that breaks prior barriers preventing the template-intensive C++ Kokkos library from executing on Sunway compute processing elements (CPEs). We further implement three targeted optimizations: (1) vectorized hash-based callback dispatch to cut runtime abstraction overhead, (2) tile-based parallel task mapping algorithm to improve flexibility and load distribution, and (3) a fast device scheduling library that reduces device-side scheduling latency. We evaluate swKokkos for performance across multiscale scenarios. Moreover, swKokkos achieves up to 34.0× speedup over the host backend. Compared to the native device backend solution, it ranges from 0.7× to 2.8×, indicating that the abstraction overhead is low and occasionally reversed into gains through improved scheduling. In particular, swKokkos scales efficiently and stably to over 100000 core simulations in a real-world application, demonstrating its ability to support extreme-scale simulations on the Sunway exascale supercomputer.

## 中文摘要

性能可移植性对于使高性能应用能够在不断演进的异构架构上高效执行至关重要。Kokkos 库提供了将算法逻辑与硬件细节解耦的抽象层。然而，Kokkos 缺乏对神威（Sunway）处理器的支持，而后者是一种重要的异构架构。我们提出 swKokkos，一个使 Kokkos 能够在神威众核架构上运行的 Athread 后端。它引入了编译期内核注册与运行时回调机制，打破了此前阻碍模板密集的 C++ Kokkos 库在神威计算处理单元（CPE）上执行的壁垒。我们进一步实现了三项有针对性的优化：(1) 向量化的基于哈希的回调分发，以削减运行时抽象开销；(2) 基于分块的并行任务映射算法，以提升灵活性与负载分布；(3) 一个快速设备调度库，以降低设备侧调度延迟。我们在多尺度场景下评估了 swKokkos 的性能。此外，swKokkos 相比主机后端最高实现 34.0 倍加速。与原生设备后端方案相比，其性能比为 0.7–2.8 倍，表明抽象开销较低，并且有时还通过改进调度反转为收益。特别地，swKokkos 在一个真实应用中高效且稳定地扩展到超过 100000 核的模拟规模，展示了其在神威百亿亿次超级计算机上支持极端规模模拟的能力。

**英文关键词：** High-performance computing, performance portability, Kokkos, Sunway architecture, parallel programming model

**中文关键词：** 高性能计算、性能可移植性、Kokkos、神威架构、并行编程模型

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
