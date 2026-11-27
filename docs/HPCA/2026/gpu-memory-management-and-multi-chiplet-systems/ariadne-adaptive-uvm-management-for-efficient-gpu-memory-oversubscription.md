---
title: "ARIADNE: Adaptive UVM Management for Efficient GPU Memory Oversubscription"
description: "HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems"
tags:
  - "HPCA2026"
  - "GPU Memory Management and Multi-Chiplet Systems"
---

# ARIADNE: Adaptive UVM Management for Efficient GPU Memory Oversubscription

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Memory Management and Multi-Chiplet Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems</p>
</div>

**论文链接**：
**作者**：Hyunkyun Shin Yonsei University , Seongtae Bang DGIST , Hyungwon Park DGIST , Daehoon Kim Yonsei University
**会议**：HPCA 2026

---

## 中文标题

ARIADNE：面向高效 GPU 内存超额订阅的自适应 UVM 管理

## 英文摘要

Unified Virtual Memory (UVM) simplifies GPU programming and supports memory oversubscription, but suffers from severe performance degradation under high memory pressure due to page fault overhead and thrashing. Existing approaches such as prefetching, access counter-based migration, and dynamic Zero-copy offer limited benefits and often require hardware or compiler modifications, undermining UVM’s portability and ease of deployment. We present ARIADNE, a run-time UVM management framework that preserves UVM’s GPU memory abstraction while ensuring high and robust performance under memory oversubscription. ARIADNE is guided by three principles: (1) pipelined fault handling to hide migration latency, (2) Sharing Degree, a runtime metric that captures thread-level access locality without requiring hardware or compiler changes, to inform placement decisions, and (3) dynamic placement of memory regions between GPU memory and Zero-copy based on real-time access patterns. Implemented entirely within NVIDIA’s UVM driver, ARIADNE requires no recompilation or hardware modifications and applies transparently to any executable or closed-source GPU UVM applications. Our experimental results show that ARIADNE delivers average speedups of 1.9×, 5.0×, and 4.8× over a state-of-the-art method at 130%, 175%, and 300% oversubscription, respectively, while effectively preventing thrashing and maintaining near-linear performance scaling.

## 中文摘要

统一虚拟内存（UVM）简化了 GPU 编程并支持内存超额订阅，但在高内存压力下会因缺页开销与抖动而出现严重性能退化。现有方法如预取、基于访问计数器的迁移以及动态 Zero-copy 收益有限，且往往需要修改硬件或编译器，损害了 UVM 的可移植性与易部署性。我们提出 ARIADNE，一个运行时 UVM 管理框架，在保留 UVM 的 GPU 内存抽象的同时，确保在内存超额订阅下仍具有高且稳健的性能。ARIADNE 遵循三条原则：(1) 流水化缺页处理以隐藏迁移时延；(2) 引入共享度（Sharing Degree）这一运行时度量，无需硬件或编译器改动即可刻画线程级访问局部性，用以指导放置决策；(3) 依据实时访问模式在 GPU 内存与 Zero-copy 之间动态放置内存区域。ARIADNE 完全实现在 NVIDIA 的 UVM 驱动内，无需重新编译或修改硬件，并可透明地适用于任何可执行文件或闭源 GPU UVM 应用。实验结果表明，在 130%、175% 和 300% 超额订阅下，ARIADNE 相比最先进方法分别取得 1.9 倍、5.0 倍和 4.8 倍的平均加速比，同时有效防止抖动并保持接近线性的性能扩展。
