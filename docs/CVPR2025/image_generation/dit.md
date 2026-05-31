---
title: "DiT: 基于 Transformer 的可扩展扩散模型"
description: "DiT 将 Transformer 替代 U-Net 作为扩散模型骨干，验证了图像生成中的扩展定律，在 ImageNet 上达到 SOTA FID。CVPR 2025 论文解读。"
tags:
  - "图像生成"
  - "扩散模型"
  - "Transformer"
  - "DiT"
  - "CVPR2025"
---

# Scalable Diffusion Models with Transformers (DiT)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DiT 用 Transformer 替代 U-Net 作为扩散模型的骨干网络，在潜在空间（LDM）中操作，随模型规模和计算量增大，生成质量单调提升，最终在 ImageNet 256×256 上达到 FID 2.27。</p>
<p class="paper-seo-summary__tags">CVPR 2025 · 图像生成 · 扩散模型 · Transformer · DiT</p>
</div>

**论文链接**：[arXiv 2212.09748](https://arxiv.org/abs/2212.09748)  
**代码**：[github.com/facebookresearch/DiT](https://github.com/facebookresearch/DiT)  
**机构**：UC Berkeley, Meta AI Research  
**发表**：CVPR 2025

---

## 一句话总结

DiT 将扩散模型的主干网络从 U-Net 替换为 Transformer，在 ImageNet 类别条件图像生成上验证了"更大的模型 + 更多计算 = 更好的图像"这一扩展定律。

---

## 背景与动机

Stable Diffusion 等主流扩散模型使用 U-Net 作为去噪网络，而 Transformer 在语言和视觉表征学习中已展现出卓越的扩展性。能否将扩散模型也迁移到 Transformer 架构？

---

## 方法详解

### 架构设计

- **潜在空间操作**：继承 LDM 框架，在 VAE 编码的潜在空间中训练，降低计算成本
- **Patch 化输入**：将 latent 图像分割为 patches，类似 ViT
- **条件注入**：通过 AdaLN-Zero 将时间步 t 和类别标签 c 注入每个 Transformer Block

### 四种条件注入方式（消融对比）

1. In-context conditioning：将条件 token 拼接到序列
2. Cross-attention：使用交叉注意力注入条件
3. Adaptive layer norm (adaLN)：用条件调制 LayerNorm 参数
4. **adaLN-Zero**（最终选择）：初始化每个块的输出为零，稳定训练

### 模型规模系列

| 模型 | 参数量 | GFLOPs |
|------|-------|--------|
| DiT-S | 33M | 6 |
| DiT-B | 130M | 23 |
| DiT-L | 458M | 80 |
| DiT-XL | 675M | 119 |

---

## 实验结果

ImageNet 256×256 类别条件生成（FID，越低越好）：

| 模型 | FID-50K |
|------|---------|
| ADM | 10.94 |
| LDM-4 | 3.60 |
| **DiT-XL/2** | **2.27** |

---

## 核心亮点

1. **扩展定律验证**：模型规模和计算量增加，FID 单调下降
2. **架构简洁**：纯 Transformer，无需 U-Net 的跳跃连接等特殊设计
3. **高效潜在空间**：在潜在空间操作，计算成本远低于像素空间
4. **影响深远**：奠定了 Sora、SD3 等后续工作的架构基础

---

## 局限性

- 训练计算量较大
- 推理速度相对 U-Net 变体略慢
- 本文仅验证类别条件生成，文本条件生成由后续工作扩展
