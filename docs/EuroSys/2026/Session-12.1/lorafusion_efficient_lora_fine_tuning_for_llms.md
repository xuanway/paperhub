---
title: "LoRAFusion: Efficient LoRA Fine-Tuning for LLMs"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Zhanda Zhu (University of Toronto, Vector Institute, NVIDIA), Qidong Su (Univers"
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# LoRAFusion: Efficient LoRA Fine-Tuning for LLMs

**中文标题：** LoRAFusion：面向 LLM 的高效 LoRA 微调

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Zhanda Zhu (University of Toronto, Vector Institute, NVIDIA), Qidong Su (University of Toronto, Vector Institute, NVIDIA), Yaoyao Ding (University of Toronto, Vector Institute, NVIDIA), Kevin Song (University of Toronto, Vector Institute, NVIDIA), Shang Wang (University of Toronto, Vector Institute, NVIDIA), Gennady Pekhimenko (University of Toronto, Vector Institute, NVIDIA)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769331)

## 英文摘要

Low-Rank Adaptation (LoRA) has become the leading Parameter-Efficient Fine-Tuning (PEFT) method for Large Language Models (LLMs), as it significantly reduces GPU memory usage while maintaining competitive fine-tuned model quality on downstream tasks. However, existing LLM LoRA fine-tuning systems mainly reuse optimizations from traditional full-model fine-tuning, and therefore cannot take full advantage of LoRA’s unique characteristics. We identify two key inefficiencies of existing works. First, existing LoRA fine-tuning systems incur substantial runtime overhead due to redundant memory accesses on large activation tensors. Second, they miss the opportunity to concurrently fine-tune multiple independent LoRA adapters that share the same base model on the same set of GPUs. This leads to missed performance gains such as reduced pipeline bubbles, better communication overlap, and improved GPU load balance.

To address these issues, we introduce LoRAFusion, an efficient LoRA fine-tuning system for LLMs. At the kernel level, we propose a graph-splitting method that fuses memory-bound operations. This design eliminates unnecessary memory accesses and preserves the performance of compute-bound GEMMs without incurring the cost of recomputation or synchronization. At the scheduling level, LoRAFusion introduces an adaptive batching algorithm for multi-job fine-tuning. It first splits LoRA adapters into groups to intentionally stagger batch execution across jobs, and then solves a bin-packing problem within each group to generate balanced, dependency-aware microbatches. LoRAFusion achieves up to 1.96× (1.47× on average) end-to-end speedup compared to Megatron-LM, and up to 1.46× (1.29× on average) improvement over mLoRA, the state-of-the-art multi-LoRA fine-tuning system. Our fused kernel achieves up to 1.39× (1.27× on average) kernel performance improvement and can directly serve as a plug-and-play replacement in existing LoRA systems. We open-source LoRAFusion at https://github.com/CentML/lorafusion.

## 中文摘要

低秩适应（LoRA）已成为大语言模型（LLM）主流的参数高效微调（PEFT）方法，因为它在显著降低 GPU 内存占用的同时，在下游任务上仍能保持有竞争力的微调模型质量。然而，现有的 LLM LoRA 微调系统主要沿用传统全模型微调的优化手段，因而无法充分利用 LoRA 的独特特性。我们发现了现有工作的两个关键低效之处。首先，现有 LoRA 微调系统因对大型激活张量的冗余内存访问而带来可观的运行时开销。其次，它们错失了在同一组 GPU 上并发微调多个共享同一基础模型的独立 LoRA 适配器的机会。这导致诸如减少流水线气泡、更好的通信重叠以及改善 GPU 负载均衡等性能收益被错过。

为解决这些问题，我们提出 LoRAFusion，一个面向 LLM 的高效 LoRA 微调系统。在内核层面，我们提出一种图拆分方法来融合访存密集型操作。该设计消除了不必要的内存访问，并在不引入重计算或同步开销的前提下保持计算密集型 GEMM 的性能。在调度层面，LoRAFusion 为多作业微调引入一种自适应批处理算法。它首先将 LoRA 适配器分组，以有意错开各作业的批次执行，然后在每组内求解一个装箱问题，以生成均衡且感知依赖关系的微批次。与 Megatron-LM 相比，LoRAFusion 端到端加速最高 1.96 倍（平均 1.47 倍），相比最先进的多 LoRA 微调系统 mLoRA 最高提升 1.46 倍（平均 1.29 倍）。我们的融合内核实现最高 1.39 倍（平均 1.27 倍）的内核性能提升，并可直接作为即插即用的替代方案用于现有 LoRA 系统。我们在 https://github.com/CentML/lorafusion 开源了 LoRAFusion。

**英文关键词：** LLM, LoRA, Systems for Machine Learning, Kernel Fusion, Distributed training

**中文关键词：** LLM、LoRA、机器学习系统、算子融合、分布式训练

## 代码与研究制品

- [代码](https://github.com/CentML/lorafusion)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
