---
title: "QPRAC: Towards Secure and Practical PRAC-based Rowhammer Mitigation using Priority Queues"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# QPRAC: Towards Secure and Practical PRAC-based Rowhammer Mitigation using Priority Queues

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Jeonghyun Woo (The University of British Columbia (UBC)), Shaopeng (Chris) Lin (University of Toronto), Prashant J. Nair (The University of British Columbia (UBC)), Aamer Jaleel (NVIDIA), Gururaj Saileshwar (University of Toronto)
**会议**：HPCA 2025

---

## 中文标题

QPRAC：基于优先级队列的安全实用 PRAC Rowhammer 缓解

## 英文摘要

JEDEC has introduced the Per Row Activation Counting (PRAC) framework for DDR5 and future DRAMs to enable precise counting of DRAM row activations. PRAC enables a holistic mitigation of Rowhammer attacks even at ultra-low Rowhammer thresholds. PRAC uses an Alert Back-Off (ABO) protocol to request the memory controller to issue Rowhammer mitigation requests. However, recent PRAC implementations are either insecure or impractical. For example, Panopticon, the inspiration for PRAC, is rendered insecure if implemented per JEDEC’s PRAC specification. On the other hand, the recent UPRAC proposal is impractical since it needs oracular knowledge of the ‘top-N’ activated DRAM rows that require mitigation. This paper provides the first secure, scalable, and practical RowHammer solution using the PRAC framework. The crux of our proposal is the design of a priority-based service queue (PSQ) for mitigations that prioritizes pending mitigations based on activation counts to avoid the security risks of prior solutions. This provides principled security using the reactive ABO protocol. Furthermore, we co-design our PSQ, with opportunistic mitigation on Refresh Management (RFM) operations and proactive mitigation during refresh (REF), to limit the performance impact of ABO-based mitigations. QPRAC provides secure and practical RowHammer mitigation that scales to Rowhammer thresholds as low as 71 while incurring a 0.8% slowdown for benign workloads, which further reduces to 0% with proactive mitigations.

## 中文摘要

JEDEC 为 DDR5 及未来 DRAM 引入了逐行激活计数（PRAC）框架，可精确统计 DRAM 行的激活次数，即使面对超低 Rowhammer 阈值也能实现整体性缓解。PRAC 使用告警退避（ABO）协议请求内存控制器发出 Rowhammer 缓解请求。然而近期的 PRAC 实现要么不安全、要么不实用：例如作为 PRAC 灵感来源的 Panopticon 若按 JEDEC 的 PRAC 规范实现便不再安全；近期的 UPRAC 方案则需要预知需缓解的“前 N 个”被激活 DRAM 行，因而难以实用。本文给出首个基于 PRAC 框架的安全、可扩展且实用的 Rowhammer 方案。其核心是为缓解设计基于优先级的服务队列（PSQ），依据激活次数对挂起的缓解排序，从而避免先前方案的安全风险，并在采用反应式 ABO 协议的同时提供有原则的安全保障。此外，我们将 PSQ 与刷新管理（RFM）操作上的机会式缓解以及刷新（REF）期间的前摄缓解协同设计，以限制基于 ABO 的缓解带来的性能影响。QPRAC 提供安全实用的 Rowhammer 缓解，可扩展至低至 71 的阈值，而良性负载的性能下降仅 0.8%，采用前摄缓解后进一步降至 0%。
