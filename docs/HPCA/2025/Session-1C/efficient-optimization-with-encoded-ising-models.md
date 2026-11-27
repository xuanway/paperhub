---
title: "Efficient Optimization with Encoded Ising Models"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# Efficient Optimization with Encoded Ising Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Devrath Iyer (Stanford University), Sara Achour (Stanford University)
**会议**：HPCA 2025

---

## 中文标题

基于编码伊辛模型的高效优化

## 英文摘要

Many promising computing substrates, including quantum computers, oscillator-based computers, and p-computers solve constrained combinatorial optimization problems by minimizing energy functions called Ising models. Because Ising solvers explore an unconstrained search space, Ising models for many popular optimization problems must include penalty terms to raise the energy of infeasible solutions that would appear optimal otherwise. We observe that for some problems, Ising solvers spend the majority of computation time exploring this invalid state and often never find a feasible solution. We introduce the encoded Ising model (E-I model), an extension to the Ising model that uses a digital encoding circuit to vastly reduce the proportion of time a solver spends exploring invalid states. We present Fuse, a software framework that enables the description of such functions and automatically lowers them to a p-computer. Our formulation reduces the number of iterations to a solution by a factor of 7.2-52000x and achieves up to 100.0% higher estimated success probability over baseline formulations.

## 中文摘要

许多富有前景的计算基底，包括量子计算机、基于振荡器的计算机以及 p 计算机，都通过最小化被称为伊辛模型的能量函数来求解受约束的组合优化问题。由于伊辛求解器在无约束的搜索空间中探索，许多常见优化问题的伊辛模型必须加入惩罚项，以提高那些否则会被视为最优的不可行解的能量。我们观察到，对某些问题，伊辛求解器将大部分计算时间用于探索这类非法状态，且往往始终找不到可行解。我们提出编码伊辛模型（E-I 模型），它是对伊辛模型的扩展，使用数字编码电路大幅降低求解器探索非法状态的时间占比。我们给出 Fuse，一个能够描述此类函数并将其自动下沉到 p 计算机的软件框架。相比基线形式化方法，我们的方案将求得解所需的迭代次数减少 7.2–52000 倍，并将估计成功概率最高提升 100.0%。
