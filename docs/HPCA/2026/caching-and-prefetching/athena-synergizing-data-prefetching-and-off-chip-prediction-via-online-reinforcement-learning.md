---
title: "Athena: Synergizing Data Prefetching and Off-Chip Prediction via Online Reinforcement Learning"
description: "HPCA 2026 · Caching and Prefetching"
tags:
  - "HPCA2026"
  - "Caching and Prefetching"
---

# Athena: Synergizing Data Prefetching and Off-Chip Prediction via Online Reinforcement Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Caching and Prefetching。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Caching and Prefetching</p>
</div>

**论文链接**：
**作者**：Zhenrong Lang ETH Zürich , Rahul Bera ETH Zurich , Caroline Hengartner ETH Zürich , Konstantinos Kanellopoulos ETH Zurich , Rakesh Kumar NTNU , Mohammad Sadrosadati ETH Zürich , Onur Mutlu ETH Zurich
**会议**：HPCA 2026

---

## 中文标题

Athena：通过在线强化学习协同数据预取与片外预测

## 英文摘要

Prefetching and off-chip prediction are two techniques proposed to hide long memory access latencies in high-performance processors. In this work, we demonstrate that: (1) prefetching and off-chip prediction often provide complementary performance benefits, yet (2) naively combining these two mechanisms often fails to realize their full performance potential, and (3) existing prefetcher control policies (both heuristic- and learning-based) leave significant room for performance improvement behind. Our goal is to design a holistic framework that can autonomously learn to coordinate an off-chip predictor with multiple prefetchers employed at various cache levels, delivering consistent performance benefits across a wide range of workloads and system configurations. To this end, we propose a new technique called Athena, which models the coordination between prefetchers and off-chip predictor (OCP) as a reinforcement learning (RL) problem. Athena acts as the RL agent that observes multiple system-level features (e.g., prefetcher/OCP accuracy, bandwidth usage) over an epoch of program execution, and uses them as state information to select a coordination action (i.e., enabling the prefetcher and/or OCP, and adjusting prefetcher aggressiveness). At the end of every epoch, Athena receives a numerical reward that measures the change in multiple system-level metrics (e.g., number of cycles taken to execute an epoch). Athena uses this reward to autonomously and continuously learn a policy to coordinate prefetchers with OCP. Athena makes a key observation that using performance improvement as the sole RL reward, as used in prior work, is unreliable, as it confounds the effects of the agent’s actions with inherent variations in workload behavior. To address this limitation, Athena introduces a composite reward framework that separates (1) system-level metrics directly influenced by Athena’s actions (e.g., last-level cache misses) from (2) metrics primarily driven by workload phase changes (e.g., number of mispredicted branches). This allows Athena to autonomously learn a coordination policy by isolating the true impact of its actions from inherent variations in workload behavior. Our extensive evaluation using a diverse set of 100 memory-intensive workloads shows that Athena consistently outperforms multiple prior state-of-the-art coordination policies across a wide range of system configurations with various combinations of underlying prefetchers at various cache levels, OCPs, and main memory bandwidths, while incurring only modest storage overhead and design complexity. The source code of Athena is freely available at https://github.com/CMU-SAFARI/Athena.

## 中文摘要

预取与片外预测是高性能处理器中用于隐藏长内存访问时延的两项技术。本文表明：两者往往带来互补的性能收益，但简单结合常无法发挥其全部潜力，且现有预取器控制策略（无论基于启发式还是基于学习）仍留有可观的性能提升空间。我们的目标是设计一个整体框架，能自主学习协调片外预测器（OCP）与不同缓存层级的多个预取器，在广泛负载与系统配置下稳定获益。为此我们提出 Athena，将预取器与 OCP 之间的协调建模为强化学习（RL）问题。Athena 作为 RL 智能体，在一个程序执行 epoch 内观察预取器/OCP 准确率、带宽使用等系统级特征作为状态，据此选择协调动作（启用预取器和/或 OCP、调整预取激进度），并在 epoch 结束时获得衡量多项系统级指标（如执行一个 epoch 所需周期数）变化的数值奖励，从而持续自主学习协调策略。Athena 的关键观察是：仅以性能提升为奖励并不可靠，因为它把智能体动作的影响与负载行为的固有波动混为一谈。为此 Athena 引入复合奖励框架，将直接受其动作影响的指标（如末级缓存缺失）与主要由负载阶段变化驱动的指标（如分支预测错误数）分离，以隔离其真实影响。在 100 个内存密集型负载上的评估显示，Athena 在多种系统配置下持续优于先前多种最先进的协调策略，且仅带来适度的存储开销与设计复杂度。源代码公开于 https://github.com/CMU-SAFARI/Athena。
