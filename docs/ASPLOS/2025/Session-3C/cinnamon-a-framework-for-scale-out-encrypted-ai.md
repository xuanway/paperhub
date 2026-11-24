---
title: "Cinnamon: A Framework for Scale-Out Encrypted AI"
description: "ASPLOS 2025 · Session 3C · Cinnamon：面向规模化扩展的加密 AI 框架"
tags:
  - "ASPLOS2025"
  - "Session 3C"
  - "ML Security"
---

# Cinnamon: A Framework for Scale-Out Encrypted AI

**中文标题：** Cinnamon：面向规模化扩展的加密 AI 框架

**所属 Session：** [Session 3C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Siddharth Jayashankar (Carnegie Mellon University), Edward Chen (Carnegie Mellon University), Tom Tang (Carnegie Mellon University), Wenting Zheng (Carnegie Mellon University), Dimitrios Skarlatos (Carnegie Mellon University)

**单位：** Carnegie Mellon University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707260) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Fully homomorphic encryption (FHE) is a promising cryptographic solution that enables computation on encrypted data, but its adoption remains a challenge due to steep performance overheads. Although recent FHE architectures have made valiant efforts to narrow the performance gap, they not only have massive monolithic chip designs but also only target small ML workloads. We present Cinnamon, a framework for accelerating state-of-the-art ML workloads that are encrypted using FHE. Cinnamon accelerates encrypted computing by exploiting parallelism at all levels of a program, using novel algorithms, compilers, and hardware techniques to create a scale-out design for FHE as opposed to a monolithic chip design. Our evaluation of the Cinnamon framework on small programs shows a 2.3× improvement in performance compared to prior state-of-the-art designs. Further, we use Cinnamon to show for the first time the scalability of large ML models such as the BERT language model in FHE. Cinnamon achieves a speedup of 36, 600× compared to a CPU bringing down the inference time from 17 hours to 1.67 seconds thereby enabling new opportunities for privacy-preserving machine learning. Finally, Cinnamon's parallelization strategies and architectural extensions reduce the required resources per-chip leading to a 5× and 2.68× improvement in performance-per-dollar compared to state-of-the-art monolithic and chiplet architectures respectively.

## 中文摘要

全同态加密（FHE）是一种有前景的密码学方案，它使在加密数据上进行计算成为可能，但由于性能开销陡峭，其采用仍面临挑战。尽管近期的 FHE 架构为缩小性能差距做出了巨大努力，但它们不仅采用庞大的单体芯片设计，而且只针对小规模的 ML 工作负载。我们提出 Cinnamon，一个用于加速使用 FHE 加密的最先进 ML 工作负载的框架。Cinnamon 通过利用程序各个层级的并行性来加速加密计算，使用新颖的算法、编译器和硬件技术，为 FHE 构建可横向扩展的设计，而非单体芯片设计。我们在小程序上对 Cinnamon 框架的评估显示，相比先前最先进的设计，性能提升 2.3×。此外，我们使用 Cinnamon 首次展示了 BERT 语言模型等大型 ML 模型在 FHE 下的可扩展性。Cinnamon 相比 CPU 实现了 36,600× 的加速，将推理时间从 17 小时降至 1.67 秒，从而为隐私保护机器学习开辟了新的机遇。最后，Cinnamon 的并行化策略与架构扩展降低了每芯片所需的资源，使其性能/美元相比最先进的单体架构和芯粒架构分别提升 5× 和 2.68×。

## 英文关键词

Fully Homomorphic Encryption, Encrypted AI, Parallelism, Accelerators

## 中文关键词

全同态加密；加密 AI；并行性；加速器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707260)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3C](index.md) · [返回 ASPLOS 2025](../index.md)
