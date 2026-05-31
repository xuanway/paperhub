---
title: "Constitutional AI: 来自 AI 反馈的无害性"
description: "Constitutional AI 通过自我批判和修订机制，无需人工标注有害内容即可训练无害 AI 助手。ICLR 2025 论文解读。"
tags:
  - "LLM安全"
  - "对齐"
  - "Constitutional AI"
  - "Anthropic"
  - "ICLR2025"
---

# Constitutional AI: Harmlessness from AI Feedback

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Constitutional AI（CAI）通过一套预定义的原则（宪法），让模型自我批判和修订有害输出，无需人工标注即可训练出既无害又有用的 AI 助手。</p>
<p class="paper-seo-summary__tags">ICLR 2025 · LLM 安全 · AI 对齐 · Constitutional AI · Anthropic</p>
</div>

**论文链接**：[arXiv 2212.08073](https://arxiv.org/abs/2212.08073)  
**机构**：Anthropic  
**发表**：ICLR 2025

---

## 一句话总结

通过让 LLM 根据预设"宪法原则"自我评价和改进输出，Constitutional AI 无需人工标注有害内容即可训练出无害的 AI 模型。

---

## 背景与动机

传统 RLHF 方法需要大量人工标注有害内容，成本高且存在隐患（标注员接触有害内容）。

**CAI 的核心理念**：利用 AI 自身来提供安全反馈，减少对人工标注的依赖。

---

## 方法详解

### 宪法（Constitution）

一套简洁的原则集合，例如：
- "请重写回复，使其不包含有害、不道德、种族主义或有毒内容"
- "请重写以确保尊重和不冒犯"

### 两阶段训练

**阶段一：监督学习阶段（SL-CAI）**
1. 用有害提示生成初始响应
2. 让模型根据宪法原则批判自己的响应
3. 根据批判修订响应
4. 在修订后的响应上微调模型

**阶段二：强化学习阶段（RL-CAI）**
1. 生成多对响应（有害 vs 改进版）
2. 让 AI 模型判断哪个更符合宪法（AI 反馈，替代人工标注）
3. 用这些偏好数据训练偏好模型
4. 用偏好模型进行 RLHF

---

## 实验结果

- CAI 模型在无害性上大幅超越 RLHF 基线，同时保持与基线相当的有用性
- 相比人工标注的 RLHF，CAI 的标注成本降低约 90%
- 模型能够更明确地说明拒绝有害请求的原因

---

## 核心亮点

1. **AI 反馈代替人工**：大幅降低安全对齐的人力成本
2. **透明可审计**：宪法原则是明确可见的，而非隐含在人工标注中
3. **无害不失用**：解决了过度拒绝的问题，保持了模型的有用性
4. **可扩展**：宪法可以根据不同场景灵活调整

---

## 局限性

- 宪法原则本身的设计仍依赖人工判断
- AI 反馈可能存在偏见或盲点
- 对于极其微妙的有害内容，AI 批评者可能无法有效识别
