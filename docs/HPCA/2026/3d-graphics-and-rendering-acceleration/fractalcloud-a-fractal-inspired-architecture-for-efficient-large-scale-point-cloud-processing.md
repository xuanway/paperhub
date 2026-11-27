---
title: "FractalCloud: A Fractal-Inspired Architecture for Efficient Large-Scale Point Cloud Processing"
description: "HPCA 2026 · 3D Graphics and Rendering Acceleration"
tags:
  - "HPCA2026"
  - "3D Graphics and Rendering Acceleration"
---

# FractalCloud: A Fractal-Inspired Architecture for Efficient Large-Scale Point Cloud Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: 3D Graphics and Rendering Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 3D Graphics and Rendering Acceleration</p>
</div>

**论文链接**：
**作者**：Yuzhe Fu Duke University , Changchun Zhou Duke University , Hancheng Ye Duke University , Bowen Duan Duke University , Qiyu Huang Yale University , Chiyue Wei Duke University , Cong Guo Duke University , Hai "Helen" Li Duke University , Yiran Chen Duke University
**会议**：HPCA 2026

---

## 中文标题

FractalCloud：一种受分形启发的高效大规模点云处理架构

## 英文摘要

Three-dimensional (3D) point clouds are increasingly used in applications such as autonomous driving, robotics, and virtual reality (VR). Point-based neural networks (PNNs) have demonstrated strong performance in point cloud analysis, originally targeting small-scale inputs. However, as PNNs evolve to process large-scale point clouds with hundreds of thousands of points, all-to-all computation and global memory access in point cloud processing introduce substantial overhead, causing O(n²) computational complexity and memory traffic where n is the number of points. Existing accelerators, primarily optimized for small-scale workloads, overlook this challenge and scale poorly due to inefficient partitioning and non-parallel architectures. To address these issues, we propose FractalCloud, a fractal-inspired hardware architecture for efficient large-scale 3D point cloud processing. FractalCloud introduces two key optimizations: (1) a co-designed Fractal method for shape-aware and hardware-friendly partitioning, and (2) block-parallel point operations that decompose and parallelize all point operations. A dedicated hardware design with on-chip fractal and flexible parallelism further enables fully parallel processing within limited memory resources. Implemented in 28 nm technology as a chip layout with a core area of 1.5 mm², FractalCloud achieves 21.7× speedup and 27× energy reduction over state-of-the-art accelerators while maintaining network accuracy, demonstrating its scalability and efficiency for PNN inference. The code for FractalCloud is available at https://github.com/Yuzhe-Fu/FractalCloud.

## 中文摘要

三维（3D）点云正越来越多地应用于自动驾驶、机器人和虚拟现实（VR）等场景。基于点的神经网络（PNN）在点云分析中表现出强大性能，其最初面向小规模输入。然而，随着 PNN 发展到需要处理包含数十万个点的大规模点云，点云处理中的全对全计算与全局内存访问带来了可观开销，导致 O(n²) 的计算复杂度与访存开销（n 为点数）。现有加速器主要面向小规模负载优化，忽视了这一挑战，并因低效的分区方式与非并行架构而难以扩展。为解决上述问题，我们提出 FractalCloud——一种受分形启发、面向高效大规模 3D 点云处理的硬件架构。FractalCloud 引入两项关键优化：(1) 协同设计的分形（Fractal）方法，实现形状感知且对硬件友好的分区；(2) 块并行的点操作，将全部点操作分解并并行化。配合片上分形与灵活并行的专用硬件设计，进一步在有限内存资源下实现完全并行处理。FractalCloud 在 28 nm 工艺下完成芯片版图实现，核心面积 1.5 mm²，相较最先进的加速器实现 21.7 倍加速与 27 倍能耗降低，同时保持网络精度，验证了其面向 PNN 推理的可扩展性与高效性。FractalCloud 的代码已开源于 https://github.com/Yuzhe-Fu/FractalCloud。
