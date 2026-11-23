---
title: "Need for zkSpeed: Accelerating HyperPlonk for Zero-Knowledge Proofs"
description: "ISCA 2025 · Session 10C · Need for zkSpeed: 为零知识证明加速HyperPlonk"
tags:
  - "ISCA2025"
  - "Session 10C"
  - "Security"
---

# Need for zkSpeed: Accelerating HyperPlonk for Zero-Knowledge Proofs

**中文标题：** Need for zkSpeed: 为零知识证明加速HyperPlonk

**所属 Session：** [Session 10C](index.md) · [ISCA 2025](../index.md)

**作者：** Alhad Daftardar, Jianqiao Mo, Joey Ah-kiow, Benedikt B?nz, Ramesh Karri, Siddharth Garg, Brandon Reagen

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731021) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Zero-Knowledge Proofs (ZKPs) are a rapidly growing technique for privacy-preserving and verifiable computation. ZKPs enable one party (a prover: P) to prove to another (a verifier: V) that a statement is true or correct without revealing any additional in- formation. This powerful capability has led to ZKPs being applied and proposed for application in blockchain technologies, verifiable machine learning, and electronic voting. However, ZKPs have yet to see widespread, ubiquitous adoption due to the exceptionally high computational complexity of the proving process. Naturally, there has been recent work to accelerate ZKP primitives and protocols using GPUs and ASICs. However, the protocols considered so far face one of two challenges: they require a trusted setup for each new application or generate large proofs with high verification costs, limiting their applicability in scenarios with numerous verifiers or strict verification time constraints. HyperPlonk is a state-of-the- art ZKP protocol that supports both one-time, universal setup and small proof sizes/verification costs expected by publicly verifiable, consensus-based systems (e.g., blockchain). While HyperPlonk’s setup and verifier properties are highly desirable, the proving phase is costly. A HyperPlonk prover must compute on large bitwidths (e.g., 255-381b) and polynomials (e.g., of degree 224), employs com- putationally (e.g., MSM) and bandwidth (e.g., SumCheck) intensive kernels, and the complete protocol comprises many steps, each constituting distinct kernels. We present an accelerator, zkSpeed, to address these challenges and effectively accelerate HyperPlonk. zk- Speed provides hardware support for all major primitives (e.g., Sum- Check and Multi-Scalar Multiplications (MSMs)) and judiciously schedules each protocol phase onto the allocated hardware. We leverage high-level synthesis to thoroughly explore and optimize the hardware design tradeoffs of each unit. These are then input into a full-chip simulator for large-scale design space exploration to optimize all aspects of the architecture in unison. Our Pareto anal- ysis demonstrates that with a 366mm2 chip and 2 TB/s of off-chip bandwidth, zkSpeed is able to accelerate the entire proof generation by 801×(geomean) over a CPU baseline.

## 中文摘要

零知识证明（ZKP）是一类快速发展的隐私保护与可验证计算技术。零知识证明允许证明方（P）向验证方（V）证明某个命题成立，同时不泄露任何额外信息。该能力让ZKP被广泛应用于区块链、可验证机器学习、电子投票等场景。但证明阶段极高的计算复杂度，阻碍了ZKP的大规模普及。已有不少工作基于GPU、ASIC加速ZKP原语与协议，然而现有协议通常存在两类短板：要么每个新应用都需要可信初始化，要么生成的证明体积大、验证开销高，不适合验证者数量多、对验证时延严格的场景。

HyperPlonk是前沿零知识证明协议，支持一次性通用可信初始化，同时具备公开可验证、共识类系统（如区块链）所需的小证明体积与低验证开销。虽然HyperPlonk的初始化与验证端特性极具优势，但证明端开销巨大。HyperPlonk证明器需要处理大位宽（例如255–381比特）、高次多项式（例如2²⁴阶），包含计算密集型核心算子（如MSM多标量乘法）与带宽密集型算子（如SumCheck求和校验）；完整协议由大量不同算子的步骤串联而成。

本文提出zkSpeed加速器，专门针对上述痛点加速HyperPlonk。zkSpeed对全部核心原语（SumCheck、MSM等）提供硬件支持，并对协议各个阶段做合理硬件调度。作者借助高层综合（HLS）充分探索各计算单元的硬件折中空间；再将单元模型送入全芯片仿真器，开展大规模设计空间搜索，对架构全局协同优化。帕累托分析表明：在芯片面积366 mm²、片外带宽2 TB/s的配置下，zkSpeed相比CPU基线，整体证明生成速度几何平均提速801倍。

## 英文关键词

Zero-Knowledge Proofs, Cryptography, Hardware Acceleration

## 中文关键词

零知识证明, 密码学, 硬件加速

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731021)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2025](../index.md)
