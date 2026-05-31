---
title: "Chain-of-Thought Prompting: 思维链提示激发 LLM 推理能力"
description: "思维链（CoT）提示通过在少样本示例中加入推理步骤，显著提升 LLM 在复杂推理任务上的表现。ICLR 2025 论文解读。"
tags:
  - "LLM推理"
  - "思维链"
  - "Chain-of-Thought"
  - "提示工程"
  - "ICLR2025"
---

# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">思维链提示（CoT）通过在少样本示例中加入中间推理步骤，使大型语言模型能够将复杂推理问题分解为子步骤逐步求解。</p>
<p class="paper-seo-summary__tags">ICLR 2025 · LLM 推理 · 提示工程 · 思维链</p>
</div>

**论文链接**：[arXiv 2201.11903](https://arxiv.org/abs/2201.11903)  
**机构**：Google Research, Brain Team  
**发表**：ICLR 2025

---

## 一句话总结

在少样本提示（few-shot prompting）的示例中加入逐步推理过程（思维链），可以大幅提升大型语言模型在算术、符号和常识推理任务上的性能。

---

## 背景与动机

大型语言模型在扩展模型规模后能够解锁许多能力，但多步推理任务（如数学应用题）仍是一大挑战。传统的少样本提示只给出问题-答案对，没有中间步骤。

**关键洞察**：人类解决复杂问题时会逐步思考，能否让 LLM 也这样做？

---

## 方法详解

### 思维链提示（CoT Prompting）

核心思想极其简单：将少样本示例从 `问题 → 答案` 改为 `问题 → 推理步骤 → 答案`。

**标准提示**：
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
A: The answer is 11.
```

**思维链提示**：
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.
```

---

## 实验结果

在 GSM8K 数学基准测试上（使用 PaLM 540B）：

| 方法 | 准确率 |
|------|-------|
| 标准少样本提示 | 17.9% |
| **思维链提示** | **56.9%** |
| Fine-tuned GPT-3 | 33.0% |

### 关键发现

- 思维链提示主要在**大模型**（>100B 参数）上有效，小模型收益有限
- 在算术推理、常识推理、符号推理等多类任务上均有显著提升
- 即使模型产生错误的推理过程，有时也能得到正确答案

---

## 核心亮点

1. **简单有效**：无需任何训练或微调，仅修改提示格式即可大幅提升推理能力
2. **可解释性**：推理过程透明可见，便于发现和纠正错误
3. **涌现能力**：思维链能力随模型规模出现涌现（emergent ability）
4. **广泛适用**：在数学、科学、代码等多种推理任务上均有效

---

## 局限性

- 依赖大模型规模（<100B 参数的模型收益有限）
- 推理步骤需要人工设计示例（后续工作如 Zero-shot CoT 解决了此问题）
- 更长的提示增加了推理延迟和 token 消耗
