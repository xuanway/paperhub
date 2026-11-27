---
title: "Multi-Dimensional Vector ISA Extension for Mobile In-Cache Computing"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# Multi-Dimensional Vector ISA Extension for Mobile In-Cache Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Alireza Khadem (University of Michigan), Daichi Fujiki (Tokyo Institute of Technology), Hilbert Chen (University of Michigan), Yufeng Gu (University of Michigan), Nishil Talati (University of Michigan), Scott Mahlke (University of Michigan/Nvidia Research), Reetu Das (University of Michigan)
**会议**：HPCA 2025

---

## 中文标题

面向移动端缓存内计算的多维向量 ISA 扩展

## 英文摘要

In-cache computing technology transforms existing caches into long-vector compute units and offers low-cost alternatives to building expensive vector engines for mobile CPUs. Unfortunately, existing long-vector Instruction Set Architecture (ISA) extensions, such as RISC-V Vector Extension (RVV) and Arm Scalable Vector Extension (SVE), provide only one-dimensional strided and random memory accesses. While this is sufficient for typical vector engines, it fails to effectively utilize the large Single Instruction, Multiple Data (SIMD) widths of in-cache vector engines. This is because mobile data-parallel kernels expose limited parallelism across a single dimension. Based on our analysis of mobile vector kernels, we introduce a long-vector Multi-dimensional Vector ISA Extension (MVE) for mobile in-cache computing. MVE achieves high SIMD resource utilization and enables flexible programming by abstracting cache geometry and data layout. The proposed ISA features multi-dimensional strided and random memory accesses and efficient dimension-level masked execution to encode parallelism across multiple dimensions. Using a wide range of data-parallel mobile workloads, we demonstrate that MVE offers significant performance and energy reduction benefits of 2.9× and 8.8×, on average, compared to the SIMD units of a commercial mobile processor, at an area overhead of 3.6%.

## 中文摘要

缓存内计算技术将现有缓存转变为长向量计算单元，为移动 CPU 提供了构建昂贵向量引擎的低成本替代方案。然而，现有的长向量指令集架构（ISA）扩展，如 RISC-V 向量扩展（RVV）与 Arm 可伸缩向量扩展（SVE），只提供一维的跨步与随机内存访问。虽然这对典型的向量引擎已足够，却无法有效利用缓存内向量引擎的大单指令多数据（SIMD）宽度，因为移动端数据并行内核在单一维度上暴露的并行性有限。基于对移动端向量内核的分析，我们为移动端缓存内计算引入长向量多维向量 ISA 扩展（MVE）。MVE 通过抽象缓存几何结构与数据布局，实现了高 SIMD 资源利用率与灵活编程。所提出的 ISA 具备多维跨步与随机内存访问，以及高效的维度级掩码执行，可编码跨多个维度的并行性。使用广泛的数据并行移动端负载，我们证明：相较于商用移动处理器的 SIMD 单元，MVE 在 3.6% 的面积开销下带来平均 2.9× 的性能提升与 8.8× 的能耗降低。
