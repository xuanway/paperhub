---
title: "Seal: Towards Diverse Specification Inference for Linux Interfaces from Security Patches"
description: "EuroSys 2025 · Security and Privacy · Wei Chen (The Hong Kong University of Science and Technology), Bowen Zhang (The "
tags:
  - "EuroSys2025"
  - "Security and Privacy"
---

# Seal: Towards Diverse Specification Inference for Linux Interfaces from Security Patches

**中文标题：** 从安全补丁推断多样化的 Linux 接口规约

**所属 Session：** [Session 9.1: Security and Privacy](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Security and Privacy。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Security and Privacy</p>
</div>

**作者**：Wei Chen (The Hong Kong University of Science and Technology), Bowen Zhang (The Hong Kong University of Science and Technology), Chengpeng Wang (HKUST), Wensheng Tang (The Hong Kong University of Science and Technology), Charles Zhang (HKUST)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717487)

## 英文摘要

Linux utilizes interfaces as communication protocols across different subsystems while ensuring manageability. These interfaces standardize interactions between various subsystems; however, the absence of complete calling contexts can result in the mishandling of data from other entities, i.e., interaction data, thus incurring vulnerabilities. Even worse, the effectiveness of static bug detectors could be severely hindered due to the lack of interface specifications. Previous solutions, seeking to automate the inference of interface specifications, are tailored to a subset of the interaction data behavior and, hence are deficient in generalizability.

This research presents Seal, a framework that leverages security patches to achieve the automatic inference of diverse interface specifications. Those specifications, formulated as value-flow properties, could adeptly characterize interaction data behaviors for individual interfaces and the synergistic relationships among multiple interfaces. Technically, Seal assesses the impact of code changes in program dependencies, abstracts specifications from changed value-flow paths, and detects bugs via reachability analysis. Experiments show Seal attains a precision of 71.9% and the specifications could accommodate various bug types. We utilized Seal to identify 167 unseen bugs in Linux, hidden for an average of 7.7 years. So far, 95 of them are confirmed by Linux maintainers, 56 of which fixed by our patches.

## 中文摘要

Linux 使用接口作为不同子系统之间的通信协议，同时保证可管理性。这些接口规范了各子系统之间的交互；然而，调用上下文的缺失可能导致对其他实体的数据（即交互数据）处理不当，从而引入漏洞。更糟的是，由于缺乏接口规范，静态缺陷检测器的有效性可能受到严重制约。以往试图自动推断接口规范的方案仅针对交互数据行为的一个子集，因而泛化能力不足。

本研究提出 Seal，一个利用安全补丁实现多样化接口规范自动推断的框架。这些规范以值流属性形式表述，能够很好地刻画单个接口的交互数据行为以及多个接口之间的协同关系。在技术上，Seal 评估代码变更对程序依赖的影响，从变更的值流路径中抽象出规范，并通过可达性分析检测缺陷。实验表明，Seal 达到 71.9% 的精确率，且这些规范可适配多种缺陷类型。我们利用 Seal 在 Linux 中识别出 167 个未发现的缺陷，这些缺陷平均隐藏了 7.7 年。目前已确认其中 95 个，其中 56 个由我们提供的补丁修复。

**英文关键词：** Linux, Specification Inference, Patch Analysis, Static Bug Detection

**中文关键词：** Linux、规范推断、补丁分析、静态缺陷检测

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
