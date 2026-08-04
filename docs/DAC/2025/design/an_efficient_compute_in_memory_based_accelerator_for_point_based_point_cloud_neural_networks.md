---
title: "An Efficient Compute-in-Memory based Accelerator for Point-based Point Cloud Neural Networks"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# An Efficient Compute-in-Memory based Accelerator for Point-based Point Cloud Neural Networks

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132775">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132775</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内计算，加速器，点神经网络，位截断</p>
</div>

---

## 研究概要
本文面向边缘点云神经网络提出软硬件协同存算加速器Point-CIM。设计VMP分块+通道最小值基点分解提升偏移比特稀疏，BTQ无硬件开销截断量化，可重构双模CIM单元配合预分解数据流削减片上数据搬运。在PointNet++测试，相较各类基线加速1.69~9.63倍，能效提升3.11~17.32倍。

## 背景和动机
1. PointNet++等点云网络特征学习ML计算占比超70%，边缘端算力、功耗受限，传统GPU/专用阵列访存开销巨大。
2. 现有点云加速器仅优化FPS、邻域搜索，忽视占时最多的特征提取阶段，未利用近点特征相似性带来稀疏优化空间。
3. 存算架构天然支持零比特跳过，但原始点云数据比特稀疏度低，且层间中间特征传输造成显著延迟能耗。
4. 现有分块方案易负载失衡、偏移存在负数导致补码大量1，降低CIM稀疏计算收益，缺少轻量化量化手段。

## 相关工作
1. 点云专用阵列加速器（Mesorasi/PointAcc）：基于脉动/BSP阵列，无法利用数据比特稀疏，片间特征搬运开销高。
2. GDPCA/MoC特征分解方案：均匀体素或莫顿全局分块，基点取中心/均值，偏移易出现负值，稀疏提升有限。
3. 通用CIM加速器：面向CNN设计，无点云专属分块、分解与数据流优化，不匹配点云非结构化数据。
4. 点云轻量化算法：仅软件压缩，无配套存算硬件协同，无法落地边缘低功耗场景。

## 本文解决方案
### 1. VMP空间分块+CM通道基点选择
融合体素划分与莫顿排序，基于索引跳变划分均衡负载簇；采用逐通道最小值作为基点，保证偏移全部为正数，大幅提升偏移比特稀疏度。
### 2. BT比特截断量化
动态截取偏移有效比特段，舍弃高低冗余位，无需新增硬件电路，直接缩短CIM串行计算周期，精度损失可控。
### 3. 双模可重构SR-CIM计算单元
区分基点高精度模式、偏移低比特模式；内置移位加法树对齐分层MAC结果，阵列原生跳过零比特降低运算能耗。
### 4. 预分解PD数据流优化
将分解、量化前移至上一层输出，缓冲区存储压缩后的基点+偏移，大幅减少层间原始特征传输比特总量，削减访存延迟。
### 5. 完整Point-CIM硬件架构
集成映射单元、VMP分块单元、共享缓冲、双模CIM阵列、全局聚合单元，覆盖FPS、邻域搜索、特征学习全流程。

## 实验分析
1. 实验环境：45nm、1GHz SRAM存算架构，NeuroSim仿真，测试ModelNet40/ShapeNet/S3DIS三大点云数据集。
2. 精度表现：BT量化后模型精度仅下降2%~3.2%，满足识别分割任务需求。
3. 稀疏收益：VMP+CM分解后偏移有效零比特占比大幅提升，CIM零跳过节能效果显著。
4. 性能对比：相对CPU提速9.63倍、A100 GPU4.23倍、同类ASIC最低1.69倍；能效最高达基线17.32倍。
5. 消融实验：分解、BT量化、PD数据流三者叠加后，吞吐与节能收益叠加最优。

## 研究启发
1. 点云优化核心瓶颈是特征学习ML，不能仅聚焦采样与邻域搜索，需挖掘近点特征相似性做稀疏预处理。
2. CIM性能高度依赖输入比特稀疏，软硬件协同的数据分解是释放存算零跳过优势的关键。
3. 基点选取直接影响偏移正负分布，纯正数偏移可避免补码引入冗余1，最大化硬件稀疏收益。
4. 层间中间特征搬运是易被忽视的开销，预分解数据流可在不损失精度前提下压缩传输数据量。
5. 存算单元需多模式重构，适配基点高精度、偏移低比特两类差异化计算负载，平衡延迟与能耗。