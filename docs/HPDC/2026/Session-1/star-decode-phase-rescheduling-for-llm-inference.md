---
title: "STAR: Decode-Phase Rescheduling for LLM Inference"
description: "HPDC 2026 · Session 1 — LLM Inference: Scheduling & Serving"
tags:
  - "HPDC2026"
  - "Session 1"
  - "LLM Inference: Scheduling & Serving"
---

# STAR: Decode-Phase Rescheduling for LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 1</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807813)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#WangHLWLMWHGZT26](https://dblp.org/db/conf/hpdc/hpdc2026.html#WangHLWLMWHGZT26)

**作者**：Zhibin Wang, Zetao Hong, Xue Li, Zibo Wang, Shipeng Li, Qingkai Meng, Qing Wang, Chengying Huan, Rong Gu, Sheng Zhong, Chen Tian

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 1 — LLM Inference: Scheduling & Serving（2026年7月14日 10:20–11:20 · Session Chair：Satish Puri）

---

## 英文摘要

Large Language Model (LLM) inference has emerged as a fundamental paradigm, however, variations in output length cause severe workload imbalance in the decode phase, particularly for long-output reasoning tasks. Existing systems, such as PD disaggregation architectures, rely on static prefill-to-decode scheduling, which often results in SLO violations and OOM failures under evolving decode workloads. In this paper, we propose STAR, a decode rescheduling system powered by length prediction to anticipate future workloads. Our core contributions include: (1) A lightweight and continuous LLM-native prediction method that leverages LLM hidden state to model remaining generation length with high precision (reducing MAE by 49.42%) and low overhead (cutting predictor parameters by 93.28%); (2) A rescheduling solution in decode phase with a dynamic balancing mechanism that integrates current and predicted workloads, reducing P99 TPOT by 75.1% and achieving 2.63× higher goodput.

## 中文摘要

大语言模型（LLM）推理已成为一种基础范式，但输出长度的变化会在解码阶段造成严重的负载不均衡，尤其是对于长输出推理任务。现有系统（如 PD 分离架构）依赖静态的预填充到解码调度，在解码负载持续演变时往往导致 SLO 违规和 OOM 失败。本文提出 STAR——一个由长度预测驱动、用于预判未来负载的解码重调度系统。我们的核心贡献包括：(1) 一种轻量且持续的 LLM 原生预测方法，利用 LLM 隐藏状态以高精度（MAE 降低 49.42%）和低开销（预测器参数减少 93.28%）对剩余生成长度建模；(2) 一种解码阶段的重调度方案，其动态均衡机制同时整合当前负载与预测负载，将 P99 TPOT 降低 75.1%，并实现 2.63 倍的有效吞吐（goodput）。

## 英文关键词

LLM Serving; Decode Rescheduling; Generation Length Prediction; Load Balancing; Prefill-Decode Disaggregation

## 中文关键词

LLM 服务；解码重调度；生成长度预测；负载均衡；预填充-解码分离

---

[← 返回 Session 1 — LLM Inference: Scheduling & Serving](index.md)
