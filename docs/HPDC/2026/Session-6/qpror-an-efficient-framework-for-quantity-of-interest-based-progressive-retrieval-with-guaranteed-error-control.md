---
title: "QProR: An Efficient Framework for Quantity-of-Interest Based Progressive Retrieval with Guaranteed Error Control"
description: "HPDC 2026 · Session 6 — Scientific Data Compression"
tags:
  - "HPDC2026"
  - "Session 6"
  - "Scientific Data Compression"
---

# QProR: An Efficient Framework for Quantity-of-Interest Based Progressive Retrieval with Guaranteed Error Control

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 6</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807579)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#LiGWCLHPKL26](https://dblp.org/db/conf/hpdc/hpdc2026.html#LiGWCLHPKL26)

**作者**：Wenbo Li, Qian Gong, Xuan Wu, Jieyang Chen, Qing Liu, Xubin He, Norbert Podhorszki, Scott Klasky, Xin Liang

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）

---

## 英文摘要

Scientific applications generate an unprecedented volume of data, overwhelming the network and file systems’ bandwidth and posing challenges for efficient and scalable data retrieval and analysis. Progressive data compression offers a promising solution by enabling on-demand retrieval at reduced size. However, existing progressive methods either fail to bound the errors in essential quantities of interest (QoIs) derived from raw data or suffer from suboptimal retrieval efficiency. In this work, we propose QProR, an efficient QoI-based progressive framework that optimizes progressive retrieval for target QoIs. Our key contributions include: (1) a systematic framework that integrates error-controlled lossy compressors with bitplane encoding while decoupling the two processes for high flexibility and adaptability; (2) a novel weighted bitplane encoding method which incorperates QoI knowledge into data refactoring to enhance retrieval efficiency; (3) an optimized retrieval strategy that accounts for the varying impacts of different variables on multivariate QoIs; (4) comprehensive evaluations using six real-world datasets from multiple scientific applications and thorough comparisons against state of the arts. Experimental results demonstrate that QProR achieves up to 80.38% reduction in the retrieval size under the same requested QoI error tolerance, when compared with the best-performing existing methods. When transferring 384 GB of scientific data to remote sites, QProR delivers up to 1.68× speedup in the end-to-end data transfer performance.

## 中文摘要

科学应用产生前所未有的数据量，压垮网络与文件系统的带宽，给高效、可扩展的数据检索与分析带来挑战。渐进式数据压缩通过支持以缩减的规模按需检索，提供了有前景的解决方案。然而，现有渐进式方法要么无法约束从原始数据导出的关键关注量（QoI）上的误差，要么检索效率欠佳。在本工作中，我们提出 QProR，一个高效的基于 QoI 的渐进式框架，针对目标 QoI 优化渐进式检索。我们的主要贡献包括：(1) 一个系统化框架，将误差控制的有损压缩器与位平面编码相结合，同时将两个过程解耦以保持高灵活性与适应性；(2) 一种新颖的加权位平面编码方法，将 QoI 知识融入数据重构以提升检索效率；(3) 一种优化的检索策略，考虑不同变量对多变量 QoI 的不同影响；(4) 使用来自多个科学应用的六个真实数据集进行全面评估，并与最先进方法进行详尽比较。实验结果表明，在相同的请求 QoI 误差容限下，与表现最佳的现有方法相比，QProR 将检索规模最高减少 80.38%。在向远程站点传输 384 GB 科学数据时，QProR 的端到端数据传输性能最高提升 1.68 倍。

---

[← 返回 Session 6 — Scientific Data Compression](index.md)
