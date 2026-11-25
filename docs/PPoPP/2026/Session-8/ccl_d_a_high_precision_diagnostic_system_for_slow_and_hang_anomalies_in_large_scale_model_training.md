---
title: "CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training"
description: "PPoPP 2026 Session 8（Distributed Training）：rank 级实时探针+自动根因定位，6 分钟内锁定故障 GPU 卡"
tags:
  - "PPoPP2026"
  - "Session-8"
  - "Distributed Training"
  - "collective communication"
  - "anomaly diagnosis"
  - "large-scale training"
authors:
  - "Yida Gu"
  - "Fakang Wang"
  - "Jianhao Fu"
  - "Zhenhang Sun"
  - "Qianyu Zhang"
  - "Hairui Zhao"
  - "Xingchen Liu"
  - "Yang Tian"
  - "Wenjing Huang"
  - "Zedong Liu"
  - "Yifan Chen"
  - "Jinwu Yang"
  - "Yueyuan Zhou"
  - "Qian Zhao"
  - "Haoxu Li"
  - "Tao Wang"
  - "Feng Yu"
  - "Zhan Wang"
  - "Guangming Tan"
  - "Dingwen Tao"
session: "Session 8: Distributed Training"
session_number: 8
session_chair: "Bo Fang"
date: "2026-02-03"
time: "15:10–15:30"
room: "Balmoral"
doi: "10.1145/3774934.3786429"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Nominee"
---

# CCL-D: A High-Precision Diagnostic System for Slow and Hang Anomalies in Large-Scale Model Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出慢/挂起异常诊断系统 CCL-D，用 rank 级实时探针测量跨层异常指标、由分析器自动定位根因，4000 卡集群一年部署可 6 分钟内锁定故障 GPU rank。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 8: Distributed Training</p>
</div>

**作者**：Yida Gu, Fakang Wang, Jianhao Fu, Zhenhang Sun, Qianyu Zhang, Hairui Zhao, Xingchen Liu, Yang Tian, Wenjing Huang, Zedong Liu, Yifan Chen, Jinwu Yang, Yueyuan Zhou, Qian Zhao, Haoxu Li, Tao Wang, Feng Yu, Zhan Wang, Guangming Tan, and Dingwen Tao — University of Chinese Academy of Sciences, China; Ant Group, China; Jilin University, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 15:10–15:30 · Session 8: Distributed Training（主席：Bo Fang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786429) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Nominee**

---

## 英文摘要

As training scales grow, collective communication libraries (CCL) increasingly face anomalies arising from complex interactions among hardware, software, and environmental factors. These anomalies typically manifest as slow/hang communication, the most frequent and time-consuming category to diagnose. However, traditional diagnostic methods remain inaccurate and inefficient, frequently requiring hours or even days for root cause analysis. To address this, 425 we propose CCL-D, a high-precision diagnostic system designed to detect and locate slow/hang anomalies in large-scale distributed training. CCL-D integrates a rank-level real-time probe with an intelligent decision analyzer. The probe measures cross-layer anomaly metrics using a lightweight distributed tracing framework to monitor communication traffic. The analyzer performs automated anomaly detection and root-cause location, precisely identifying the faulty GPU rank. Deployed on a 4,000-GPU cluster over one year, CCL-D achieved near-complete coverage of known slow/hang anomalies and pinpointed affected ranks within 6 minutes—substantially outperforming existing solutions.

## 中文摘要

随着训练规模增长，集合通信库（CCL）日益面临由硬件、软件与环境因素之间复杂交互所引发的异常。这些异常通常表现为通信缓慢/挂起，是出现最频繁、诊断最耗时的一类问题。然而，传统诊断方法仍不准确且效率低下，根因分析常常需要数小时甚至数天。为此，我们提出 CCL-D，一个用于检测并定位大规模分布式训练中缓慢/挂起异常的高精度诊断系统。CCL-D 将 rank 级实时探针与智能决策分析器相结合。探针使用轻量级分布式追踪框架测量跨层异常指标，以监控通信流量。分析器执行自动异常检测与根因定位，精确识别出故障 GPU rank。CCL-D 在 4,000 块 GPU 的集群上部署一年，对已知的缓慢/挂起异常实现了近乎完全的覆盖，并在 6 分钟内定位受影响的 rank，显著优于现有方案。

## 英文关键词

Fault tolerance, anomaly detection, diagnosic system, LLM training

## 中文关键词

容错；异常检测；诊断系统；LLM 训练

---

## 一句话总结

> 提出慢/挂起异常诊断系统 CCL-D，用 rank 级实时探针测量跨层异常指标、由分析器自动定位根因，4000 卡集群一年部署可 6 分钟内锁定故障 GPU rank。

## 研究问题

训练规模扩大使集合通信库受硬件、软件与环境复杂交互影响而频发异常，其中慢/挂起通信最常见且最耗时诊断，传统方法不准确、往往需要数小时甚至数天才能定位根因。

## 方法简述

- 将 rank 级实时探针与智能决策分析器相结合，构建高精度诊断系统。
- 探针基于轻量级分布式追踪框架测量跨层异常指标，以监控通信流量。
- 分析器执行自动异常检测与根因定位，精确识别出故障的 GPU rank。

## 主要结果

- 在 4000-GPU 集群上部署运行一年，对已知的慢/挂起异常实现了近乎完全的覆盖。
- 可在 6 分钟内定位受影响的 rank，显著优于现有方案。

---

> 所属 Session：[Session 8: Distributed Training](index.md) · 返回 [PPoPP 2026 总览](../index.md)
