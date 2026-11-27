---
title: "LUT-DLA: Lookup Table as Efficient Extreme Low-Bit Deep Learning Accelerator"
description: "HPCA 2025 · Stacking the Layers (Quantization)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Quantization)"
---

# LUT-DLA: Lookup Table as Efficient Extreme Low-Bit Deep Learning Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Quantization)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Quantization)</p>
</div>

**论文链接**：
**作者**：Guoyu Li (Microsoft Research), Chunyun Chen (NTU Singapore), Shengyu Ye (Microsoft Research), Yang Wang (Microsoft Research), Fan Yang (Microsoft Research), Ting Cao (Microsoft Research), Mohamed M. Sabry Aly (NTU Singapore), Cheng Liu (University of Chinese Academy of Sciences), Mao Yang (Microsoft Research)
**会议**：HPCA 2025

---

## 中文标题

LUT-DLA：查找表作为高效极致低位深度学习加速器

## 英文摘要

The emergence of neural network capabilities invariably leads to a significant surge in computational demands due to expanding model sizes and increased computational complexity. To reduce model size and lower inference costs, recent research has focused on simplifying models and designing hardware accelerators using low-bit quantization. However, due to numerical representation limits, scalar quantization cannot reduce bit width lower than 1-bit, diminishing its benefits. To break through these limitations, we introduce LUT-DLA, a Look-Up Table (LUT) Deep Learning Accelerator Framework that utilizes vector quantization to convert neural network models into LUTs, achieving extreme low-bit quantization. The LUT-DLA framework facilitates efficient and cost-effective hardware accelerator designs and supports the LUTBoost algorithm, which helps to transform various DNN models into LUT-based models via multistage training, drastically cutting both computational and hardware overhead. Additionally, through co-design space exploration, LUT-DLA assesses the impact of various model and hardware parameters to fine-tune hardware configurations for different application scenarios, optimizing performance and efficiency. Our comprehensive experiments show that LUT-DLA achieves improvements in power efficiency and area efficiency with gains of 1.4~7.0× and 1.5~146.1×, respectively, while maintaining only a modest accuracy drop. For CNNs, accuracy decreases by 0.1%~3.1% using the L2 distance similarity, 0.1%~3.4% with the L1 distance similarity, and 0.1%~3.8% when employing the Chebyshev distance similarity. For transformer-based models, the accuracy drop ranges from 1.4% to 3.0%.

## 中文摘要

神经网络能力的进步总是伴随模型规模扩大与计算复杂度增加而带来算力需求的激增。为减小模型规模并降低推理成本，近期研究聚焦于简化模型以及使用低位量化设计硬件加速器。然而受数值表示限制，标量量化无法将位宽降到 1-bit 以下，其收益随之减弱。为突破这些限制，我们提出 LUT-DLA，一个查找表（LUT）深度学习加速器框架，它利用矢量量化将神经网络模型转换为查找表，实现极致低位量化。LUT-DLA 框架便于实现高效且低成本的硬件加速器设计，并支持 LUTBoost 算法，该算法通过多阶段训练帮助将各种 DNN 模型转换为基于 LUT 的模型，大幅削减计算与硬件开销。此外，通过协同设计空间探索，LUT-DLA 评估各种模型与硬件参数的影响，以便针对不同应用场景微调硬件配置，优化性能与效率。我们的全面实验表明，LUT-DLA 在功耗效率与面积效率上分别取得 1.4~7.0× 与 1.5~146.1× 的提升，同时仅带来适度精度下降。对 CNN，使用 L2 距离相似度时精度下降 0.1%~3.1%，使用 L1 距离相似度为 0.1%~3.4%，采用切比雪夫距离相似度时为 0.1%~3.8%。对基于 transformer 的模型，精度下降范围为 1.4% 到 3.0%。
