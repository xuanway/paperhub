---
title: "Maverick: Rethinking TFHE Bootstrapping on GPUs via Algorithm-Hardware Co-Design"
description: "ASPLOS 2026 · Session 7A · Maverick：借助算法-硬件协同设计重新思考GPU上的TFHE自举"
tags:
  - "ASPLOS2026"
  - "Session 7A"
  - "Fully Homomorphic Encryption"
---

# Maverick: Rethinking TFHE Bootstrapping on GPUs via Algorithm-Hardware Co-Design

**中文标题：** Maverick：借助算法-硬件协同设计重新思考GPU上的TFHE自举

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Zhiwei Wang (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS), Haoqi He (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS), Lutan Zhao (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS), Qingyun Niu (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS), Dan Meng (Institute of Information Engineering, CAS), Rui Hou (State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS)

**单位：** State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS；Institute of Information Engineering, CAS

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790186) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Fully homomorphic encryption (FHE) enables arbitrary computation over encrypted data (ciphertext) without compromising confidentiality. Within this family, TFHE features versatile bootstrapping mechanisms that is attractive for security-critical applications. However, its prohibitive computational cost severely limits practical deployment. While hardware acceleration is promising, mere compute scaling fails to overcome the inherent barriers. In particular, the combination of limited algorithmic parallelism and inadequate understanding of hardware behaviors prevents full exploitation of the available performance headroom. In this paper, we present Maverick, a GPU-based solution that rethinks TFHE bootstrapping acceleration through joint algorithm–hardware co-design. At the algorithmic level, we reconstruct blind rotation by shifting test vectors from pre-loading to post-injection. This reformulation turns the original length-𝑛single chain into a multi-chain structure with √𝑛sub-chains of depth √𝑛, raising external-product (EP) parallelism from 1 to the theoretical bound of √𝑛. At the hardware level, we introduce a partial-domain transformation strategy that terminates the NTT early in a stage-aware manner and selectively shifts computation to downstream operators, redefining operator boundaries to balance the workload across EP operators. Experimental results show that Maverick delivers state-of-the-art GPU acceleration. It outperforms the best existing CPU and GPU baselines by 331.2× and 3.4×, respectively, on programmable bootstrapping, and achieves up to 108.5× speedup over CPU-based circuit bootstrapping. Together, these results highlight the substantial potential of algorithm–hardware co-design for advancing FHE performance on general-purpose platforms.

## 中文摘要

全同态加密（FHE）能够在不损害机密性的情况下对加密数据（密文）进行任意计算。在这一类方案中，TFHE具有灵活多样的自举机制，对安全关键型应用颇具吸引力。然而，其高昂的计算成本严重限制了实际部署。尽管硬件加速前景可期，但单纯的计算规模扩展无法克服其固有障碍。特别是，有限的算法并行性与对硬件行为认识不足相结合，使得无法充分利用可获得的性能空间。本文提出Maverick，一个基于GPU的解决方案，通过算法-硬件联合协同设计重新思考TFHE自举加速。在算法层面，我们通过将测试向量从预加载移位到后注入来重构盲旋转。这一重构将原本长度为𝑛的单链转变为由√𝑛条子链组成、深度为√𝑛的多链结构，将外积（EP）并行度从1提升到理论上界√𝑛。在硬件层面，我们引入部分域变换策略，以阶段感知的方式提前终止NTT，并将计算有选择地转移到下游算子，从而重新定义算子边界，以平衡各EP算子之间的工作负载。实验结果表明，Maverick提供了最先进的GPU加速。在可编程自举上，它分别比现有最好的CPU和GPU基线快331.2×和3.4×，并在基于CPU的电路自举上实现最高108.5×的加速。这些结果共同凸显了算法-硬件协同设计在提升通用平台上FHE性能方面的巨大潜力。

## 英文关键词

Fully Homomorphic Encryption, TFHE, Bootstrapping, GPU acceleration

## 中文关键词

全同态加密；TFHE；自举；GPU加速

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790186)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2026](../index.md)
