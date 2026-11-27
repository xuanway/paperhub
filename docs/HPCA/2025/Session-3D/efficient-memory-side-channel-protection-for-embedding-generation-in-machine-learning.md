---
title: "Efficient Memory Side-Channel Protection for Embedding Generation in Machine Learning"
description: "HPCA 2025 · Securing your Chips"
tags:
  - "HPCA2025"
  - "Securing your Chips"
---

# Efficient Memory Side-Channel Protection for Embedding Generation in Machine Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Securing your Chips。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Securing your Chips</p>
</div>

**论文链接**：
**作者**：Muhammad Umar (Cornell University), Akhilesh Parag Marathe (Virginia Tech), Monami Dutta Gupta (Virginia Tech), Shubham Jogprakash Ghosh (Virginia Tech), G. Edward Suh (NVIDIA / Cornell University), Wenjie Xiong (Virginia Tech)
**会议**：HPCA 2025

---

## 中文标题

面向机器学习中嵌入生成的高效内存侧信道保护

## 英文摘要

Modern machine learning (ML) models need to process both continuous and categorical/discrete feature values, e.g., deep learning recommendation models (DLRMs) rely on users’ categorical features to make recommendations, and large language models (LLMs) take discrete words/tokens as input. ML models process such discrete features by converting them to numerical vectors called embeddings. Unfortunately, embedding table lookups are vulnerable to side-channel attacks, as table indices leak input feature values. Due to the size of the embedding tables, using conventional oblivious computing techniques such as ORAM to protect memory access patterns to the tables incur significant overhead. In this paper, we propose to use a different technique, Deep Hash Embedding (DHE), to secure embedding table accesses, even though it is not commonly used today due to its compute-intensive nature. We investigate three embedding generation methods with side-channel protection: linear scan of the embedding table, embedding table protected by ORAM, and DHE. Our experiments on DLRMs and LLMs show that DHE or a hybrid scheme combining DHE and linear scan can significantly improve both performance and memory footprint compared to the conventional ORAM protection. For DLRM on Criteo datasets, our hybrid scheme improves performance by about 4× for large embedding tables, and up to 3.08× end-to-end over the optimized ORAM baseline without any loss in accuracy, while reducing the model memory footprint by up to 1116×. For a GPT-2 LLM, using DHE speeds up the prompt prefill by up to 1.32× and decoding by up to 1.07× over ORAM, depending on the batch size, with comparable output quality.

## 中文摘要

现代机器学习（ML）模型需要同时处理连续特征值与类别/离散特征值，例如深度学习推荐模型（DLRM）依赖用户的类别特征进行推荐，大语言模型（LLM）则以离散的词/词元作为输入。ML 模型通过将这类离散特征转换为称为嵌入的数值向量来处理它们。遗憾的是，嵌入表查找容易受到侧信道攻击，因为表索引会泄露输入特征值。由于嵌入表规模庞大，使用 ORAM 等传统不经意计算技术来保护对嵌入表的内存访问模式会带来显著开销。本文提出使用另一种技术——深度哈希嵌入（DHE）来保护嵌入表访问，尽管其计算密集的特性使其目前并不常用。我们研究三种带侧信道保护的嵌入生成方法：嵌入表线性扫描、受 ORAM 保护的嵌入表以及 DHE。在 DLRM 与 LLM 上的实验表明，与传统的 ORAM 保护相比，DHE 或结合 DHE 与线性扫描的混合方案能显著提升性能并改善内存占用。对于 Criteo 数据集上的 DLRM，我们的混合方案在大型嵌入表上将性能提升约 4 倍，并在优化后的 ORAM 基线上实现最高 3.08 倍的端到端提升，且没有任何精度损失，同时将模型内存占用最多降低 1116 倍。对于 GPT-2 LLM，使用 DHE 可将提示预填充加速最高 1.32 倍、解码加速最高 1.07 倍（相对 ORAM，取决于批大小），且输出质量相当。
