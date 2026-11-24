---
title: "DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs"
description: "EuroSys 2025 · LLM Serving · Xiaozhe Yao (ETH Zurich), Qinghao Hu (MIT), Ana Klimovic (ETH Zurich)"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# DeltaZip: Efficient Serving of Multiple Full-Model-Tuned LLMs

**中文标题：** 高效服务多个全模型微调的大语言模型

**所属 Session：** [Session 1.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Xiaozhe Yao (ETH Zurich), Qinghao Hu (MIT), Ana Klimovic (ETH Zurich)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717468)

## 英文摘要

Fine-tuning large language models (LLMs) greatly improves model quality for downstream tasks. However, serving many fine-tuned LLMs concurrently is challenging due to the sporadic, bursty, and varying request patterns of different LLMs. To bridge this gap, we present DeltaZip, an LLM serving system that efficiently serves multiple full-parameter fine-tuned models concurrently by aggressively compressing model deltas by up to 10× while maintaining high model quality. The key insight behind this design is that fine-tuning results in small-magnitude changes to the pre-trained model. By co-designing the serving system with the compression algorithm, DeltaZip achieves 2× to 12× improvement in throughput compared to the state-of-the-art systems.

## 中文摘要

微调大语言模型（LLM）能大幅提升模型在下游任务上的质量。然而，由于不同 LLM 的请求模式具有偶发、突发和多变的特点，并发服务多个微调后的 LLM 颇具挑战。为弥补这一差距，我们提出 DeltaZip，一个能够高效并发服务多个全参数微调模型的 LLM 服务系统，它通过将模型增量压缩至最高 10 倍，同时保持较高的模型质量。该设计背后的关键洞见在于：微调只会给预训练模型带来幅度较小的变化。通过将服务系统与压缩算法协同设计，DeltaZip 相比最先进的系统实现了 2 倍到 12 倍的吞吐提升。

**英文关键词：** Machine Learning Systems, Model Compression, Quantization, Sparsity, Hardware Acceleration, Model Inference and Serving

**中文关键词：** 机器学习系统、模型压缩、量化、稀疏性、硬件加速、模型推理与服务

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
