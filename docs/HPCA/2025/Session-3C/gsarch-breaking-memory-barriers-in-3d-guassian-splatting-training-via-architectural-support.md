---
title: "GSArch: Breaking Memory Barriers in 3D Guassian Splatting Training via Architectural Support"
description: "HPCA 2025 · High Stakes Vision"
tags:
  - "HPCA2025"
  - "High Stakes Vision"
---

# GSArch: Breaking Memory Barriers in 3D Guassian Splatting Training via Architectural Support

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: High Stakes Vision。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · High Stakes Vision</p>
</div>

**论文链接**：
**作者**：Houshu He (Department of Computer Science and Engineering, Shanghai Jiao Tong University, Shanghai, China), Gang Li (Institute of Automation, Chinese Academy of Sciences), Fangxin Liu (Shanghai Jiao Tong University), Li Jiang (Shanghai Jiaotong University), Xiaoyao Liang (Shanghai Jiao Tong University), Zhuoran Song (Department of Computer Science and Engineering, Shanghai Jiao Tong University, Shanghai, China)
**会议**：HPCA 2025

---

## 中文标题

GSArch：通过架构支持打破 3D 高斯泼溅训练的内存屏障

## 英文摘要

3D Gaussian Splatting (3DGS) introduces a novel methodology for representing scenes with anisotropic 3D Gaussian primitives, achieving exceptional quality and rendering speed in neural scene representation (NSR). However, the insufficient training speed of 3DGS limits its applicability in tasks that require online learning to perceive dynamic environments, such as autonomous driving and embodied intelligence. Although recent work, GSCore, has introduced a specialized accelerator for the rendering process of 3DGS, it overlooks the time-consuming backward propagation during 3DGS training. In this paper, we propose GSArch, a hardware architecture designed to overcome memory barriers and boost the efficiency of 3DGS training. Through a thorough characterization of 3DGS training, we identify three root causes of inefficiency: redundant data loading from off-chip memory, time-consuming atomic write operations, and severe bank conflicts during on-chip buffer reading. To address these challenges, GSArch introduces three architectural innovations. First, acknowledging that Gaussians vary in shape and often span multiple pixels, with larger Gaussians causing more repetitive data loading, GSArch employs hybrid memory management. This approach categorizes Gaussians into ‘hot’ and ‘cold’ ones, storing hot Gaussians in a fast but small on-chip buffer to reduce redundant loading while minimizing hardware costs. Second, GSArch leverages the informativeness variability of Gaussians’ gradients to filter out low-contribution gradients, significantly reducing atomic operations. Lastly, a rearrangement unit is designed to pack conflicting memory read requests into non-conflicting bundles. Our evaluation results demonstrate that GSArch achieves up to 6.49× and 15.42× speedups compared to Nvidia A100 and Jetson AGX Xavier, respectively, with substantially lower energy consumption and negligible image quality loss.

## 中文摘要

3D 高斯泼溅（3DGS）提出了一种用各向异性 3D 高斯基元表示场景的新方法，在神经场景表示（NSR）中实现了出色的质量与渲染速度。然而，3DGS 训练速度不足，限制了其在需要在线学习以感知动态环境的任务（如自动驾驶与具身智能）中的适用性。尽管近期工作 GSCore 为 3DGS 的渲染过程引入了专用加速器，但它忽略了 3DGS 训练中耗时的反向传播。本文提出 GSArch，一种旨在克服内存屏障并提升 3DGS 训练效率的硬件架构。通过对 3DGS 训练的深入刻画，我们识别出低效的三个根本原因：来自片外内存的冗余数据加载、耗时的原子写操作，以及片上缓冲区读取时严重的 bank 冲突。为应对这些挑战，GSArch 引入了三项架构创新。首先，鉴于高斯形状各异且常跨越多个像素、较大的高斯会导致更多重复数据加载，GSArch 采用混合内存管理，将高斯划分为“热”与“冷”两类，把热高斯存放在快速但容量小的片上缓冲区中，以减少冗余加载并最小化硬件开销。其次，GSArch 利用高斯梯度在信息量上的差异，过滤掉贡献低的梯度，从而显著减少原子操作。最后，设计了一个重排单元，将冲突的内存读请求打包为无冲突的请求束。评估结果表明，与 Nvidia A100 和 Jetson AGX Xavier 相比，GSArch 分别实现最高 6.49 倍和 15.42 倍的加速，同时能耗大幅降低且图像质量损失可忽略。
