---
title: "A Framework for Developing and Optimizing Fully Homomorphic Encryption Programs on GPUs"
description: "ASPLOS 2026 · Session 7A · 面向GPU的全同态加密程序开发与优化框架"
tags:
  - "ASPLOS2026"
  - "Session 7A"
  - "Fully Homomorphic Encryption"
---

# A Framework for Developing and Optimizing Fully Homomorphic Encryption Programs on GPUs

**中文标题：** 面向GPU的全同态加密程序开发与优化框架

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhuoran Ji (Shandong University), Jianyu Zhao (Shandong University), Guang Fan (Ant Group), Mingzhe Zhang (Ant Research), Shoumeng Yan (Ant Group), Xueyu Wu (The University of Hong Kong), Lei Ju (Shandong University)

**单位：** Shandong University；Ant Group；Ant Research；The University of Hong Kong

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790120) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

In sensitive domains such as healthcare and finance, machine learning increasingly employs Fully Homomorphic Encryption (FHE) to secure both user data and models. Although FHE's intrinsic parallelism naturally aligns with GPU architectures, optimizing GPU kernels alone remains insufficient for efficient end-to-end FHE application development. The inherent complexity of FHE schemes and intricate GPUspecific details impede developers from focusing on highlevel program logic. Additionally, FHE's high memory requirements, fine-grained memory operations, and redundant computations introduce further optimization challenges, resulting in inefficiencies even when GPU kernels are individually optimized. This paper introduces EasyFHE, a framework designed to simplify the development and optimization of GPU-accelerated FHE applications. Similar to PyTorch, EasyFHE provides high-level interfaces for defining computational logic while automatically handling low-level tasks, such as implementation selection and memory management. Furthermore, it incorporates an optimization framework that systematically addresses performance bottlenecks by applying tailored optimization passes during the lowering from high-level FHE programs to GPU kernels. Compared to state-of-the-art open-source GPU FHE libraries, EasyFHE uniquely supports FHE programs with memory requirements exceeding typical GPU capacities, achieving an average speedup of 2.88× with a peak of 4.39×.

## 中文摘要

在医疗和金融等敏感领域，机器学习越来越多地采用全同态加密（Fully Homomorphic Encryption, FHE）来同时保护用户数据和模型。尽管FHE固有的并行性与GPU架构天然契合，但仅优化GPU内核仍不足以支撑高效的端到端FHE应用开发。FHE方案自身的复杂性以及错综复杂的GPU相关细节，阻碍开发者专注于高层程序逻辑。此外，FHE的高内存需求、细粒度内存操作和冗余计算带来了进一步的优化挑战，导致即使各个GPU内核分别得到优化，整体仍然低效。本文提出EasyFHE，一个旨在简化GPU加速FHE应用开发与优化的框架。与PyTorch类似，EasyFHE提供高层接口用于定义计算逻辑，同时自动处理实现选择与内存管理等底层任务。此外，它包含一个优化框架，在将高层FHE程序下降为GPU内核的过程中应用定制化的优化 pass，系统性地解决性能瓶颈。与最先进的开源GPU FHE库相比，EasyFHE独有地支持内存需求超出典型GPU容量的FHE程序，平均加速2.88×，峰值达4.39×。

## 英文关键词

Fully homomorphic encryption, Cryptography, GPU, Framework, Optimization

## 中文关键词

全同态加密；密码学；GPU；框架；优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790120)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2026](../index.md)
