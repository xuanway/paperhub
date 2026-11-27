---
title: "BASES: Enabling Energy-Efficient and Error-Resilient Analog CIM Acceleration via Reformation of Coding Bases"
description: "HPCA 2026 · Emerging Compute Paradigms"
tags:
  - "HPCA2026"
  - "Emerging Compute Paradigms"
---

# BASES: Enabling Energy-Efficient and Error-Resilient Analog CIM Acceleration via Reformation of Coding Bases

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Emerging Compute Paradigms。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Emerging Compute Paradigms</p>
</div>

**论文链接**：
**作者**：hongrui guo Institute of Computing Technology, Chinese Academy of Sciences , Tianrui Ma Institute of Computing Technology, Chinese Academy of Sciences , zidong du Institute of Computing Technology, Chinese Academy of Sciences , Mo Zou Institute of Computing Technology, Chinese Academy of Sciences , Yifan Hao ICT, Chinese Academy of Sciences , Yongwei Zhao Institute of Computing Technology, Chinese Academy of Sciences , Rui Zhang Chinese Academy of Sciences , Wei Li Institute of Software Chinese Academy of Sciences; University of Chinese Academy of Sciences , Xing Hu Institute of Computing Technology, Chinese Academy of Sciences , Zhiwei Xu Institute of Computing Technology of the Chinese Academy of Sciences, China , Qi Guo Chinese Academy of Sciences , Tianshi Chen Cambricon Technologies
**会议**：HPCA 2026

---

## 中文标题

BASES：通过重构编码基实现高能效、抗错误的模拟 CIM 加速

## 英文摘要

Recently, multi-bit slicing has emerged as a promising technique to improve the energy efficiency of charge-domain Compute-In-Memory (CIM) accelerators by reducing the number of Analog-to-Digital (A/D) conversions. However, multi-bit slicing requires shift-and-add operations to reconstruct outputs, which exponentially amplify errors and cause significant accuracy degradation. Existing works mainly rely on hardware-aware retraining or noise-suppression techniques, incurring considerable design or power overhead. Thus, multi-bit CIM designs often face the dilemma of trading off energy efficiency for error resilience. In this paper, we propose Cambricon-CIM, a charge-domain multi-bit CIM accelerator that achieves both high energy efficiency and strong error resilience, without requiring retraining. The core insight is that the error amplification is proportional to digit weights; and by redefining these digit weights with smaller non-binary coding bases, it is possible to reduce the total error amplification. Leveraging this principle, Cambricon-CIM dynamically selects the minimal coding bases for every analog dot-product. With novel circuit and architectural support, Cambricon-CIM enables fast, low-overhead reconfiguration of coding bases at runtime. Experimental results show that Cambricon-CIM achieves 2.27× energy efficiency and 3.06× performance over RAELLA, a state-of-the-art error-resilient multi-bit slicing CIM architecture.

## 中文摘要

近年来，多位切片已成为一种颇具前景的技术，可通过减少模数（A/D）转换次数提升电荷域存内计算（CIM）加速器的能效。但它需要移位相加操作重建输出，会使误差呈指数级放大，导致精度明显下降。已有工作主要依赖面向硬件的重训练或噪声抑制技术，带来可观的设计开销或功耗开销，因此多位 CIM 设计常面临在能效与抗错误能力之间权衡的困境。本文提出 Cambricon-CIM，一种电荷域多位 CIM 加速器，无需重训练即可兼具高能效与强抗错误能力。核心洞见是：误差放大与数字位权成正比，用更小的非二进制编码基重新定义数字位权即可降低总的误差放大。基于该原理，Cambricon-CIM 为每个模拟点积动态选择最小的编码基，并借助新颖的电路与架构支持，在运行时以低开销快速重构编码基。实验表明，相比最先进的抗错误多位切片 CIM 架构 RAELLA，Cambricon-CIM 的能效为 2.27 倍，性能为 3.06 倍。
