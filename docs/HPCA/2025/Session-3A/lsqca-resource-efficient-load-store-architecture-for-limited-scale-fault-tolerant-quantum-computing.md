---
title: "LSQCA: Resource-Efficient Load/Store Architecture for Limited-Scale Fault-Tolerant Quantum Computing"
description: "HPCA 2025 · Quantum Slots"
tags:
  - "HPCA2025"
  - "Quantum Slots"
---

# LSQCA: Resource-Efficient Load/Store Architecture for Limited-Scale Fault-Tolerant Quantum Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Quantum Slots。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Quantum Slots</p>
</div>

**论文链接**：
**作者**：Takumi Kobori (Department of Physics, The University of Tokyo), Yasunari Suzuki (NTT Computer and Data Science Laboratories), Yosuke Ueno (RIKEN), Teruo Tanimoto (Kyushu University), Synge Todo (Department of Physics, The University of Tokyo), Yuuki Tokunaga (NTT Computer and Data Science Laboratories)
**会议**：HPCA 2025

---

## 中文标题

LSQCA：面向有限规模容错量子计算的资源高效加载/存储架构

## 英文摘要

Current fault-tolerant quantum computer (FTQC) architectures utilize several encoding techniques to enable reliable logical operations with restricted qubit connectivity. However, such logical operations demand additional memory overhead to ensure fault tolerance. Since the main obstacle to practical quantum computing is the limited qubit count, our primary mission is to design floorplans that can reduce memory overhead without compromising computational capability. Despite extensive efforts to explore FTQC architectures, even the current state-of-the-art floorplan strategy devotes 50% of memory space to this overhead, not to data storage, to guarantee unit-time random access to all logical qubits. In this paper, we propose an FTQC architecture based on a novel floorplan strategy, Load/Store Quantum Computer Architecture (LSQCA), which can achieve almost 100% memory density. The idea behind our architecture is to separate the whole memory regions into small computational space called Computational Registers (CR) and space-efficient memory space called Scan-Access Memory (SAM). We define an instruction set for these abstract structures and provide concrete designs named point-SAM and line-SAM architectures. With this design, we can improve the memory density by allowing variable-latency memory access while concealing the latency with other bottlenecks. We also propose optimization techniques to exploit properties of quantum programs observed in our static analysis, such as access locality in memory reference timestamps. Our numerical results indicate that LSQCA successfully leverages this idea. In a resource-restricted situation, a specific benchmark shows that we can achieve approximately 90% memory density with 5% increase in the execution time compared to a conventional floorplan, which achieves at most 50% memory density for unit-time random access. Our design is defined as an abstract form, making this principle ubiquitous and applicable to a wide range of quantum devices, qubit-connectivity configurations, and error-correcting codes.

## 中文摘要

容错量子计算机（FTQC）采用多种编码技术，以在受限连通性下实现可靠的逻辑操作，但这些操作需要额外存储开销来保证容错。由于量子比特数量有限是实用量子计算的主要障碍，我们的首要任务是设计不牺牲算力即可降低存储开销的布局方案。即使最先进的布局也要将 50% 的存储空间用于这种开销而非数据存储，以保证单位时间随机访问。本文提出基于新布局策略的 FTQC 架构——加载/存储量子计算机架构（LSQCA），可实现近 100% 的存储密度。其思路是把存储区域划分为计算寄存器（CR）与扫描访问存储器（SAM），并为这些抽象结构定义指令集，给出点-SAM 与线-SAM 两种设计。由此，我们允许可变时延的存储访问并用其他瓶颈掩盖时延，从而提高存储密度；我们还利用静态分析中观察到的量子程序特性（如存储引用的访问局部性）进行优化。数值结果表明，资源受限时某基准相比传统布局（最多 50% 存储密度）可在执行时间仅增 5% 时达到约 90% 存储密度。设计以抽象形式定义，可推广到多种量子器件、连通性配置与纠错码。
