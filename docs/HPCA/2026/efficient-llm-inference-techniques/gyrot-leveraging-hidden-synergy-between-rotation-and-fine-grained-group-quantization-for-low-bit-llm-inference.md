---
title: "GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference"
description: "HPCA 2026 · Efficient LLM Inference Techniques"
tags:
  - "HPCA2026"
  - "Efficient LLM Inference Techniques"
---

# GyRot: Leveraging Hidden Synergy between Rotation and Fine-grained Group Quantization for Low-bit LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient LLM Inference Techniques。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient LLM Inference Techniques</p>
</div>

**论文链接**：
**作者**：Sangjin Kim KAIST , Yuseon Choi KAIST , Byeongcheol Kim KAIST , Jungjun Oh KAIST , Hoi-Jun Yoo KAIST
**会议**：HPCA 2026

---

## 中文标题

GyRot：利用旋转与细粒度分组量化之间的隐藏协同实现低比特 LLM 推理

## 英文摘要

Low-bit quantization is essential for efficient LLM inference, and both rotation and fine-grained group quantization have shown individual promise. However, their combination often leads to accuracy degradation or hardware overhead due to a mismatch between the global nature of rotation and the localized behavior of group scaling. We propose GyRot, a quantization framework and hardware accelerator that bridges this gap through algorithm–hardware co-design. GyRot introduces Coarse Rotation, Fine Grouping (CoRFiG) and Harmonic-Aligned Permutation (HAP) to enable cooperative integration of rotation and group quantization, enhancing quantizability while relaxing scaling factor precision. To further reduce hardware cost, we reformulate asymmetric quantization and introduce a zero-point rounding strategy that enables fully integer dequantization. Implemented on an INT4-based tensor PE architecture, GyRot achieves state-of-the-art 4-bit accuracy across LLaMA-family models, while delivering up to 3.4× speedup and 3.6× energy efficiency over baseline LLM accelerators. These results validate GyRot’s practical effectiveness for scalable and energy-efficient LLM deployment.

## 中文摘要

低比特量化对高效 LLM 推理至关重要，旋转与细粒度分组量化各自都展现出潜力。然而二者的结合常因旋转的全局性与分组缩放的局部性不匹配，导致精度下降或硬件开销增加。我们提出 GyRot，一个通过算法—硬件协同设计弥合这一差距的量化框架与硬件加速器。GyRot 引入粗粒度旋转、细粒度分组（CoRFiG）与谐波对齐置换（HAP），实现旋转与分组量化的协同集成，在提升可量化性的同时放宽对缩放因子精度的要求。为进一步降低硬件开销，我们重新表述非对称量化，并引入零点舍入策略，实现全整数反量化。GyRot 在基于 INT4 的张量处理单元架构上实现，在 LLaMA 系列模型上取得最先进的 4 比特精度，同时相对基线 LLM 加速器提供最高 3.4× 加速与 3.6× 能效提升。这些结果验证了 GyRot 在可扩展且高能效的 LLM 部署中的实际有效性。
