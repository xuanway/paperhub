---
title: "Manta: Hybrid-Sensitive Type Inference Toward Type-Assisted Bug Detection for Stripped Binaries"
description: "ASPLOS 2025 · Session 6D · Manta：面向剥离二进制文件类型辅助缺陷检测的混合敏感度类型推断"
tags:
  - "ASPLOS2025"
  - "Session 6D"
  - "Testing"
---

# Manta: Hybrid-Sensitive Type Inference Toward Type-Assisted Bug Detection for Stripped Binaries

**中文标题：** Manta：面向剥离二进制文件类型辅助缺陷检测的混合敏感度类型推断

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Chengfeng Ye (The Hong Kong University of Science and Technology), Yuandao Cai (The Hong Kong University of Science and Technology), Anshunkang Zhou (The Hong Kong University of Science and Technology), Heqing Huang (City University of Hong Kong), Hao Ling (The Hong Kong University of Science and Technology), Charles Zhang (The Hong Kong University of Science and Technology)

**单位：** The Hong Kong University of Science and Technology；City University of Hong Kong

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674177) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Static binary bug detection has been a prominent approach for ensuring the security of binaries used in our daily lives. However, the type information lost in binaries prevents the improvement opportunity for a static analyzer to utilize type information to prune away infeasible facts and increase analysis precision. To make binary bug detection more practical with higher precision, in this work, we propose the first hybrid-sensitive type inference, Manta, that combines dataflow analysis with different sensitivities to complement each other and infer precise types for many variables. The inferred types are then used to assist with bug detection by pruning infeasible indirect call targets and data dependencies. Our experiments indicate Manta outperforms prior work by inferring types with 78.7% precision and 97.2% recall. Based on the inferred types, we can prune away 63.9% more infeasible indirect-call targets compared to existing type analysis techniques and perform program slicing on binaries with 61.1% similarity to that on source code. Moreover, Manta has led to 86 new developer-confirmed vulnerabilities in many popular IoT firmware, with 64 CVE/PSV IDs assigned.

## 中文摘要

静态二进制缺陷检测一直是保障我们日常使用的二进制文件安全的一种重要方法。然而，二进制文件中丢失的类型信息使静态分析器无法利用类型信息剔除不可行的事实并提升分析精度，从而错失改进机会。为使二进制缺陷检测更实用且精度更高，本工作提出首个混合敏感度类型推断方法 Manta，它将具有不同敏感度的数据流分析相结合、彼此互补，为众多变量推断出精确的类型。推断出的类型随后被用于辅助缺陷检测，通过剔除不可行的间接调用目标与数据依赖来实现。实验表明，Manta 以 78.7% 的精度和 97.2% 的召回率推断类型，优于先前工作。基于推断出的类型，相比现有类型分析技术，我们能够多剔除 63.9% 的不可行间接调用目标，并在二进制文件上执行程序切片，其结果与在源代码上切片的相似度达到 61.1%。此外，Manta 在许多流行的 IoT 固件中促成了 86 个经开发者确认的新漏洞，并分配了 64 个 CVE/PSV 编号。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674177)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2025](../index.md)
