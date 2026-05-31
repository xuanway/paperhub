---
title: "Llama 2: 开源基础模型与对话微调模型"
description: "Meta AI 发布的 Llama 2 开源大语言模型，Llama 2-Chat 通过 RLHF 微调在安全性和实用性上与 GPT-3.5 相当。ACL 2025 论文解读。"
tags:
  - "LLM"
  - "Llama"
  - "开源"
  - "RLHF"
  - "Meta"
  - "ACL2025"
---

# Llama 2: Open Foundation and Fine-Tuned Chat Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Meta AI 发布 7B-70B 参数规模的开源 LLM 系列。Llama 2-Chat 通过监督微调（SFT）和基于人类反馈的强化学习（RLHF）优化，在安全性和有用性上与商业模型 GPT-3.5 相当。</p>
<p class="paper-seo-summary__tags">ACL 2025 · LLM · 开源模型 · RLHF · Meta AI</p>
</div>

**论文链接**：[arXiv 2307.09288](https://arxiv.org/abs/2307.09288)  
**代码**：[github.com/facebookresearch/llama](https://github.com/facebookresearch/llama)  
**机构**：Meta AI  
**发表**：ACL 2025

---

## 一句话总结

Llama 2 是 Meta 发布的开源 LLM 系列（7B/13B/34B/70B），通过 Ghost Attention 等创新技术的 RLHF 微调，Llama 2-Chat 在安全性和实用性上接近 GPT-3.5 水平。

---

## 背景与动机

GPT-4/ChatGPT 等商业模型性能领先，但不开源，研究社区难以深入研究。Llama 1 开源了基础模型但未包含对话微调版本。

**目标**：发布完整的开源对话模型，推动安全、有用的 AI 研究。

---

## 方法详解

### 预训练

- **数据**：2 万亿 token（相比 Llama 1 增加 40%），聚焦更多公开数据，移除 Meta 内部数据
- **架构**：GQA（分组查询注意力，70B 模型）、RoPE 位置编码
- **上下文长度**：4096 token（Llama 1 的两倍）

### 微调阶段

**阶段 1：监督微调（SFT）**
- 使用 ~27K 高质量人工标注对话数据
- 强调质量 > 数量

**阶段 2：RLHF**
- 训练两个独立的奖励模型（有用性 RM + 安全性 RM）
- 使用 PPO 算法进行强化学习
- **Ghost Attention（GAtt）**：使模型在多轮对话中始终遵守系统提示（如角色扮演指令）

### 安全优化

- **Red Teaming**：内部安全测试，发现并修复安全漏洞
- **Safety Context Distillation**：在推理时注入安全系统提示，提升安全性

---

## 实验结果

人工评估（胜率，对比 ChatGPT）：

| 评估维度 | Llama 2-Chat 70B |
|---------|-----------------|
| 有用性 | 与 ChatGPT 相当（~50%） |
| 安全性 | 优于 ChatGPT |

学术基准（Llama 2 70B vs 其他开源模型）：在 MMLU、TruthfulQA、HellaSwag 等基准上显著优于同规模开源模型。

---

## 核心亮点

1. **完全开源**：包含基础模型和对话微调版本，可商用
2. **安全先行**：大量红队测试和安全优化
3. **Ghost Attention**：创新性解决多轮对话中指令遗忘问题
4. **推动开源生态**：成为最广泛使用的开源 LLM 基础模型之一

---

## 局限性

- 相比 GPT-4 仍有明显差距
- 训练数据截止于 2022 年 7 月
- 过于保守的安全机制导致有时拒绝合理请求
- 多语言能力相对薄弱
