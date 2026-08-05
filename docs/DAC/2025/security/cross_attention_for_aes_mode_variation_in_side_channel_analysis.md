---
title: "Cross-Attention for AES Mode Variation in Side-Channel Analysis"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "side-channel-analysis"
  - "aes"
  - "cross-attention"
  - "domain-adaptation"
  - "deep-learning"
---

# Cross-Attention for AES Mode Variation in Side-Channel Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132714">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132714</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 侧信道分析，交叉注意力机制，无监督域自适应，深度学习 </p>
</div>

---


## 研究概要
本文提出CA-SCA跨注意力侧信道分析框架，融合跨注意力与无监督域自适应UDA解决AES不同加密模式间迁移攻击难题。通过MMD损失对齐多模式功耗迹高维特征，仅单源标注数据集即可跨ECB/CBC等5类AES密钥恢复，相比现有方案所需攻击迹大幅减少，跨模式泛化能力显著领先SOTA方法。

## 背景和动机
1. 现有深度学习侧信道攻击(DL-SCA)仅在训练与目标AES模式一致时有效，跨模式下迹分布差异大，模型极易失效。
2. ECB、CTR等五种AES运算流程不同，功耗泄漏时序、特征偏移严重，传统CNN无法消除域间分布偏移。
3. 主流跨设备SCA方案依赖多套标注数据集或精细微调，现实攻击中难以获取目标模式标注迹，部署门槛高。
4. 缺乏专门适配AES模式差异的特征对齐机制，现有域适配方法未挖掘迹间关联关键泄漏特征。
5. 尚无将交叉注意力引入跨模式侧信道分析的成熟方案，无法自动筛选各模式共有密钥泄漏特征。

## 相关工作
1. 基础DL-SCA：DL-PA等单域卷积模型，同模式攻击效果好，但跨模式泛化极差，模式差异大时密钥完全无法恢复。
2. 跨设备侧信道：X-DeepSCA、MDM依赖多硬件标注样本，仅解决芯片差异，无法适配AES运算模式带来的分布偏移。
3. 对抗/域适配SCA：AL-PA、CD-PA采用对抗域迁移，需要大量调参，跨AES模式性能提升有限。
4. 传统域自适应算法：MMD仅全局缩小分布距离，无注意力机制筛选密钥相关关键泄漏点，易受噪声干扰。
5. 注意力视觉模型：多头交叉注意力多用于多模态任务，未落地功耗迹时序特征对齐场景。

## 本文解决方案
### 1 跨注意力+UDA一体化网络架构
CNN基础提取时序功耗特征，嵌入多头交叉注意力模块匹配源/目标迹共享密钥泄漏点；联合分类损失与MMD域对齐损失完成无监督域自适应训练。
### 2 跨注意力特征匹配机制
分别将源、目标迹作为Q/K/V输入，计算跨样本时序相关性，自动聚焦AES最后一轮S盒、逆移位等密钥敏感POI点，过滤模式无关噪声时序。
### 3 双联合损失优化目标
总损失=分类交叉熵+λ×MMD分布损失；标注源迹保证密钥分类精度，无标注目标迹缩小跨模式特征分布差，无需目标模式标签。
### 4 标准化跨模式训练流程
仅单类AES标注数据集训练，搭配少量目标无标注迹协同优化；攻击阶段仅数百迹即可完整恢复128位AES密钥。
### 5 多模式泄漏建模适配
针对ECB/CBC/CTR/CFB/OFB五种AES分别定义末轮泄漏模型，统一网络输入格式适配各类时序偏移迹。

## 实验分析
1. 实验平台：CW308+STM32F3采集5类AES功耗迹，每类25000条，对比DL-PA、MDM、X-Deep等主流方案，评价指标猜测熵GE。
2. 单源数据集场景：仅ECB训练攻击OFB，CA-SCA仅需31条迹GE归零，基线方法上千迹仍无法恢复密钥。
3. 多源数据集场景：ECB+CTR训练攻击OFB仅需21条，持续优于全部对比方案。
4. 超参消融：MMD权重λ最优值0.001；注意力头数H=8综合性能最佳，过少特征提取不足、过多易过拟合。
5. 分布量化：NICV、MMD指标验证不同模式泄漏差异巨大，CA-SCA可有效缩小域间特征偏移。

## 研究启发
1. AES不同加密模式带来时序、功耗分布偏移是跨SCA攻击核心障碍，仅靠CNN无法提取通用密钥特征，必须引入注意力筛选关键泄漏点。
2. 无监督域自适应搭配交叉注意力，仅一套标注数据集即可实现多AES模式迁移攻击，大幅降低实战攻击数据门槛。
3. MMD全局对齐不能单独使用，需注意力前置筛选密钥相关时序，否则噪声会干扰域对齐效果。
4. 多头注意力存在最优头数区间，过少丢失细粒度泄漏特征，过多引入冗余参数引发过拟合。
5. 侧信道跨域优化不能仅针对硬件差异，AES运算模式造成的泄漏分布偏移同样需要专用特征对齐架构。


## 相关资源

- **DL-SCA 综述**：Picek et al., "SoK: Deep Learning-Based Physical Side-Channel Analysis" (ACM Computing Surveys, 2023)
- **域自适应方法**：Ganin et al., "Domain-Adversarial Training of Neural Networks" (DANN, JMLR 2016)
- **ChipWhisperer**：[https://github.com/newaetech/chipwhisperer](https://github.com/newaetech/chipwhisperer)
