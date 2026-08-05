---
title: "FedEDA: Federated Learning Framework for Privacy-Preserving Machine Learning in EDA"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# FedEDA: Federated Learning Framework for Privacy-Preserving Machine Learning in EDA

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132983">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132983</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 联邦学习，电子设计自动化，隐私保护 </p>
</div>


---

## 研究概要
本文提出FedEDA，首个面向EDA场景的联邦学习聚合算法。利用Rent系数、电路规模等分层电路元数据构造定制正则项，缓解多客户端数据非均衡偏移。在布线可布性、RC寄生、线长三类EDA预测任务验证，相较FedAvg、FedProx、FLNet，回归指标最高提升74.5%，可兼容CNN/MLP/GNN主流EDA模型。

## 背景和动机
1. 各厂商电路IP涉密，无法集中汇总版图数据训练ML模型，EDA数据集稀缺、数据分布不均衡，制约机器学习EDA落地。
2. 通用联邦学习FedAvg/FedPro未适配电路分层结构，EDA客户端数据偏移严重，全局模型精度大幅下滑。
3. 现有EDA联邦方案FLNet仅通过修改网络结构缓解偏置，无法通用适配各类预测模型，泛化性差。
4. EDA数据熵低于图像/文本数据集，小型电路特征高度重叠，简单加权平均会向局部特征偏移，收敛质量差。
5. 缺乏结合Rent规则、模块多样性等电路专属特征的联邦加权聚合策略，未从数据分布根源修正模型漂移。

## 相关工作
1. FedAvg：基础联邦平均，IID数据表现良好，EDA非均衡场景模型漂移严重。
2. FedProx/FedNova/SCAFFOLD：通用FL正则方案，仅面向图像文本，未利用电路领域先验。
3. FLNet：EDA专用联邦方案，依靠修改网络层适配布线预测，无法迁移至RC、线长等其他任务。
4. 通用EDA预测模型（CNN/GNN/MLP）：集中式训练效果优，但无法解决IP隐私数据隔离问题。
5. Rent规则相关版图分析：仅用于划分、预估互连线，未引入联邦学习权重聚合流程。

## 本文解决方案
### 1 电路元数据CM构建机制
提取电路规模、Rent指数p、子模块p标准差σ三类元数据，量化电路分层复杂度；通过min-max逆归一化生成加权系数α，区分简单重复与复杂多模块设计。
### 2 定制化本地损失正则项
在标准训练损失基础上增加α加权L2漂移惩罚，规模小、模块单一电路权重更低，抑制其局部最优主导全局更新。
### 3 三阶段FedEDA联邦框架
初始化：客户端上传CM至服务端统一归一；联邦迭代：本地带正则训练后上传权重，全局简单平均聚合；推理阶段下发全局模型完成EDA预测。
### 4 多模型通用兼容设计
无网络结构修改限制，原生适配CNN可布性、ML寄生RC、GNN线长三类主流EDA预测网络，无需改动模型主干。
### 5 多非均衡场景适配
支持数量倾斜QS、标签倾斜LS、混合LS+QS三类真实厂商数据分布，适配多客户端分布式训练环境。

## 实验分析
1. 实验环境：OpenCores开源电路数据集，ASAP7nm工艺，AMD CPU+RTX GPU，对比FedAvg、FedProx、FLNet。
2. 数据分布特性：EDA数据集熵仅2.74，远低于图像文本，小型电路特征高度重叠易引发模型偏移。
3. 精度对比：混合LS+QS真实场景，RC预测R²提升74.5%，线长提升33.5%；相较FLNet可布性精度最高提升8.74%。
4. 消融与基线：纯本地训练指标衰减超41%，FedEDA相比集中式仅平均下降1.98%，兼顾隐私与精度。
5. 泛化验证：2/3/6客户端、CNN/MLP/GNN多模型下均稳定最优，无任务/规模适配缺陷。

## 研究启发
1. EDA联邦学习不能直接套用通用FL算法，必须引入Rent规则、电路规模等版图领域先验缓解数据偏移。
2. 基于元数据的损失正则化方案具备模型无关优势，相比修改网络结构的FL方案通用性更强。
3. 小型重复电路会主导全局权重平均，需降低其更新权重以避免全局模型局部最优。
4. 联邦学习是解决芯片IP数据隐私隔离的可行路径，可实现多厂商协同训练而不泄露原始版图。
5. 电路分层、模块多样性等版图固有特征可量化为加权因子，是优化分布式EDA模型的低成本有效手段。
