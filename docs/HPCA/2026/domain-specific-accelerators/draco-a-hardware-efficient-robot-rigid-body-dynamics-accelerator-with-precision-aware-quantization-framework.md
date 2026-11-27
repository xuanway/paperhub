---
title: "DRACO: A Hardware-Efficient Robot Rigid Body Dynamics Accelerator with Precision-Aware Quantization Framework"
description: "HPCA 2026 · Domain Specific Accelerators"
tags:
  - "HPCA2026"
  - "Domain Specific Accelerators"
---

# DRACO: A Hardware-Efficient Robot Rigid Body Dynamics Accelerator with Precision-Aware Quantization Framework

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Domain Specific Accelerators。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Domain Specific Accelerators</p>
</div>

**论文链接**：
**作者**：Xingyu Liu The Hong Kong University of Science and Technology , Jiawei Liang The Hong Kong University of Science and Technology , Yipu Zhang The Hong Kong University of Science and Technology , Linfeng Du The Hong Kong University of Science and Technology , Chaofang Ma The Hong Kong University of Science and Technology , Hui Yu Hong Kong University of Science and Technology , Xu Jiang University of Electronic Science and Technology of China , Wei Zhang The Hong Kong University of Science and Technology
**会议**：HPCA 2026

---

## 中文标题

DRACO：带精度感知量化框架的硬件高效机器人刚体动力学加速器

## 英文摘要

Rigid Body Dynamics (RBD) computation is a critical component of robotic control, often dominating system runtime due to its algorithmic complexity and high parallelism demands. CPUs suffer from limited parallelism and cache-unfriendly access patterns, while GPUs incur prohibitive memory-access latency and per-task response time, making them unsuitable for real-time control. Both platforms also consume excessive power for edge deployment. FPGAs offer superior latency, energy efficiency, and customizable hardware-level parallelism, emerging as promising targets for RBD acceleration. However, existing FPGA designs still face critical limitations. First, the intensive use of multiply-accumulate operations leads to high Digital Signal Processing (DSP) slices consumption— especially for high degrees-of-freedom (DOF) robots—resulting in limited scalability. Second, RBD functions include mass matrix inversion function, which is inefficient on FPGA due to reciprocal operations falling on the longest latency path, severely limiting performance. Third, mismatched processing rates across modules introduce idle cycles, resulting in poor DSP utilization. To address these issues, we propose DRACO, a hardware-efficient and high-performance RBD accelerator based on FPGA, introducing three key innovations. First, we propose a precision-aware quantization framework that reduces DSP demand by up to 4× while preserving motion accuracy. This is also the first study to systematically evaluate quantization impact on robot control and motion for hardware acceleration. Second, we leverage a hardware-efficient division deferring optimization in mass matrix inversion algorithm, which decouples reciprocal operations from the longest latency path to improve the performance. Finally, we present an inter-module DSP reuse methodology to improve DSP utilization and save DSP usage. Experiment results show that DRACO achieves up to 8× throughput improvement and 7.4× latency reduction over state-of-the-art (SOTA) RBD accelerators across various robot types, demonstrating its effectiveness and scalability for high-DOF robotic systems.

## 中文摘要

刚体动力学（RBD）计算是机器人控制的关键组成部分，其算法复杂性与高并行度需求常使其主导系统运行时间。CPU 并行度有限且访存对缓存不友好，GPU 则存在难以承受的访存时延与单任务响应时间，二者均不适合实时控制，且为边缘部署消耗过多功耗。FPGA 具有更优的时延、能效与可定制硬件级并行性，成为 RBD 加速的有前景目标。然而现有 FPGA 设计仍有关键限制：乘加运算的大量使用使 DSP 切片消耗高，高自由度（DOF）机器人尤甚，可扩展性受限；质量矩阵求逆的倒数运算落在最长时延路径上，效率低下；各模块处理速率不匹配引入空闲周期，DSP 利用率低。为此我们提出 DRACO，一种基于 FPGA 的硬件高效高性能 RBD 加速器。它提出精度感知量化框架，在保持运动精度的同时将 DSP 需求降低至多 4 倍，这也是首个系统评估量化对机器人控制与运动影响的研究；在质量矩阵求逆中采用硬件高效的延迟除法优化，把倒数运算从最长时延路径解耦；并提出模块间 DSP 复用方法以提高利用率。实验表明，DRACO 在多种机器人类型上相比最先进的 RBD 加速器取得最高 8 倍吞吐提升与 7.4 倍时延降低。
