---
title: "Can Large Language Models Write Parallel Code?"
description: "HPDC 2024 · Session 5 — Performance modeling & LLMs"
tags:
  - "HPDC2024"
  - "Session 5"
  - "Performance modeling & LLMs"
---

# Can Large Language Models Write Parallel Code?

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 5</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658689)

**作者**：Daniel Nichols, Joshua H. Davis, Zhaojun Xie, Arjun Rajaram, Abhinav Bhatele

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）

---

## 英文摘要

Large language models are increasingly becoming a popular tool for software development. Their ability to model and generate source code has been demonstrated in a variety of contexts, including code completion, summarization, translation, and lookup. However, they often struggle to generate code for complex programs. In this paper, we study the capabilities of state-of-the-art language models to generate parallel code. In order to evaluate language models, we create a benchmark, ParEval, consisting of prompts that represent 420 different coding tasks related to scientific and parallel computing. We use ParEval to evaluate the effectiveness of several state-of-the-art open- and closed-source language models on these tasks. We introduce novel metrics for evaluating the performance of generated code, and use them to explore how well each large language model performs for 12 different computational problem types and six different parallel programming models.

## 中文摘要

大语言模型正日益成为软件开发的常用工具。它们在多种场景中展示了建模与生成源代码的能力，包括代码补全、摘要、翻译与查找。然而，它们往往难以生成复杂程序的代码。本文研究最先进语言模型生成并行代码的能力。为评估语言模型，我们创建了基准 ParEval，由代表 420 个与科学与并行计算相关的编码任务的提示组成。我们使用 ParEval 评估若干最先进开源与闭源语言模型在这些任务上的有效性。我们引入用于评估生成代码性能的新指标，并借此探究每个大语言模型在 12 种计算问题类型与 6 种并行编程模型上的表现。

## 英文关键词

Large language models, Parallel code generation, Performance evaluation, Benchmarking, HPC

## 中文关键词

大语言模型，并行代码生成，性能评估，基准测试，HPC

---

[← 返回 Session 5 — Performance modeling & LLMs](index.md)
