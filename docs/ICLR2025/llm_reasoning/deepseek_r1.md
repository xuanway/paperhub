---
title: "DeepSeek-R1: 通过强化学习激励 LLM 推理能力"
description: "DeepSeek-R1 通过强化学习训练大语言模型的推理能力，无需监督微调即可与 OpenAI-o1 媲美。ICLR 2025 论文解读。"
tags:
  - "LLM推理"
  - "强化学习"
  - "DeepSeek"
  - "ICLR2025"
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">通过强化学习（RL）训练大语言模型的推理能力，无需监督微调（SFT）即可达到与 OpenAI-o1 相当的推理性能。</p>
<p class="paper-seo-summary__tags">ICLR 2025 · LLM 推理 · 强化学习 · DeepSeek</p>
</div>

**论文链接**：[arXiv 2501.12948](https://arxiv.org/abs/2501.12948)  
**代码**：[github.com/deepseek-ai/DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1)  
**机构**：DeepSeek AI  
**发表**：ICLR 2025

---

## 一句话总结

DeepSeek-R1 通过纯强化学习（无需冷启动 SFT）激励 LLM 的推理能力，在数学、代码、推理等任务上与 OpenAI-o1 持平甚至超越。

---

## 背景与动机

大型语言模型（LLM）在通用语言任务上表现出色，但在需要多步推理的数学和编程任务上仍存在明显不足。现有方法通常依赖大量人工标注的思维链数据进行监督微调（SFT），成本高昂且难以扩展。

**核心问题**：能否仅通过强化学习，让 LLM 自主习得推理能力，而无需大量标注数据？

---

## 方法详解

### DeepSeek-R1-Zero（纯 RL 训练）

1. **基础模型**：以 DeepSeek-V3-Base 为起点
2. **强化学习算法**：使用 GRPO（Group Relative Policy Optimization），相对于 PPO 更加稳定高效
3. **奖励信号**：
   - **准确性奖励**：对数学题（验证答案正确性）和代码题（通过测试用例）给予奖励
   - **格式奖励**：鼓励模型使用 `<think>...</think>` 格式进行思维链推理
4. **涌现行为**：模型自主学会了反思、自我验证、延长思考链等高级推理策略

### DeepSeek-R1（加入冷启动 SFT）

为解决 R1-Zero 的可读性问题，DeepSeek-R1 采用两阶段训练：

1. **冷启动 SFT**：使用少量高质量长思维链数据微调基础模型
2. **面向推理的 RL**：在冷启动模型上继续强化学习训练
3. **拒绝采样 SFT**：收集 RL checkpoint 的推理数据，进行第二轮 SFT
4. **全场景 RL**：结合推理奖励与人类偏好奖励，对齐通用能力

---

## 实验结果

| 基准测试 | DeepSeek-R1 | OpenAI-o1-1217 |
|---------|------------|----------------|
| AIME 2024 (Pass@1) | **79.8%** | 79.2% |
| MATH-500 | **97.3%** | 96.4% |
| Codeforces Rating | **2029** | 2061 |
| MMLU | **90.8%** | 91.8% |
| LiveCodeBench | **65.9%** | 63.4% |

---

## 核心亮点

1. **纯 RL 可行**：首次证明无需 SFT 冷启动，纯 RL 训练即可使 LLM 习得复杂推理能力
2. **自主涌现**：模型在 RL 过程中自发学会了"aha moment"（重新反思之前的错误）
3. **蒸馏有效**：将 R1 的推理能力蒸馏到 1.5B~70B 的小模型，小模型表现远超同等规模的纯 RL 训练模型
4. **开源**：DeepSeek-R1 及其蒸馏模型全部开源

---

## 局限性

- 语言混用：训练过程中模型偶尔会在英中文之间切换
- 思维链可读性：R1-Zero 的推理过程可读性较差
- 通用能力对齐：推理能力提升的同时，通用对话能力有所下降，需要额外对齐
