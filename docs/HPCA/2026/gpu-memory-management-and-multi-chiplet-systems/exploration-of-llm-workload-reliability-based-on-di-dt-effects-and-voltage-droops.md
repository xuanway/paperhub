---
title: "Exploration of LLM Workload Reliability based on di/dt effects and Voltage Droops"
description: "HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems"
tags:
  - "HPCA2026"
  - "GPU Memory Management and Multi-Chiplet Systems"
---

# Exploration of LLM Workload Reliability based on di/dt effects and Voltage Droops

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Memory Management and Multi-Chiplet Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Memory Management and Multi-Chiplet Systems</p>
</div>

**论文链接**：
**作者**：Zhixing Jiang University of Texas at Austin , Justin Garrigus University of Texas at Austin , Allison Seigler University of Texas at Austin , Ethan Syed University of Texas at Austin , Yan-Lun Huang University of Texas at Austin , Mehdi Sadi Advanced Micro Devices , Tawfik Rahal-Arabi Advanced Micro Devices , Lizy John University of Texas, Austin
**会议**：HPCA 2026

---

## 中文标题

基于 di/dt 效应与电压跌落的大语言模型负载可靠性探究

## 英文摘要

Large language model (LLM) inference workloads have emerged as a critical reliability challenge for cloud GPU systems. Unlike traditional workloads, the highly structured execution of LLMs creates large power oscillations. These oscillations become a vulnerability when their frequency aligns with the resonant modes of a GPU’s power delivery network (PDN), leading to excessive voltage droops and unreliable operation. In this work, we present the first comprehensive profiling of LLM-induced power oscillations, revealing that many workloads generate oscillatory patterns in the MHz range—critically aligning with typical GPU PDN resonant frequencies and leading to excessive voltage droops. To systematically investigate this phenomenon, we developed a novel stressmark framework that generates workloads with controllable, high-frequency power oscillations and voltage droops. Our evaluation shows that operating at a resonant frequency induces voltage droops up to 2× larger than conventional workloads, exceeding critical noise margins. Critically, we find that real LLM workloads operating even near these frequencies generate significant voltage droops greater than 100mV. Based on these findings, we propose a kernel staggering technique that mitigates this threat by shifting power oscillation frequencies away from resonance frequency, successfully reducing voltage droops and reducing reliability concerns. This work provides the first systematic understanding of LLM-PDN resonance and offers a practical solution to improve GPU reliability in AI cloud environments.

## 中文摘要

大语言模型（LLM）推理负载已成为云 GPU 系统的关键可靠性挑战。与传统负载不同，LLM 高度结构化的执行会产生大幅功率振荡。当这些振荡的频率与 GPU 供电网络（PDN）的谐振模式对齐时，便会成为一种脆弱性，导致过大的电压跌落与不可靠运行。本文首次对 LLM 引发的功率振荡进行全面的刻画，发现许多负载会产生 MHz 量级的振荡模式，恰好与典型 GPU PDN 的谐振频率对齐，从而造成过大的电压跌落。为系统研究这一现象，我们开发了一个新颖的 stressmark 框架，可生成具有可控高频功率振荡与电压跌落的负载。评估表明，在谐振频率下运行所引起的电压跌落可达传统负载的 2 倍，超出关键噪声容限。关键的是，我们发现即使运行在接近这些频率的真实 LLM 负载也会产生超过 100mV 的显著电压跌落。基于这些发现，我们提出内核错峰（kernel staggering）技术，通过将功率振荡频率移离谐振频率来缓解该威胁，成功降低了电压跌落并减少了可靠性问题。本工作首次系统性理解了 LLM 与 PDN 的谐振问题，并为提升 AI 云环境中 GPU 的可靠性提供了实用方案。
