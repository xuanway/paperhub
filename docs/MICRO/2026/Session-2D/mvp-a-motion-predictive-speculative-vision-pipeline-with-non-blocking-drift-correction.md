---
title: "MVP: A Motion-Predictive Speculative Vision Pipeline with Non-Blocking Drift Correction"
description: "MICRO 2026 · Session 2D · MVP：具备非阻塞漂移校正的运动预测式推测视觉流水线"
tags:
  - "MICRO2026"
---

# MVP: A Motion-Predictive Speculative Vision Pipeline with Non-Blocking Drift Correction

**中文标题：** MVP：具备非阻塞漂移校正的运动预测式推测视觉流水线

**所属 Session：** [Session 2D](index.md) · [MICRO 2026](../index.md)

**作者：** Raul Taranco, Antonio González

**来源：** MICRO 2026，pp. 834–847；[DOI](https://doi.org/10.1109/MICRO67795.2026.00069)

## 英文摘要

Continuous Vision (CV) systems underpin real-time applications such as autonomous driving and augmented reality, where latency, throughput, and energy are tightly constrained on mobile platforms. Modern CV SoC pipelines, however, still serialize image capture and processing, leading to high end-to-end latency. Prior work reduces this latency by predicting future frames and running pixel-domain backend inference speculatively, but incorrect predictions force re-execution on real frames, increasing energy and complexity. We present MVP, a motion-predictive speculative vision pipeline that operates entirely in the motion domain. Instead of forecasting full images, MVP predicts future motion vectors and uses them to extrapolate perception results from previously processed frames before the next frame arrives. A lightweight hardware extension in the Image Signal Processor (ISP) reuses existing motion-estimation logic to predict motion with minimal area and energy cost. MVP introduces a scheduling model that treats motion extrapolation as the default path, while full backend inference runs periodically in the background for drift correction off the critical path. It also supports optional frontend scaling, allowing the system to reduce sensor sampling under low or predictable motion to save energy. We evaluate MVP on object detection, demonstrating up to 66.8% reduction in tail latency and 46% energy savings, at a small accuracy cost.

## 中文摘要

连续视觉 (CV) 系统支撑自动驾驶和增强现实等实时应用，其中时延、吞吐量和能量在移动平台上受到严格限制。然而，现代 CV SoC 管道仍然串行化图像捕获和处理，从而导致较高的端到端时延。先前的工作通过预测未来帧并推测性地运行像素域后端推理来减少这种时延，但不正确的预测会迫使在真实帧上重新执行，从而增加能量和复杂性。我们提出了 MVP，一种完全在运动领域运行的运动预测推测视觉管道。 MVP 不是预测完整图像，而是预测未来的运动向量，并使用它们在下一帧到达之前从先前处理的帧推断感知结果。图像信号处理器 (ISP) 中的轻量级硬件扩展重复使用现有的运动估计逻辑，以最小的面积和能源成本预测运动。 MVP 引入了一种调度模型，该模型将运动外推视为默认路径，而完整的后端推理则在后台定期运行，以纠正偏离关键路径的偏差。它还支持可选的前端缩放，允许系统在低运动或可预测运动下减少传感器采样，以节省能源。我们在目标检测上评估了 MVP，结果表明，以较小的准确度成本，尾部时延减少了 66.8%，节能了 46%。

## 中文关键词

连续视觉；图像信号处理器；运动矢量；推测执行；移动片上系统

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 2D](index.md) · [MICRO 2026 主页](../index.md)
