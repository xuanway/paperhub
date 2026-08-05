---
title: "DAWN: Accelerating Point Cloud Object Detection via Object-Aware Partitioning and 3D Similarity-Based Filtering"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# DAWN: Accelerating Point Cloud Object Detection via Object-Aware Partitioning and 3D Similarity-Based Filtering

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132746">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132746</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>点云目标检测加速，对象感知分区，相似性过滤，帧间冗余点过滤 </p>
</div>

---

## 研究概要
本文提出DAWN点云检测加速框架，利用帧间局部相似性过滤冗余点。设计目标感知分块避免物体割裂，搭配轴排序点采样均衡分区粒度，基于并行豪斯多夫距离实现3D相似度快速判别。在主流检测网络平均提速1.59倍，最高1.70倍，平均过滤超50%点，精度损失可忽略。

## 背景和动机
1. 自动驾驶LiDAR点云检测计算量大，基于点/点体混合网络帧率不足10Hz，无法满足实时车载需求，点处理是核心时延瓶颈。
2. 传统固定网格分块易把物体切分到多个分区，破坏空间完整度，造成检测精度大幅下降。
3. 点云空间分布极不均匀，固定划分会出现空分区与超密分区，难以开展细粒度帧间相似比对。
4. 现有加速方法兼容性差，仅适配单一网络，缺少可兼顾精度、可调时延-精度权衡的通用过滤方案。
5. 帧间大量静态区域重复计算，现有方案未复用历史检测结果，算力浪费严重。

## 相关工作
1. 硬件加速器类（Mars、PointAcc、Point-X）：侧重访存与图遍历优化，未利用时序帧间相似性，无法减少原始点输入量。
2. 网络层优化（Mesorasi）：依靠聚合层延迟计算，仅适配纯点网络，对点体混合、体素网络不兼容。
3. 点采样加速QuickFPS：仅做全局最远点下采样，不区分帧间动态/静态区域，精度损耗更大。
4. 体素/点云基础检测网络（PointRCNN、PV-RCNN、SECOND）：无帧间复用机制，逐帧完整处理全部点，推理延迟高。

## 本文解决方案
### 1 目标感知动态分块算法
利用上一帧检测框坐标划分当前帧边界，分割平面避开物体包围盒，将物体完整保留在单一分区；消除固定网格带来的物体割裂，物体碎片率从34.8%降至2.6%。
### 2 轴排序细粒度点筛选
先后沿X、Y轴对点排序分组，结合历史物体范围调整分组规模，均衡各分区点数量，避免空/过密分区，提供均匀粒度用于相似度对比。
### 3 GPU并行3D豪斯多夫相似度计算
并行求解双向最近点距离得到豪斯多夫值，自适应场景阈值判断分区相似；静态复用历史检测结果，仅对变化分区重新推理。
### 4 可调精度-时延权衡机制
基础阈值叠加场景调节因子，复杂场景收紧判定、简单场景放宽，可灵活控制点过滤比例适配不同车载实时约束。
### 5 通用流水线架构
前置分块-点筛选-相似度过滤模块，无缝对接体素、纯点、点体混合三类检测网络，无需修改原始网络结构。

## 实验分析
1. 实验环境：i7-9700K、RTX2080Ti，KITTI数据集，评测PointRCNN、PV-RCNN、CasA-PV、SECOND。
2. 速度与精度：平均过滤50%点时，PointRCNN提速1.70x(mAP降0.3)、PV-RCNN1.51x(mAP降0.2)、CasA-PV1.56x(mAP降0.4)，整体平均加速1.59倍。
3. 资源开销：过滤后GPU显存、平均利用率显著下降，内存压力大幅缓解。
4. 消融对比：目标分块大幅降低物体碎片化；叠加轴排序后分区粒度更均衡，同等过滤率下精度衰减最慢。
5. 横向对比：相比QuickFPS、Mesorasi，DAWN兼容全部三类检测网络，同精度下帧率更高。

## 研究启发
1. 点云实时加速可从时序维度挖掘冗余，复用静态区域检测结果，比单纯网络/硬件优化收益更显著。
2. 分块策略不能采用固定网格，基于历史检测框的目标感知划分可从源头规避物体割裂带来的精度损失。
3. 点云分布不均问题需通过坐标轴有序分组均衡粒度，才能可靠开展细粒度帧间相似性比对。
4. 豪斯多夫距离适合表征局部3D场景差异，GPU并行计算可将相似度判别开销控制在极低水平。
5. 加速框架需做到网络无关、支持可调权衡阈值，才能适配自动驾驶、机器人等差异化实时硬件约束。