---
title: "PICK: An SRAM-based Processing-in-Memory Accelerator for K-Nearest-Neighbor Search in Point Clouds"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PICK: An SRAM-based Processing-in-Memory Accelerator for K-Nearest-Neighbor Search in Point Clouds

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132408">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132408</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存内处理，静态随机存取存储器，K近邻搜索 </p>
</div>


---

## 研究概要
本文提出基于SRAM位串行存内计算的PICK加速器，面向点云kNN搜索。设计位宽裁剪缩短距离计算时延，过滤-选择混合策略适配任意k值，两级流水线并行计算与检索。实测相比SOTA BitNN提速4.17倍、能耗降低4.42倍，高精度场景精度损失可忽略。

## 背景和动机
1. 自动驾驶、SLAM等点云任务中kNN占总时延80%，欧式距离计算与Top-k检索计算密集、访存开销巨大。
2. 现有BitNN等位串行加速器片上/片外数据搬运占35%能耗，位串行乘法循环数多，距离计算延迟高。
3. 主流加速器固定并行Top-k单元，k值变化时硬件利用率失衡，小k闲置、大k多轮迭代拖慢速度。
4. 基于八叉树、kd树的近似方案会大幅损失检索精度，无法满足自动驾驶安全需求。

## 相关工作
1. GPU方案（PyG）：通用并行架构，点云不规则访存带宽利用率低，功耗极高。
2. 树类专用加速器QuickNN/ParallelNN：依赖空间划分近似，精度下降明显，预处理开销大。
3. BitNN位串行存内加速器：基础BS-PIM架构，但无位宽裁剪，Top-k固定并行单元，k可变场景性能差。
4. JUNO等近似NN加速器：面向高维数据，不适用于三维点云精确kNN检索。

## 本文解决方案
### 1 完整BS-PIM存内计算硬件架构
多核心+PE分层设计，6T-SRAM位串行阵列原位完成坐标差、平方、累加，大容量片上缓存消除运行时片外访存。
### 2 位宽裁剪优化距离计算
利用近点距离低位即可区分的特性，截断高位做近似平方运算，大幅减少位串行操作，仅带来可忽略精度损耗。
### 3 过滤-选择混合Top-k检索
k较小时迭代最小值搜索；k较大时二分动态阈值过滤，少量修正补齐精确k，实现近似常数复杂度检索。
### 4 两级流水线并行机制
距离计算阶段与Top检索阶段流水执行，搭配快速阈值表加速二分收敛，掩盖单阶段延迟、提升吞吐。

## 实验分析
1. 实验配置：28nm工艺，分小/大两种PICK硬件规格；KITTI/SONN/S3DIS/DALES四类真实点云数据集。
2. 精度表现：合理裁剪位宽下检索精度超99.999998%，自动驾驶场景几乎无误差。
3. 性能能耗：对比BitNN平均提速4.17倍、能耗节省4.42倍；位宽裁剪单独带来2.74倍加速收益。
4. 访存优化：运行时无片外数据读写，片外访问量相较BitNN降低70%以上。
5. 消融实验：位宽裁剪是核心优化，k增大后过滤策略增益显著，快速阈值进一步缩短二分迭代周期。

## 研究启发
1. 点云kNN无需完整16bit距离参与排序，利用近邻数值低位特征做位宽裁剪是低成本提速思路。
2. 固定并行Top-k硬件无法适配多变k值，分大小k混合检索策略可平衡硬件利用率与延迟。
3. 位串行SRAM存内计算适合低精度几何运算，原位计算能彻底消除重复片外点云数据搬运。
4. 流水线解耦距离计算与Top检索可充分利用PE阵列并行资源，掩盖单阶段瓶颈延迟。
5. 面向自动驾驶等安全场景，存内计算硬件优化可在无损精度前提下大幅降低边缘端时延与功耗。
