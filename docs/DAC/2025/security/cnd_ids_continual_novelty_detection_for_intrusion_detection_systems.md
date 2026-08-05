---
title: "CND-IDS: Continual Novelty Detection for Intrusion Detection Systems"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "intrusion-detection"
  - "continual-learning"
  - "novelty-detection"
  - "iot-security"
  - "unsupervised-learning"
---

# CND-IDS: Continual Novelty Detection for Intrusion Detection Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC1: AI/ML Security/Privacy</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.14094">https://arxiv.org/abs/2502.14094</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/Sean-Fuhrman/CND-IDS">https://github.com/Sean-Fuhrman/CND-IDS</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 持续新颖性检测，入侵检测系统，无监督连续学习，主成分分析重建 </p>
</div>

---


## 研究概要
本文提出CND-IDS无标签持续异常入侵检测框架，由持续特征提取器与PCA重构异常检测器构成。设计融合聚类分离、重建、持续正则的复合损失，仅依靠正常数据训练，无需攻击标签。在4类IoT/网络入侵数据集验证，相比SOTA无监督持续学习方法F1最高提升6.1倍，零日攻击泛化能力提升6.5倍。

## 背景和动机
1. 网络、IoT攻击持续迭代，流量分布不断偏移，传统静态IDS模型易发生灾难性遗忘，对新型零日攻击识别效果极差。
2. 真实环境难以获取大量标注攻击样本，现有持续学习IDS普遍依赖攻击标签，无法适配无标注数据流场景。
3. 传统孤立森林、OC-SVM等异常检测模型不具备持续更新能力，分布漂移后检测精度大幅衰减。
4. 现有持续学习方案未区分正常/异常数据内在特征差异，特征空间混叠，难以区分从未见过的新型攻击。
5. 缺乏面向无标签流式流量、兼顾抗遗忘与零日泛化的一体化持续新奇检测IDS方案。

## 相关工作
1. 有监督持续学习IDS：Ella、LwF等算法依赖攻击标注，工业场景标签获取成本极高，无法落地无标注流量环境。
2. 传统静态异常检测：LOF、OC-SVM、普通PCA仅离线训练，分布变化后性能断崖式下跌，无在线更新机制。
3. 通用持续新奇检测：ADCN、INCDFM面向通用图像数据，未针对网络流量、攻击特征做定制优化。
4. 深度学习IDS：XGBoost、DNN等静态模型仅适配固定分布，新型零攻击识别准确率极低。
5. 增量聚类检测：仅完成样本分簇，不优化特征区分度，正常与异常特征易重叠，误报率高。

## 本文解决方案
### 1 流式数据分片划分机制
将时序流量划分为多段体验流，每段包含全新攻击类别；仅预留纯净正常子集训练PCA检测器，全部训练流无任何攻击标签，模拟真实无标注线上场景。
### 2 三层复合持续损失CND Loss
包含聚类分离损失LCS：借助K-Means与三元损失拉大正常/异常特征距离；重建损失LR保证特征信息完整；持续正则损失LCL约束新旧嵌入，缓解灾难性遗忘。
### 3 MLP自编码器持续特征提取器CFE
四层MLP编解码结构，每段数据流迭代更新；仅保存模型权重无需缓存历史流量，大幅降低存储开销，持续适配分布变化。
### 4 PCA重构异常检测器
用纯净正常子集编码后的特征训练PCA，以重建误差作为异常分数，通过Best-F阈值划分攻击/正常流量，天然适配未知零日威胁。
### 5 完整线上推理流水线
逐段更新CFE、重训PCA检测器，使用AVG、前向/后向迁移三类指标量化持续检测效果，兼顾已知攻击与新型威胁评估。

## 实验分析
1. 实验设置：CICIDS2017、UNSW-NB15、WUSTL-IIoT、X-IIoT四类数据集，基线ADCN、LwF、LOF、DIF等，RTX3090完成训练。
2. 持续学习指标：相较ADCN、LwF，平均F1最高提升6.1倍，零日前向迁移最高提升6.5倍，多数数据集后向迁移为正，无严重遗忘。
3. 静态异常对比：CND-IDS平均F1优于DIF、PCA、LOF，PR-AUC阈值无关指标同样全面领先。
4. 消融实验：移除聚类分离损失会大幅降低异常区分能力；移除重建损失引发严重灾难性遗忘。
5. 推理开销：单样本推理仅0.0019ms，接近纯PCA速度，远低于ADCN、DIF，满足实时流量检测需求。

## 研究启发
1. 工业级IDS不能依赖攻击标注，仅使用纯净正常样本构建异常基准是低成本实用方案。
2. 持续学习与新奇检测必须耦合，仅增量更新不做特征区分会大幅削弱零日攻击识别能力。
3. 三元聚类损失可有效拉开正常、异常特征边界，显著降低流量误报、漏报率。
4. 基于嵌入权重的持续正则无需存储历史流量，解决流式大数据存储瓶颈。
5. 评估持续IDS不能只看已知攻击精度，前向迁移指标是衡量零日泛化能力核心标准。

