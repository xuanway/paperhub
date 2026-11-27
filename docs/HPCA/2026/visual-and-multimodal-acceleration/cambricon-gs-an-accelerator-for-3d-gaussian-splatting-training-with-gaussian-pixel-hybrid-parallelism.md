---
title: "Cambricon-GS: An Accelerator for 3D Gaussian Splatting Training with Gaussian-Pixel Hybrid Parallelism"
description: "HPCA 2026 · Visual and Multimodal Acceleration"
tags:
  - "HPCA2026"
  - "Visual and Multimodal Acceleration"
---

# Cambricon-GS: An Accelerator for 3D Gaussian Splatting Training with Gaussian-Pixel Hybrid Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Visual and Multimodal Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Visual and Multimodal Acceleration</p>
</div>

**论文链接**：
**作者**：Rui Wen Institute of Computing Technology, Chinese Academy of Sciences , Zhifei Yue University of Science and Technology of China , Tianbo Liu University of Science and Technology of China , Xinkai Song Institute of Computing Technology, Chinese Academy of Sciences , Jin Li Institute of Computing Technology, Chinese Academy of Sciences , Di Huang Chinese Academy of Sciences, Institute of Computing Technology , Jiaming Guo Institute of Computing Technology, Chinese Academy of Sciences , Xing Hu Institute of Computing Technology, Chinese Academy of Sciences , zidong du Institute of Computing Technology, Chinese Academy of Sciences , Qi Guo Chinese Academy of Sciences , Tianshi Chen Cambricon Technologies
**会议**：HPCA 2026

---

## 中文标题

Cambricon-GS：面向 3D 高斯泼溅训练的高斯—像素混合并行加速器

## 英文摘要

3D Gaussian Splatting (3DGS) is a breakthrough in 3D reconstruction using 3D Gaussians. However, even on high-end GPUs like the NVIDIA A100, reconstructing complex scenes remains time-consuming, taking over 15 minutes. The main bottleneck is α-computation, which accounts for 71.25% of training workload, yet 93.03% of it is invalid due to the localized influence of Gaussians. To address this issue, we propose Cambricon-GS, an accelerator for 3DGS training with Gaussian–Pixel hybrid parallelism. At the software level, we introduce a hybrid parallel workflow that breaks the limitation of conventional pixel-only parallelism through two key techniques: Center-Pixel Gaussian Culling (CPGC), which eliminates invalid Gaussians early, and Seed-Driven Gaussian Region Exploration (SDGRE), which reduces invalid computation for partially valid Gaussians by selectively exploring valid regions. Overall, the workflow significantly reduces α computations, lowering the workload to 17.99%. At the hardware level, Cambricon-GS decouples α-computation and α-blending into GUnits and PUnits, organized in a 2D mesh-based NoC that supports asynchronous execution and efficient data routing. We further boost performance via Gaussian/Pixel load balancing and tiled SSIM based pipelining. The evaluation results show that Cambricon-GS achieves 19.63×, 14.86×, 15.42×, 2.98× and 2.63× speedup, and 78.62×, 63.00×, 61.72×, 3.89× and 3.22× energy saving, compared to A100, GSCore, GBU, GSArch, and GauSPU, respectively, with negligible image quality loss.

## 中文摘要

3D 高斯泼溅（3DGS）是利用 3D 高斯进行三维重建的突破性技术。然而即便在 NVIDIA A100 这样的高端 GPU 上，重建复杂场景仍需超过 15 分钟。主要瓶颈是 α 计算，它占训练负载的 71.25%，但其中 93.03% 因高斯的局部影响而是无效的。为此我们提出 Cambricon-GS，一种采用高斯—像素混合并行的 3DGS 训练加速器。软件层面，我们引入混合并行工作流，以两项关键技术突破传统仅像素并行的限制：中心—像素高斯剔除（CPGC）提前剔除无效高斯，种子驱动高斯区域探索（SDGRE）通过选择性探索有效区域减少部分有效高斯的无效计算，从而把 α 计算负载降至 17.99%。硬件层面，Cambricon-GS 将 α 计算与 α 混合解耦为 GUnits 与 PUnits，组织在支持异步执行与高效数据路由的二维网格 NoC 中，并通过高斯/像素负载均衡与基于分块 SSIM 的流水线进一步提升性能。评估显示，相比 A100、GSCore、GBU、GSArch 与 GauSPU，Cambricon-GS 分别取得 19.63 倍、14.86 倍、15.42 倍、2.98 倍与 2.63 倍加速，以及 78.62 倍、63.00 倍、61.72 倍、3.89 倍与 3.22 倍节能，图像质量损失可忽略。
