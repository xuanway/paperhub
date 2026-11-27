---
title: "Ditto: Accelerating Diffusion Model via Temporal Value Similarity"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# Ditto: Accelerating Diffusion Model via Temporal Value Similarity

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Sungbin Kim (Yonsei University), Hyunwuk Lee (Yonsei University), Wonho Cho (Yonsei University), Mincheol Park (Yonsei University), Won Woo Ro (Yonsei University)
**会议**：HPCA 2025

---

## 中文标题

Ditto：利用时间维数值相似性加速扩散模型

## 英文摘要

Diffusion models achieve superior performance in image generation tasks. However, it incurs significant computation overheads due to its iterative structure. To address these overheads, we analyze this iterative structure and observe that adjacent time steps in diffusion models exhibit high value similarity, leading to narrower differences between consecutive time steps. We adapt these characteristics to a quantized diffusion model and reveal that the majority of these differences can be represented with reduced bit-width, and even zero. Based on our observations, we propose the Ditto algorithm, a difference processing algorithm that leverages temporal similarity with quantization to enhance the efficiency of diffusion models. By exploiting the narrower differences and the distributive property of layer operations, it performs full bit-width operations for the initial time step and processes subsequent steps with temporal differences. In addition, Ditto execution flow optimization is designed to mitigate the memory overhead of temporal difference processing, further boosting the efficiency of the Ditto algorithm. We also design the Ditto hardware, a specialized hardware accelerator, fully exploiting the dynamic characteristics of the proposed algorithm. As a result, the Ditto hardware achieves up to 1.5× speedup and 17.74% energy saving compared to other accelerators.

## 中文摘要

扩散模型在图像生成任务中取得了优异性能，但其迭代结构带来显著的计算开销。为应对这些开销，我们分析了该迭代结构，观察到扩散模型中相邻时间步具有很高的数值相似性，使得相邻时间步之间的差值更小。我们将这些特性应用于量化扩散模型，发现这些差值大多可用更低的位宽表示，甚至为零。基于此，我们提出 Ditto 算法，一种利用时间相似性与量化来提升扩散模型效率的差值处理算法。它利用更小的差值与层操作的分配律，在初始时间步执行全位宽操作，随后各步则处理时间差值。此外，我们设计了 Ditto 执行流优化以缓解时间差值处理的内存开销，进一步提升算法效率。我们还设计了 Ditto 硬件——专用加速器，充分利用所提算法的动态特性。最终，与其他加速器相比，Ditto 硬件实现高达 1.5× 的加速比与 17.74% 的节能。
