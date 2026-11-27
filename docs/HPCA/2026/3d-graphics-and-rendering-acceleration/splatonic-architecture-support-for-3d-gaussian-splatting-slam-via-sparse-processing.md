---
title: "Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing"
description: "HPCA 2026 · 3D Graphics and Rendering Acceleration"
tags:
  - "HPCA2026"
  - "3D Graphics and Rendering Acceleration"
---

# Splatonic: Architecture Support for 3D Gaussian Splatting SLAM via Sparse Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: 3D Graphics and Rendering Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · 3D Graphics and Rendering Acceleration</p>
</div>

**论文链接**：
**作者**：Xiaotong Huang Shanghai Jiao Tong University , He Zhu Shanghai Jiao Tong University , Tianrui Ma Institute of Computing Technology, Chinese Academy of Sciences , Yuxiang Xiong Shanghai Jiao Tong University , Fangxin Liu Shanghai Jiao Tong University , Zhezhi He Shanghai Jiao Tong University , Yiming Gan Institute of Computing Technology, Chinese Academy of Sciences , Zihan Liu Shanghai Jiao Tong University , Jingwen Leng Shanghai Jiao Tong University , Yu Feng Shanghai Jiao Tong University , Minyi Guo Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

Splatonic：通过稀疏处理为 3D 高斯泼溅 SLAM 提供架构支持

## 英文摘要

3D Gaussian splatting (3DGS) has emerged as a promising direction for SLAM due to its high-fidelity reconstruction and rapid convergence. However, 3DGS-SLAM algorithms remain impractical for mobile platforms due to their high computational cost, especially for their tracking process. This work introduces SPLATONIC, a sparse and efficient real-time 3DGS-SLAM algorithm-hardware co-design for resource-constrained devices. Inspired by classical SLAMs, we propose an adaptive sparse pixel sampling algorithm that reduces the number of rendered pixels by up to 256× while retaining accuracy. To unlock this performance potential on mobile GPUs, we design a novel pixel-based rendering pipeline that improves hardware utilization via Gaussian-parallel rendering and preemptive α-checking. Together, these optimizations yield up to 121.7× speedup on the bottleneck stages and 14.6× end-to-end speedup on off-the-shelf GPUs. To further address new bottlenecks introduced by our rendering pipeline, we propose a pipelined architecture that simplifies the overall design while addressing newly emerged bottlenecks in projection and aggregation. Evaluated across four 3DGS-SLAM algorithms, SPLATONIC achieves up to 274.9× speedup and 4738.5× energy savings over mobile GPUs and up to 25.2× speedup and 241.1× energy savings over state-of-the-art accelerators, all with comparable accuracy.

## 中文摘要

凭借高保真重建与快速收敛，3D 高斯泼溅（3DGS）已成为 SLAM 的一个富有前景的方向。然而，由于计算开销高昂（尤其是跟踪过程），3DGS-SLAM 算法在移动平台上仍难以实用。本文提出 SPLATONIC——一种面向资源受限设备的稀疏、高效实时 3DGS-SLAM 算法-硬件协同设计。受经典 SLAM 方法启发，我们提出自适应稀疏像素采样算法，在保持精度的同时将渲染像素数最多减少 256 倍。为在移动 GPU 上释放这一性能潜力，我们设计了一种新颖的基于像素的渲染流水线，通过高斯并行渲染与抢占式 α 检验（preemptive α-checking）提升硬件利用率。这些优化共同在瓶颈阶段带来最高 121.7 倍加速，并在现成 GPU 上实现 14.6 倍端到端加速。为进一步解决渲染流水线引入的新瓶颈，我们提出一种流水线架构，在简化整体设计的同时应对投影与聚合阶段新出现的瓶颈。在四种 3DGS-SLAM 算法上评估，SPLATONIC 相较移动 GPU 实现最高 274.9 倍加速与 4738.5 倍能耗节省，相较最先进的加速器实现最高 25.2 倍加速与 241.1 倍能耗节省，且精度相当。
