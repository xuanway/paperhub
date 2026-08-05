---
title: "Look Before You Leap: A Self-Review Bayesian Optimization Method for Constrained High-Dimensional Design Space Exploration"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Look Before You Leap: A Self-Review Bayesian Optimization Method for Constrained High-Dimensional Design Space Exploration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132771">https://ieeexplore.ieee.org/document/11132771</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高维设计空间探索，师生范式，深度集成，RISC-V处理器 </p>
</div>


---

## 研究概要
本文提出SRBO自检视贝叶斯优化框架，面向含时序约束的RISC-V高维DSE。在局部BO基础上引入师生模型降低代理误差，深度集成多分类器过滤不可行候选。基于BOOM、Rocket两款RISC-V核心测试，同等时间下超体积相较SOTA最高提升41.47倍，能有效规避局部最优、减少无效仿真。

## 背景和动机
1. RISC-V微架构+EDA综合工具组合参数超50维，设计空间规模达10^30，单配置仿真耗时1~6小时，昂贵仿真限制采样规模。
2. 传统进化算法NSGA-II等采样量巨大，不适配长周期芯片DSE；早期BO仅适配少量微架构参数，忽略EDA工具变量。
3. 现有局部BO（REMOTune/ROI-HIT）缺少约束处理机制，大量违反时序的无效配置占用仿真资源。
4. 有限样本下高斯代理模型预测偏差大，易误导采集函数陷入局部最优，帕累托前沿质量差。
5. 主流方法无变量筛选机制，全空间搜索算力浪费，未聚焦对PPA敏感的关键设计参数。

## 相关工作
1. 进化多目标算法(NSGA-II/MOEA/D)：海量仿真需求，不适用于VLSI长周期评估场景。
2. BOOM-Explorer/GRL-DSE：仅覆盖少量RISC微架构参数，未纳入EDA综合工具参数，维度偏低。
3. REMOTune/ROI-HIT：局部贝叶斯优化+降维，适配高维空间，但无专用约束过滤模块。
4. 标准GPR贝叶斯：单一代理模型，有限样本预测误差高，易误导候选点选取。
5. 常规约束惩罚BO：通过损失惩罚不可行点，时序违例参数空间不连续，惩罚项难以有效引导搜索。

## 本文解决方案
### 1 局部贝叶斯优化核心流程
基于敏感度矩阵筛选影响PPA的关键变量；以当前最高超贡献点为中心划定局部搜索域，缩小优化范围、降低维度；计算HVI指标选取最优候选做仿真。
### 2 师生(TSP)自检视代理模型
MLP作为教师预训候选伪标签，GPR学生基于伪标签+真值训练；学生预测误差回传给教师更新损失，迭代修正模型偏差，缓解有限样本预测失真。
### 3 深度集成约束分类器
多独立MLP集成二分类器，预测配置满足时序可行性；预测概率>0.5判定为可行，提前筛除违例设计，大幅减少无效仿真次数。
### 4 完整SRBO迭代流水线
初始化样本→变量筛选+局部域划定→师生模型预测→集成分类器过滤不可行点→HVI选最优仿真→数据集更新循环。
### 5 适配RISC-V完整评估链路
对接Chipyard、Genus、Verilator，覆盖CPI、面积、功耗、时序约束多目标评估。

## 实验分析
1. 测试基准：7nm ASAP7工艺，BOOM(53维)、Rocket(40维)两类RISC-V，对比BOOM-Explorer、GRL-DSE、REMOTune、ROI-HIT。
2. 超体积(HV)指标：BOOM场景SR相较REMOTune提升41.47倍，Rocket场景提升6.79倍，帕累托解集覆盖范围显著更广。
3. 消融实验：移除师生模块后SRBO性能大幅下降，证明自检视机制可跳出局部最优；集成分类器显著降低仿真失败率。
4. 仿真开销：同等仿真预算下SRBO产出更优解集，无效时序违例样本数量明显少于无约束基线。
5. 收敛特性：SRBO前期收敛速度快，随迭代持续拉开与SOTA超体积差距，鲁棒性更强。

## 研究启发
1. 高维昂贵芯片DSE不能全局遍历，局部搜索+关键变量筛选是平衡算力与优化效果的有效手段。
2. 单一代理模型在少样本场景偏差严重，师生互检架构可互相校正预测，提升采集函数引导精度。
3. 时序等硬约束不适合简单惩罚建模，集成分类前置过滤能从源头节省仿真资源。
4. 微架构+EDA工具参数需统一联合探索，仅优化处理器参数会遗漏综合带来巨大PPA改善空间。
5. 自校正代理+约束过滤+局部贝叶斯的组合范式可迁移至其他昂贵多目标EDA优化任务。