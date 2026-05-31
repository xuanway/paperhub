---
title: "Focus: 高效视觉语言模型的流式集中架构"
description: "HPCA 2026 Best Paper候选：Focus提出流式集中架构，通过识别和聚焦视觉token中的信息密集区域，大幅提升VLM推理效率。"
tags: ["HPCA2026", "LLM推理", "视觉语言模型", "Best Paper", "Duke"]
---

# Focus: A Streaming Concentration Architecture for Efficient Vision-Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Focus 通过流式集中机制，在 VLM 推理时动态识别图像中的信息密集区域，跳过冗余视觉 token 的计算，实现 2.1× 推理加速，精度损失 < 0.5%。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM推理 · VLM加速 · 体系结构设计 · Best Paper候选</p>
</div>

**作者**：Chiyue Wei, Cong Guo, Junyao Zhang, Haoxuan Shan, Yifan Xu, Ziyue Zhang, Yudong Liu, Qinsi Wang, Changchun Zhou, Hai "Helen" Li, Yiran Chen  
**机构**：Duke University  
**会议**：HPCA 2026, Sydney, Australia（**Best Paper 候选**）  

---

## 一句话总结

> 视觉语言模型中大量视觉 token 存在信息冗余，Focus 通过流式集中架构动态过滤冗余 token，在不损失精度的前提下将推理速度提升 2.1 倍。

## 背景与动机

- **问题**：VLM（如 LLaVA、InternVL）将图像编码为数百至数千个视觉 token，但图像中大部分区域对回答特定问题无关，导致注意力计算严重浪费。
- **现有方案的不足**：静态裁剪方法需预先确定保留比例，无法适应不同图像和问题的多样性；Token压缩方法损失精度较大。
- **本文思路**：引入流式集中机制，在生成第一个回答 token 时同步完成视觉 token 的重要性评估，避免额外延迟。

## 方法详解

### 核心思想

**流式集中（Streaming Concentration）**：在自回归解码流式输出第一个 token 时，同步计算各视觉 token 的注意力得分，保留得分最高的 K 个 token，后续所有解码步骤只使用这 K 个 token。

### 关键模块

1. **重要性评估器**：利用第一个解码步骤的注意力权重作为代理指标，无额外前向传播
2. **流式缓冲区**：硬件缓冲区动态维护 TopK 视觉 token，支持流式替换
3. **稀疏注意力计算单元**：只对选中 token 执行完整注意力

### 硬件设计

- 在现有 LLM 推理加速器上增加轻量级流式选择逻辑
- 面积开销 < 2%，无需修改现有 GEMM 单元

## 实验结果

| 基准 | 精度保留 | 速度提升 | Token保留率 |
|------|---------|---------|------------|
| VQAv2 | 99.6% | 2.1× | 25% |
| TextVQA | 99.1% | 1.9× | 30% |
| MMBench | 99.3% | 2.0× | 28% |

## 核心亮点

1. 零额外前向传播开销，与自回归解码流水线完全重叠
2. 适用于所有基于 Transformer 的 VLM，无需重新训练
3. 硬件友好设计，面积/功耗开销极小

## 局限性

- 对需要全局理解的任务（如 OCR 完整文档）效果有限
- TopK 比例选择需要针对不同模型调优
