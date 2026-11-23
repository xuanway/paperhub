---
title: "Dadu-Corki: Algorithm-Architecture Co-Design for Embodied AI-powered Robotic Manipulation"
description: "ISCA 2025 · Session 3B · Dadu-Corki：面向具身智能机器人操控的算法—架构协同设计"
tags:
  - "ISCA2025"
  - "Session 3B"
  - "Domain Specific Accelerators I"
---

# Dadu-Corki: Algorithm-Architecture Co-Design for Embodied AI-powered Robotic Manipulation

**中文标题：** Dadu-Corki：面向具身智能机器人操控的算法—架构协同设计

**所属 Session：** [Session 3B](index.md) · [ISCA 2025](../index.md)

**作者：** Yiyang Huang, Yuhui Hao, Bo Yu, Feng Yan, Yuxin Yang, Feng Min, Yinhe Han, Lin Ma, Shaoshan Liu, Qiang Liu, Yiming Gan

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731099) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Embodied AI robots have the potential to fundamentally improve

the way human beings live and manufacture. Continued progress

in the burgeoning field of using large language models to control

robots depends critically on an efficient computing substrate, and

this trend is strongly evident in manipulation tasks. In particular, to-

day’s computing systems for embodied AI robots for manipulation

tasks are designed purely based on the interest of algorithm develop-

ers, where robot actions are divided into a discrete frame basis. Such

an execution pipeline creates high latency and energy consumption.

This paper proposes Corki, an algorithm-architecture co-design

framework for real-time embodied AI-powered robotic manipu-

lation applications. We aim to decouple LLM inference, robotic

control, and data communication in the embodied AI robots’ com-

pute pipeline. Instead of predicting action for one single frame,
Corki predicts the trajectory for the near future to reduce the fre-

quency of LLM inference. The algorithm is coupled with a hardware

that accelerates transforming trajectory into actual torque signals

used to control robots and an execution pipeline that parallels data

communication with computation. Corki largely reduces LLM in-

ference frequency by up to 5.1×, resulting in up to 5.9×speed up.

The success rate improvement can be up to 13.9%.

## 中文摘要

具身智能机器人有望从根本上改变人类的生活与生产方式。利用大语言模型控制机器人这一新兴方向能否持续取得进展，高度依赖高效的计算底座，这一点在操作任务中尤为突出。当前面向具身智能机器人操作任务的计算系统，完全由算法开发者的需求主导设计，机器人动作按照离散帧进行划分。这类执行流水线会带来较高的延迟与能耗。

本文提出Corki，一款面向实时具身智能机器人操作应用的算法-架构协同设计框架。我们旨在将具身智能机器人计算流水线中的LLM推理、机器人控制与数据通信三者解耦。Corki不再逐帧预测动作，而是预测未来短时间内的运动轨迹，以此降低LLM推理的调用频次。该算法配套专用硬件，加速将轨迹转换为用于控制机器人的扭矩信号；同时采用通信与计算并行的执行流水线。Corki最高可将LLM推理频次降低至原来的1/5.1，实现最高5.9倍加速，任务成功率最高提升13.9%。

## 英文关键词

Algorithm-architecture co-design, Embodied AI, Robotics, Hardware accelerator

## 中文关键词

算法-架构协同设计, 具身人工智能, 机器人学, 硬件加速器

## 代码与研究制品

- [代码仓库](https://github.com/hyy02/Corki)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731099)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 3B](index.md) · [返回 ISCA 2025](../index.md)
