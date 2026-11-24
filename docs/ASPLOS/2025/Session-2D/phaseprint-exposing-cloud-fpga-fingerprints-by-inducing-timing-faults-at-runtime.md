---
title: "PhasePrint: Exposing Cloud FPGA Fingerprints by Inducing Timing Faults at Runtime"
description: "ASPLOS 2025 · Session 2D · PhasePrint：通过在运行时诱发时序故障揭示云 FPGA 指纹"
tags:
  - "ASPLOS2025"
  - "Session 2D"
  - "FPGAs"
---

# PhasePrint: Exposing Cloud FPGA Fingerprints by Inducing Timing Faults at Runtime

**中文标题：** PhasePrint：通过在运行时诱发时序故障揭示云 FPGA 指纹

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jubayer Mahmod (Virginia Tech), Matthew Hicks (Virginia Tech)

**单位：** Virginia Tech

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716012) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Cloud FPGAs, with their scalable and flexible nature, are rapidly gaining traction as go-to hardware acceleration platforms for compute-intensive workloads. However, their increasing adoption introduces unique security challenges. The hardware-level access that FPGAs provide leads to many vulnerabilities, including the leakage of sensitive information through data remanence and the creation of analog-domain covert channels among users. A foundational requirement in these scenarios is the ability to target an individual FPGA; knowing this, cloud vendors prevent FPGA localization by restricting access to low-level information of the underlying hardware. Beyond aiding adversaries, FPGA localization enables defenders to strategically rotate FPGA usage, preventing prolonged exposure that can lead to confidential data leakage due to long-term data remanence. This paper introduces PhasePrint, a cloud FPGA localization approach using dynamic timing faults in functionally valid circuits. PhasePrint induces timing faults in a specially crafted circuit at runtime and infers delay characteristics from the resulting error pattern—without incorporating information sources blocked by cloud vendors. PhasePrint utilizes an FPGA's internal clock synthesizer to derive a clock pair with a strict phase relationship. By adjusting the phase relationship of these clocks, PhasePrint intentionally causes timing faults at runtime that reveal manufacturing variations among FPGA chips. We transform these fault locations into feature vectors to create device signatures and train a multiclass classifier on a dataset from 300 unique FPGAs across four AWS geographic regions. This entirely on-chip signature extraction method achieves >99% accuracy, operates 13× faster, and costs 92% less than the state-of-the-art.

## 中文摘要

云 FPGA 凭借可扩展、灵活的特性，正迅速成为计算密集型工作负载首选的硬件加速平台。然而，其日益广泛的应用也带来了独特的安全挑战。FPGA 所提供的硬件级访问权限导致了许多漏洞，包括通过数据残留泄露敏感信息，以及在用户之间建立模拟域隐蔽信道。这些场景中的一项基础性需求是能够定位到单个 FPGA；云厂商深知这一点，因此通过限制对底层硬件低级信息的访问来阻止 FPGA 定位。除了有助于攻击者之外，FPGA 定位还能让防御者策略性地轮换 FPGA 的使用，避免因长期数据残留可能导致机密数据泄露而造成的长时间暴露。本文提出 PhasePrint，一种利用功能正确的电路中的动态时序故障实现云 FPGA 定位的方法。PhasePrint 在运行时于特制电路中诱发时序故障，并根据由此产生的错误模式推断延迟特征——且不引入被云厂商屏蔽的信息源。PhasePrint 利用 FPGA 内部的时钟合成器导出具有严格相位关系的一对时钟。通过调整这些时钟的相位关系，PhasePrint 在运行时有意造成时序故障，从而揭示 FPGA 芯片之间的制造差异。我们将这些故障位置转化为特征向量以构建设备签名，并在来自四个 AWS 地理区域的 300 个不同 FPGA 的数据集上训练多分类器。这种完全在片上完成签名提取的方法达到 >99% 的准确率，运行速度快 13×，成本比现有最先进方法低 92%。

## 英文关键词

Cloud FPGA security; FPGA localization; OnChip device fingerprinting

## 中文关键词

云 FPGA 安全；FPGA 定位；片上设备指纹

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716012)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2025](../index.md)
