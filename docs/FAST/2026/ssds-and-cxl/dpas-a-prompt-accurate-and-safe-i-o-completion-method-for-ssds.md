---
title: "DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs"
description: "FAST 2026 · SSDs and CXL · 第 381–398 页"
tags:
  - "FAST2026"
  - "SSDs and CXL"
---

# DPAS: A Prompt, Accurate and Safe I/O Completion Method for SSDs

**中文标题**：DPAS：一种及时、准确且安全的 SSD I/O 完成方法

**Session**：SSDs and CXL · 2026-02-25 14:00–15:40 · Chair：Ethan Miller（University of California, Santa Cruz, and Pure Storage）

**作者**：Dongjoo Seo, University of California, Irvine; Jihyeon Jung and Yeohwan Yoon, Kookmin University; Ping-Xiang Chen, University of California, Irvine; Yongsoo Joo and Sung-Soo Lim, Kookmin University; Nikil Dutt, University of California, Irvine

**会议**：FAST 2026 · Santa Clara, CA · 第 381–398 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/seo](https://www.usenix.org/conference/fast26/presentation/seo)

**论文 PDF**：[fast26-seo.pdf](https://www.usenix.org/system/files/fast26-seo.pdf)

---

## 英文摘要

Modern SSDs demand faster I/O completion methods. While polling is a potential alternative to interrupts, it suffers under CPU contention. Hybrid polling mitigates this by sleeping early and polling later, yet it cannot keep up with rapidly varying I/O latencies and incurs context-switch overheads. We introduce PAS, an accurate latency tracking method for hybrid polling that adjusts sleep duration using the two most recent I/Os, and DPAS, which dynamically switches among polling, interrupts, and PAS to overcome the inherent drawbacks of hybrid polling. Experiments show that PAS reduces CPU usage by 21 percentage points compared to Linux hybrid polling for 4 KB random reads, and DPAS improves YCSB performance by 9% on a 3D XPoint SSD and 5% on a TLC NAND SSD, even under simultaneous CPU contention and I/O interference.

## 中文摘要

现代 SSD 需要更快的 I/O 完成方法。轮询是中断的一种潜在替代方案，但在 CPU 竞争下表现不佳。混合轮询通过先睡眠、后轮询来缓解这一问题，但它无法跟上快速变化的 I/O 延迟，并且会带来上下文切换开销。我们提出 PAS，一种用于混合轮询的准确延迟跟踪方法，它利用最近两次 I/O 调整睡眠时长；并提出 DPAS，它在轮询、中断和 PAS 之间动态切换，以克服混合轮询的固有缺陷。实验表明，对于 4 KB 随机读，PAS 相比 Linux 混合轮询将 CPU 使用率降低 21 个百分点；即使在 CPU 竞争和 I/O 干扰同时存在的情况下，DPAS 也能在 3D XPoint SSD 上将 YCSB 性能提升 9%，在 TLC NAND SSD 上提升 5%。
