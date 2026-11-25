---
title: "Adaptive Parallel Training for Graph Neural Networks"
description: "PPoPP 2025 Session 1（Graph Neural Networks）：代价模型自动选择多 GPU 并行策略，训练时间降低 2× 以上"
tags:
  - "PPoPP2025"
  - "Session-1"
  - "Graph Neural Networks"
  - "GNN Training"
  - "Parallel Strategy"
  - "Cost Model"
authors:
  - "Kaihao Ma"
  - "Renjie Liu"
  - "Xiao Yan"
  - "Zhenkun Cai"
  - "Xiang Song"
  - "Minjie Wang"
  - "Yichao Li"
  - "James Cheng"
session: "Session 1: Graph Neural Networks"
session_number: 1
session_chair: "Miao Yin"
date: "2025-03-03"
time: "10:40–11:00"
room: "Acacia D"
doi: "10.1145/3710848.3710883"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Adaptive Parallel Training for Graph Neural Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 APT 系统，用轻量代价模型为不同图数据、模型和硬件自动选择最优的多 GPU GNN 训练并行策略，并以统一执行引擎支撑策略切换。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 1: Graph Neural Networks</p>
</div>

**作者**：Kaihao Ma (The Chinese University of Hong Kong); Renjie Liu (Southern University of Science and Technology); Xiao Yan (Centre for Perceptual and Interactive Intelligence); Zhenkun Cai, Xiang Song (Amazon); Minjie Wang (AWS Shanghai AI Lab); Yichao Li, James Cheng (The Chinese University of Hong Kong)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 10:40–11:00 · Session 1: Graph Neural Networks（主席：Miao Yin）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710883) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 APT 系统，用轻量代价模型为不同图数据、模型和硬件自动选择最优的多 GPU GNN 训练并行策略，并以统一执行引擎支撑策略切换。

## 研究问题

GNN 多 GPU 训练存在多种并行策略，但没有一种策略始终最优；最佳选择取决于图数据集、GNN 模型、训练算法与硬件配置的组合。

## 方法简述

- 分析采样、分区、流水等并行策略的权衡，建立简单而有效的执行时间代价模型。
- 抽象出统一的策略接口，实现可通过配置运行不同策略的统一执行引擎。
- 运行时依据代价模型自动选择并行策略。

## 主要结果

- APT 通常能选中最优或接近最优的策略。
- 与始终使用单一策略相比，训练时间可降低 2× 以上。
- 系统已开源（github.com/kaihaoma/APT）。

<details>
<summary>原文摘要（英文）</summary>

There are several strategies to parallelize graph neural network (GNN) training over multiple GPUs. We observe that there is no consistent winner (i.e., with the shortest running time), and the optimal strategy depends on the graph dataset, GNN model, training algorithm, and hardware configurations. As such, we design the APT system to automatically select efficient parallelization strategies for GNN training tasks. To this end, we analyze the trade-offs of the strategies and design simple yet effective cost models to compare their execution time and facilitate strategy selection. Moreover, we also propose a general abstraction of the strategies, which allows to implement a unified execution engine that can be configured to run different strategies. Our experiments show that APT usually chooses the optimal or a close to optimal strategy, and the training time can be reduced by over 2x compared with always using a single strategy. APT is open-source at.

</details>

---

> 所属 Session：[Session 1: Graph Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
