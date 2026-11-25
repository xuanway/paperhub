---
title: "LLMFolder: Revisiting Constant Folding in Large Language Models"
description: "EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning · Gansen Hu (Shanghai Jiao Tong University), Zhaoguo Wang (Shanghai Jiao Tong Univ"
tags:
  - "EuroSys2026"
  - "ML Model Optimization: Compilers, Quantization & Fine-Tuning"
---

# LLMFolder: Revisiting Constant Folding in Large Language Models

**中文标题：** LLMFolder：重新审视大语言模型中的常量折叠

**所属 Session：** [Session 12.1: ML Model Optimization: Compilers, Quantization & Fine-Tuning](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：ML Model Optimization: Compilers, Quantization & Fine-Tuning。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · ML Model Optimization: Compilers, Quantization & Fine-Tuning</p>
</div>

**作者**：Gansen Hu (Shanghai Jiao Tong University), Zhaoguo Wang (Shanghai Jiao Tong University), Wei Huang (Shanghai Jiao Tong University), Jinglin Wei (Shanghai Jiao Tong University), Haibo Chen (Shanghai JiaoTong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769339)

## 英文摘要

Large language models (LLMs) demonstrate remarkable capabilities but face deployment challenges due to their massive parameter counts. While pruning can reduce model size, it leads to significant accuracy degradation under high compression ratios. We present a novel perspective inspired by constant folding in compiler optimization. Our approach enables parameter reduction by treating activation functions in LLMs as linear functions.

However, recent LLMs use complex non-linear activations like GELU that prevent direct application of this technique. We propose LLMFolder, which enables optimization of LLMs with non-linear activations by partially approximating them with linear functions in frequently occurring input ranges. For outlier inputs, LLMFolder employs an online predictor to dynamically fall back to original computations.

Our experiments demonstrate that LLMFolder achieves 80% parameter reduction in feed-forward networks, while significantly outperforming state-of-the-art pruning methods with up to 65% higher accuracy. When combined with quantization and pruning, LLMFolder can further achieve 92.5% parameter reduction with only 4.4% average accuracy drop for a 7B model, where neither technique alone or combination can achieve. In practical deployments for a 7B model, LLMFolder achieves 1.6× end-to-end inference speedup when integrated with the vLLM serving system, and 1.4× speedup with the widely adopted HuggingFace implementation, while incurring only a 10.9% accuracy trade-off.

## 中文摘要

大语言模型（LLM）展现出卓越的能力，但因其庞大的参数规模而面临部署挑战。剪枝可以减小模型规模，但在高压缩率下会导致显著的精度下降。我们从编译器优化中的常量折叠获得灵感，提出一个新的视角。我们的方法将 LLM 中的激活函数视为线性函数，从而实现参数削减。

然而，近期的 LLM 使用 GELU 等复杂非线性激活函数，使该技术无法直接应用。我们提出 LLMFolder，通过在频繁出现的输入区间内用线性函数部分近似非线性激活函数，使 LLM 的优化成为可能。对于离群输入，LLMFolder 采用在线预测器动态回退到原始计算。

我们的实验表明，LLMFolder 在前馈网络中实现 80% 的参数削减，同时显著优于最先进的剪枝方法，精度最高提升 65%。当与量化和剪枝结合时，LLMFolder 可对 7B 模型进一步实现 92.5% 的参数削减，平均精度仅下降 4.4%，而单独使用任一技术或二者组合都无法做到。在 7B 模型的实际部署中，LLMFolder 集成 vLLM 服务系统时端到端推理加速 1.6 倍，与广泛采用的 HuggingFace 实现配合时加速 1.4 倍，而精度折衷仅为 10.9%。

**英文关键词：** large language model serving, constant folding

**中文关键词：** 大语言模型服务、常量折叠

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
