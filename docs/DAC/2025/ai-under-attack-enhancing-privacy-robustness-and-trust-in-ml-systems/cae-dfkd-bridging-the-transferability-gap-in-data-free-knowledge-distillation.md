---
title: "CAE-DFKD: Bridging the Transferability Gap in Data-Free Knowledge Distillation"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "ai-ml-security"
  - "knowledge-distillation"
  - "data-free"
  - "transfer-learning"
  - "privacy"
---

# CAE-DFKD: Bridging the Transferability Gap in Data-Free Knowledge Distillation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.21478">https://arxiv.org/abs/2504.21478</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 知识蒸馏，表示学习，迁移学习，对比学习 </p>
</div>

---


## 研究概要
本文提出CAE-DFKD无数据知识蒸馏框架，摒弃图像层操作转向嵌入层优化。设计CEND类别嵌入扩散模块生成结构化潜空间，搭配CNCL嵌入级对比学习，解决合成图质量不均、泛化迁移差问题。多分辨率图像及分割、检测等下游任务验证，精度与迁移能力全面超越现有SOTA。

## 背景和动机
1. 无数据知识蒸馏(DFKD)无需原始训练集，保护数据隐私，但现有方法仅聚焦图像分类，模型表征跨任务迁移能力弱。
2. 生成器随机高斯采样导致合成图像类别质量差异大，大量低语义噪声样本，直接套用图像级Mixup、对比学习会降低学生精度。
3. 传统DFKD生成潜空间无类别先验，生成器收敛速度慢，模式坍塌严重，生成样本多样性不足。
4. 现有对比学习基于图像构建正负样本，低质量合成图会混淆语义边界，破坏域不变特征提取。
5. 缺少统一框架兼顾分类精度与下游分割、检测、深度估计等任务的迁移性能。

## 相关工作
1. 生成式DFKD：DAFL、NAYER、SpaceShipNet等优化生成样本多样性，仅提升分类指标，未关注跨任务泛化。
2. 图像级对比学习：基于真实图像构建正负样本，直接用于DFKD会放大合成图噪声，带来精度衰减。
3. 蒸馏优化方案：KDCI、AdaDFKD等通过因果推理、课程学习缓解分布偏移，但仍停留在图像维度。
4. 数据集浓缩类方法：依赖梯度匹配合成数据，训练开销大，难以适配多下游迁移任务。
5. 特征蒸馏方法：仅对齐中间特征，未利用类别文本先验构建结构化嵌入空间。

## 本文解决方案
### 1 类别嵌入噪声扩散层C
利用CLIP预训练语言模型离线生成类别结构化初始嵌入；多分布噪声源对嵌入做元素扰动，丰富潜空间、加速生成器收敛，规避随机高斯噪声的无结构缺陷。
### 2 嵌入级类别噪声对比学习CN
不操作图像，以不同扩散程度嵌入生成样本构建正负对，同类扩散样本为正、异类样本为负，引导学生学习域不变类别特征。
### 3 双阶段联合损失优化
生成器融合交叉熵、BN稳定、对抗损失；学生网络结合传统KD的KL损失与CNCL对比损失，平衡分类精度与泛化能力。
### 4 端到端DFKD训练流水线
离线生成类别嵌入→CEND扩充潜空间→生成器合成图像→学生同时执行知识蒸馏与嵌入对比学习，完整适配无数据场景。
### 5 多下游任务迁移评测方案
训练后的学生模型直接微调语义分割、目标检测、深度估计等任务，量化表征可迁移性。

## 实验分析
1. 实验配置：CIFAR/Tiny-ImageNet/ImageNet多分辨率数据集，ResNet/VGG/WRN师生模型，RTX3090训练。
2. 分类性能：各类数据集下Top-1精度优于NAYER、SpaceShipNet等SOTA，Tiny-ImageNet达64.72%。
3. 迁移能力：NYUv2、ADE20K分割、COCO检测任务中mIoU/mAP显著高于对比方法，部分指标超过有数据蒸馏基线。
4. 消融实验：CEND提升训练速度最高1.71倍，CNCL大幅提升下游任务精度；噪声源N=4时综合性能最优。
5. 泛化测试：CLIP作为文本编码器效果最优，仅使用类别索引提示也能保持稳定性能。

## 研究启发
1. DFKD瓶颈并非分类精度，而是表征跨任务迁移能力，嵌入层优化比图像层增广更适合合成噪声数据。
2. 引入大语言模型类别先验可构造结构化潜空间，从根源缓解生成器模式坍塌、收敛慢问题。
3. 图像级对比学习不适用于低质量合成样本，嵌入层构建正负对能避免语义混淆，强化通用特征。
4. 评估DFKD不能只看分类准确率，必须增加分割、检测等下游迁移任务作为核心指标。
5. 无数据隐私场景下，结构化嵌入+嵌入对比学习可兼顾隐私、精度与模型复用价值。
