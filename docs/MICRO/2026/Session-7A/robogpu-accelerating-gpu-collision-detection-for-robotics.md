---
title: "RoboGPU: Accelerating GPU Collision Detection for Robotics"
description: "MICRO 2026 · Session 7A · RoboGPU：加速机器人应用中的 GPU 碰撞检测"
tags:
  - "MICRO2026"
  - "GPU"
---

# RoboGPU: Accelerating GPU Collision Detection for Robotics

**中文标题：** RoboGPU：加速机器人应用中的 GPU 碰撞检测

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Lufei Liu, Liwei Xue, Yuan Hsi Chou, Jocelyn Zhao, Lara Kawasme, Youssef Mohammed, Tor M. Aamodt

**来源：** MICRO 2026，pp. 2357–2372；[DOI](https://doi.org/10.1109/MICRO67795.2026.00162)

## 英文摘要

Autonomous robots are anticipated to be deployed soon in domains ranging from transportation to healthcare and home assistance. Enabling autonomous robotics requires a computation platform flexible enough to execute a diverse and evolving collection of workloads while meeting real-time requirements. We believe a GPU-like architecture will be a key component of such platforms. Recent GPUs combine a flexible parallel processing fabric augmented with efficient support for important application domains via embedded accelerators (e.g., Tensor Cores), and a GPU-like architecture has reportedly been adopted for the Tesla AI5 accelerator. While current GPUs are effective at supporting emerging neural motion planners, we find that collision detection is crucial for evaluating their proposed trajectories and that this step appears to require dedicated acceleration to operate in real-time. In this work, we propose RoboCore, an accelerator block embedded within a robotics-focused GPU (RoboGPU) architecture. We explore and compare architectural modifications to address the gaps of existing ray tracing accelerators (RTAs) for robotics and find that RoboCore computes collision queries 2.8x faster than RTA implementations using 48% less energy with 2% more area than RTAs. RoboCore is 13.3x faster than a CUDA baseline, and achieves 3.4x end-to-end speedup on a neural motion planner and 1.1x speedup on Monte Carlo Localization compared to a baseline GPU. This demonstrates that a hybrid approach of embedded specialization within a flexible general-purpose GPU architecture is suitable for supporting advancements in robotics. Code available at: https://ubc-aamodt-group.github.io/robogpu/

## 中文摘要

预计自主机器人将很快部署在交通、医疗保健和家庭援助等领域。实现自主机器人技术需要一个足够灵活的计算平台，能够执行多样化且不断变化的工作负载集合，同时满足实时要求。我们相信类似 GPU 的架构将成为此类平台的关键组件。最近的 GPU 结合了灵活的并行处理结构，通过嵌入式加速器（例如 Tensor Core）增强了对重要应用领域的有效支持，据报道 Tesla AI5 加速器已采用类似 GPU 的架构。虽然当前的 GPU 可以有效地支持新兴的神经运动规划器，但我们发现碰撞检测对于评估其提出的轨迹至关重要，并且这一步似乎需要专用加速才能实时运行。在这项工作中，我们提出了 RoboCore，这是一种嵌入在以机器人为中心的 GPU (RoboGPU) 架构中的加速器块。我们探索并比较了架构修改，以解决现有机器人光线追踪加速器 (RTA) 的差距，并发现 RoboCore 计算碰撞查询的速度比 RTA 实现快 2.8 倍，且能耗比 RTA 少 48%，面积多 2%。 RoboCore 比 CUDA 基准快 13.3 倍，与基准 GPU 相比，在神经运动规划器上实现 3.4 倍的端到端加速，在蒙特卡洛定位上实现 1.1 倍的加速。这表明灵活的通用 GPU 架构中的嵌入式专业化混合方法适合支持机器人技术的进步。代码位于：https://ubc-aamodt-group.github.io/robogpu/

## 中文关键词

图形处理器；碰撞检测；机器人；运动规划

## 代码与研究制品

- 项目主页（论文标注的代码入口）：[https://ubc-aamodt-group.github.io/robogpu/](https://ubc-aamodt-group.github.io/robogpu/)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
