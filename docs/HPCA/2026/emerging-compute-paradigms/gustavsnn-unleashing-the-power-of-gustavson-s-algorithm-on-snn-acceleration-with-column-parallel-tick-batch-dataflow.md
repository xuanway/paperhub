---
title: "GustavSNN: Unleashing the Power of Gustavson's Algorithm on SNN Acceleration with Column-Parallel Tick-Batch Dataflow"
description: "HPCA 2026 · Emerging Compute Paradigms"
tags:
  - "HPCA2026"
  - "Emerging Compute Paradigms"
---

# GustavSNN: Unleashing the Power of Gustavson's Algorithm on SNN Acceleration with Column-Parallel Tick-Batch Dataflow

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Emerging Compute Paradigms。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Emerging Compute Paradigms</p>
</div>

**论文链接**：
**作者**：Sangwoo Hwang Korea University , Donghun Lee Korea University , Jahyun Koo DGIST , Jaeha Kung Korea University
**会议**：HPCA 2026

---

## 中文标题

GustavSNN：以列并行 Tick-Batch 数据流释放 Gustavson 算法在 SNN 加速中的潜力

## 英文摘要

Spiking neural networks (SNNs) require sequential computation over long timesteps, introducing substantial memory and energy overheads due to frequent updates of neuron membrane potentials. Previous SNN accelerators address this by employing tick-batch techniques, which process all timesteps within a layer before moving on to the next. However, existing approaches rely on neuron-centric scheduling, limiting their ability to exploit temporal sparsity. In this work, we propose a novel scheduling approach along with its hardware architecture for Gustavson product (GP)-based SNN acceleration. We introduce a column-parallel tick-batch (CPTB) dataflow that partitions the spike matrix into multiple submatrices and processes each submatrix of a timestep in parallel while maintaining tick-batch semantics. To support this, we present the first GP-based SNN accelerator, named GustavSNN, which avoids accessing the global membrane potential memory by updating neuron states directly in local registers. In addition, we propose a non-zero row vector (NRV) spike format that enables fine-grained skipping of inactive spike rows. As a result, our proposed architecture achieves up to 11.8× higher energy efficiency (GOPS/W) than naı̈ve GP-based accelerator and 1.43× higher energy efficiency compared to state-of-the-art SNN accelerators.

## 中文摘要

脉冲神经网络（SNN）需要跨长时步的顺序计算，神经膜电位的频繁更新带来可观的存储与能耗开销。此前的 SNN 加速器采用 tick-batch 技术应对，即先处理一层内的所有时步，再进入下一层。但已有方法依赖以神经元为中心的调度，限制了对时间稀疏性的利用。本文提出一种新的调度方法及其硬件架构，用于基于 Gustavson 乘积（GP）的 SNN 加速。我们引入列并行 tick-batch（CPTB）数据流，将脉冲矩阵划分为多个子矩阵，并在保持 tick-batch 语义的前提下并行处理一个时步的各个子矩阵。为此，本文给出首个基于 GP 的 SNN 加速器 GustavSNN，它直接在本地寄存器中更新神经元状态，从而避免访问全局膜电位存储。此外，我们提出非零行向量（NRV）脉冲格式，可细粒度地跳过非活跃脉冲行。最终，所提架构的能效（GOPS/W）最高达到朴素 GP 加速器的 11.8 倍，并比最先进的 SNN 加速器高 1.43 倍。
