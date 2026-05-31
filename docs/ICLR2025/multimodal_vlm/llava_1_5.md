---
title: "LLaVA-1.5: 视觉指令微调的改进基线"
description: "LLaVA-1.5 通过 MLP 连接器和高分辨率输入，以极低成本在多个多模态基准上达到 SOTA。ICLR 2025 论文解读。"
tags:
  - "多模态"
  - "视觉语言模型"
  - "LLaVA"
  - "VLM"
  - "ICLR2025"
---

# LLaVA-1.5: Improved Baselines with Visual Instruction Tuning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">通过将线性投影层替换为 MLP 连接器、加入高分辨率输入支持，LLaVA-1.5 以不到 1 天的训练时间在 11 个多模态基准上超越所有先前方法。</p>
<p class="paper-seo-summary__tags">ICLR 2025 · 多模态 VLM · 视觉指令微调 · LLaVA</p>
</div>

**论文链接**：[arXiv 2310.03744](https://arxiv.org/abs/2310.03744)  
**代码**：[github.com/haotian-liu/LLaVA](https://github.com/haotian-liu/LLaVA)  
**机构**：UW-Madison, Microsoft Research  
**发表**：ICLR 2025

---

## 一句话总结

两个简单改进（MLP 连接器 + 高分辨率支持）让 LLaVA-1.5 以极低训练成本在 11 个多模态基准上全面超越现有方法。

---

## 背景与动机

原始 LLaVA 使用线性层将视觉特征投影到语言空间，结构简单但性能有限。如何用最小的改动最大化提升多模态理解能力？

---

## 方法详解

### 两大核心改进

1. **MLP 连接器**：将视觉-语言连接层从线性层（Linear）替换为两层 MLP，更好地跨模态对齐
2. **高分辨率输入**：将图像切分为多个高分辨率区域分别编码，保留细节信息
3. **数据**：加入学术任务导向数据（VQA、OCR 等），弥补对话数据的不足

### 架构

- **视觉编码器**：CLIP ViT-L/14@336px
- **连接器**：两层 MLP（新增）
- **语言模型**：Vicuna-7B/13B

---

## 实验结果

| 基准 | LLaVA | **LLaVA-1.5** | InstructBLIP |
|------|-------|--------------|--------------|
| VQAv2 | 76.9 | **80.0** | 79.9 |
| GQA | 62.0 | **63.3** | 63.1 |
| TextVQA | 46.1 | **58.2** | 50.1 |
| MMBench | 38.7 | **67.2** | 36.0 |

---

## 核心亮点

1. **简单有效**：仅需两项改动，无需复杂架构设计
2. **训练高效**：在 8×A100 上训练不到 1 天
3. **全面领先**：在 11 个基准上均达到 SOTA
4. **开源友好**：完整代码和模型权重开源

---

## 局限性

- 高分辨率处理增加了计算开销
- 对长文本/密集 OCR 场景仍有提升空间
