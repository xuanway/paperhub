---
title: "High-throughput Point-Cloud Accelerator with Sparsity-aware Hierarchical Neighbor Voxel Search and Skipping"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# High-throughput Point-Cloud Accelerator with Sparsity-aware Hierarchical Neighbor Voxel Search and Skipping

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132726">https://ieeexplore.ieee.org/document/11132726</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 点云，3D物体检测，加速器，自动驾驶 </p>
</div>


---

## 研究概要
本文面向自动驾驶点云3D稀疏卷积，提出软硬件协同HVSS加速器框架。算法端采用阈值实时体素跳过抑制空洞扩张；硬件设计三级分层并行CAM邻域搜索单元，搭配64×64权重驻留脉动阵列。65nm工艺实测，延迟降低77.7%，相较SPADE、PointAcc能效、吞吐量分别提升1.34×、2.22×，精度仅微增0.48%。

## 背景和动机
1. 激光雷达点云体素稀疏度超98，但标准稀疏卷积扩张会逐层生成大量无效体素，算力、访存开销暴涨，车载边缘设备难以实时推理。
2. 传统暴力邻域搜索需遍历27个邻域坐标，大量空体素造成流水线气泡，PE硬件利用率极低。
3. 现有SPADE、PointAcc加速器采用全局哈希表存储坐标，搜索与存储开销巨大，未区分中心/邻域体素，缺少分层筛选机制。
4. 主流幅值剪枝算法需全局排序，无法硬件实时在线判定有效体素，难以嵌入卷积流水线。
5. SubmConv与SpConv混合网络缺少统一硬件适配方案，无法兼顾两种稀疏卷积的跳过逻辑。

## 相关工作
1. 点云算法：SubmConv维持稀疏但速度受限，SpConv扩张冗余；幅值剪枝需离线预处理，不支持流水线实时过滤。
2. SEC加速器：全量哈希表存储坐标组合，存储开销极大，暴力遍历邻域周期浪费严重。
3. SPADE：去除大哈希表，但无分层并行邻域搜索，空体素气泡问题未解决，不兼容在线体素过滤。
4. PointAcc：基础脉动阵列架构，未设计稀疏感知搜索单元，无法利用点云高稀疏特性。
5. 通用稀疏硬件：仅面向2D CNN，无法适配3D 3×3×3卷积的27邻域不规则坐标检索。

## 本文解决方案
### 1 硬件友好实时阈值体素跳过算法
舍弃百分位排序，采用特征均值固定阈值在线判定重要体素；SFP单元卷积途中同步计算特征均值，无需中间缓存，平均跳过65.7%冗余体素，小幅提升检测精度。区分SpConv/SubmConv执行逻辑，重要体素做扩张、次要体素维持稀疏。
### 2 HVSS三级分层并行体素搜索单元
Stage0：从队列读取仅非零中心体素，跳过全零中心计算；Stage1：X/Y/Z三维并行CAM对角边界预筛选，将27次遍历压缩至2周期生成有效掩码；Stage2：轮询仲裁释放有效邻域坐标送入计算阵列，大幅消除流水线气泡。
### 3 多维并行CAM存储架构
独立CAM-X/CAM-Y/CAM-Z分别存储三轴坐标，并行匹配后按位与判定有效邻域，硬件面积、功耗开销不足1%。
### 4 64×64权重驻留脉动阵列
PE内置27组3×3×3卷积权重寄存器，8bit激活/32累加；配套SFP专用函数单元，卷积、均值计算流水线融合，省去psum中间存储读写。
### 5 多模型兼容流水线
同时支持体素型、柱形点云网络，切换内核寄存器配置适配3×3/3×3×3卷积，端到端覆盖Voxel R-CNN全3D骨干。

## 实验分析
1. 实验环境：65nm 1GHz RTL综合布局布线，KITTI数据集、Voxel R-CNN基线，对比SPADE、PointAcc、暴力搜索BFS。
2. 算法收益：在线体素跳过平均削减65.7%计算量，3D检测精度提升0.48%。
3. 搜索单元消融：HVSS相较BFS邻域搜索次数降低5.16~6.34倍，CAM硬件面积、功耗开销仅0.71%、0.014%。
4. 整体性能：完整软硬件协同方案延迟降低77.7%；相较SPADE能效1.34倍，相较PointAcc吞吐量2.22倍，峰值GOPS/W达1514。
5. 硬件拆解：卷积脉动阵列占96%面积与功耗，HV辅助控制单元开销极低，片上SRAM仅156KB。

## 研究启发
1. 点云高稀疏是核心优化抓手，但仅靠算法剪枝不足，必须配套专用坐标检索硬件消除流水线气泡。
2. 三维邻域无需逐点遍历，对角边界并行CAM预筛选可大幅减少无效坐标查询周期。
3. 离线排序式体素过滤难以硬件落地，卷积途中同步均值判定可实现零额外访存开销的在线剪枝。
4. 权重驻留脉动阵列搭配专用SFP单元，可融合卷积与稀疏过滤两步计算，消除中间特征缓存。
5. 自动驾驶边缘加速器需同时兼容SubmConv、SpConv，分层搜索架构可统一两类卷积的稀疏跳过逻辑。
