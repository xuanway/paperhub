---
title: "BEVSA: A Real-Time Bird's-Eye-View Semantic Segmentation Accelerator for Multi-Camera System"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# BEVSA: A Real-Time Bird's-Eye-View Semantic Segmentation Accelerator for Multi-Camera System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132909">https://ieeexplore.ieee.org/document/11132909</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 3D感知，BEV池化，BEV语义分割，异构集群，多相机系统，并行化，稀疏性利用</p>
</div>


---

## 研究概要
本文面向自动驾驶多相机BEV语义分割提出异构集群加速器BEVSA。设计分块分层BEV池化集群压缩搜索空间、并行计算；粗细粒度结合零跳过卷积集群挖掘特征稀疏。28nm流片测试，BEV池化提速43.2倍，卷积吞吐提升1.61倍，单集群实时23.1帧，每帧能效提升167.4倍。

## 背景和动机
1. 自动驾驶多相机BEV分割依赖Lift-Splat架构，边缘端部署存在两大性能瓶颈。
2. BEV池化需大量特征排序与不规则访存，占总延迟64%，单芯片串行搜索空间巨大，并行度极低。
3. BEV编码器输入激活平均稀疏度69.1，无效零运算占卷积总量55.7%，算力浪费严重。
4. 现有单传感器空间划分方案无法处理多相机视场重叠，通用GPU边缘平台功耗高、帧率不满足车载实时83.3ms约束。

## 相关工作
1. 单传感器3D感知处理器：RGB-D、激光雷达专用空间搜索单元，仅适配单一传感器，无法处理多相机重叠视区。
2. 通用DNN稀疏加速器：仅支持固定粒度稀疏跳过，未利用BEV帧间稀疏稳定特性，无异构稀疏/稠密双核心调度。
3. 车载边缘GPU平台（Jetson Orin）：通用架构无法定制BEV池化并行逻辑，稀疏计算无硬件加速，能效极差。
4. 现有BEV专用硬件：未解决多相机分块并行，缺少分层累加与粗细粒度结合的零跳过机制。

## 本文解决方案
### 1. 整体异构集群架构
由BEV池化集群BPC、混合卷积集群CC、顶层控制器与片上网络组成，分别处理视图转换与编码推理。
### 2. 分块分层BEV池化集群
- 视锥分块：按网格局部性拆分相机特征，消除全局排序，搜索空间缩减99.6%；
- 视锥拼接：处理相机重叠区域，消除跨块重复检索；
- 分层累加单元：高度并行+宽度逐次求和，循环数大幅降低，16路并行CS单元硬件加速。
### 3. 粗细粒度联合零跳过卷积集群
- 粗粒度通道级即时剪枝：帧间全零通道长期稳定，永久跳过对应计算，削减50%以上运算；
- 细粒度瓦片级稀疏调度：VPC稀疏核心、MPC稠密核心，基于帧间稀疏相似度查表动态分配任务；
- CSR压缩存储非零特征，双缓冲复用权重，聚合单元合并双核心输出。

## 实验分析
1. 硬件实现：28nm工艺、500MHz，面积4.91mm²，峰值功耗877.6mW，片上SRAM共861KB。
2. BEV池化增益：分块并行提速11.6倍，拼接优化至2.03倍，分层累加再提升1.83倍，合计较Orin基线提速43.2倍。
3. 卷积稀疏收益：粗剪枝吞吐提升1.37~1.42倍，细粒度调度再加1.11~1.13倍，整体提升1.52~1.61倍。
4. 整机性能：单CC实时23.1fps，双CC可达44.6fps；相比Jetson Orin，吞吐2.45倍，单帧能效提升167.4倍。
5. 多相机扩展性：相机数量增加时，BEV池化延迟涨幅被严格控制，远优于通用边缘GPU。

## 研究启发
1. BEV视图转换是车载感知核心瓶颈，不能复用单传感器硬件，必须针对多相机重叠视区设计分块并行机制。
2. 稀疏加速要分层设计：通道粗粒度剪枝减少整体运算，瓦片细粒度异构核心调度充分利用硬件并行。
3. 帧间特征稀疏高度稳定，可预先缓存稀疏模式，省去实时稀疏统计开销，降低访存与延迟。
4. 异构双核心架构适配BEV混合稀疏/稠密特征，单一PE阵列难以兼顾两类数据的计算效率。
5. 车载边缘场景优先专用ASIC集群，相比通用GPU可实现百倍级能效提升，满足低功耗实时自动驾驶需求。