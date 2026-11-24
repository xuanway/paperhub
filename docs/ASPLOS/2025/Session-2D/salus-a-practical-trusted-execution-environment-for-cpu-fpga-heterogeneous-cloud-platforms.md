---
title: "Salus: A Practical Trusted Execution Environment for CPU-FPGA Heterogeneous Cloud Platforms"
description: "ASPLOS 2025 · Session 2D · Salus：面向 CPU-FPGA 异构云平台的实用可信执行环境"
tags:
  - "ASPLOS2025"
  - "Session 2D"
  - "FPGAs"
---

# Salus: A Practical Trusted Execution Environment for CPU-FPGA Heterogeneous Cloud Platforms

**中文标题：** Salus：面向 CPU-FPGA 异构云平台的实用可信执行环境

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yu Zou (Alibaba Group), Yiran Li (Alibaba Group), Sheng Wang (Alibaba Group), Le Su (Alibaba Group), Zhen Gu (DAMO Academy, Alibaba Group,Hupan Lab), Yanheng Lu (DAMO Academy, Alibaba Group,Hupan Lab), Yijin Guan (DAMO Academy, Alibaba Group,Hupan Lab), Dimin Niu (DAMO Academy, Alibaba Group,Hupan Lab), Mingyu Gao (Tsinghua University,Shanghai AI Laboratory), Yuan Xie (DAMO Academy, Alibaba Group,Hupan Lab), Feifei Li (Alibaba Group)

**单位：** Alibaba Group；DAMO Academy, Alibaba Group,Hupan Lab；Tsinghua University,Shanghai AI Laboratory

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674169) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

CPU-FPGA heterogeneous architectures have become increasingly popular in cloud environments for accelerating compute-intensive tasks. Ensuring the protection of sensitive data processed by these architectures requires the presence of a trusted execution environment (TEE). This work highlights the requirements for designing an FPGA TEE, the challenges faced in deploying existing solutions on commercial-off-theshelf (COTS) cloud FPGA services, and the limitations of previous works that primarily focus on standalone FPGA TEEs. In response to these challenges, Salus introduces an innovative approach by leveraging an enclave running on the host with a TEE-enabled CPU. This approach aims to protect and attest the bitstream loaded on the FPGA side. By repurposing COTS FPGA bitstream utilities in a novel manner and adopting a proposed security-enhanced FPGA IP, Salus presents a practical design for an FPGA TEE, with minor efforts required.

## 中文摘要

CPU-FPGA 异构架构在云环境中用于加速计算密集型任务已日益流行。要确保这类架构所处理的敏感数据得到保护，就需要具备可信执行环境（TEE）。本工作阐释了设计 FPGA TEE 的需求、在商用现货（COTS）云 FPGA 服务上部署现有方案所面临的挑战，以及此前主要聚焦于独立 FPGA TEE 的工作的局限性。为应对这些挑战，Salus 提出一种创新方法，利用运行在具备 TEE 能力的 CPU 主机上的 enclave。该方法旨在保护并认证（attest）加载到 FPGA 一侧的比特流。通过以新颖的方式改造 COTS FPGA 比特流工具，并采用所提出的安全增强 FPGA IP，Salus 以较小的投入给出了 FPGA TEE 的实用设计。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674169)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2025](../index.md)
