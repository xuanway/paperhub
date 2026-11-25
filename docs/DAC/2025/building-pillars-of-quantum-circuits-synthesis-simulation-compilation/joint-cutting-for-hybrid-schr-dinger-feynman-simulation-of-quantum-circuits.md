---
title: "Joint Cutting for Hybrid Schrödinger-Feynman Simulation of Quantum Circuits"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Joint Cutting for Hybrid Schrödinger-Feynman Simulation of Quantum Circuits


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.06959">https://arxiv.org/abs/2502.06959</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>量子计算，经典模拟，混合薛定谔-费曼，联合切割，电路切割 </p>
</div>


---

## 研究概要
本文提出联合切割Joint Cutting混合薛定谔-费曼(HSF)量子电路仿真方法。将跨分区门合并为块统一施密特分解，抑制路径数量指数爆炸。基于QAOA电路测试，相较标准HS最高提速4000倍，相比纯薛定谔仿真最高快200倍，开源实现已发布。

## 背景和动机
1. 纯薛定谔仿真存储随量子比特指数增长，大规模电路硬件无法承载；HSF通过电路分块降低内存，但切割门会产生指数级仿真路径，运行开销极高。
2. 现有标准HS对每个跨分区门单独分解，路径数为各门施密特秩乘积，深电路仿真超时不可用。
3. 两量子门级联电路单独切割开销巨大，缺少块级联合分解策略；门合并矩阵乘与SVD预处理的权衡机制缺失。
4. 主流QAOA等优化电路存在大量可合并纠缠门，现有HS未利用块结构削减路径，仿真效率严重受限。

## 相关工作
1. 标准薛定谔仿真：直接向量矩阵运算，精度高但2^n内存开销，30比特以上难以运行。
2. 传统HSF仿真：逐门施密特切割分块降内存，路径指数膨胀，深电路失效。
3. 量子电路切割QCC：硬件运行时分块，采用准概率分解，与HSF矩阵分解目标不同。
4. 张量网络、决策图仿真：通过张量收缩压缩存储，未结合HSF分块切割优化路径数量。

## 本文解决方案
### 1 门块联合施密特分解
将同一切割线的连续跨分区门合并为整体酉矩阵，统一SVD做施密特分解；单块路径数由分区维度上限约束，不再随门数指数增长。
### 2 门块筛选策略
针对RZZ、CNOT级联等可交换门自动聚合为块；控制块规模，平衡矩阵相乘+SVD预处理开销与路径削减收益。
### 3 混合仿真流水线
分预处理（门融合+联合分解生成路径）、并行多路径子电路仿真、结果克罗内克叠加三步。
### 4 解析分解加速
对CNOT、RZZ级联等标准门链推导解析分解式，跳过数值SVD，大幅降低预处理耗时。

## 实验分析
1. 测试平台：16核AMD CPU，基于Google qsim改造，数据集为不同规模MaxCut QAOA电路。
2. 路径优化：标准HS路径随门数暴涨，联合切割路径收敛至固定上限，大量测试用例路径缩减上千倍。
3. 速度对比：相较标准HS平均提速数百至4000倍；相比纯薛定谔仿真最高提速200倍，超时电路可正常完成。
4. 预处理开销：小规模门块融合代价极低，仅深超大块才会抵消路径收益。
5. 通用性：适配QA、多体动力学、量子优势采样等结构化电路，稠密深层电路收益有限。

## 研究启发
1. HSF仿真瓶颈是逐门切割带来指数路径，块级联合分解是抑制路径爆炸核心手段。
2. 门合并预处理存在开销边界，需控制块大小实现预处理与仿真耗时权衡。
3. 可交换两量子门级联是联合切割最优场景，解析分解能完全规避数值SVD成本。
4. 分块仿真算法需结合电路结构优化，结构化量子算法（QAOA）可获得巨大加速。
5. 联合切割与QCC思路同源，但HSF面向经典仿真矩阵分解，无需准概率采样，实现约束更低。
