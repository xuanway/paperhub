---
title: "Cyclone: Designing Efficient and Highly Parallel QCCD Architectural Codesigns for Fault Tolerant Quantum Memory"
description: "HPCA 2026 · Quantum Computing Architecture"
tags:
  - "HPCA2026"
  - "Quantum Computing Architecture"
---

# Cyclone: Designing Efficient and Highly Parallel QCCD Architectural Codesigns for Fault Tolerant Quantum Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Computing Architecture。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Computing Architecture</p>
</div>

**论文链接**：
**作者**：Sahil Khan Duke University , Abhinav Anand Duke University , Kenneth R. Brown Duke University , Jonathan M. Baker University of Texas, Austin
**会议**：HPCA 2026

---

## 中文标题

Cyclone：面向容错量子存储器的高效高并行 QCCD 架构协同设计

## 英文摘要

Modular trapped-ion quantum computing hardware, known as Quantum Charge Coupled Devices (QCCDs) require shuttling operations in order to maintain effective all-to-all connectivity. Each module or trap can perform only one operation at a time, resulting in low intra-trap parallelism, but there is no restriction on operations happening on independent traps, enabling high inter-trap parallelism. Unlike their superconducting counterparts, the design space for QCCDs is relatively flexible and can be explored beyond the constraints of two-dimensional grids. In this work, we are motivated by the opportunity to explore the QCCD design space in the context of optimizing for non-topological CSS codes. In particular, current grid-based architectures significantly limit the performance of many promising, high-rate codes such as hypergraph product codes and bivariate bicycle codes. Many of these codes are highly parallelizable, meaning that with appropriate hardware layouts and matching software schedules, execution latency can be greatly reduced. Faster execution, in turn, reduces error accumulation from decoherence and heating, ultimately improving code performance when mapped to realistic hardware. However, current 2D grid designs suffer from numerous trap to trap “roadblocks”, forcing serialization and destroying the inherent parallelism of these codes. To address this, we propose Cyclone, a circular software-hardware codesign that departs from traditional 2D grids in favor of a flexible ring topology, where ancilla qubits move in lockstep. Cyclone eliminates roadblocks, bounds total movement, and enables high levels of parallelism, resulting in up to 4× speedup in execution times. In addition to temporal efficiency, Cyclone also offers large spatial efficiency when compared to a grid codesign. It requires fewer traps, fewer junctions, and only a constant number of Digital-to-Analog Converters (DAC), as opposed to grid architectures, where DAC count scales linearly with the number of traps. With hypergraph product codes, Cyclone achieves up to a 2× order of magnitude improvement in logical error rate, and with bivariate bicycle codes, this improvement reaches up to a 3× in order of magnitude. Spatially, Cyclone reduces the number of required traps and ancilla qubits by 2×. The overall spacetime improvement over a standard grid is up to ∼ 20×, demonstrating Cyclone as a scalable and efficient alternative to conventional 2D QCCD architectures.

## 中文摘要

模块化离子阱量子计算硬件（即量子电荷耦合器件，QCCD）需要穿梭操作以维持有效的全连接。每个模块或阱一次只能执行一个操作，阱内并行度低，但独立阱上的操作不受限制，可实现高阱间并行度。与超导器件不同，QCCD 的设计空间相对灵活，可突破二维网格的约束。本文在面向非拓扑 CSS 码优化的背景下探索该设计空间：当前基于网格的架构显著限制了许多有前景的高码率码（如超图乘积码与双变量自行车码）的性能，而这些码大多高度可并行，配合恰当的硬件布局与匹配的软件调度可大幅降低执行时延，从而减少退相干与加热造成的错误累积。然而 2D 网格设计存在大量阱间“路障”，迫使串行化并破坏这些码固有的并行性。为此我们提出 Cyclone，一种圆形的软硬件协同设计，以灵活的环形拓扑取代传统 2D 网格，辅助量子比特以锁步方式移动。Cyclone 消除路障、限定总移动量并实现高并行，使执行时间最多加速 4 倍。它还具有很高的空间效率：所需阱与交叉点更少，且只需常数个模数转换器（DAC），而网格架构中 DAC 数量随阱数线性增长。在超图乘积码上逻辑错误率最多改善 2 个数量级，双变量自行车码上最多改善 3 个数量级；所需阱数与辅助量子比特数减少 2 倍。相比标准网格，整体时空改善最多约 20 倍。
