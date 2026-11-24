---
title: "Skyler: Static Analysis for Predicting API-Driven Costs in Serverless Applications"
description: "ASPLOS 2026 · Session 8B · Skyler：预测无服务器应用中 API 驱动成本的静态分析"
tags:
  - "ASPLOS2026"
  - "Session 8B"
  - "Serverless & Cloud Networking"
---

# Skyler: Static Analysis for Predicting API-Driven Costs in Serverless Applications

**中文标题：** Skyler：预测无服务器应用中 API 驱动成本的静态分析

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Bernardo Ribeiro (INESC-ID, Instituto Superior Técnico, University of Lisbon), Mafalda Ferreira (INESC-ID, Instituto Superior Técnico, University of Lisbon), José Fragoso Santos (INESC-ID, Instituto Superior Técnico, University of Lisbon), Rodrigo Bruno (INESC-ID, Instituto Superior Técnico, University of Lisbon), Nuno Santos (INESC-ID, Instituto Superior Técnico, University of Lisbon)

**单位：** INESC-ID, Instituto Superior Técnico, University of Lisbon

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790221) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Unpredictable costs are a growing concern in serverless computing, where applications rely on cloud APIs with complex tiered pricing models. In many deployments, API calls dominate expenses, and a single overlooked design choice can escalate costs by thousands of dollars. Existing tools fall short: provider calculators need unrealistic manual estimates, and dynamic profilers only work post-deployment. We present Skyler, a static analysis framework for predeployment cost estimation of API invocations in serverless workflows. Skyler models control flow behavior and pricing semantics to construct symbolic cost expressions using SMT formulas, exposing economic sinks, i.e., code paths where API usage disproportionately impacts cost. This enables developers to identify hotspots and prevent costly architectural errors early. Skyler supports JavaScript-based serverless applications across AWS Lambda, Google Cloud Functions, and Azure Functions, achieving high accuracy (mean absolute percentage error <1% for AWS and Google, 4.5% for Azure).

## 中文摘要

不可预测的成本是无服务器计算中日益受到关注的问题，因为应用依赖具有复杂分级定价模型的云 API。在许多部署中，API 调用主导了开支，而一个被忽视的设计选择就可能使成本增加数千美元。现有工具力有未逮：云厂商的计算器需要不切实际的人工估算，而动态 profiler 只能在部署之后才起作用。我们提出 Skyler，一个用于在部署前估算无服务器工作流中 API 调用成本的静态分析框架。Skyler 对控制流行为与定价语义建模，使用 SMT 公式构造符号化成本表达式，从而揭示经济汇点，即 API 使用对成本影响不成比例的代码路径。这使开发者能够识别热点，并在早期防止代价高昂的架构错误。Skyler 支持基于 JavaScript 的无服务器应用，覆盖 AWS Lambda、Google Cloud Functions 与 Azure Functions，并达到很高精度（AWS 与 Google 的平均绝对百分比误差小于 1%，Azure 为 4.5%）。

## 英文关键词

Static Analysis, Serverless Computing

## 中文关键词

静态分析；无服务器计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790221)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2026](../index.md)
