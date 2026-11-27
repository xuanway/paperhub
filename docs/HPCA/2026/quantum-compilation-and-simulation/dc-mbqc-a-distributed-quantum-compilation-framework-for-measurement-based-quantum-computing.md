---
title: "DC-MBQC: A Distributed Quantum Compilation Framework for Measurement-Based Quantum Computing"
description: "HPCA 2026 · Quantum Compilation and Simulation"
tags:
  - "HPCA2026"
  - "Quantum Compilation and Simulation"
---

# DC-MBQC: A Distributed Quantum Compilation Framework for Measurement-Based Quantum Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Compilation and Simulation。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Compilation and Simulation</p>
</div>

**论文链接**：
**作者**：Yecheng Xue Peking University , Rui Yang Peking University , Zhiding Liang The Chinese University of Hong Kong , Tongyang Li Peking University
**会议**：HPCA 2026

---

## 中文标题

DC-MBQC：面向基于测量的量子计算的分布式量子编译框架

## 英文摘要

Distributed quantum computing (DQC) is a promising technique for scaling up quantum systems. While significant progress has been made in DQC for quantum circuit models, there exists much less research on DQC for measurement-based quantum computing (MBQC), which is a universal quantum computing model that is essentially different from the circuit model and particularly well-suited to photonic quantum platforms. In this paper, we propose DC-MBQC, the first distributed quantum compilation framework tailored for MBQC. We identify and address two key challenges in enabling DQC for MBQC. First, for task allocation among quantum processing units (QPUs), we develop an adaptive graph partitioning algorithm that preserves the structure of the graph state while balancing the workload across QPUs. Second, for inter-QPU communication, we introduce the layer scheduling problem and propose an algorithm to solve it. Regrading realistic hardware requirements, we optimize the execution time of running quantum programs and the corresponding required photon lifetime to avoid fatal failures caused by photon loss. Our experiments demonstrate a 7.46× improvement on required photon lifetime and 6.82× speedup with 8 fully-connected QPUs, which further confirm the advantage of distributed quantum computing in photonic systems.

## 中文摘要

分布式量子计算（DQC）是扩展量子系统规模的一项有前景的技术。面向量子线路模型的 DQC 已取得显著进展，但面向基于测量的量子计算（MBQC）的 DQC 研究少得多——MBQC 是一种本质上不同于线路模型的通用量子计算模型，尤其适合光子量子平台。本文提出 DC-MBQC，首个为 MBQC 量身定制的分布式量子编译框架。我们识别并解决了实现 MBQC 分布式计算的两个关键挑战。首先，针对量子处理单元（QPU）间的任务分配，我们提出自适应图划分算法，在保持图态结构的同时均衡各 QPU 的负载。其次，针对 QPU 间通信，我们提出层调度问题并给出求解算法。面向真实硬件需求，我们优化量子程序的执行时间与相应的所需光子寿命，以避免光子丢失导致的致命失败。实验表明，在 8 个全连接 QPU 上，所需光子寿命提升 7.46 倍、加速比达 6.82 倍，进一步印证了分布式量子计算在光子系统中的优势。
