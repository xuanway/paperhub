---
title: "Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "quantum-computing"
  - "anomaly-detection"
  - "autoencoder"
  - "unsupervised-learning"
---

# Quorum: Zero-Training Unsupervised Anomaly Detection using Quantum Autoencoders

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.13113">https://arxiv.org/abs/2504.13113</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 零训练无监督异常检测，量子自编码器，随机量子变换 </p>
</div>

---

## 研究概要
本文提出零训练无监督量子异常检测框架Quorum，无需参数优化与梯度计算。采用振幅编码、随机量子自编码器与SWAP测试，结合分桶集成统计打分。在医疗、电力等4类数据集测试，相比训练型QNN平均F1提升23%，对含噪声量子硬件具备强鲁棒性。

## 背景和动机
1. 现有量子异常检测依赖参数化电路训练，梯度易出现贫瘠高原问题，计算开销极高。
2. 主流量子检测方法多为监督/半监督，现实金融、电网场景缺少标注样本，落地受限。
3. 训练流程依赖大量量子-经典交互，NISQ噪声设备下精度衰减严重。
4. 缺少无需训练、通用型无监督量子检测方案，难以适配多行业无标签数据。
5. 传统量子自编码器必须迭代优化门参数，无法快速对流式工业数据实时异常筛查。

## 相关工作
1. 训练型量子自编码器：VQAE、量子GAN类方案，依赖梯度优化，存在贫瘠高原、训练成本高缺陷。
2. 监督量子检测网络：QNN等需标注样本，仅适配特定领域数据集，泛化能力差。
3. 混合量子经典检测：需后端经典模型辅助训练，量子通信开销大。
4. 领域专用量子异常算法：高能物理、网络专用检测器，无通用适配能力。
5. 经典无监督方法：孤立森林、传统自编码器，高维数据特征挖掘弱，无量子加速优势。

## 本文解决方案
### 1 标准化数据预处理与归一化
数值哈希转换、特征归一化约束幅值，保证振幅编码后总概率和为1，消除特征量纲带来的量子状态失衡。
### 2 双轨振幅编码+SWAP相似度比对
两路并行编码原始量子态，随机酉自编码器做变换，通过SWAP测试计算原始与重构态重叠度表征样本偏离程度。
### 3 分桶随机特征选择机制
数据集划分为多个子桶，每组随机选取特征适配量子比特容量，放大正常/异常样本分布差异。
### 4 无训练随机量子自编码器
编码器门角度均匀随机初始化，解码器使用逆变换；通过部分重置比特构建信息瓶颈，全程无参数迭代训练。
### 5 多集成统计异常打分
多组随机电路、多压缩层级并行运算，统计各桶SWAP得分标准差偏移值累加得到最终异常分，天然支持并行计算。

## 实验分析
1. 实验环境：Qiskit仿真，匹配IBM Brisbane真实噪声参数，4096次电路采样，测试4类公开数据集。
2. 精度对比：Quorum在全部数据集F1均优于QNN，平均提升23%；QNN存在漏检、召回极低问题。
3. 噪声鲁棒：带噪声仿真性能仅小幅下降，无需复杂纠错电路，适配近中期NISQ设备。
4. 检测效率：前10%高分样本可检出80%异常，分桶 ablation显示中等桶尺寸综合指标最优。
5. 并行优势：各集成组完全独立，可大规模分布式仿真，资源扩展性强。

## 研究启发
1. 量子异常检测不必依赖梯度训练，随机酉变换+量子态相似度可替代参数优化流程。
2. SWAP测试是高效量子距离度量手段，适合无监督场景下量化样本偏离基准程度。
3. 分桶与多集成策略能弱化噪声干扰，显著提升高维无标签数据异常区分度。
4. NISQ时代算法设计应规避高频梯度迭代，零训练架构更适配现有噪声量子硬件。
5. 量子自编码器核心价值不在重构拟合，而在于随机投影下样本分布差异的放大能力。