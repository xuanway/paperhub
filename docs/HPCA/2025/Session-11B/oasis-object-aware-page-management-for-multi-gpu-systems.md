---
title: "OASIS: Object-Aware Page Management for Multi-GPU Systems"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# OASIS: Object-Aware Page Management for Multi-GPU Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Yueqi Wang (University of Pittsburgh), Bingyao Li (University of Pittsburgh), Mohamed Tarek Ibn Ziad (NVIDIA), Lieven Eeckhout (Ghent University), Jun Yang (University of Pittsburgh), Aamer Jaleel (NVIDIA), Xulong Tang (University of Pittsburgh)
**会议**：HPCA 2025

---

## 中文标题

OASIS：面向多 GPU 系统的对象感知页管理

## 英文摘要

The ever-growing need for high-performance computing has driven the popularity of employing multi-GPU systems. Modern multi-GPU systems employ unified virtual memory (UVM) to manage page placement and migration. However, the page management in UVM is application object agnostic. In this paper, we characterize the page access behaviors in relation to the application objects, and reveal that the beneficial page management policy varies according to (i) the different data objects within the same application, and (ii) the different execution phases of the same object. This motivates the need for dynamic and proactive page management in multi-GPU systems. To this end, we propose OASIS, which dynamically identifies object patterns during the execution and proactively determines the appropriate page management policies for these objects at runtime. Experimental results show that OASIS improves the performance over uniformly adopting on-touch migration, access counter-based migration, and duplication by an average of 64%, 35%, and 42%, respectively. Moreover, OASIS achieves a 12% performance improvement over the state-of-the-art technique (i.e., GRIT) while having significantly lower design complexity.

## 中文摘要

对高性能计算不断增长的需求推动了多 GPU 系统的广泛普及。现代多 GPU 系统采用统一虚拟内存（UVM）来管理页面的放置与迁移。然而，UVM 中的页管理与应用对象无关。本文刻画了与应用对象相关的页面访问行为，并揭示出：有益的页管理策略会随（i）同一应用内不同的数据对象，以及（ii）同一对象的不同执行阶段而变化。这促使多 GPU 系统亟需动态且主动的页管理策略。为此，我们提出 OASIS，它在执行过程中动态识别对象模式，并在运行时主动为这些对象确定合适的页管理策略。实验结果表明，与统一采用 on-touch 迁移、基于访问计数器的迁移与复制相比，OASIS 的性能平均分别提升 64%、35% 和 42%。此外，OASIS 相较最先进的技术（即 GRIT）实现了 12% 的性能提升，同时设计复杂度显著更低。
