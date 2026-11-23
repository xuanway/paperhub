---
title: "SWIPER: Minimizing Fault-Tolerant Quantum Program Latency via Speculative Window Decoding"
description: "ISCA 2025 · Session 7C · SWIPER: 通过推测窗口解码最小化容错量子程序延迟"
tags:
  - "ISCA2025"
  - "Session 7C"
  - "Quantum II"
---

# SWIPER: Minimizing Fault-Tolerant Quantum Program Latency via Speculative Window Decoding

**中文标题：** SWIPER: 通过推测窗口解码最小化容错量子程序延迟

**所属 Session：** [Session 7C](index.md) · [ISCA 2025](../index.md)

**作者：** Joshua Viszlai, Jason Chadwick, Sarang Joshi, Gokul Ravi, Yanjing Li, Fred Chong

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731022) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Real-time decoding is a key ingredient in future fault-tolerant quan- tum systems, yet many decoders are too slow to run in real time. Prior work has shown that parallel window decoding can scal- ably meet throughput requirements in the presence of increasing decoding times. However, windowed decoding require that some decoding tasks be delayed until others have completed, which can be problematic during time-sensitive operations such as T gate teleportation, leading to suboptimal program runtimes. To alleviate this, we introduce SWIPER, a speculative window decoder. Taking inspiration from branch prediction in classical computer architec- ture, SWIPER utilizes a light-weight speculation step to predict data dependencies between adjacent decoding windows, allowing multi- ple layers of decoding tasks to be resolved simultaneously. Through a state-of-the-art compilation pipeline and a detailed open-source simulator, we find that SWIPER reduces application runtimes by 40% on average compared to prior parallel window decoders.

## 中文摘要

实时解码是未来容错量子系统的核心组成部分，但很多解码器速度过慢，无法满足实时运行要求。已有研究表明，并行窗口解码具备可扩展性，能够在解码耗时不断增长的情况下满足吞吐需求。然而窗口解码需要部分解码任务等待其他任务完成后才能执行，在T门隐形传态这类对时序敏感的操作中会产生瓶颈，造成程序运行时间不理想。
针对该问题，本文提出SWIPER，一种推测式窗口解码器。该方案借鉴经典计算机体系结构中的分支预测思想，通过轻量推测步骤预测相邻解码窗口之间的数据依赖，从而可以同时求解多层解码任务。依托前沿编译流水线与开源精细仿真器，实验结果表明：对比现有并行窗口解码器，SWIPER可将应用运行时间平均缩短40%。

## 英文关键词

Quantum Computing, Quantum Error Correction, Surface Code, Decoding, Window Decoding, Lattice Surgery

## 中文关键词

量子计算, 量子纠错, 表面码, 解码, 窗口解码, 晶格手术

## 代码与研究制品

- [代码仓库](https://github.com/jviszlai/swiper)
- [研究制品](https://zenodo.org/records/15338731)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731022)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7C](index.md) · [返回 ISCA 2025](../index.md)
