---
title: "Deadlock-Free Bridge Module for Inter-Chiplet Communication in Open Chiplet Ecosystem"
description: "HPCA 2026 · Cache Coherence and Chiplet Interconnects"
tags:
  - "HPCA2026"
  - "Cache Coherence and Chiplet Interconnects"
---

# Deadlock-Free Bridge Module for Inter-Chiplet Communication in Open Chiplet Ecosystem

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Cache Coherence and Chiplet Interconnects。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Cache Coherence and Chiplet Interconnects</p>
</div>

**论文链接**：
**作者**：Zhiqiang Chen National University of Defense Technology , Wenwen Fu National University of Defense Technology , Yongwen Wang National University of Defense Technology , Hongwei Zhou National University of Defense Technology
**会议**：HPCA 2026

---

## 中文标题

开放芯粒生态中面向芯粒间通信的无死锁桥接模块

## 英文摘要

The envisioned open chiplet ecosystem promises significant reductions in chip design complexity and cost by enabling designers to rapidly assemble standard chiplets from diverse vendors. Constructing such an open chiplet ecosystem requires support from Network-on-Chip (NoC) routing algorithms, as integrating multiple chiplets onto an interposer can potentially lead to inter-chiplet deadlock. Prior work avoids deadlock through methods like turn restrictions, virtual channel isolation, or packet injection control, or recovers from deadlock using mechanisms such as escape channels or bubble flow control. These approaches achieve a favorable balance regarding modularity, performance, and cost. However, they still rely on designers possessing detailed knowledge of the internal NoC architecture within each chiplet. This requirement impedes the development of a truly open ecosystem, as it constrains chiplet interoperability and vendor independence. Addressing this limitation, we propose a Deadlock-Free Bridge Module (DFBM) designed to resolve inter-chiplet deadlock without relying on the specifics of individual chiplet NoC implementations. The DFBM infers the transmission behavior of inter-chiplet packets by analyzing the dependency relationships among coherence protocol transaction flows. It then employs a packet injection control mechanism to isolate inter- and intra-chiplet packets, thereby preventing deadlock. DFBMs can be seamlessly interconnected between arbitrary chiplets to achieve deadlock-freedom, eliminating the need for modifications to their internal NoC architectures. Experimental results demonstrate that DFBM incurs only 2.5% area overhead, while achieving a performance improvement ranging from 1% to 7%.

## 中文摘要

设想的开放芯粒生态有望通过让设计者快速组装来自不同厂商的标准芯粒，显著降低芯片设计复杂度与成本。构建这样的开放芯粒生态需要片上网络（NoC）路由算法的支持，因为将多个芯粒集成到中介层上可能导致芯粒间死锁。已有工作通过转弯限制、虚拟通道隔离或报文注入控制等方法避免死锁，或借助逃生通道、气泡流控等机制从死锁中恢复。这些方法在模块化、性能与成本之间取得了良好平衡。然而，它们仍要求设计者掌握每个芯粒内部 NoC 架构的详细信息。这一要求阻碍了真正开放生态的发展，因为它限制了芯粒的互操作性与厂商独立性。针对该局限，我们提出无死锁桥接模块（DFBM），旨在不依赖各芯粒 NoC 具体实现的前提下解决芯粒间死锁。DFBM 通过分析一致性协议事务流之间的依赖关系推断芯粒间报文的传输行为，进而采用报文注入控制机制隔离芯粒间与芯粒内报文，从而防止死锁。DFBM 可无缝互连于任意芯粒之间以实现无死锁，无需修改其内部 NoC 架构。实验结果表明，DFBM 仅带来 2.5% 的面积开销，同时取得 1% 至 7% 的性能提升。
