---
title: "Leveraging ASIC AI Chips for Homomorphic Encryption"
description: "HPCA 2026 · Homomorphic Encryption Acceleration"
tags:
  - "HPCA2026"
  - "Homomorphic Encryption Acceleration"
---

# Leveraging ASIC AI Chips for Homomorphic Encryption

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Homomorphic Encryption Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Homomorphic Encryption Acceleration</p>
</div>

**论文链接**：[https://arxiv.org/abs/2501.07047](https://arxiv.org/abs/2501.07047)
**作者**：Jianming Tong Georgia Institute of Technology , Tianhao Huang MIT , Leo de Castro MIT , Anirudh Itagi Georgia Institute of Technology , Jingtian Dang Georgia Tech , Anupam Golder Georgia Institute of Technology , Asra Ali Google , Jevin Jiang Google , Jeremy Kun Google , Arvind Massachusetts Institute of Technology , G. Edward Suh Cornell University, USA , Tushar Krishna Georgia Institute of Technology
**会议**：HPCA 2026

---

## 中文标题

利用 ASIC AI 芯片进行同态加密

## 英文摘要

Homomorphic Encryption (HE) provides strong data privacy for cloud services but at the cost of prohibitive computational overhead. While GPUs have emerged as a practical platform for accelerating HE, there remains an order-of-magnitude energy-efficiency gap compared to specialized (but expensive) HE ASICs. This paper explores an alternate direction: leveraging existing AI accelerators, like Google’s TPUs with coarse-grained compute and memory architectures, to offer a path toward ASIC-level energy efficiency for HE. However, this architectural paradigm creates a fundamental mismatch with SoTA HE algorithms designed for GPUs. These algorithms rely heavily on: (1) high-precision (32-bit) integer arithmetic to now run on a TPU’s low-throughput vector unit, leaving its high-throughput low-precision (8-bit) matrix engine (MXU) idle, and (2) fine-grained data permutations that are inefficient on the TPU’s coarse-grained memory subsystem. Consequently, porting GPU-optimized HE libraries to TPUs results in severe resource under-utilization and performance degradation. To tackle above challenges, we introduce CROSS, a compiler framework that systematically transforms HE workloads to align with the TPU’s architecture. CROSS makes two key contributions: (1) Basis-Aligned Transformation (BAT), a novel technique that converts high-precision modular arithmetic into dense, low-precision (INT8) matrix multiplications, unlocking and improving the utilization of TPU’s MXU for HE, and (2) Memory-Aligned Transformation (MAT), which eliminates costly runtime data reordering by embedding reordering into compute kernels through offline parameter transformation. Our evaluation on a real single-host Google TPU v6e refreshes the SoTA Number Theoretic Transform (NTT) throughput record with up-to 1.43× throughput improvement over WarpDrive on a NVIDIA A100. Furthermore, CROSS achieves 451×, 7.81×, 1.83×, 1.31×, 1.86×, and 1.15× higher throughput per watt than OpenFHE, WarpDrive, FIDESlib, FAB, HEAP, and Cheddar, respectively, establishing AI ASIC as the SotA efficient platform for HE operators. Code: https://github.com/EfficientPPML/CROSS.

## 中文摘要

同态加密（HE）为云服务提供强大的数据隐私保护，但计算开销高得难以承受。GPU 已成为加速 HE 的实用平台，但与专用（且昂贵）的 HE ASIC 相比仍存在一个数量级的能效差距。本文探索另一条路线：利用现有的 AI 加速器（如具有粗粒度计算与存储架构的 Google TPU），为 HE 提供通往 ASIC 级能效的路径。然而该范式与面向 GPU 设计的 SoTA HE 算法存在根本性不匹配：这些算法严重依赖高精度（32 位）整数运算与细粒度数据重排，前者如今落在 TPU 低吞吐的向量单元上、使其高吞吐低精度（8 位）矩阵引擎（MXU）闲置，后者在 TPU 粗粒度存储子系统上效率低下。因此，将 GPU 优化的 HE 库移植到 TPU 会造成严重的资源利用不足与性能下降。为此我们提出 CROSS，一个系统性地转换 HE 负载以对齐 TPU 架构的编译器框架。其关键贡献有二：(1) 基对齐变换（BAT），将高精度模运算转换为稠密低精度（INT8）矩阵乘法，解锁并提升 TPU MXU 在 HE 中的利用率；(2) 存储对齐变换（MAT），通过离线参数变换将重排嵌入计算内核，从而消除昂贵的运行时数据重排。在真实单主机 Google TPU v6e 上的评测刷新了 SoTA 数论变换（NTT）吞吐记录，比 NVIDIA A100 上的 WarpDrive 提升多达 1.43 倍；CROSS 的每瓦吞吐分别比 OpenFHE、WarpDrive、FIDESlib、FAB、HEAP 和 Cheddar 高 451 倍、7.81 倍、1.83 倍、1.31 倍、1.86 倍和 1.15 倍，确立了 AI ASIC 作为 HE 算子的 SoTA 高效平台。代码：https://github.com/EfficientPPML/CROSS。
