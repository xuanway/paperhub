---
title: "BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs"
description: "ASPLOS 2025 · Session 9D · BatchZK：面向零知识证明批量生成的全流水线 GPU 加速系统"
tags:
  - "ASPLOS2025"
  - "Session 9D"
  - "Trust"
---

# BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs

**中文标题：** BatchZK：面向零知识证明批量生成的全流水线 GPU 加速系统

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Tao Lu (Zhejiang University,National University of Singapore), Yuxun Chen (Zhejiang University), Zonghui Wang (Zhejiang University), Xiaohang Wang (Zhejiang University), Wenzhi Chen (Zhejiang University), Jiaheng Zhang (National University of Singapore)

**单位：** Zhejiang University,National University of Singapore；Zhejiang University；National University of Singapore

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707270) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Zero-knowledge proof (ZKP) is a cryptographic primitive that enables one party to prove the validity of a statement to other parties without disclosing any secret information. With its widespread adoption in applications such as blockchain and verifiable machine learning, the demand for generating zero-knowledge proofs has increased dramatically. In recent years, considerable efforts have been directed toward developing GPU-accelerated systems for proof generation. However, these previous systems only explored efficiently generating a single proof by reducing latency rather than batch generation to provide high throughput. We propose a fully pipelined GPU-accelerated system for batch generation of zero-knowledge proofs. Our system has three features to improve throughput. First, we design a pipelined approach that enables each GPU thread to continuously execute its designated proof generation task without being idle. Second, our system supports recent efficient ZKP protocols with their computational modules: sum-check protocol, Merkle tree, and linear-time encoder. We customize these modules to fit our pipelined execution. Third, we adopt a dynamic loading method for the data required for proof generation, reducing the required device memory. Moreover, multi-stream technology enables the overlap of data transfers and GPU computations, reducing overhead caused by data exchanges between host and device memory. We implement our system and evaluate it on various GPU cards. The results show that our system achieves more than 259.5× higher throughput compared to state-of-the-art GPUaccelerated systems. Moreover, we deploy our system in the verifiable machine learning application, where our system generates 9.52 proofs per second, successfully achieving subsecond proof generation for the first time in this field.

## 中文摘要

零知识证明（ZKP）是一种密码学原语，使一方能够在向其他方证明某个陈述有效性的同时不披露任何秘密信息。随着其在区块链和可验证机器学习等应用中的广泛采用，零知识证明的生成需求急剧增长。近年来，已有大量工作致力于开发用于证明生成的 GPU 加速系统。然而，此前的这些系统仅通过降低时延来高效生成单个证明，而未着眼于以批量生成提供高吞吐。我们提出一种用于零知识证明批量生成的全流水线 GPU 加速系统。该系统具备三项提升吞吐的特性。首先，我们设计了一种流水线方法，使每个 GPU 线程无需空闲即可持续执行其指定的证明生成任务。其次，我们的系统支持近期的高效 ZKP 协议及其计算模块：sum-check 协议、Merkle 树和线性时间编码器。我们对这些模块进行定制以适配流水线执行。第三，我们对证明生成所需的数据采用动态加载方法，减少所需的设备内存。此外，多流技术使数据传输与 GPU 计算得以重叠，从而降低主机与设备内存之间数据交换所带来的开销。我们实现了该系统并在多种 GPU 卡上进行评估。结果表明，与最先进的 GPU 加速系统相比，我们的系统吞吐量高出 259.5× 以上。此外，我们已将系统部署于可验证机器学习应用中，该系统中每秒生成 9.52 个证明，首次在该领域实现了亚秒级证明生成。

## 英文关键词

GPU acceleration; zero-knowledge proof; pipeline; sumcheck protocol; Merkle tree; linear-time encoder

## 中文关键词

GPU 加速；零知识证明；流水线；sumcheck 协议；Merkle 树；线性时间编码器

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707270)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2025](../index.md)
