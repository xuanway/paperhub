---
title: "Ensembler: Protect Collaborative Inference Privacy from Model Inversion Attack via Selective Ensemble"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "ai-privacy"
  - "collaborative-inference"
  - "model-inversion"
  - "ensemble-learning"
  - "privacy-preserving"
---

# Ensembler: Protect Collaborative Inference Privacy from Model Inversion Attack via Selective Ensemble

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://par.nsf.gov/servlets/purl/10653116">https://par.nsf.gov/servlets/purl/10653116</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模型反转攻击，协同推理，选择性集成，隐私保护</p>
</div>

---

## 研究概要
本文提出Ensembler选择性集成框架，抵御边缘云协同推理下模型逆攻击。云端部署多分支网络，客户端私有选择子集融合特征，搭配分层训练与正则约束。仅客户端保留单层极端轻量化场景仍可防护，相比基线SSIM最高下降43.5%，推理总开销仅4.8%，兼容噪声类隐私防护方案。

## 背景和动机
1. 边缘算力受限，协同推理拆分网络后客户端仅浅层网络，云端攻击者可通过中间特征实施模型逆攻击还原原始图像。
2. 现有Shredder噪声注入方案缺陷明显：浅层加噪保护弱，深层加噪大幅加重边缘计算负担，人脸等敏感图像仍可被重建。
3. 加密类隐私推理时延数千倍，无法满足实时边缘业务需求；单纯Dropout防护抗逆攻击效果有限。
4. 缺乏兼顾轻量边缘负载、低推理开销、强抗重建能力的协同推理隐私保护方案。
5. 现有防护未利用多网络混淆思路，云端单一网络极易被攻击者拟合逆向解码器。

## 相关工作
1. 噪声扰动类防护（Shredder）：向中间特征注入噪声，浅层防护失效，深层开销巨大，敏感图像重建效果仍较好。
2. 加密安全推理（STAMP等）：同态加密、两方安全计算，隐私强度高但推理延迟提升上百倍，不适合边缘设备。
3. Dropout轻量化防护：单一网络随机失活，混淆能力弱，攻击者易拟合模型实施逆攻击。
4. 模型逆攻击研究：攻击者利用同分布数据集拟合客户端浅层逆向网络，还原人脸、医疗等敏感输入图像。
5. 拆分/联邦学习隐私方案：侧重训练阶段保护，推理阶段针对模型逆攻击的轻量化防护不足。

## 本文解决方案
### 1 云端多网络集成架构
云端部署N组独立后端网络，客户端完成浅层计算并添加高斯噪声后下发特征，云端并行输出多组中间结果回传边缘。
### 2 客户端私有选择器
客户端持有秘密选择规则，仅选取P组云端输出融合，攻击者无法获取选择子集，暴力枚举复杂度指数级提升。
### 3 三阶段专属训练流程
阶段1：分别训练N套完整分支网络；阶段2固定后端网络；阶段3训练客户端首尾层，加入余弦相似度正则，强制浅层适配全部后端分支。
### 4 混合损失函数
分类交叉熵保证推理精度，正则项约束客户端浅层特征与各分支输出保持低相似度，避免偏向单一网络导致泄露。
### 5 兼容扩展设计
可与Shredder噪声、Dropout等方案叠加，客户端计算量与标准协同推理完全一致，云端多网络可并行加速。

## 实验分析
1. 实验配置：ResNet18，CIFAR10/100、CelebA人脸数据集，客户端仅首尾单层，N=10、P=3，对比Shredder、无防护基线、加密方案。
2. 隐私防护：相较单网络基线，SSIM最高下降43.5%、PSNR下降40.5%；优于Shredder，人脸重建清晰度大幅降低。
3. 精度损耗：分类准确率仅下降2.13%，精度损失可控，远优于深层噪声方案。
4. 推理开销：批量128样本总时延仅增加0.19s，额外开销4.8%；加密方案时延超300s差距巨大。
5. 消融验证：私有选择器是核心防护模块，移除后重建质量显著上升；多网络并行可抵消云端计算时延。

## 研究启发
1. 仅靠特征噪声不足以保护单层轻量边缘推理，多网络混淆+私有选择能从模型拟合根源阻碍逆攻击。
2. 隐私防护可分层解耦：边缘仅做浅层计算，混淆逻辑部署云端，不增加客户端算力负担。
3. 指数级枚举复杂度能大幅抬高攻击成本，轻量集成架构比加密方案更适配实时边缘业务。
4. 训练正则约束浅层特征不偏向单一后端网络，是防止攻击者拟合逆向解码器关键手段。
5. 隐私框架需具备兼容性，可与噪声、Dropout等轻量化防护叠加，进一步提升抗攻击上限。


## 相关资源

- **模型逆向攻击**：Fredrikson et al., "Model Inversion Attacks that Exploit Confidence Information" (CCS 2015)
- **协作推理（Split Inference）**：Kang et al., "Neurosurgeon: Collaborative Intelligence" (ASPLOS 2017)
- **隐私保护推理**：
  - GAZELLE (USENIX Security 2018)
  - Delphi (USENIX Security 2020)
  - CrypTen (Meta, 2020)
