---
title: "Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Ataberk Olgun (ETH Zürich), Nisa Bostanci (ETH Zürich), Ismail Emir Yuksel (ETH Zürich), Giray Yaglikci (ETH Zürich), Geraldo F. Oliveira (ETH Zürich), Haocong Luo (ETH Zürich), Oguzhan Canpolat (ETH Zürich), Minesh Patel (Rutgers University), Onur Mutlu (ETH Zürich)
**会议**：HPCA 2025

---

## 中文标题

可变读干扰：DRAM 读干扰时间变化的实验分析

## 英文摘要

Modern DRAM chips are subject to read disturbance errors. These errors manifest as security-critical bitflips in a victim DRAM row that is physically nearby a repeatedly activated (opened) aggressor row (RowHammer) or an aggressor row that is kept open for a long time (RowPress). State-of-the-art read disturbance mitigations rely on accurate and exhaustive characterization of the read disturbance threshold (RDT) (e.g., the number of aggressor row activations needed to induce the first RowHammer or RowPress bitflip) of every DRAM row (of which there are millions or billions in a modern system) to prevent read disturbance bitflips securely and with low overhead. We experimentally demonstrate for the first time that the RDT of a DRAM row significantly and unpredictably changes over time. We call this new phenomenon variable read disturbance (VRD). Our extensive experiments using 160 DDR4 chips and 4 HBM2 chips from three major manufacturers yield three key observations. First, it is very unlikely that relatively few RDT measurements can accurately identify the RDT of a DRAM row. The minimum RDT of a DRAM row appears after tens of thousands of measurements (e.g., up to 94,467), and the minimum RDT of a DRAM row is 3.5× smaller than the maximum RDT observed for that row. Second, the probability of accurately identifying a row’s RDT with a relatively small number of measurements reduces with increasing chip density or smaller technology node size. Third, data pattern, the amount of time an aggressor row is kept open, and temperature can affect the probability of accurately identifying a DRAM row’s RDT. Our empirical results have implications for the security guarantees of read disturbance mitigation techniques: if the RDT of a DRAM row is not identified accurately, these techniques can easily become insecure. We discuss and evaluate using a guardband for RDT and error-correcting codes for mitigating read disturbance bitflips in the presence of RDTs that change unpredictably over time. We conclude that a >10% guardband for the minimum observed RDT combined with SECDED or Chipkill-like SSC error-correcting codes could prevent read disturbance bitflips at the cost of large read disturbance mitigation performance overheads (e.g., 45% performance loss for an RDT guardband of 50%). We hope and believe future work on efficient online profiling mechanisms and configurable read disturbance mitigation techniques could remedy the challenges imposed on today’s read disturbance mitigations by the variable read disturbance phenomenon.

## 中文摘要

现代 DRAM 芯片会遭受读干扰错误，表现为受害 DRAM 行中的安全相关位翻转，该行物理上邻近被反复激活（打开）的攻击者行（Rowhammer），或邻近长期保持打开的攻击者行（RowPress）。最先进的缓解手段依赖对每个 DRAM 行（现代系统中有数百万至数十亿行）的读干扰阈值（RDT，即引发首个 Rowhammer 或 RowPress 位翻转所需的攻击者行激活次数）进行准确而详尽的表征，才能安全低开销地防止位翻转。我们首次通过实验证明，DRAM 行的 RDT 会随时间显著且不可预测地变化，并称之为可变读干扰（VRD）。基于三家主要厂商的 160 颗 DDR4 与 4 颗 HBM2 芯片的大量实验给出三点观察：其一，用少量测量几乎不可能准确确定某行 RDT，其最小值常在数万次测量（如多达 94,467 次）后才出现，且比该行最大 RDT 小 3.5×；其二，芯片密度增大或工艺节点缩小时，用较少测量准确确定 RDT 的概率降低；其三，数据模式、攻击者行保持打开的时间与温度都会影响该概率。这些结果对缓解技术的安全保证有直接含义：若 RDT 未被准确确定，技术很容易变得不安全。我们讨论并评估了以 RDT 保护带与纠错码缓解位翻转的方案，结论是对最小观测 RDT 采用 >10% 的保护带并结合 SECDED 或类 Chipkill 的 SSC 纠错码可防止位翻转，但代价是巨大的性能开销（如 50% 的 RDT 保护带导致 45% 的性能损失）。我们希望未来关于高效在线剖析与可配置缓解技术的工作能应对该现象带来的挑战。
