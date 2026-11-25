---
title: "Matrix‑PIC: Harnessing Matrix Outer-product for High‑Performance Particle‑in‑Cell Simulations"
description: "EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing · Yizhuo Rao (Sun Yat-sen University), Xingjian Cui (Sun Yat-sen University), Jiab"
tags:
  - "EuroSys2026"
  - "Architecture, Accelerators & Heterogeneous Computing"
---

# Matrix‑PIC: Harnessing Matrix Outer-product for High‑Performance Particle‑in‑Cell Simulations

**中文标题：** Matrix-PIC：利用矩阵外积实现高性能粒子网格模拟

**所属 Session：** [Session 8.3: Architecture, Accelerators & Heterogeneous Computing](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Architecture, Accelerators & Heterogeneous Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Architecture, Accelerators & Heterogeneous Computing</p>
</div>

**作者**：Yizhuo Rao (Sun Yat-sen University), Xingjian Cui (Sun Yat-sen University), Jiabin Xie (Sun Yat-sen University), Shangzhi Pang (Sun Yat-sen University), Guangnan Feng (Sun Yat-sen University), Jinhui Wei (Sun Yat-sen University), Zhiguang Chen (Sun Yat-sen University), Yutong Lu (Sun Yat-sen University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769378)

## 英文摘要

Particle-in-Cell (PIC) simulations devote most cycles to particle-grid interactions, and their fine-grained atomic updates become a severe bottleneck on traditional many-core CPUs. The evolution of CPU architectures, particularly the integration of specialized Matrix Processing Units (MPUs) designed for efficient matrix outer-product operations, presents a paradigm shift and an opportunity to alleviate these bottlenecks. Capitalizing on this architectural advancement, this work focuses on adapting the critical current deposition step in PIC simulations to this new matrix-centric computational model.

We introduce MatrixPIC, a novel framework representing, to our knowledge, the first holistic co-design of the deposition kernel, data layout, and an incremental sorting mechanism, all tailored specifically for the hybrid MPU-VPU SIMD execution model on modern CPUs. It provides a validated design paradigm for the scientific computing community to leverage the next generation of high-density hardware. The key technical innovations are: (i) the refactoring of the current deposition algorithm into block-matrix updates that map efficiently onto the MPU’s native operational paradigm; (ii) a hybrid execution pipeline that synergistically orchestrates MPU kernels for high-density accumulation with VPU stages for data preparation and control flow; and (iii) an 𝑂(1)-amortized incremental particle sorter, which utilizes a gapped packed-memory array to establish and maintain the crucial data locality required for MPU efficiency.

Evaluated on a next-generation high-performance computing platform, MatrixPIC demonstrates substantial performance improvements. In complex Laser-Wakefield Acceleration (LWFA) simulations, it yields up to a 2.63× speedup in total simulation time. Most significantly, for a higher-order, third-order deposition scheme, MatrixPIC accelerates the core deposition kernel by 8.7× over the original baseline and is 2.0× faster than our best hand-tuned VPU implementation. Furthermore, our CPU-based framework reaches 83.08% of theoretical peak performance, a hardware utilization rate nearly 2.8× higher than a highly-optimized CUDA kernel on a data center GPU. These results underscore the transformative potential of co-designing scientific algorithms for emerging, matrix-capable CPU architectures, paving the way for enhanced performance in large-scale computations.

## 中文摘要

粒子网格（Particle-in-Cell，PIC）模拟将大部分周期花费在粒子—网格交互上，其细粒度原子更新在传统众核 CPU 上成为严重瓶颈。CPU 架构的演进，特别是为高效矩阵外积运算而设计的专用矩阵处理单元（MPU）的集成，带来了范式转变，也为缓解这些瓶颈提供了机遇。借助这一架构进步，本文聚焦于将 PIC 模拟中关键的电流沉积步骤适配到这种以矩阵为中心的新计算模型上。

我们提出 MatrixPIC，这是一个新颖的框架；据我们所知，它首次针对现代 CPU 上的 MPU–VPU 混合 SIMD 执行模型，对沉积内核、数据布局以及增量排序机制进行了整体协同设计。它为科学计算界利用下一代高密度硬件提供了一个经过验证的设计范式。关键技术创见包括：（i）将电流沉积算法重构为块矩阵更新，使其高效映射到 MPU 的原生运算范式；（ii）一条混合执行流水线，协同编排用于高密度累积的 MPU 内核与用于数据准备和控制流的 VPU 阶段；（iii）一个具有 𝑂(1) 摊销复杂度的增量粒子排序器，它利用带空隙的紧凑内存数组来建立并维持 MPU 高效运行所必需的数据局部性。

在下一代高性能计算平台上评估表明，MatrixPIC 取得了显著的性能提升。在复杂的激光尾波场加速（LWFA）模拟中，它将总模拟时间最多加速 2.63 倍。最重要的是，对于更高阶的三阶沉积方案，MatrixPIC 相比原始基线将核心沉积内核加速 8.7 倍，并比我们最佳的手工调优 VPU 实现快 2.0 倍。此外，我们基于 CPU 的框架达到理论峰值性能的 83.08%，这一硬件利用率为数据中心 GPU 上高度优化 CUDA 内核的近 2.8 倍。这些结果凸显了为新兴的、具备矩阵能力的 CPU 架构协同设计科学算法的变革潜力，为大规模计算性能的提升铺平了道路。

**英文关键词：** Particle-in-Cell simulation, High-Performance Computing, Scientific Computing, Hardware Acceleration

**中文关键词：** Particle-in-Cell 模拟、高性能计算、科学计算、硬件加速

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
