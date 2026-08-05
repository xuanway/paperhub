---
title: "LIO-DPC: Accurate and Fast LiDAR-Inertial Odometry with Dynamic Pose Chain"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# LIO-DPC: Accurate and Fast LiDAR-Inertial Odometry with Dynamic Pose Chain

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS1: Autonomous Systems (Automotive, Robotics, Drones)</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11345708">https://ieeexplore.ieee.org/document/11345708</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>激光雷达-惯性里程计，同步定位与地图构建，状态估计 </p>
</div>

---

## 研究概要
本文提出LIO-DPC激光惯性里程计框架，设计动态位链解耦滤波与图优化，实现并行运算；设计环路稀疏化指标筛选高质量回环约束。在多公开数据集验证，定位RMSE远优于FAST-LIO2、LIO-SAM等SOTA，单帧耗时接近轻量化滤波方案，兼顾实时性与长期精度。

## 背景和动机
1. 激光惯性里程计分滤波、图优化两类：滤波法高频实时但累积漂移严重；图优化通过回环修正误差，但计算量大、实时性差。
2. 现有融合方案需等待图优化完成再更新滤波状态，引入巨大延迟，无法兼顾低时延与高精度。
3. 同时间段会产生大量时空邻近回环，全部参与优化大幅提升算力，还易引入匹配噪声带来额外定位误差。
4. 缺少可并行执行滤波增量更新与局部图批量优化的统一载体，难以平衡时延与轨迹漂移。

## 相关工作
1. 滤波类LIO（FAST-LIO/FASTER-LIO）：基于ESKF/IESKF实现高频位姿输出，无全局回环校正，长距离轨迹累积漂移显著。
2. 图优化类LIO（LIO-SAM/LILI-OM）：因子图融合IMU预积分与回环约束，精度高，但单帧计算耗时极高，无法嵌入式实时运行。
3. 滤波+图融合方案：检测回环后阻塞滤波流程等待优化结果，牺牲实时性能，未实现并行解耦。
4. 回环优化相关工作：多采用全部回环参与图求解，无筛选机制，冗余约束增加计算开销与匹配误差。

## 本文解决方案
### 1 动态位链DPC核心载体
定义由初始位姿+连续相对位姿构成的位链；分为增量更新、批量更新两条独立流水线，二者互不阻塞，实现滤波与图优化并行。
- 增量更新：利用滤波短时高精度相对位姿追加到位链，维持高频里程输出；
- 批量更新：局部图优化后批量替换位链片段，消除累积漂移。
### 2 局部位姿图最小二乘优化
检测到回环后截取位链局部片段构建带回环约束因子图，最小化变换误差求解优化后相对位姿，再对位链批量替换更新。
### 3 环路稀疏筛选策略
设计综合打分指标：归一化时间跨度（优化规模）+归一化点云匹配分数，加权计算后仅保留最高分回环参与优化，剔除低质量冗余回环。

## 实验分析
1. 测试数据集：UTBM、URBAN、NCLT、LIO-SAM共13条真实车载序列，对比FAST-LIO2、FASTER-LIO、LILI-OM、LIO-SAM。
2. 定位精度：全序列LIO-DPC平移RMSE显著低于基线，长距离场景漂移抑制效果突出，LIO-SAM无法运行的数据集仍稳定输出轨迹。
3. 实时性能：单帧平均耗时3.5~4.5ms，与轻量化FASTER-LIO接近，远低于LILI-OM、LIO-SAM数十毫秒的处理延迟。
4. 消融实验：移除图优化后漂移大幅上升；移除回环稀疏化，图总耗时提升50%以上且定位精度下降。
5. 轨迹可视化：长里程闭环场景，本文轨迹与真值贴合度显著优于滤波基线。

## 研究启发
1. 滤波与图优化无需串行阻塞，通过相对位姿动态位链解耦两条流水线，可同时拥有高频实时输出与回环校正能力。
2. 大量时空邻近回环存在冗余，设计综合质量筛选指标能在不损失精度前提下大幅降低图优化计算量。
3. 仅对局部位姿片段做小规模因子图求解，相比全局图可大幅削减算力，适配车载、嵌入式低算力设备。
4. 采用短时滤波相对位姿增量扩展，能避免单步大误差传导，为局部优化提供可靠初始值。
5. 融合类LIO设计核心是分离实时增量输出与低频率批量校正，二者并行是平衡时延与长期定位精度的关键思路。
