---
title: "NPUWattch: ML-based Power, Area, and Timing Modeling for Neural Accelerators"
description: "HPCA 2026 · Accelerator Design and Modeling"
tags:
  - "HPCA2026"
  - "Accelerator Design and Modeling"
---

# NPUWattch: ML-based Power, Area, and Timing Modeling for Neural Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Accelerator Design and Modeling。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Accelerator Design and Modeling</p>
</div>

**论文链接**：
**作者**：Sehyeon Kim Yonsei University , Minkwan Kim Yonsei University , Chanho Park Yonsei University , Hanmok Park Kyungpook National University , Seonghoon Kim Kyungpook National University , Taigon Song Kyungpook National University , William Song Yonsei University
**会议**：HPCA 2026

---

## 中文标题

NPUWattch：面向神经网络加速器的机器学习功耗、面积与时序建模

## 英文摘要

Pre-silicon modeling tools for characterizing power, area, and timing (PAT) have enabled numerous architectural studies, but traditional analytical and table-based models begin to exhibit limitations in their applicability as architectural design complexity increases and process technology scales below 5nm with the emergence of advanced transistors. Previous modeling techniques typically assume static scaling factors across different designs and technology nodes, derived from small circuit design benchmarks using old processes. Consequently, they do not reflect complex design variability and nonlinear projection to advanced technology nodes. Moreover, reference logic and SRAM implementations serving as the baseline for design and technology scaling are often created using different technologies and design rules, leading to significant estimation inaccuracies that distort the relative contributions of individual components. To address these challenges, this paper introduces NPUWattch, a machine learning-based PAT modeling framework for neural accelerators. It leverages neural network regression models to learn complex nonlinear relationships in technology and design scaling based on diverse post-layout logic and SRAM design datasets formulated using unified technology libraries. To this end, we developed technology libraries from 65nm to 2nm, constructed and validated diverse logic and SRAM datasets, and trained neural network models using an adaptive loss function to reinforce underrepresented regions of the design space. NPUWattch is validated against the post-layout results of numerous open-source neural accelerators, and evaluation results demonstrate that NPUWattch outperforms existing tools with an average estimation error of 2.7%, offering reliable and accurate PAT estimation.

## 中文摘要

面向功耗、面积与时序（PAT）的流片前建模工具支撑了大量体系结构研究，但随着设计复杂度提升、工艺在 5nm 以下随先进晶体管出现而微缩，传统解析式与查表式模型的适用性开始显现局限。以往建模技术通常假设跨不同设计与技术节点存在静态缩放因子，这些因子来自旧工艺下的小规模电路设计基准，因而无法反映复杂的设计差异性与向先进节点的非线性外推。此外，用作设计与工艺缩放基线的参考逻辑与 SRAM 实现常基于不同工艺与设计规则构建，导致显著估计误差，扭曲了各组成部分的相对贡献。为应对这些挑战，本文提出 NPUWattch，一个面向神经网络加速器的机器学习 PAT 建模框架。它利用神经网络回归模型，在基于统一技术库构建的多样版图后逻辑与 SRAM 设计数据集上学习工艺与设计缩放中的复杂非线性关系。为此我们构建了 65nm 至 2nm 的技术库，构建并验证了多样的逻辑与 SRAM 数据集，并使用自适应损失函数训练神经网络模型以强化设计空间中样本不足的区域。NPUWattch 在众多开源神经网络加速器的版图后结果上得到验证，评估结果表明其平均估计误差为 2.7%，优于现有工具，可提供可靠准确的 PAT 估计。
