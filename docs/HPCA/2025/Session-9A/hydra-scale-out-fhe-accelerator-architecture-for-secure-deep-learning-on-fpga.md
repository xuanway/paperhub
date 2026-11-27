---
title: "Hydra: Scale-out FHE Accelerator Architecture for Secure Deep Learning on FPGA"
description: "HPCA 2025 · The Poker Face of FHE"
tags:
  - "HPCA2025"
  - "The Poker Face of FHE"
---

# Hydra: Scale-out FHE Accelerator Architecture for Secure Deep Learning on FPGA

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Poker Face of FHE。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Poker Face of FHE</p>
</div>

**论文链接**：
**作者**：Yinghao Yang (Institute of Computing Technology, Chinese Academy of Sciences), Xicheng Xu (Institute of Computing Technology, Chinese Academy of Sciences), Hang Lu (Institute of Computing Technology, Chinese Academy of Sciences), Xiaowei Li (Institute of Computing Technology, Chinese Academy of Sciences)
**会议**：HPCA 2025

---

## 中文标题

Hydra：面向 FPGA 上安全深度学习的横向扩展 FHE 加速器架构

## 英文摘要

Deep learning, including Convolutional Neural Network (CNN) and Large Language Model (LLM), under Fully Homomorphic Encryption (FHE) is very computationally intensive because of the burdensome computations like ciphertext convolution and matrix multiplication, non-linear layers, and bootstrapping. Existing FHE accelerators focus on the high throughput computational units, stacking parallelized clusters to maximize ciphertext inference performance. Nevertheless, this design philosophy cannot leverage the substantial parallelism at the application level and is not scalable for further performance enhancement by simply adding additional compute nodes to cope with the ever-increasing model sizes in the future. In this paper, we propose the high-performance FHE acceleration architecture in a “scale-out” manner for secure deep learning, termed as Hydra. It supports the multi-server scaling and arbitrary computational nodes theoretically, each handling a portion of the deep learning model governed by the central scheduling mechanism on the host server. Hydra exhibits excellent scalability and delivers outstanding performance across a range of compute resource sizes. We highlight the following results: (1) up to 74× and 160× speedup over the SOTA single card accelerator Poseidon and FAB; (2) outperforms 8-card FAB-2 by 12× to 21× for FHE-based CNNs and LLMs; (3) outperforms SOTA ASIC accelerators, CraterLake and SHARP, by 8.1× and 2.5× for LLM OPT-6.7B, and achieves comparable or superior energy efficiency under the same chip technology.

## 中文摘要

在全同态加密（FHE）下进行深度学习，包括卷积神经网络（CNN）和大语言模型（LLM），由于密文卷积、矩阵乘法、非线性层和自举等繁重计算而具有极高的计算强度。现有 FHE 加速器专注于高吞吐计算单元，通过堆叠并行集群来最大化密文推理性能。然而这种设计思路无法利用应用层面的巨大并行性，也不能通过简单增加计算节点来扩展性能，以应对未来不断增长的模型规模。本文提出一种以“横向扩展”方式实现的高性能 FHE 加速架构 Hydra，用于安全深度学习。它理论上支持多服务器扩展与任意数量的计算节点，每个节点处理深度学习模型的一部分，由主机服务器上的中心调度机制控制。Hydra 展现出优异的可扩展性，并在各种计算资源规模下都能提供出色性能。我们强调以下结果：（1）相比最先进的单卡加速器 Poseidon 和 FAB，分别实现最高 74 倍和 160 倍的加速；（2）对于基于 FHE 的 CNN 与 LLM，比 8 卡的 FAB-2 快 12 倍到 21 倍；（3）对于 LLM OPT-6.7B，比最先进的 ASIC 加速器 CraterLake 和 SHARP 分别快 8.1 倍和 2.5 倍，并在相同芯片工艺下达到相当或更优的能效。
