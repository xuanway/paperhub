---
title: "TensorTEE: Unifying Heterogeneous TEE Granularity for Efficient Secure Collaborative Tensor Computing"
description: "ASPLOS 2025 · Session 9D · TensorTEE：统一异构 TEE 粒度以实现高效安全协同张量计算"
tags:
  - "ASPLOS2025"
  - "Session 9D"
  - "Trust"
---

# TensorTEE: Unifying Heterogeneous TEE Granularity for Efficient Secure Collaborative Tensor Computing

**中文标题：** TensorTEE：统一异构 TEE 粒度以实现高效安全协同张量计算

**所属 Session：** [Session 9D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Husheng Han (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences), Xinyao Zheng (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences ), Yuanbo Wen (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Yifan Hao (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Erhu Feng (IPADS, Shanghai Jiao Tong University,Engineering Research Center for Domain-specific Operating Systems (MoE)), Ling Liang (Peking university), Jianan Mu (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences ), Xiaqing Li (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Tianyun Ma (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Cambricon Technologies), Pengwei Jin (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences ), Xinkai Song (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Zidong Du (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Shanghai Innovation Center for Processor Technologies, SHIC), Qi Guo (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Xing Hu (SKLP, Institute of Computing Technology, Chinese Academy of Sciences,ZGC LAB)

**单位：** SKLP, Institute of Computing Technology, Chinese Academy of Sciences,University of Chinese Academy of Sciences；SKLP, Institute of Computing Technology, Chinese Academy of Sciences；MoE；Peking university；SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Cambricon Technologies；SKLP, Institute of Computing Technology, Chinese Academy of Sciences,Shanghai Innovation Center for Processor Technologies, SHIC；SKLP, Institute of Computing Technology, Chinese Academy of Sciences,ZGC LAB

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674168) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Heterogeneous collaborative computing with NPU and CPU has received widespread attention due to its substantial performance benefits. To ensure data confidentiality and integrity during computing, Trusted Execution Environments (TEE) is considered a promising solution because of its comparatively lower overhead. However, existing heterogeneous TEE designs are inefficient for collaborative computing due to fine and different memory granularities between CPU and NPU. 1) The cacheline granularity of CPU TEE intensifies memory pressure due to its extra memory access, and 2) the cacheline granularity MAC of NPU escalates the pressure on the limited memory storage. 3) Data transfer across heterogeneous enclaves relies on the transit of non-secure regions, resulting in cumbersome re-encryption and scheduling. To address these issues, we propose TensorTEE, a unified tensor-granularity heterogeneous TEE for efficient secure collaborative tensor computing. First, we virtually support tensor granularity in CPU TEE to eliminate the off-chip metadata access by detecting and maintaining tensor structures on-chip. Second, we propose tensor-granularity MAC management with predictive execution to avoid computational stalls while eliminating off-chip MAC storage and access. Moreover, based on the unified granularity, we enable direct data transfer without re-encryption and scheduling dilemmas. Our evaluation is built on enhanced Gem5 and a cycle-accurate NPU simulator. The results show that TensorTEE improves the performance of Large Language Model (LLM) training workloads by 4.0x compared to existing work and incurs only 2.1% overhead compared to non-secure training, offering a practical security assurance for LLM training.

## 中文摘要

基于 NPU 与 CPU 的异构协同计算因其显著的性能收益而受到广泛关注。为在计算过程中确保数据的机密性与完整性，可信执行环境（Trusted Execution Environment，TEE）因开销相对较低而被视为一种有前景的方案。然而，由于 CPU 与 NPU 之间存储粒度细且互不相同，现有异构 TEE 设计在协同计算中效率低下。1）CPU TEE 的缓存行（cacheline）粒度因其额外的内存访问而加剧了内存压力；2）NPU 的缓存行粒度 MAC 加重了有限内存存储的压力；3）跨异构飞地的数据传输依赖非安全区域中转，导致繁琐的重新加密与调度。为解决这些问题，我们提出 TensorTEE，一种统一的张量粒度异构 TEE，用于高效的安全协同张量计算。首先，我们在 CPU TEE 中虚拟地支持张量粒度，通过在片上检测并维护张量结构来消除片外元数据访问。其次，我们提出带预测执行的张量粒度 MAC 管理，在消除片外 MAC 存储与访问的同时避免计算停顿。此外，基于统一的粒度，我们实现了无需重新加密、也无调度困境的直接数据传输。我们的评估基于增强的 Gem5 和周期精确的 NPU 模拟器。结果表明，与现有工作相比，TensorTEE 将大语言模型（LLM）训练工作负载的性能提升 4.0 倍，且相比非安全训练仅引入 2.1% 的开销，为 LLM 训练提供了实用的安全保障。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674168)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9D](index.md) · [返回 ASPLOS 2025](../index.md)
