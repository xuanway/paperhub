---
title: "Machine Learning-Guided Memory Optimization for DLRM Inference on Tiered Memory"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Machine Learning-Guided Memory Optimization for DLRM Inference on Tiered Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Jie Ren (William & Mary), Bin Ma (University of California, Merced), Shuangyan Yang (University of California, Merced), Benjamin Francis (Meta), Ehsan Ardestani (Meta), Min Si (Meta), Dong Li (University of California, Merced)
**会议**：HPCA 2025

---

## 中文标题

机器学习引导的分层内存 DLRM 推理优化

## 英文摘要

Deep learning recommendation models (DLRMs) are widely used in industry, and their memory capacity requirements reach the terabyte scale. Tiered memory architectures provide a cost-effective solution but introduce challenges in embedding-vector placement due to complex embedding-access patterns. We propose RecMG, a machine learning (ML)-guided system for vector caching and prefetching on tiered memory. RecMG accurately predicts accesses to embedding vectors with long reuse distances or few reuses. The design of RecMG focuses on making ML feasible in the context of DLRM inference by addressing unique challenges in data labeling and navigating the search space for embedding-vector placement. By employing separate ML models for caching and prefetching, plus a novel differentiable loss function, RecMG narrows the prefetching search space and minimizes on-demand fetches. Compared to state-of-the-art temporal, spatial, and ML-based prefetchers, RecMG reduces on-demand fetches by 2.2×, 2.8×, and 1.5×, respectively. In industrial-scale DLRM inference scenarios, RecMG effectively reduces end-to-end DLRM inference time by up to 43%.

## 中文摘要

深度学习推荐模型（DLRM）在工业界被广泛使用，其内存容量需求可达 TB 级。分层内存架构提供了高性价比的解决方案，但由于嵌入向量访问模式复杂，其在嵌入向量放置方面引入挑战。我们提出 RecMG，一个机器学习（ML）引导的分层内存向量缓存与预取系统。RecMG 能准确预测对复用距离长或复用次数少的嵌入向量的访问。RecMG 的设计重点在于解决数据标注中的独特挑战并应对嵌入向量放置的搜索空间问题，从而使 ML 在 DLRM 推理场景中切实可行。通过为缓存与预取分别采用独立的 ML 模型，并结合一种新颖的可微损失函数，RecMG 缩小了预取搜索空间并最小化按需取回。与最先进的时序、空间及基于 ML 的预取器相比，RecMG 分别将按需取回减少 2.2 倍、2.8 倍和 1.5 倍。在工业级 DLRM 推理场景中，RecMG 可将端到端 DLRM 推理时间最多缩短 43%。
