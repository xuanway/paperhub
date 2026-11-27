---
title: "Toward Scalable Gate-Level Parallelism on Trapped-Ion Processors with Racetrack Electrodes"
description: "HPCA 2026 · Quantum Computing Architecture"
tags:
  - "HPCA2026"
  - "Quantum Computing Architecture"
---

# Toward Scalable Gate-Level Parallelism on Trapped-Ion Processors with Racetrack Electrodes

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Computing Architecture。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Computing Architecture</p>
</div>

**论文链接**：
**作者**：Enhyeok Jang Yonsei University , Hyungseok Kim Yonsei University , Yongju Lee Yonsei University , Jaewon Kwon Yonsei University , Yipeng Huang Rutgers University , Won Woo Ro Yonsei University
**会议**：HPCA 2026

---

## 中文标题

迈向基于跑道形电极的离子阱处理器的可扩展门级并行

## 英文摘要

A recent advancement in quantum computing shows a quantum advantage of certified randomness on the racetrack processor. This work investigates the execution efficiency of this architecture for general-purpose programs. We first explore the impact of increasing zones on runtime efficiency. Counterintuitively, our evaluations using variational programs reveal that expanding zones may degrade runtime performance under the existing scheduling policy. This degradation may be attributed to the increase in track length, which increases ion circulation overhead, offsetting the benefits of enhanced parallelism. To mitigate this, the proposed Plutarch exploits 3 strategies: (i) unitary decomposition and translation to maximize zone utilization, (ii) prioritizing the execution of nearby gates over ion circulation, and (iii) implementing shortcuts to provide the alternative path.

## 中文摘要

量子计算近期的进展显示，跑道形处理器上可实现可认证随机性的量子优势。本文研究该架构运行通用程序的执行效率。我们首先探讨增加区域数量对运行时效率的影响。与直觉相反，我们使用变分程序进行的评估表明，在现有调度策略下扩展区域反而可能降低运行时性能。这种退化可能归因于轨道长度增加，使离子绕行开销上升，抵消了并行性增强带来的收益。为缓解该问题，所提出的 Plutarch 采用三种策略：(i) 酉分解与转换，以最大化区域利用率；(ii) 优先执行邻近的门而非进行离子绕行；(iii) 实现捷径以提供替代路径。
