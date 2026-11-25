---
title: "Session 2: GPU I"
description: "PPoPP 2025 Session 2（GPU I），2025 年 3 月 3 日 11:20–12:20，Acacia D，共 3 篇论文。"
tags:
  - "PPoPP2025"
  - "Session-2"
  - "GPU I"
---

# Session 2: GPU I

**PPoPP 2025 · 2025 年 3 月 3 日 11:20–12:20 · Acacia D · Session Chair：Xipeng Shen**

关注 GPU 上的通用计算与运行时优化：用光线追踪硬件加速 n-body 模拟、运行时节能的 DVFS 控制，以及高性能且容错的 FFT。

本 Session 共收录 **3** 篇论文。

**官方议程：** [PPoPP 2025 Main Conference](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

| # | 论文 | 作者 | 亮点 |
|---|------|------|------|
| 1 | [RT–BarnesHut: Accelerating Barnes–Hut Using Ray-Tracing Hardware](rt_barneshut_accelerating_barnes_hut_using_ray_tracing_hardware.md) | Vani Nagarajan 等 5 人 | 把 Barnes–Hut 树遍历重构为光线追踪，利用 RT core 加速 n-body |
| 2 | [🏆 EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs](everest_an_effective_and_versatile_runtime_energy_saving_tool_for_gpus.md) | Anna Yue 等 3 人 | 运行时自动发现 GPU 节能机会，兼顾性能保证与跨厂商可移植 |
| 3 | [TurboFFT: Co-Designed High-Performance and Fault-Tolerant Fast Fourier Transform on GPUs](turbofft_co_designed_high_performance_and_fault_tolerant_fast_fourier_transform_on_gpus.md) | Shixun Wu 等 9 人 | 架构感知 FFT 模板 + 两级 ABFT，容错开销仅 7%–15% |

### 获奖

- **EVeREST: An Effective and Versatile Runtime Energy Saving Tool for GPUs** —— Distinguished Paper Award

---

[← Session 1: Graph Neural Networks](../Session-1/index.md) · [PPoPP 2025 总览](../index.md) · [Session 3: Concurrent Data Structures and Synchronization I →](../Session-3/index.md)
