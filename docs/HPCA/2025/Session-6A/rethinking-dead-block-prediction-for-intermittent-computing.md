---
title: "Rethinking Dead Block Prediction for Intermittent Computing"
description: "HPCA 2025 · Cacheno Royale"
tags:
  - "HPCA2025"
  - "Cacheno Royale"
---

# Rethinking Dead Block Prediction for Intermittent Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Cacheno Royale。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Cacheno Royale</p>
</div>

**论文链接**：
**作者**：Gan Fang (Purdue University), Changhee Jung (Purdue University)
**会议**：HPCA 2025

---

## 中文标题

重新审视面向间歇计算的死块预测

## 英文摘要

Existing dead block predictors have proven to be effective in reducing cache leakage power of conventional systems. However, prior work is significantly less effective in energy harvesting systems in that it does not take into account their unique characteristic, i.e., frequent power failure during program execution. Even if some cache blocks are predicted to be live, they may not be used due to their loss upon power failure. In response, this paper introduces EDBP, an extension to existing dead block predictors, to enhance their performance in various energy harvesting environments. EDBP can identify and deactivate those cache blocks that are not reused before upcoming power failure—though they are considered live by the existing predictor—thereby lowering cache leakage and preserving more energy for forward execution progress. Experimental results show that for 20 applications from Mediabench and MiBench, EDBP alone reduces total energy consumption by 6.5% and improves performance by 6.9% compared to the baseline with no dead block predictor. When combined with a conventional dead block predictor (Cache Decay), EDBP achieves 9.8% reduction in total energy consumption—approaching the theoretical minimum— and 11.9% performance improvement.

## 中文摘要

现有死块预测器已被证明能有效降低传统系统的缓存漏电功耗。然而，先前工作在能量收集系统中效果显著变差，因为它没有考虑这些系统的独特特性，即程序执行期间频繁的掉电。即使某些缓存块被预测为存活，它们也可能因掉电丢失而未被使用。为此，本文提出 EDBP，即对现有死块预测器的扩展，以增强其在各种能量收集环境中的性能。EDBP 能够识别并停用那些在即将到来的掉电之前不会被复用的缓存块——尽管现有预测器认为它们是存活的——从而降低缓存漏电并为前向执行进展保留更多能量。实验结果表明，对于来自 Mediabench 与 MiBench 的 20 个应用，与没有死块预测器的基线相比，单独使用 EDBP 可降低 6.5% 的总能耗并提升 6.9% 的性能。当与传统死块预测器（Cache Decay）结合时，EDBP 实现 9.8% 的总能耗降低——接近理论下界——以及 11.9% 的性能提升。
