---
title: "ControlNet: 为文生图扩散模型添加条件控制"
description: "ControlNet 通过可训练副本和零卷积为 Stable Diffusion 添加精确的空间条件控制（边缘、姿态、深度等）。CVPR 2025 论文解读。"
tags:
  - "图像生成"
  - "扩散模型"
  - "条件控制"
  - "ControlNet"
  - "CVPR2025"
---

# ControlNet: Adding Conditional Control to Text-to-Image Diffusion Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">ControlNet 通过冻结原始扩散模型权重，训练一个可训练的编码器副本，并使用"零卷积"连接，为 Stable Diffusion 添加精确的空间条件控制能力，同时保留原模型的生成质量。</p>
<p class="paper-seo-summary__tags">CVPR 2025 · 图像生成 · 条件控制 · Stable Diffusion · ControlNet</p>
</div>

**论文链接**：[arXiv 2302.05543](https://arxiv.org/abs/2302.05543)  
**代码**：[github.com/lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet)  
**机构**：Stanford University  
**发表**：CVPR 2025

---

## 一句话总结

ControlNet 通过"冻结原模型 + 可训练副本 + 零卷积"的精妙设计，以极低的训练成本为任意预训练扩散模型添加边缘、姿态、深度等空间条件控制。

---

## 背景与动机

Stable Diffusion 等文生图模型仅接受文本提示，无法精确控制生成图像的空间结构（如人物姿态、物体轮廓）。直接微调会破坏原模型的生成质量。

**核心问题**：如何在不破坏预训练模型的前提下，添加精确的空间条件控制？

---

## 方法详解

### 核心架构

1. **冻结原模型**：Stable Diffusion 的 U-Net 权重完全固定
2. **可训练副本**：复制 U-Net 的编码器部分，形成可训练的条件编码器
3. **零卷积（Zero Convolution）**：使用权重和偏置初始化为零的 1×1 卷积连接两者
   - 初始状态：ControlNet 输出全为零，不影响原模型
   - 随训练进行：逐渐学习将条件信息融入生成过程

### 支持的条件类型

- **Canny 边缘**：精确控制物体轮廓
- **HED 软边缘**：更柔和的轮廓控制
- **人体姿态（OpenPose）**：控制人物动作
- **深度图**：控制空间结构
- **语义分割图**：区域级别控制
- **涂鸦（Scribble）**：草图转图像

---

## 实验结果

用户研究（偏好率，越高越好）：

| 条件类型 | ControlNet vs. DALL-E 2 |
|---------|------------------------|
| 姿态控制 | **ControlNet 胜出 75%** |
| 边缘控制 | **ControlNet 胜出 81%** |

---

## 核心亮点

1. **零卷积妙招**：保证训练初期完全不影响原模型，训练稳定
2. **训练高效**：只训练副本，参数量仅为原模型一半，单 GPU 可训练
3. **通用框架**：可适配任何基于 U-Net 的扩散模型
4. **广泛影响**：ControlNet 迅速成为图像生成领域最广泛使用的条件控制方法

---

## 局限性

- 每种条件类型需要独立训练一个 ControlNet
- 多条件同时控制时效果可能不一致
- 深度图等条件的提取质量直接影响生成效果
