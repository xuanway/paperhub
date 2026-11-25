---
title: "Proteus: Heterogeneous FPGA Virtualization"
description: "EuroSys 2026 · OS & Virtualization · Felix Gust (Technical University of Munich), Shu Anzai (University of California"
tags:
  - "EuroSys2026"
  - "OS & Virtualization"
---

# Proteus: Heterogeneous FPGA Virtualization

**中文标题：** Proteus：异构 FPGA 虚拟化

**所属 Session：** [Session 1.1: OS & Virtualization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：OS & Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · OS & Virtualization</p>
</div>

**作者**：Felix Gust (Technical University of Munich), Shu Anzai (University of California, Los Angeles), Charalampos Mainas (Technical University of Munich), Atsushi Koshiba (Tokyo University of Science), Pramod Bhatotia (Technical University of Munich)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803577)

## 英文摘要

Cloud providers have widely adopted FPGAs to meet the high-performance, energy-efficient demands of cloud workloads. While they offer homogeneous FPGAs per service, recent FPGA products exhibit increasing heterogeneity in terms of vendors, capacity, off-chip memory, and performance. These diverse properties not only render applications incompatible across different FPGAs but also lead to performance disparities and resource inefficiency.

To fill these gaps, we propose Proteus, a heterogeneous FPGA virtualization framework. Proteus allows applications to manage diverse FPGAs transparently by abstracting their properties with four key contributions: an FPGA virtualization stack to abstract different FPGA stacks from applications, a platform-agnostic API to manage FPGAs regardless of their vendors/architectures, memory virtualization to optimize memory allocation depending on the off-chip memory type, and a performance-aware scheduler to deploy applications on the best-suited FPGAs based on their predicted performance.

We implement Proteus for cross-vendor FPGAs: AMD (U50, U280) and Intel (Stratix 10). Our evaluation highlights that Proteus makes applications deployable on any FPGA with 4.9-6.8% overheads for AMD FPGAs, and the performance-aware scheduler yields 13.8% throughput gain on average.

## 中文摘要

云服务提供商已广泛采用 FPGA 以满足云工作负载的高性能、高能效需求。虽然它们为每项服务提供同构的 FPGA，但近期的 FPGA 产品在厂商、容量、片外内存和性能方面呈现出日益加剧的异构性。这些多样的特性不仅使应用无法在不同 FPGA 之间兼容，还导致性能差异和资源效率低下。

为填补这些空白，我们提出 Proteus，一个异构 FPGA 虚拟化框架。Proteus 通过四项关键贡献抽象 FPGA 的各种特性，使应用能够透明地管理多样的 FPGA：一个 FPGA 虚拟化栈，用于向应用抽象不同的 FPGA 栈；一个平台无关的 API，可在不考虑厂商/架构的情况下管理 FPGA；内存虚拟化，根据片外内存类型优化内存分配；以及一个性能感知调度器，根据预测性能将应用部署到最合适的 FPGA 上。

我们为跨厂商 FPGA 实现了 Proteus：AMD（U50、U280）和 Intel（Stratix 10）。评估表明，Proteus 使应用能够部署到任何 FPGA 上，在 AMD FPGA 上的开销为 4.9–6.8%，而性能感知调度器平均带来 13.8% 的吞吐量提升。

**英文关键词：** FPGA, operating systems, virtualization, orchestration, shell, schedulers, memory virtualization, heterogeneous systems

**中文关键词：** FPGA、操作系统、虚拟化、编排、shell、调度器、内存虚拟化、异构系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
