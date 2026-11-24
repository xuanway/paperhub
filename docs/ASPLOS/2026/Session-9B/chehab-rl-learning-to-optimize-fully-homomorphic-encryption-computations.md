---
title: "CHEHAB RL: Learning to Optimize Fully Homomorphic Encryption Computations"
description: "ASPLOS 2026 · Session 9B · CHEHAB RL：学习优化全同态加密计算"
tags:
  - "ASPLOS2026"
  - "Session 9B"
  - "Quantum & Emerging Computing"
---

# CHEHAB RL: Learning to Optimize Fully Homomorphic Encryption Computations

**中文标题：** CHEHAB RL：学习优化全同态加密计算

**所属 Session：** [Session 9B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Bilel Sefsaf (New York University Abu Dhabi and Ecole Superieure d'Informatique), Abderraouf Dandani (New York University Abu Dhabi and Ecole Superieure d'Informatique), Abdessamed Seddiki (New York University Abu Dhabi and Ecole Superieure d'Informatique), Arab Mohammed (New York University Abu Dhabi and Ecole Superieure d'Informatique), Eduardo Chielle (New York University Abu Dhabi), Mihalis Maniatakos (New York University Abu Dhabi), Riyadh Baghdadi (New York University Abu Dhabi)

**单位：** New York University Abu Dhabi and Ecole Superieure d'Informatique；New York University Abu Dhabi

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790138) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fully Homomorphic Encryption (FHE) enables computations directly on encrypted data, but its high computational cost remains a significant barrier. Writing efficient FHE code is a complex task requiring cryptographic expertise, and finding the optimal sequence of program transformations is often intractable. In this paper, we propose CHEHAB RL, a novel framework that leverages deep reinforcement learning (RL) to automate FHE code optimization. Instead of relying on predefined heuristics or combinatorial search, our method trains an RL agent to learn an effective policy for applying a sequence of rewriting rules to automatically vectorize scalar FHE code while reducing instruction latency and noise growth. The proposed approach supports the optimization of both structured and unstructured code. To train the agent, we synthesize a diverse dataset of computations using a large language model (LLM). We integrate our proposed approach into the CHEHAB FHE compiler and evaluate it on a suite of benchmarks, comparing its performance against Coyote, a state-of-the-art vectorizing FHE compiler. The results show that our approach generates code that is 5.3× faster in execution, accumulates 2.54× less noise, while the compilation process itself is 27.9× faster than Coyote (geometric means).

## 中文摘要

全同态加密（FHE）使得可以直接在加密数据上进行计算，但其高昂的计算成本仍是显著障碍。编写高效的 FHE 代码是一项需要密码学专业知识的复杂任务，而找到最优的程序变换序列往往难以处理。在本文中，我们提出 CHEHAB RL，一个利用深度强化学习（RL）来自动化 FHE 代码优化的新框架。我们的方法不依赖预定义的启发式规则或组合搜索，而是训练一个 RL 智能体，让它学习一种有效的策略，用于应用一系列重写规则，从而自动向量化标量 FHE 代码，同时降低指令延迟和噪声增长。所提方法支持对结构化和非结构化代码的优化。为训练该智能体，我们使用大语言模型（LLM）合成了一个多样化的计算数据集。我们将所提方法集成到 CHEHAB FHE 编译器中，并在一组基准上对其进行评估，将其性能与最先进的向量化 FHE 编译器 Coyote 进行比较。结果表明，我们的方法生成的代码执行速度快 5.3×、累积噪声少 2.54×，而编译过程本身比 Coyote 快 27.9×（几何平均值）。

## 英文关键词

Automatic Code Optimization, Compiler, FHE, Fully Homomorphic Encryption, Reinforcement Learning

## 中文关键词

自动代码优化；编译器；FHE；全同态加密；强化学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790138)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9B](index.md) · [返回 ASPLOS 2026](../index.md)
