---
title: "Everything You Need to Know About Virtual Machine Live Migration Between Heterogeneous Processors"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Kenta Ishiguro (Université Grenoble Alpes), Fonyuy-Asheri Caleb (INRIA), Elouan "
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Everything You Need to Know About Virtual Machine Live Migration Between Heterogeneous Processors

**中文标题：** 异构处理器间虚拟机热迁移的全面解析

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Kenta Ishiguro (Université Grenoble Alpes), Fonyuy-Asheri Caleb (INRIA), Elouan Barraud (Université Grenoble Alpes), Renaud Lachaize (Université Grenoble Alpes), Yérom-David Bromberg (University of Rennes, INRIA), Alain Tchana (Université Grenoble Alpes)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803609)

## 英文摘要

This paper focuses on the live migration of virtual machines (VMs) across semi-heterogeneous processors (SH), which share the same ISA but expose different features. Processor incompatibilities in such settings can block or break migrations, limiting resource utilization and operational flexibility. We provide the first detailed study of live migration feasibility across SH processors, yielding several findings valuable to cloud tenants, operators and hypervisor vendors. Building on these insights, we present MigCheck, a simulation tool that predicts the feasibility and outcome of VM migrations across SH processors without requiring costly real migrations. We demonstrate its accuracy and effectiveness through multiple use cases, including machine addition/removal, hypervisor updates, and VM platform adjustments.

## 中文摘要

本文关注虚拟机（VM）在半异构（semi-heterogeneous，SH）处理器之间的热迁移，这些处理器共享相同的 ISA 但暴露不同的特性。此类场景下的处理器不兼容性会阻碍或破坏迁移，从而限制资源利用率与运维灵活性。我们首次对跨 SH 处理器的热迁移可行性进行了详尽研究，得出了对云租户、运营商与虚拟机监控器厂商均有价值的若干发现。基于这些洞见，我们提出 MigCheck，一个仿真工具，可在无需进行昂贵真实迁移的情况下预测跨 SH 处理器虚拟机迁移的可行性与结果。我们通过多个用例（包括机器增减、虚拟机监控器升级以及虚拟机平台调整）证明了其准确性与有效性。

**英文关键词：** hypervisors, virtual machines, live migration, heterogeneous processors

**中文关键词：** 虚拟机监控器、虚拟机、热迁移、异构处理器

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
