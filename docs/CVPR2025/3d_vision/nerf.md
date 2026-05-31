---
title: "NeRF: 神经辐射场用于新视角合成"
description: "NeRF 用 MLP 隐式表示场景，通过体渲染合成任意视角的高质量图像，开创神经隐式表示新范式。CVPR 2025 论文解读。"
tags:
  - "3D视觉"
  - "新视角合成"
  - "神经辐射场"
  - "NeRF"
  - "CVPR2025"
---

# NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">NeRF 用一个 MLP 将 5D 输入（位置 + 方向）映射到颜色和体积密度，通过经典体渲染方程合成任意视角图像，在新视角合成任务上大幅超越先前方法。</p>
<p class="paper-seo-summary__tags">CVPR 2025 · 3D 视觉 · 新视角合成 · 神经辐射场 · NeRF</p>
</div>

**论文链接**：[arXiv 2003.08934](https://arxiv.org/abs/2003.08934)  
**代码**：[github.com/bmild/nerf](https://github.com/bmild/nerf)  
**机构**：UC Berkeley, Google Research  
**发表**：CVPR 2025（原发 ECCV 2020，重新收录）

---

## 一句话总结

NeRF 用 MLP 隐式编码场景的三维结构和外观，在给定多视角图像监督下，能合成任意新视角的高质量图像。

---

## 背景与动机

传统新视角合成方法（光场、MVS 点云）难以处理复杂的遮挡、反射和精细结构。

**核心想法**：将场景表示为连续的神经函数，而非离散的网格或点云。

---

## 方法详解

### 场景表示

将场景表示为一个连续函数 $F_\Theta$：

$$F_\Theta: (\mathbf{x}, \mathbf{d}) \to (\mathbf{c}, \sigma)$$

其中：
- $\mathbf{x} = (x, y, z)$：三维空间位置
- $\mathbf{d} = (\theta, \phi)$：观察方向
- $\mathbf{c} = (r, g, b)$：颜色
- $\sigma$：体积密度

### 体渲染

沿相机光线积分得到像素颜色：

$$C(\mathbf{r}) = \int_{t_n}^{t_f} T(t) \sigma(\mathbf{r}(t)) \mathbf{c}(\mathbf{r}(t), \mathbf{d}) dt$$

其中 $T(t) = \exp\left(-\int_{t_n}^{t} \sigma(\mathbf{r}(s)) ds\right)$ 为透射率。

### 位置编码

将输入坐标映射到高频特征空间，使 MLP 能表示高频细节：

$$\gamma(p) = (\sin(2^0\pi p), \cos(2^0\pi p), \ldots, \sin(2^{L-1}\pi p), \cos(2^{L-1}\pi p))$$

### 分层采样

粗网络 + 细网络，专注于高密度区域进行精细采样。

---

## 实验结果

在 Blender 合成场景（PSNR，越高越好）：

| 方法 | PSNR |
|------|------|
| SRN | 22.26 |
| NV | 26.05 |
| **NeRF** | **31.01** |

---

## 核心亮点

1. **隐式表示**：连续函数比离散表示更紧凑、更平滑
2. **高质量渲染**：真实感远超先前方法
3. **无需显式几何**：不需要 3D 点云或网格
4. **开创性影响**：催生了 NeRF 系列数百篇后续工作

---

## 局限性

- 每个场景需要单独训练（~1-2 天）
- 渲染速度极慢（秒级）
- 需要密集的多视角输入图像
- 对动态场景的处理能力有限
