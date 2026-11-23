---
title: "Fair-CO2: Fair Attribution for Cloud Carbon Emissions"
description: "ISCA 2025 · Session 4C · Fair-CO2：云碳排放的公平归因"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# Fair-CO2: Fair Attribution for Cloud Carbon Emissions

**中文标题：** Fair-CO2：云碳排放的公平归因

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Leo Han, Jash Kakadia, Benjamin C. Lee, Udit Gupta

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731023) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Fair-CO2 is a system for fairly attributing operational and embodied carbon in cloud data centers to user workloads. It leverages the Shapley value, a game theory solution for fair shared cost attribu- tion with theoretical fairness guarantees. We propose the standard Shapley value solution as a ground truth for attribution in cloud data centers, addressing two key gaps in existing carbon attribu- tion methods that lead to unfair attributions: the effect of dynamic demand on embodied carbon, and interference effects in colocated scenarios. However, the computational cost of the Shapley value solution scales exponentially with the number of workloads and becomes intractable for large systems. Fair-CO2 addresses the scal- ability challenges of the Shapley value while preserving its fairness benefits via two core components: demand-aware embodied carbon attribution and interference-aware resource cost attribution. Using Monte Carlo simulations of workload schedules and colocation sce- narios, we show that Fair-CO2 can approximate the ground truth Shapley attribution solution at scale. We also show how users, once provided a fair way of estimating their workload carbon footprint, can dynamically optimize workload deployment for carbon savings.

## 中文摘要

Fair-CO2 是一个系统，用于将云数据中心的运行碳排放与隐含碳排放公平分摊到各个用户负载。该系统采用夏普利值（Shapley value）——一种博弈论方法，用于公平分摊共享成本，具备理论上的公平性保证。本文提出将标准夏普利值方案作为云数据中心碳排放分摊的基准真值，解决现有碳排放分摊方法造成不公平的两大短板：动态需求对隐含碳排放带来的影响，以及同机部署场景下的相互干扰效应。但是夏普利值的计算开销随负载数量呈指数增长，在大规模系统中难以直接计算。Fair-CO2 通过两个核心模块，在保留夏普利值公平性优势的同时解决可扩展性难题：感知需求的隐含碳排放分摊、感知干扰的资源成本分摊。
我们基于负载调度与同机部署场景开展蒙特卡洛仿真，结果表明 Fair-CO2 能够在大规模场景下近似基准真值夏普利分摊结果。同时文章展示：当用户可以公平估算自身负载的碳足迹时，能够动态优化负载部署，实现碳排放节约。

## 英文关键词

sustainable computing, cloud computing, carbon accounting

## 中文关键词

可持续计算, 云计算, 碳核算

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15192349)
- [代码仓库](https://github.com/S4AI-CornellTech/fair-co2)
- [研究制品](https://doi.org/10.5281/zenodo.15104035)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731023)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
