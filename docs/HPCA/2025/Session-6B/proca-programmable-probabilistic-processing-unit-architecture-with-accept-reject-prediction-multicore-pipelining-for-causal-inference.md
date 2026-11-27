---
title: "PROCA: Programmable Probabilistic Processing Unit Architecture with Accept/Reject Prediction & Multicore Pipelining for Causal Inference"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# PROCA: Programmable Probabilistic Processing Unit Architecture with Accept/Reject Prediction & Multicore Pipelining for Causal Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Yihan Fu (Peking University), Anjunyi Fan (Peking University), Wenshuo Yue (Peking University), Hongxiao Zhao (Peking University), Daijing Shi (Peking University), Qiuping Wu (Peking University), Jiayi Li (Peking University), Xiangyu Zhang (Independent Researcher), Yaoyu Tao (Peking University), Yuchao Yang (School of Integrated Circuits, Peking University, Beijing), Bonan Yan (Peking University)
**会议**：HPCA 2025

---

## 中文标题

PROCA：面向因果推断、具备接受/拒绝预测与多核流水的可编程概率处理单元架构

## 英文摘要

Causal inference is an important field in data science and cognitive artificial intelligence. It requires the construction of complex probabilistic models to describe the causal relationships between random variables. Probabilistic models rely on probabilistic programming as a flexible framework. However, the computing speed of probabilistic programming is often hindered by the extensive use of Markov chain Monte Carlo (MCMC) algorithms, even though they are powerful in Bayesian inference. To accelerate MCMC, this work presents PROCA, a programmable MCMC-based probabilistic processing unit architecture. PROCA exploits processing-in-memory function units to generate new samples of Markov chains. PROCA is programmable to execute the computation for arbitrary forms of posterior distribution formulas that software probabilistic programming frameworks support. We develop a novel accept/reject prediction methodology to accelerate the sequential MCMC computation, thereby introducing efficient multi-core pipelining methods. We implement and validate the PROCA architecture with commercial process development kits. The implementation is evaluated based on 9 representative benchmarks, covering PyMC official tutorial probabilistic problems, single-variable probabilistic problems, and real-world causal inference problems. Our comprehensive experiments demonstrate that PROCA achieves a speedup of 172∼4871× compared to Intel Xeon Gold CPU, 42∼1058× compared to NVIDIA A100 GPU, and 1.765× over state-of-the-art MCMC accelerators, respectively. PROCA achieves comparable statistical robustness to the software probabilistic programming frameworks. Compared with state-of-the-art MCMC domain-specific accelerators, our design boosts the energy efficiency by 9.47×.

## 中文摘要

因果推断是数据科学与认知人工智能的重要领域，需构建复杂概率模型描述随机变量间的因果关系，这类模型依赖概率编程这一灵活框架。然而，马尔可夫链蒙特卡洛（MCMC）算法虽在贝叶斯推断中十分强大，其大量使用却常制约概率编程速度。为加速 MCMC，本文提出 PROCA，一种基于 MCMC 的可编程概率处理单元架构。PROCA 利用存内处理功能单元生成马尔可夫链新样本，并可编程执行软件框架支持的任意后验分布公式。我们提出接受/拒绝预测方法加速串行 MCMC 计算，并由此引入高效多核流水。我们基于商用工艺开发工具包实现并验证 PROCA，并在 9 个代表性基准（PyMC 官方教程问题、单变量问题与真实因果推断问题）上评估。实验表明，PROCA 相比 Intel Xeon Gold CPU、NVIDIA A100 GPU 和最先进的 MCMC 加速器分别取得 172∼4871 倍、42∼1058 倍和 1.765 倍加速；其统计鲁棒性与软件框架相当，相比最先进的 MCMC 加速器能效高 9.47 倍。
