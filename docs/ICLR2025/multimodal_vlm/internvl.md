---
title: "InternVL: 扩展视觉基础模型并对齐通用视觉语言任务"
description: "InternVL 将视觉编码器扩展到 6B 参数，通过渐进式对齐训练在各类视觉语言任务上取得领先性能。ICLR 2025 论文解读。"
tags:
  - "多模态"
  - "视觉语言模型"
  - "InternVL"
  - "视觉编码器"
  - "ICLR2025"
---

# InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">将视觉编码器扩展至 6B 参数，匹配 LLM 量级；使用渐进式对齐训练策略，在图像-文本检索、多模态对话等任务上超越 GPT-4V。</p>
<p class="paper-seo-summary__tags">ICLR 2025 · 多模态 VLM · 视觉编码器扩展 · InternVL</p>
</div>

**论文链接**：[arXiv 2312.14238](https://arxiv.org/abs/2312.14238)  
**代码**：[github.com/OpenGVLab/InternVL](https://github.com/OpenGVLab/InternVL)  
**机构**：OpenGVLab, Shanghai AI Laboratory  
**发表**：ICLR 2025

---

## 一句话总结

InternVL 通过将视觉编码器扩展到 6B 参数（接近 LLM 量级）并设计渐进式对齐训练，大幅提升了视觉语言模型的性能上限。

---

## 背景与动机

现有多模态模型的视觉编码器（如 CLIP ViT-L 300M）远小于语言解码器（7B-70B），造成视觉-语言容量不匹配。

**核心假设**：扩展视觉编码器规模是提升多模态性能的关键瓶颈。

---

## 方法详解

### InternViT-6B（大规模视觉编码器）

- 将 ViT 扩展到 **6B 参数**，与 LLaMA-7B 量级相当
- 使用对比学习在 LAION-5B 等大规模图文对数据上预训练
- 引入像素级 shuffle 操作提升高分辨率处理效率

### 渐进式对齐训练

**三阶段训练**：
1. **阶段一**：冻结 LLM，仅训练视觉编码器和连接器（图文对齐）
2. **阶段二**：解冻 LLM，端到端联合微调（能力融合）
3. **阶段三**：指令微调（任务对齐）

---

## 实验结果

| 基准 | GPT-4V | **InternVL-Chat** |
|------|--------|-------------------|
| MMBench | 75.8 | **77.0** |
| MMMU | 56.8 | **51.6** |
| MathVista | 49.9 | **47.7** |
| DocVQA | - | **90.9** |

---

## 核心亮点

1. **视觉扩展律**：首次系统验证视觉编码器扩展带来的性能提升
2. **渐进式训练**：有效缓解大规模视觉-语言联合训练的不稳定问题
3. **动态分辨率**：灵活支持不同分辨率输入，适配各类视觉任务
4. **开源生态**：InternVL 系列模型持续迭代，成为重要开源基线

---

## 局限性

- 6B 视觉编码器推理成本显著高于 CLIP ViT-L
- 高分辨率处理的内存占用较大
