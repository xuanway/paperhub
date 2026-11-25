---
title: "Concord: Learning Network Configuration Contracts"
description: "EuroSys 2026 · Security · Ryan Beckett (Microsoft Research), Francis Y. Yan (University of Illinois Urbana"
tags:
  - "EuroSys2026"
  - "Security"
---

# Concord: Learning Network Configuration Contracts

**中文标题：** Concord：学习网络配置契约

**所属 Session：** [Session 6.1: Security](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security</p>
</div>

**作者**：Ryan Beckett (Microsoft Research), Francis Y. Yan (University of Illinois Urbana-Champaign), Raghunadha Reddy Pocha (Microsoft), Vineesh V. Raj (Microsoft), Ayyub Shaik (Microsoft), Siva Kesava Reddy Kakarla (Microsoft Research)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769338)

## 英文摘要

Misconfiguration is frequently cited as a leading cause of service disruptions and outages. To prevent misconfiguration, we introduce network contracts—lightweight configuration checks that run efficiently, localize errors to specific lines, and require no heavyweight modeling of network protocols. We develop a tool Concord to learn contracts automatically from example network configurations. By checking these learned contracts against new or changed configurations, Concord finds likely configuration bugs before they can impact the network. Key to our approach is a scalable algorithm for learning “relational” contracts that capture complex dependencies between configuration settings. We deployed Concord as part of a cloud-based configuration management service and evaluated its scalability, coverage, precision, and utility on two large real-world configuration datasets.

## 中文摘要

配置错误常被认为是服务中断和故障的主要原因之一。为预防配置错误，我们引入网络契约——轻量级的配置检查，它们运行高效、可将错误定位到具体代码行，且无需对网络协议进行重量级建模。我们开发了工具Concord，从示例网络配置中自动学习契约。通过将学到的契约应用于新的或变更后的配置，Concord能在配置缺陷影响网络之前发现它们。我们方法的关键是一种可扩展的算法，用于学习能够刻画配置项之间复杂依赖关系的“关系型”契约。我们将Concord作为基于云的配置管理服务的一部分进行部署，并在两个大型真实配置数据集上评估了其可扩展性、覆盖度、精确度和实用性。

**英文关键词：** Configuration validation, Misconfiguration detection, Network reliability, Association rule learning

**中文关键词：** 配置验证、配置错误检测、网络可靠性、关联规则学习

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
