---
title: "Hardware Sentinel: Protecting Software Applications from Hardware Silent Data Corruptions"
description: "ASPLOS 2025 · Session 9C · Hardware Sentinel：保护软件应用免受硬件静默数据损坏"
tags:
  - "ASPLOS2025"
  - "Session 9C"
  - "Verification & Reliability"
---

# Hardware Sentinel: Protecting Software Applications from Hardware Silent Data Corruptions

**中文标题：** Hardware Sentinel：保护软件应用免受硬件静默数据损坏

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Rhea Dutta (Meta Platforms, Inc.), Harish Dattatraya Dixit (Meta Platforms, Inc.), Rik Van Riel (Meta Platforms, Inc.), Gautham Vunnam (Meta Platforms, Inc.), Sriram Sankar (Meta Platforms, Inc.)

**单位：** Meta Platforms, Inc.

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716258) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Silent Data Corruptions (SDCs) pose a significant challenge in large-scale infrastructures, affecting data center applications unpredictably and reducing service reliability. Primarily caused by silicon defects, traditional hardware testing methods are insufficient to prevent SDC propagation. SDCs are influenced by various factors, including data randomization, workload characteristics, environmental conditions, and aging, necessitating top-down approaches from the application layer. In this paper, we introduce Hardware Sentinel, a novel framework that detects SDCs through typical software failure indicators such as segmentation faults, core dumps, application crashes, and logs. We have validated our framework in a large-scale data center fleet, across diverse application, kernel, and hardware configurations, achieving a high success rate of SDC detection. Hardware Sentinel has uncovered novel instances of SDCs, surpassing the detection capabilities of published testing techniques. Our analysis of over 6 years' worth of application and system failure data within a large-scale infrastructure has successfully identified hundreds of defective CPUs that triggered SDCs. Notably, the Hardware Sentinel flow increases effective coverage over existing hardware-testing methods like Fleetscanner (outof-production testing) by 1.74x and Ripple (in-production testing) by 1.92x. We share the top kernel exceptions with the highest correlation to silent data corruption failures. We present results spanning 7 CPU generations from multiple semiconductor manufacturers, 13 large-scale workloads, and 27 data center regions, providing insights into the trade-offs involved in detection and fleet deployment.

## 中文摘要

静默数据损坏（SDC）在超大规模基础设施中构成重大挑战，会不可预测地影响数据中心应用并降低服务可靠性。SDC 主要由硅缺陷引起，传统硬件测试方法不足以阻止 SDC 的传播。SDC 受数据随机化、工作负载特征、环境条件与老化等多种因素影响，因此需要从应用层自顶向下的方法。本文提出 Hardware Sentinel，一个新框架，它通过段错误、核心转储、应用崩溃与日志等典型软件故障指示来检测 SDC。我们在一个大规模数据中心集群中、跨多种应用、内核与硬件配置对该框架进行了验证，取得了很高的 SDC 检测成功率。Hardware Sentinel 发现了 SDC 的新实例，超越了已发表的测试技术的检测能力。我们对某超大规模基础设施中超过 6 年的应用与系统故障数据进行分析，成功识别出数百颗触发 SDC 的缺陷 CPU。值得注意的是，Hardware Sentinel 流程相比 Fleetscanner（生产外测试）等现有硬件测试方法将有效覆盖提升 1.74 倍，相比 Ripple（生产内测试）提升 1.92 倍。我们分享了与静默数据损坏故障相关性最高的内核异常。我们给出了覆盖来自多家半导体制造商的 7 代 CPU、13 种大规模工作负载与 27 个数据中心区域的结果，为检测与集群部署中的权衡提供了洞见。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716258)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2025](../index.md)
