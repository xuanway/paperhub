---
title: "From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs"
description: "ISCA 2026 · Session 4B · From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs"
tags:
  - "ISCA2026"
  - "Session 4B"
  - "Industry Track 1"
---

# From Lab to Fleet: Building and Deploying a Practical Rowhammer Defense in Cloud SoCs

**中文标题：** 从实验室到机群：在云 SoC 中构建与部署实用的 Rowhammer 防御

**所属 Session：** [Session 4B](index.md) · [ISCA 2026](../index.md)

**作者：** Stefan Saroiu, Daniel Berger, Sujay Yadalam, Isaac H. Luna, Alec Wolman, Ishwar Agarwal, Will Remaklus, Jacob R. Lorch

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Rowhammer attacks pose a significant threat to modern DRAM, with potentially serious security consequences for a cloud vendor, such as data corruption or infrastructure outages. Existing defenses fail to satisfy key industry requirements, including minimal overhead in the absence of attacks, predictable performance when under attack, system liveness, low hardware cost, adaptability to diverse hardware configurations, and tunable security guarantees. This paper introduces Sigries, a hybrid Rowhammer defense implemented by Microsoft in the Azure Cobalt 200 SoC, combining the Misra-Gries algorithm for efficient row tracking with a fallback row-sampling mode for robustness under all attack scenarios. Sigries’s design meets all our performance goals and offers configurable security guarantees allowing a cloud vendor to assess the security risks to its fleet. Our trace-driven evaluation shows that Sigries maintains minimal DRAM bandwidth overhead while keeping performance overhead consistently low. This work represents the first detailed description of a fully implemented, industry-grade Rowhammer defense and provides insights to inform research prototypes about real-world requirements.

## 中文摘要

Rowhammer 攻击对现代 DRAM 构成严重威胁，可能导致云服务商的数据损坏或基础设施中断。现有防御方案无法同时满足低开销、可预测性能、系统活性、低硬件成本、多样硬件适配性和可调安全保证等关键工业需求。本文介绍 Sigries——微软在 Azure Cobalt 200 SoC 中实现的混合 Rowhammer 防御方案，结合 Misra-Gries 算法的高效行跟踪和后备行采样模式的鲁棒性。Sigries 的设计满足所有性能目标，并提供可配置的安全保证。基于踪迹驱动的评估表明，Sigries 将 DRAM 带宽开销维持在最低水平，性能开销始终较低。这是首个关于完全实现的工业级 Rowhammer 防御的详细描述。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2026](../index.md)
