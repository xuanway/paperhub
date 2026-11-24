---
title: "AnA: An Attentive Autonomous Driving System"
description: "ASPLOS 2025 · Session 4D · AnA：一种注意力驱动的自动驾驶系统"
tags:
  - "ASPLOS2025"
  - "Session 4D"
  - "Autonomous Systems"
---

# AnA: An Attentive Autonomous Driving System

**中文标题：** AnA：一种注意力驱动的自动驾驶系统

**所属 Session：** [Session 4D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Wonkyo Choe (University of Virginia), Rongxiang Wang (University of Virginia), Felix Xiaozhu Lin (University of Virginia)

**单位：** University of Virginia

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707261) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

In an autonomous driving system (ADS), the perception module is crucial to driving safety and efficiency. Unfortunately, the perception in today's ADS remains oblivious to driving decisions, contrasting to how humans drive. Our idea is to refactor ADS so that (1) the ADS guides its perception with the driving knowledge in situ; (2) the perception differentiates between awareness and attention. We propose a system called AnA with three novel mechanisms: (1) a query interface for the planning to express its interest in perception; (2) a query executor that maps queries to an optimal set of perception tasks; (3) a monitor for handling abnormal task executions with driving knowledge. On challenging driving benchmarks, AnA outperforms competitive baselines: it responds to adversarial events timely, reducing collisions by 2x; it reduces compute usage by 44% without compromising driving safety. We attribute AnA's efficacy to its attentive driving, a human-like behavior that improves resource proportionality.

## 中文摘要

在自动驾驶系统（ADS）中，感知模块对驾驶的安全性与效率至关重要。然而，与人类驾驶的方式形成对比的是，当今 ADS 中的感知对驾驶决策依然无感知。我们的思路是重构 ADS，使得：(1) ADS 在原地利用驾驶知识来引导其感知；(2) 感知区分“觉察”与“注意”。我们提出了名为 AnA 的系统，包含三项新颖机制：(1) 一个查询接口，供规划模块表达其对感知的关注点；(2) 一个查询执行器，将查询映射到最优的感知任务集合；(3) 一个监视器，利用驾驶知识处理异常的任务执行。在具有挑战性的驾驶基准上，AnA 优于有竞争力的基线：它能及时响应对抗性事件，将碰撞减少 2 倍；它在不牺牲驾驶安全的前提下将计算开销降低 44%。我们将 AnA 的有效性归因于其注意力驱动的驾驶方式，这是一种类似人类的行为，可提升资源使用的比例相称性。

## 英文关键词

Autonomous Driving Systems; Edge computing

## 中文关键词

自动驾驶系统；边缘计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707261)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4D](index.md) · [返回 ASPLOS 2025](../index.md)
