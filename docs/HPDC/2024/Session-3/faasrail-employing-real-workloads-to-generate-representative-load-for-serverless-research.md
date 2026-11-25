---
title: "FaaSRail: Employing Real Workloads to Generate Representative Load for Serverless Research"
description: "HPDC 2024 · Session 3 — Serverless Computing"
tags:
  - "HPDC2024"
  - "Session 3"
  - "Serverless Computing"
---

# FaaSRail: Employing Real Workloads to Generate Representative Load for Serverless Research

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 3</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658684)

**作者**：Christos Katsakioris, Chloe Alverti, Konstantinos Nikas, Dimitrios Siakavaras, Stratos Psomadakis, Nectarios Koziris

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 3 — Serverless Computing（2024年6月6日 10:00–11:15 · Session Chair：Lixian Ma）

---

## 英文摘要

With the proliferation of Serverless Computing, the Function-as-a-Service (FaaS) paradigm is nowadays ubiquitous. As a result, the domain has attracted extensive research, both in industry and academia, identifying opportunities and addressing limitations across all aspects of this new Cloud paradigm. Recently, FaaS providers have released production workload traces of their commercial platforms. These expose important characteristics, such as the execution time of function invocations, their number and the distribution of their inter-arrival times, which must be taken into account for a concrete evaluation of innovative solutions. Nevertheless, the Serverless ecosystem still lacks a unified evaluation methodology based on such information. In this paper we attempt to fill this gap, by developing a methodology for fitting existing, real, open-source workloads found in FaaS benchmarking suites to production FaaS workload traces, in a way that sufficiently preserves the aforementioned core statistical properties of such traces. Based on this, we build FaaSRail, an open-source load generator that receives a target maximum request rate and a target total execution duration as inputs from the user and generates representative, scaled down FaaS load.

## 中文摘要

随着无服务器计算的普及，函数即服务（FaaS）范式如今无处不在。因此，该领域在工业界与学术界都吸引了大量研究，识别机会并解决这一新云范式各方面的局限。近来，FaaS 提供商发布了其商业平台的生产负载轨迹。这些轨迹揭示了重要特征，如函数调用的执行时间、调用数量及其到达间隔时间的分布，在具体评估创新方案时必须加以考虑。然而，无服务器生态仍缺乏基于此类信息的统一评估方法。本文试图填补这一空白：开发一种方法，将 FaaS 基准套件中现有的真实开源负载拟合到生产 FaaS 负载轨迹，并在足够程度上保留上述轨迹的核心统计特性。在此基础上，我们构建了 FaaSRail，一个开源负载生成器，接收用户给定的目标最大请求速率与目标总执行时长作为输入，生成具有代表性的、按比例缩减的 FaaS 负载。

## 英文关键词

Datacenter; Cloud; Serverless; FaaS; Load Generation; Benchmarking; Open Source

## 中文关键词

数据中心；云；无服务器；FaaS；负载生成；基准测试；开源

---

[← 返回 Session 3 — Serverless Computing](index.md)
