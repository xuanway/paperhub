---
title: "ATTNChecker: Highly-Optimized Fault Tolerant Attention for Large Language Model Training"
description: "PPoPP 2025 Session 6（Large Language Models）：首个注意力 ABFT，训练开销 7%，恢复开销降 49×"
tags:
  - "PPoPP2025"
  - "Session-6"
  - "Large Language Models"
  - "Fault Tolerance"
  - "ABFT"
  - "Attention"
authors:
  - ".  Yuhang Liang"
  - "Xinyi Li"
  - "Jie Ren"
  - "Ang Li"
  - "Bo Fang"
  - "Jieyang Chen"
session: "Session 6: Large Language Models"
session_number: 6
session_chair: "Minjia Zhang"
date: "2025-03-04"
time: "10:40–11:00"
room: "Acacia D"
doi: "10.1145/3710848.3710870"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# ATTNChecker: Highly-Optimized Fault Tolerant Attention for Large Language Model Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出首个面向 LLM 注意力机制的算法级容错技术 ATTNChecker，基于故障传播模式检测并纠正 INF、NaN 与近 INF 错误，训练开销平均仅 7%。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 6: Large Language Models</p>
</div>

**作者**：Yuhang Liang (University of Oregon); Xinyi Li (Pacific Northwest National Laboratory); Jie Ren (College of William & Mary); Ang Li, Bo Fang (Pacific Northwest National Laboratory); Jieyang Chen (University of Oregon)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 10:40–11:00 · Session 6: Large Language Models（主席：Minjia Zhang）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710870) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出首个面向 LLM 注意力机制的算法级容错技术 ATTNChecker，基于故障传播模式检测并纠正 INF、NaN 与近 INF 错误，训练开销平均仅 7%。

## 研究问题

LLM 训练计算密集且易受故障影响，注意力机制中的 INF、NaN 和近 INF 值会沿计算传播，触发模型不可训练状态，迫使训练从检查点恢复。

## 方法简述

- 通过系统性故障注入实验，分析 INF、NaN 与近 INF 错误的传播模式。
- 基于传播模式设计注意力机制的 ABFT 方案。
- 加入性能优化，在系统可靠性与模型脆弱性之间取得平衡，为快速训练提供轻量保护。

## 主要结果

- 在 4 个 LLM 上平均仅引入 7% 训练开销，同时检测并纠正全部极端错误。
- 相比 SOTA 的 checkpoint/restore 方案，恢复开销最高降低 49×。

<details>
<summary>原文摘要（英文）</summary>

Large Language Models (LLMs) have demonstrated remarkable performance in various natural language processing tasks. However, the training of these models is computationally intensive and susceptible to faults, particularly in the attention mechanism, which is a critical component of transformer-based LLMs. In this paper, we investigate the impact of faults on LLM training, focusing on INF, NaN, and near-INF values in the computation results with systematic fault injection experiments. We observe the propagation patterns of these errors, which can trigger non-trainable states in the model and disrupt training, forcing the procedure to load from checkpoints. To mitigate the impact of these faults, we propose ATTNChecker, the first Algorithm-Based Fault Tolerance (ABFT) technique tailored for the attention mechanism in LLMs. ATTNChecker is designed based on fault propagation patterns of LLM and incorporates performance optimization to adapt to both system reliability and model vulnerability while providing lightweight protection for fast LLM training. Evaluations on four LLMs show that ATTNChecker incurs on average 7% overhead on training while detecting and correcting all extreme errors. Compared with the state-of-the-art checkpoint/restore approach, ATTNChecker reduces recovery overhead by up to 49×.

</details>

---

> 所属 Session：[Session 6: Large Language Models](index.md) · 返回 [PPoPP 2025 总览](../index.md)
