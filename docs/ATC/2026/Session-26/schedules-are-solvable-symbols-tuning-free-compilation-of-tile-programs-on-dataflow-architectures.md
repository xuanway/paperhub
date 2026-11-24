# Schedules Are Solvable Symbols: Tuning-Free Compilation of Tile Programs on Dataflow Architectures

**中文标题**：调度是可求解的符号：数据流架构上分块程序的免调优编译

**所属 Session**：[Session 26: LLM Inference III](index.md) · [ATC 2026](../index.md)

**作者**：Heru Wang (National University of Singapore), Zhenyu Bai (National University of Singapore), Wei Li (National University of Singapore), Tulika Mitra (National University of Singapore)

## 英文摘要
Modern AI and HPC accelerators increasingly expose dataflow features: software-visible mechanisms for data movement and overlap, such as inter-core communication through the on-chip network and intra-core asynchronous pipelining. These features shift scheduling responsibility from hardware to the compiler, and—because placement, movement, and synchronization become software-visible— they also make the performance of static schedules predictable. Yet high performance on such hardware still relies on vendor-engineered kernel libraries or profile-based auto-tuning, whose embedded expert knowledge transfers poorly across architectures and algorithms. We present Loom, a tuning-free symbolic compiler framework for tile-based SPMD programs on spatial dataflow architectures. The central idea is to treat tile-based SPMD compilation as a hardware-explicit static optimization problem. Loom enumerates discrete spatial-mapping and communication candidates while keeping value parameters—such as tiling factors and pipeline knobs—symbolic within each candidate. From an explicit hardware description, it derives symbolic legality constraints and latency expressions, formulates one CP-SAT problem per schedule candidate, and jointly solves inter-core dataflow, intra-core asynchronous scheduling, and block sizes at compile time. Evaluated on two generations of Tenstorrent hardware (Wormhole/Blackhole), Loom achieves geometric-mean speedups of 0.99×/1.16× on GEMM, 2.29×/2.15× on Flash Attention, and 1.01×/1.17× on Flash Decode. These results suggest that hardware-derived symbolic compilation provides a retargetable alternative to profiling-based tuning for spatial dataflow architectures while remaining interpretable by keeping optimization decisions traceable to source-level symbols.

## 中文摘要
现代 AI 与 HPC 加速器越来越多地暴露数据流特性：软件可见的数据搬运与重叠机制，例如通过片上网络进行的核间通信以及核内异步流水线。这些特性将调度职责从硬件转移到编译器，并且——由于放置、搬运和同步变为软件可见——也使静态调度的性能变得可预测。然而，在此类硬件上获得高性能仍依赖厂商精心打造的 kernel 库或基于剖析的自动调优，而其中内嵌的专家知识难以在不同架构与算法之间迁移。我们提出 Loom，一个面向空间数据流架构上基于 tile 的 SPMD 程序的免调优符号编译框架。其核心思想是将基于 tile 的 SPMD 编译视为一个硬件显式的静态优化问题。Loom 枚举离散的空间映射与通信候选方案，同时在每个候选方案内部将取值参数——例如分块因子和流水线旋钮——保持为符号形式。它从显式的硬件描述中推导符号化的合法性约束与延迟表达式，为每个调度候选方案构造一个 CP-SAT 问题，并在编译期联合求解核间数据流、核内异步调度与块大小。在两代 Tenstorrent 硬件（Wormhole/Blackhole）上评测，Loom 在 GEMM 上取得 0.99×/1.16× 的几何平均加速，在 Flash Attention 上取得 2.29×/2.15×，在 Flash Decode 上取得 1.01×/1.17×。这些结果表明，硬件推导的符号化编译为空间数据流架构提供了一种可重定向的替代方案，以取代基于剖析的调优，同时通过使优化决策可追溯到源码级符号而保持可解释性。

## 英文关键词
Dataflow Architectures, Compiler Scheduling, Tile Programs

## 中文关键词
数据流架构，编译器调度，Tile 程序

[返回 Session 26](index.md) · [返回 ATC 2026](../index.md)
