---
title: "3D Gaussian Splatting: 实时辐射场渲染"
description: "3D Gaussian Splatting 用三维高斯椭球显式表示场景，结合可微分光栅化实现实时高质量渲染。CVPR 2025 论文解读。"
tags:
  - "3D视觉"
  - "新视角合成"
  - "高斯溅射"
  - "实时渲染"
  - "CVPR2025"
---

# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">3DGS 用数百万个三维高斯椭球显式表示场景，通过高效的基于 tile 的光栅化器进行可微分渲染，在 1080p 分辨率下实现 >100 FPS 的实时渲染，同时保持 NeRF 级别的图像质量。</p>
<p class="paper-seo-summary__tags">CVPR 2025 · 3D 视觉 · 实时渲染 · 高斯溅射 · 3DGS</p>
</div>

**论文链接**：[arXiv 2308.04079](https://arxiv.org/abs/2308.04079)  
**代码**：[github.com/graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting)  
**机构**：INRIA, Max Planck Institute  
**发表**：CVPR 2025（原发 SIGGRAPH 2023）

---

## 一句话总结

3D Gaussian Splatting 以三维高斯椭球为场景表示，利用可微分光栅化渲染，在不牺牲质量的前提下将 NeRF 的渲染速度提升 100 倍以上。

---

## 背景与动机

NeRF 渲染质量高但速度极慢（每张图需秒级），难以实现实时应用。后续工作（Instant-NGP 等）提速有限，且内存占用大。

**目标**：实现与 NeRF 同等质量的实时渲染。

---

## 方法详解

### 场景表示：三维高斯

每个高斯椭球由以下属性参数化：
- **位置** $\mu \in \mathbb{R}^3$
- **协方差矩阵** $\Sigma \in \mathbb{R}^{3\times3}$（控制椭球形状和方向）
- **不透明度** $\alpha \in [0, 1]$
- **颜色**：球谐函数系数（支持视角相关外观）

### 初始化

从 SfM 稀疏点云初始化高斯中心位置。

### 可微分光栅化渲染

1. 将三维高斯投影到二维图像平面（2D 高斯溅射）
2. 按深度排序，从前到后 alpha 混合
3. 基于 tile（16×16 像素块）并行处理，GPU 友好

### 自适应密度控制

训练中动态增删高斯：
- **克隆/分裂**：对梯度大的高斯进行增殖
- **删除**：移除不透明度低的高斯

---

## 实验结果

在 Tank & Temples 数据集：

| 方法 | PSNR | FPS |
|------|------|-----|
| Mip-NeRF 360 | 27.69 | 0.06 |
| Instant-NGP | 23.62 | 9 |
| **3DGS** | **27.15** | **>100** |

---

## 核心亮点

1. **实时渲染**：1080p 分辨率下 >100 FPS，较 NeRF 提升 1000 倍
2. **显式表示**：高斯属性可直接编辑，利于后处理
3. **训练快速**：约 30 分钟完成单场景训练
4. **广泛应用**：迅速成为动态场景重建、虚拟现实的核心技术

---

## 局限性

- 内存消耗较大（百万级高斯）
- 对薄结构和精细细节的建模能力有限
- 动态场景处理需要额外扩展
- 渲染结果存在 "爆炸高斯" 等伪影
