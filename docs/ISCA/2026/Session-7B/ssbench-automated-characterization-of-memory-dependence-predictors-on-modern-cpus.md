---
title: "SSBench: Automated Characterization of Memory Dependence Predictors on Modern CPUs"
description: "ISCA 2026 · Session 7B · SSBench: Automated Characterization of Memory Dependence Predictors on Modern CPUs"
tags:
  - "ISCA2026"
  - "Session 7B"
  - "Performance Modeling / Datacenter"
---

# SSBench: Automated Characterization of Memory Dependence Predictors on Modern CPUs

**中文标题：** SSBench: 现代 CPU 上内存依赖预测器的自动化刻画

**所属 Session：** [Session 7B](index.md) · [ISCA 2026](../index.md)

**作者：** Chang Liu, Yu Jin, Yuchen Fan, Tianrui Xiao, Lingfeng Yin, Trevor E. Carlson, Shuwen Deng, Dongsheng Wang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Memory Dependence Predictors (MDPs) improve the performance of modern CPUs by exposing additional parallelism through predicting data dependence between store and load instructions. Since the 1990s, various MDP designs have been proposed across architectures. Recent studies reveal that MDPs are widely deployed on modern CPUs and can be exploited as side channels to leak data. However, because MDP designs are undocumented, characterizing an MDP design still requires complicated manual analysis. This paper presents SSBench, the first framework to automate the study of MDPs for security on modern CPUs. We first propose a novel workflow-based MDP taxonomy to classify current MDP designs into six categories, and exploit MDP timing side channels for automated MDP identification. We then propose the counter-based model solver for state machine analysis, and the store-load bounce method for organization analysis. Based on these techniques, we deploy SSBench, which performs cross-platform automated identification and characterization of MDPs on more than 30 CPUs from Intel, AMD, Arm, Apple and RISC-V, and uncovers 14 distinct MDP configurations. Based on SSBench’s findings, we propose three novel MDP side-channel attacks. First, on Intel CPUs, we build an MDP-based Weird Machine that achieves up to a 100ˆ performance improvement over state-of-the-art implementations. Second, on AMD CPUs, we develop a byte-level control-flow attack that breaks the inverse modular function used in RSA key generation in the latest version of WolfSSL. Third, we build the first cache/TLB-free covert channel on Apple CPUs, achieving better performance and stealthiness than the state-of-the-art cache and TLB covert channels.

## 中文摘要

内存依赖预测器（MDP）通过预测存储与加载指令之间的数据依赖来暴露额外并行性，从而提升现代 CPU 的性能。自 20 世纪 90 年代以来，各种 MDP 设计在不同架构上被相继提出。近期研究表明，MDP 在现代 CPU 上被广泛部署，并可被用作泄露数据的侧信道。然而，由于 MDP 设计未公开文档，刻画一个 MDP 设计仍需复杂的人工分析。本文提出 SSBench，首个面向现代 CPU 上 MDP 安全研究的自动化框架。我们首先提出一种新颖的基于工作流的 MDP 分类法，将现有 MDP 设计分为六类，并利用 MDP 时序侧信道实现 MDP 的自动化识别。随后，我们提出用于状态机分析的基于计数器的模型求解器，以及用于组织结构分析的存储-加载弹跳（store-load bounce）方法。基于这些技术，我们部署了 SSBench，在来自 Intel、AMD、Arm、Apple 和 RISC-V 的 30 多个 CPU 上执行跨平台的 MDP 自动化识别与刻画，并发现了 14 种不同的 MDP 配置。基于 SSBench 的发现，我们提出三种新颖的 MDP 侧信道攻击。首先，在 Intel CPU 上，我们构建了一个基于 MDP 的 Weird Machine，相比最先进实现实现了最高 100× 的性能提升。其次，在 AMD CPU 上，我们开发了一种字节级控制流攻击，攻破了最新版 WolfSSL 中用于 RSA 密钥生成的模逆函数。第三，我们在 Apple CPU 上构建了首个无缓存、无 TLB 的隐蔽信道，其性能与隐蔽性均优于最先进的缓存和 TLB 隐蔽信道。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：CPU-Security/SSBench](https://github.com/CPU-Security/SSBench)
- [实验材料归档（Zenodo 19447258）](https://zenodo.org/records/19447258)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 7B](index.md) · [返回 ISCA 2026](../index.md)
