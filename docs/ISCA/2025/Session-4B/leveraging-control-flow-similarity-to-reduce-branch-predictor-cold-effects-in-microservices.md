---
title: "Leveraging Control-flow Similarity to Reduce Branch Predictor Cold Effects in Microservices"
description: "ISCA 2025 · Session 4B · 利用控制流相似性降低微服务中的分支预测器冷启动效应"
tags:
  - "ISCA2025"
  - "Session 4B"
  - "Microarchitecture I"
---

# Leveraging Control-flow Similarity to Reduce Branch Predictor Cold Effects in Microservices

**中文标题：** 利用控制流相似性降低微服务中的分支预测器冷启动效应

**所属 Session：** [Session 4B](index.md) · [ISCA 2025](../index.md)

**作者：** Haris Volos, Stylianos Vassiliou, Georgia Antoniou, Davide Basilio Bartolini, Yiannakis Sazeides

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731059) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Modern datacenter applications commonly adopt a microservice software architecture, where an application is decomposed into smaller interconnected microservices communicating via the net- work. These microservices often operate under strict latency re- quirements, rendering them particularly vulnerable to microarchi- tectural cold effects that may arise from the interleaved execution of services on cores or power-gating cores between invocations. Previous analyses of microservices find branch mispredictions due to cold predictor resources to be a significant contributor to performance degradation, indicating that the dynamic control flow must be very similar in the set and order of executed instructions across different requests. Our analysis of control-flow similarity across requests, using static and dynamic control flow information to determine dynamic control flow reconvergence, confirms that, indeed, a large portion of requests follow similar paths. Motivated by the above findings, we propose Similarity-based Branch Prediction (SBP), a hybrid predictor architecture that en- hances conventional predictors with a similarity component. SBP leverages the control-flow similarity across microservice requests to predict control flow (branch direction and target) by utilizing the control flow of past executions encoded in a reference execution trace. We realize a specific instantiation of SBP, called CHESS, which combines a conventional history-based fetch predictor, a static-hint predictor, and a similarity predictor. CHESS judiciously applies sim- ilarity prediction for branches identified as hard-to-predict through conventional prediction techniques, effectively mitigating branch predictor cold-start effects while keeping the length of the refer- ence trace practical. Evaluation through a suite of microservices shows that CHESS reduces branch MPKI by 94% over a cold fetch predictor and 78% over a state-of-the-art predictor, while requiring a modest 18.1KB of additional storage space. This enables CHESS to deliver performance that is, on average, within 95% of a warm baseline system.

## 中文摘要

现代数据中心应用普遍采用微服务软件架构：一个应用被拆分为多个小型互联微服务，服务之间通过网络通信。这类微服务通常有严格的延迟约束，因此很容易受到微架构冷启动效应的影响——该效应源于多个服务在核心上交替执行，或是调用间隙核心被断电。以往针对微服务的研究发现，预测器资源冷态导致的分支预测失败是性能下降的重要原因，这说明不同请求执行的指令集合与顺序对应的动态控制流具备很高相似度。我们结合静态与动态控制流信息判断控制流重新汇聚，对请求间控制流相似度开展分析，证实大量请求确实遵循相近的执行路径。

基于上述结论，本文提出基于相似度的分支预测（SBP），一种混合预测器架构，在传统预测器基础上增加相似度模块。SBP利用微服务请求之间的控制流相似度，借助参考执行轨迹中记录的历史执行信息预测控制流（分支走向与目标地址）。本文给出SBP的具体实现CHESS，融合传统基于历史的取指预测器、静态提示预测器以及相似度预测器。CHESS只对传统预测方案难以预测的分支启用相似度预测，在控制参考轨迹长度的同时，有效缓解分支预测器的冷启动问题。

在一组微服务负载上的评测表明：相比冷态取指预测器，CHESS将分支MPKI降低94%；对比前沿预测器降低78%，额外存储开销仅18.1KB。CHESS的平均性能可以达到热态基线系统的95%。

## 英文关键词

Microservices, branch prediction, cold start

## 中文关键词

微服务, 分支预测, 冷启动

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731059)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2025](../index.md)
