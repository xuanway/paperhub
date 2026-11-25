---
title: "LA-MTL: Latency-Aware Automated Multi-Task Learning"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# LA-MTL: Latency-Aware Automated Multi-Task Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132930">https://ieeexplore.ieee.org/document/11132930</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/shamvbs/LA-MTL">https://github.com/shamvbs/LA-MTL</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多任务学习，卷积神经网络，边缘设备，梯度冲突，任务干扰，代理延迟 </p>
</div>

---

## 研究概要
本文提出LA-MTL时延感知多任务学习自动搜索框架，设计ALF解析时延代理指标，构建兼顾时延、参数量、任务精度联合损失，配套分层梯度冲突消解策略。支持ResNet/MobileNet/MobileOne多种骨干，在Jetson Orin平台最高降低50%推理时延，参数量压缩超20个百分点，分割/深度估计精度仅浮动±2个百分点。

## 背景和动机
1. 自动驾驶等边缘实时场景需多任务同步推理，传统MTL仅优化精度与参数量，未将硬件时延纳入优化目标，部署后难以满足实时约束。
2. FLOPs与时延相关性差，单纯计算量缩减无法保证推理提速，缺少通用、跨硬件的时延代理指标用于NAS搜索。
3. 多任务共享层易产生梯度冲突，单任务更新会损害其他任务精度，现有方法无法在搜索流程中同步缓解冲突。
4. 主流AutoMTL、MTNAS框架要么无时延感知，要么仅适配单一网络，跨骨干迁移需要大量手动调参。
5. 时延、参数量、任务精度三者存在复杂权衡，缺少一体化自动搜索优化流水线平衡多目标。

## 相关工作
1. 通用多任务学习（Cross-Stitch/AdaShare/AutoMTL）：专注参数共享与精度提升，无硬件时延优化，未处理梯度冲突。
2. 时延感知NAS（MTNAS）：引入硬件时延约束，但网络适配性差，缺少梯度冲突消解模块。
3. 梯度冲突优化（muNet/MGD）：仅缓解任务梯度干扰，完全不考虑边缘推理时延需求。
4. 硬件感知搜索：多基于查表或真实硬件回环，开销巨大，代理指标泛化能力弱。
5. 轻量化MTL：仅做固定网络剪枝，无法逐层动态选择共享/复制/跳跃三种分支策略。

## 本文解决方案
### 1 ALF解析时延代理指标
区分局部单层时延与全局多任务并行开销，为共享/复制/跳跃三种层分支分配标准化时延系数，无需硬件实测即可预估整体推理耗时，适配任意CNN骨干。
### 2 多目标联合损失函数
融合各任务分类损失、ALF时延正则、参数共享正则；设置自适应权重α，满足时延约束时侧重参数量压缩，不满足时优先惩罚高时延分支。
### 3 三层式搜索训练流水线
预热阶段平均三种分支输出；联合阶段基于Gumbel-Softmax学习层分支策略；固定策略后从头重训网络，稳定任务精度。
### 4 分层梯度冲突消解
计算各层S冲突分数，将冲突最高层转为任务专属副本；其余共享层采用梯度修正算法抵消任务梯度互斥干扰，BN层强制独立。
### 5 保守/激进双搜索模式
保守模式时延约束宽松，均衡时延与精度；激进模式追求更低推理延迟，适配极致实时边缘设备，两套方案可按需切换。

## 实验分析
1. 实验环境：CityScapes、NYUv2数据集，ResNet34/MobileNet/MobileOne骨干，Jetson Orin、骁龙Gen2设备，ONNX/TRT/QNN三种推理后端。
2. 时延收益：激进版LA-MTL在Orin最高降低50%推理延迟，保守版兼顾精度，单任务时延小幅上涨但多任务并发速度显著提升。
3. 参数压缩：相较AutoMTL基线参数量再降低20~40个百分点，MobileNet激进方案参数量压缩达87.91%。
4. 精度表现：分割、深度估计任务mIo/误差指标仅±2p.p.浮动，梯度修正后精度优于多数SOTA多任务模型。
5. 消融实验：全局ALF可同时提升时延与参数优化效果；梯度冲突模块能完全消除共享层任务性能衰减。

## 研究启发
1. FLOPs不能替代真实时延，分层全局ALF代理可低成本、跨骨干预估多任务推理耗时，省去硬件回环开销。
2. MTL优化必须将时延纳入搜索主目标，仅靠参数共享无法满足自动驾驶等实时边缘场景需求。
3. 梯度冲突与时延优化可一体化处理，搜索阶段同步识别高冲突层并转为独立分支，避免精度损失。
4. 提供保守/激进两套搜索范式，可适配不同边缘设备的实时、精度权衡需求，工程落地灵活性更高。
5. 分层动态分支（共享/复制/跳跃）相比固定剪枝，能在时延、参数量、精度三者间取得更优帕累托解。
