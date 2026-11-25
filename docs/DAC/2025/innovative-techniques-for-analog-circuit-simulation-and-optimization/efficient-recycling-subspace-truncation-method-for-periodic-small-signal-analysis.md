---
title: "Efficient Recycling Subspace Truncation Method for Periodic Small-Signal Analysis"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Efficient Recycling Subspace Truncation Method for Periodic Small-Signal Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133327">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133327</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>射频仿真，周期小信号分析，子空间截断  </p>
</div>


---

## 研究概要
本文面向射频周期小信号仿真提出Krylov子空间截断复用框架，基于Floquet理论设计子空间筛选策略，搭配最优初值复用方法。解决大规模电路频扫时子空间膨胀、内存溢出、迭代过多问题。工业射频电路测试，同等内存上限下相较GCRO-DR最高提速2.65倍，矩阵向量乘次数显著减少。

## 背景和动机
1. 周期PAC/PNoise频扫需求求解大量移位线性方程组，传统R-GCR/R-GMRES通过复用Krylov子空间加速，但电路规模增大后子空间维度爆炸，内存成为新瓶颈。
2. 简单重启复用算法会丢失有效收敛向量，导致迭代次数暴增，仿真效率大幅下滑。
3. 通用GCRO-DR截断策略无电路周期性特征引导，仅按最小Ritz值保留向量，射频周期系统收敛提升有限。
4. 现有初值复用直接复用前次解，未做最优加权，初始残差偏大，每频点迭代开销高。
5. 周期系统转移矩阵Floquet乘子特征未被现有复用算法利用，缺少针对性子空间筛选依据。

## 相关工作
1. R-GCR/R-GMRES周期复用算法：可复用子空间加速频扫，但无截断机制，大规模电路内存溢出。
2. GCRO-DR通用子空间截断：面向普通线性方程组，未结合Floquet周期特性，射频场景收敛提升有限。
3. 通用GMRES/重启GMRES：无跨频点子空间复用，每个频点从零迭代，总计算量极高。
4. 周期稳态PSS仿真工具：仅求解工作点，未配套小信号频扫加速求解器。
5. 传统SPICE类周期小信号求解：直接LU分解，频点线性增加耗时，无法适配大规模射频设计。

## 本文解决方案
### 1 整体子空间截断复用框架
统一兼容R-GCR、R-GMRES两类复用内核，设置子空间维度硬上限；每频点求解前后执行截断，超出上限自动重启，控制内存占用。
### 2 最优初值复用算法
引入复加权系数α最小化当前频点初始残差，仅通过内积运算求解α，无需额外矩阵向量乘，大幅降低单频点迭代起步开销。
### 3 基于Floquet理论的子空间截断策略
利用周期转移矩阵乘子分布特征，通过QZ广义特征分解提取对应最大Floquet乘子的Ritz特征向量，优先保留对收敛关键向量，丢弃无效维度。
### 4 移位线性系统标准化预处理
基于改进节点法MNA离散周期DAE方程，预分解L对角块，化简为标准移位矩阵形式，降低每次矩阵向量乘计算代价。
### 5 频扫迭代完整调度流程
线性/十倍频两种扫序适配；截断、初值计算、Krylov扩充、残差校验形成闭环，收敛达标后切换下一频点。

## 实验分析
1. 实验环境：MATLAB实现，4套工业射频电路，不同时间步离散方案，残差收敛阈值1e-8，对比GCRO-DR。
2. 特征验证：测试电路PM矩阵最大特征值接近1，存在多枚近1乘子，匹配Floquet理论预判。
3. 初值效果：对比零初值、直接复用前解，本文加权初值全频区间迭代数明显下降。
4. 截断对比：Floquet筛选相比DR截断无迭代尖峰，低频恶劣场景优势突出。
5. 整体效率：相同内存约束下，十倍频扫最高提速2.65倍，线性频扫最高2.53倍，矩阵向量乘总量大幅缩减。

## 研究启发
1. 周期射频电路求解不能套用通用线性方程组截断方案，必须结合Floquet乘子周期特性筛选子空间。
2. 简单复用前次解作为初值存在缺陷，加权最小残差初值可极低代价减少整体迭代轮次。
3. 设置固定子空间维度上限是解决大规模射频仿真内存瓶颈的可行路径，搭配定向截断可规避重启性能损失。
4. Krylov复用加速的核心瓶颈在子空间存储，定向筛选向量可在内存与迭代次数间取得良好权衡。
5. 周期小信号仿真可标准化为统一移位方程组，专用子空间复用框架能显著降低EDA射频签核耗时。
