---
title: "IPComp: Interpolation Based Progressive Lossy Compression for Scientific Applications"
description: "HPDC 2025 · Session 7 — Best Paper and Best Student Paper Finalists"
tags:
  - "HPDC2025"
  - "Session 7"
  - "Best Paper and Best Student Paper Finalists"
---

# IPComp: Interpolation Based Progressive Lossy Compression for Scientific Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 7</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731578) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/yang.pdf)

**作者**：Zhuoxun Yang, Sheng Di, Longtao Zhang, Ruoyu Li, Ximiao Li, Jiajun Huang, Jinyang Liu, Franck Cappello, Kai Zhao

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 7 — Best Paper and Best Student Paper Finalists（2025年7月23日 13:00–14:30 · Session Chair：Robert Wisniewski）

**荣誉**：HPDC 2025 最佳论文入围（Best Paper Finalist）

---

## 英文摘要

Compression is a crucial solution for data reduction in modern scientific applications due to the exponential growth of data from simulations, experiments, and observations. Compression with progressive retrieval capability allows users to quickly access coarse approximations of data and then incrementally refine these approximations to higher fidelity. Existing progressive compression solutions suffer from low reduction ratios or high operation costs, effectively undermining the approach’s benefits. In this paper, we propose our interpolation-based progressive lossy compression solution that has both high reduction ratios and low operation costs. The interpolation-based algorithm has been verified as one of the best for scientific data reduction, but previously, no effort exists to make it support progressive retrieval. Our contributions are threefold: (1) We thoroughly analyze the error characteristics of the interpolation algorithm and propose our solution, IPComp, with multi-level bitplane and predictive coding. (2) We derive optimized strategies toward minimum data retrieval under different fidelity levels indicated by users through error bounds and bitrates. (3) We evaluate the proposed solution using six real-world datasets from four diverse domains. Experimental results demonstrate our solution archives up to 487% higher compression ratios and 698% faster speed than other state-of-the-art progressive compressors, and reduces the data volume for retrieval by up to 83% compared to baselines under the same error bound, and reduces the error by up to 99% under the same bitrate.

## 中文摘要

由于仿真、实验与观测产生的数据呈指数级增长，压缩已成为现代科学应用中数据缩减的关键方案。具备渐进式检索能力的压缩允许用户快速访问数据的粗近似，再逐步将这些近似精化到更高保真度。现有渐进式压缩方案存在压缩比低或操作成本高的问题，实际上削弱了该方法的收益。本文提出基于插值的渐进式有损压缩方案，兼具高压缩比与低操作成本。基于插值的算法已被验证为科学数据缩减的最佳方法之一，但此前尚无工作使其支持渐进式检索。我们的贡献有三方面：(1) 我们深入分析了插值算法的误差特性，并提出采用多级位平面与预测编码的方案 IPComp；(2) 我们推导了优化策略，以在用户通过误差界与比特率指定的不同保真度级别下实现最小数据检索；(3) 我们使用来自四个不同领域的六个真实数据集评估所提方案。实验结果表明，与其他最先进的渐进式压缩器相比，我们的方案压缩比最高提升 487%、速度最高提升 698%，在相同误差界下将检索数据量最多减少 83%，在相同比特率下将误差最多降低 99%。

## 英文关键词

error-bounded lossy compression, scientific data management

## 中文关键词

误差有界有损压缩，科学数据管理

---

[← 返回 Session 7 — Best Paper and Best Student Paper Finalists](index.md)
