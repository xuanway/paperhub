---
title: "SnakeCharmer: Orchestrating Utility, Timeliness, and Placement in GPU Prefetching"
description: "MICRO 2026 · Session 1A · SnakeCharmer：统筹 GPU 预取的效用、及时性与数据放置"
tags:
  - "MICRO2026"
  - "GPU"
  - "Prefetching"
  - "Register File"
---

# SnakeCharmer: Orchestrating Utility, Timeliness, and Placement in GPU Prefetching

**中文标题：** SnakeCharmer：统筹 GPU 预取的效用、及时性与数据放置

**所属 Session：** [Session 1A](index.md) · [MICRO 2026](../index.md)

**作者：** Yuhan Tang, Tiejun Li, Jianmin Zhang, An Hu, Guangyu Sun, Sheng Ma, Yiqun Lang, Hanqing Li, Siqing Fu

**来源：** MICRO 2026，pp. 97–111；[DOI](https://doi.org/10.1109/MICRO67795.2026.00023)

## 英文摘要

GPUs rely on massive thread-level parallelism to tolerate long memory latency, yet they still suffer severe stalls when many warps simultaneously wait for data from the memory system. Address-prediction-based GPU prefetchers can mitigate such stalls, but accurate prediction alone does not guarantee performance improvement: a predicted prefetch becomes beneficial only if it is worth issuing, arrives at the right time, and is retained without harmful interference. Because these requirements interact, optimizing any single dimension in isolation can simply move the bottleneck to another. We capture these requirements with a predicted-prefetch-to-realized-benefit perspective and propose SnakeCharmer, a unified backend prefetch-control framework for address-prediction-based GPU prefetchers. SnakeCharmer separates address prediction from prefetch realization: the frontend predictor generates prefetch candidates, while the backend control path jointly controls utility, timeliness, and placement by determining whether each candidate should be issued, when it should be issued, and where the returned data should be retained. SnakeCharmer realizes this control path with zero-value-aware filtering for utility, hierarchical feedback-driven distance tuning for timeliness, and a register-assisted prefetch buffer for placement. We design and implement SnakeCharmer primarily on top of Snake, and adapt the same backend-control principles to APOGEE to demonstrate that SnakeCharmer's benefits are not limited to a single frontend predictor. On an A100 GPU model, SnakeCharmer improves performance energy efficiency by 12.8%/20.8% over Snake and by 1.7%/3.2% over APOGEE, with modest hardware overhead.

## 中文摘要

GPU 依靠大规模线程级并行隐藏较长的内存访问时延，但当多个线程束同时等待内存系统中的数据时，仍会发生严重停顿。基于地址预测的 GPU 预取器可以缓解此类停顿，不过，预测准确并不必然带来性能提升：只有当一次预取值得发出、能够及时到达，且返回数据的保留不会引发有害干扰时，预测才会转化为收益。这些要求彼此影响，孤立优化其中任一维度，可能只是将瓶颈转移到其他维度。我们从“预测预取如何转化为实际收益”的角度刻画这些要求，提出 SnakeCharmer，一种面向地址预测型 GPU 预取器的统一后端预取控制框架。SnakeCharmer 将地址预测与预取实现分离：前端预测器生成预取候选，后端控制路径决定候选是否发出、何时发出，以及返回数据保留在哪里，从而联合控制效用、及时性与放置。其实现包括用于效用控制的零值感知过滤、用于及时性控制的分层反馈驱动预取距离调节，以及用于放置控制的寄存器辅助预取缓冲区。我们主要基于 Snake 设计并实现 SnakeCharmer，同时将相同的后端控制原则移植到 APOGEE，表明收益并不依赖单一前端预测器。在 A100 GPU 模型上，相比 Snake，SnakeCharmer 的性能和能效分别提高 12.8% 与 20.8%；相比 APOGEE，则分别提高 1.7% 与 3.2%，硬件开销较小。

## 中文关键词

图形处理器；预取；寄存器文件；一级缓存；预取及时性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 1A](index.md) · [MICRO 2026 主页](../index.md)
