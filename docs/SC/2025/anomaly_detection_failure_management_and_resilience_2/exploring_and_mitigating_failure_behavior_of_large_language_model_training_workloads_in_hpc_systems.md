---
title: "Exploring and Mitigating Failure Behavior of Large Language Model Training Workloads in HPC Systems"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 2 · Pengfei Yu; Jingjing Gu; Hao Han; Dazhong Shen; Bao Wen; Yang Liu"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 2"
---

# Exploring and Mitigating Failure Behavior of Large Language Model Training Workloads in HPC Systems

**中文标题：** 探索并缓解 HPC 系统中大语言模型训练工作负载的故障行为

**所属 Session：** [Anomaly Detection, Failure Management, and Resilience 2](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 2</p>
</div>

**作者**：Pengfei Yu; Jingjing Gu; Hao Han; Dazhong Shen; Bao Wen; Yang Liu

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap912&sess=sess178)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The exponential growth of large language model (LLM) training demands in HPC systems has exposed critical reliability challenges, particularly from transient faults. Unlike resilience studies in conventional DNN inference, the massive parameter scale and iterative updates in LLM training trigger more complex failure patterns. To address these challenges, we introduce LLMFI, a new fault injection tool, and reveal six distinct failure behaviors through 300K+ fault injection experiments (exceeding 5K GPU node-hours). Our key insight is that, while most injected faults are eventually masked by the training iteration mechanism, a critical subset leads to catastrophic failures or performance degradation. Further, we propose LLMFT, a novel machine-learning-based fault tolerance framework that implements closed-loop error control via heuristic feature extraction, fault detector, and dual recovery mechanisms. Extensive evaluation demonstrates that LLMFT achieves an average of 97.61% F1-score in

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
