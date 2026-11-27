---
title: "throttLL’eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# throttLL’eM: Predictive GPU Throttling for Energy Efficient LLM Inference Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Andreas Kosmas Kakolyris (National Technical University of Athens), Dimosthenis Masouros (National Technical University of Athens), Petros Vavaroutsos (National Technical University of Athens), Sotirios Xydis (National Technical University of Athens), Dimitrios Soudris (National Technical University of Athens)
**会议**：HPCA 2025

---

## 中文标题

throttLL’eM：面向节能 LLM 推理服务的预测式 GPU 降频

## 英文摘要

As Large Language Models (LLMs) gain traction, their reliance on power-hungry GPUs places ever-increasing energy demands, raising environmental and monetary concerns. Inference dominates LLM workloads, presenting a critical challenge for providers: minimizing energy costs under Service-Level Objectives (SLOs) that ensure optimal user experience. In this paper, we present throttLL’eM, a framework that reduces energy consumption while meeting SLOs through the use of instance and GPU frequency scaling. throttLL’eM features mechanisms that project future Key-Value (KV) cache usage and batch size. Leveraging a Machine-Learning (ML) model that receives these projections as inputs, throttLL’eM manages performance at the iteration level to satisfy SLOs with reduced frequencies and instance sizes. We show that the proposed ML model achieves R2 scores greater than 0.97 and miss-predicts performance by less than 1 iteration per second on average. Experimental results on LLM inference traces show that throttLL’eM achieves up to 43.8% lower energy consumption and an energy efficiency improvement of at least 1.71× under SLOs, when compared to NVIDIA’s Triton server. throttLL’eM is publicly available at https://github.com/WilliamBlaskowicz/throttLL-eM.

## 中文摘要

随着大语言模型（LLM）日益普及，其对高功耗 GPU 的依赖带来不断增长的能耗需求，引发环境与经济方面的担忧。推理在 LLM 负载中占主导地位，这为服务提供商带来关键挑战：在保证最优用户体验的服务等级目标（SLO）下最小化能耗成本。本文提出 throttLL’eM，一个通过实例与 GPU 频率伸缩在满足 SLO 的同时降低能耗的框架。throttLL’eM 具备预测未来键值（KV）缓存用量与批量大小的机制。借助以这些预测为输入的机器学习（ML）模型，throttLL’eM 在迭代级别管理性能，以更低的频率与实例规格满足 SLO。我们表明所提出的 ML 模型 R2 分数高于 0.97，且平均每秒的性能预测误差小于 1 次迭代。在 LLM 推理 trace 上的实验结果表明，与 NVIDIA 的 Triton 服务器相比，throttLL’eM 在满足 SLO 的情况下最多降低 43.8% 的能耗，能效提升至少 1.71 倍。throttLL’eM 已开源于 https://github.com/WilliamBlaskowicz/throttLL-eM。
