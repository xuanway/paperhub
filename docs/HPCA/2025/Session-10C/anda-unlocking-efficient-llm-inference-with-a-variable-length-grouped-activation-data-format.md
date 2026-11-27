---
title: "Anda: Unlocking Efficient LLM Inference with a Variable-Length Grouped Activation Data Format"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# Anda: Unlocking Efficient LLM Inference with a Variable-Length Grouped Activation Data Format

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Chao Fang (Nanjing University, MICAS KU Leuven), Man Shi (MICAS KU Leuven), Robin Geens (MICAS KU Leuven), Arne Symons (MICAS KU Leuven), Zhongfeng Wang (Nanjing University), Marian Verhelst (MICAS KU Leuven)
**会议**：HPCA 2025

---

## 中文标题

Anda：面向高效 LLM 推理的可变长分组激活数据格式

## 英文摘要

The widely-used, weight-only quantized large language models (LLMs), which leverage low-bit integer (INT) weights and retain floating-point (FP) activations, reduce storage requirements while maintaining accuracy. However, this shifts the energy and latency bottlenecks towards the FP activations that are associated with costly memory accesses and computations. Existing LLM accelerators focus primarily on computation optimizations, overlooking the potential of jointly optimizing FP computations and data movement, particularly for the dominant FP-INT GeMM operations in LLM inference. To address these challenges, we investigate the sensitivity of activation precision across various LLM modules and its impact on overall model accuracy. Based on our findings, we first propose the Anda data type: an adaptive data format with group-shared exponent bits and dynamic mantissa bit allocation. Secondly, we develop an iterative post-training adaptive precision search algorithm that optimizes the bit-width for different LLM modules to balance model accuracy, energy efficiency, and inference speed. Lastly, a suite of hardware optimization techniques is proposed to maximally exploit the benefits of the Anda format. These include a bit-plane-based data organization scheme, Anda-enhanced processing units with bit-serial computation, and a runtime bit-plane Anda compressor to simultaneously optimize storage, computation, and memory footprints. Our evaluations on FP-INT GeMM operations show that Anda achieves a 2.4× speedup, 4.0× area efficiency, and 3.1× energy efficiency improvement on average for popular LLMs including OPT, LLaMA, and LLaMA-2 series over the GPU-like FP-FP baseline. Anda demonstrates strong adaptability across various application scenarios, accuracy requirements, and system performance, enabling efficient LLM inference across a wide range of deployment scenarios.

## 中文摘要

广泛使用的仅权重量化大语言模型（LLM）采用低比特整型（INT）权重并保留浮点（FP）激活，在保持精度的同时降低了存储需求。然而，这也把能耗与时延瓶颈转向了伴随高昂访存与计算开销的 FP 激活。现有 LLM 加速器主要关注计算优化，忽视了联合优化 FP 计算与数据移动的潜力，尤其是 LLM 推理中占主导的 FP-INT GeMM 运算。为应对这些挑战，我们研究了不同 LLM 模块中激活精度的敏感性及其对整体模型精度的影响。基于这些发现，我们首先提出 Anda 数据类型：一种具有组共享指数位和动态尾数位分配的自适应数据格式。其次，我们开发了迭代式训练后自适应精度搜索算法，为不同 LLM 模块优化位宽，以平衡模型精度、能效与推理速度。最后，我们提出一套硬件优化技术以最大化发挥 Anda 格式的优势，包括基于位平面的数据组织方案、采用位串行计算的 Anda 增强处理单元，以及运行时位平面 Anda 压缩器，从而同时优化存储、计算与内存占用。在 FP-INT GeMM 运算上的评估表明，对于 OPT、LLaMA 和 LLaMA-2 系列等主流 LLM，Anda 相比类 GPU 的 FP-FP 基线平均实现 2.4 倍加速、4.0 倍面积效率和 3.1 倍能效提升。Anda 在各类应用场景、精度需求和系统性能下均展现出很强的适应性。
