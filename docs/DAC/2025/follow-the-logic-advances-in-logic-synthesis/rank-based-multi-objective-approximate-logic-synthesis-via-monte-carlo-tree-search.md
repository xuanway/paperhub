---
title: "Rank-based Multi-objective Approximate Logic Synthesis via Monte Carlo Tree Search"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Rank-based Multi-objective Approximate Logic Synthesis via Monte Carlo Tree Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132589">https://ieeexplore.ieee.org/document/11132589</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 近似逻辑综合，多目标优化，蒙特卡洛树搜索，排序变换器 </p>
</div>


---

## 研究概要
本文提出基于蒙特卡洛树搜索的排序型多目标近似逻辑综合框架，设计电路非支配排序划分解空间，构建Rank-Transformer预测局部近似变换LAC优劣。在ER、NMED两类误差约束下，相比主流方法平均延时降低25.51%~29.84%、面积缩减15.93%~23.24%，整体运行速度提升1.19~4.16倍。

## 背景和动机
1. 现有近似逻辑综合分为延时优先、面积优先两类单目标算法，难以同时优化延时与面积，极易陷入局部最优帕累托解。
2. 进化、贝叶斯多目标算法求解空间庞大，大规模电路迭代开销极高，收敛速度慢。
3. 传统MCTS依赖精准电路性能模型，复杂电路建模误差大，搜索易偏移优质优化区域。
4. 筛选局部近似变换LAC需多次时序仿真评估，逐条验证耗时严重，缺少快速优劣预测手段。
5. 全局与局部LAC搜索策略失衡，延时类仅聚焦关键路径，面积类遍历全电路，无法兼顾双向优化收益。

## 相关工作
1. 延时驱动ALS（HEDALS/TCAD24/DCGWO）：仅围绕关键路径做近似变换，面积优化幅度有限。
2. 面积驱动ALS（VECBEE-SASIMI）：全局贪心删减门，时序性能损失严重。
3. 多目标进化/贝叶斯优化：迭代仿真成本极高，工业电路落地效率低。
4. LAMOO-MCTS：依赖精准电路性能模型，复杂电路建模偏差导致搜索失效。
5. 传统LAC贪心筛选：每条变换均调用STA时序分析，迭代时间成本巨大。

## 本文解决方案
### 1 电路域非支配排序拆分策略
基于帕累托层级+拥挤距离对近似电路分级，划分优劣叶子集合，指导MCTS树拆分，无需精准性能模型即可筛选高潜力优化样本。
### 2 UCT多目标叶子选择函数
融合超体积HV、平均误差加权计算置信上限，优先选取延时/面积均衡、误差合规的电路分支迭代。
### 3 Rank-Transformer路径LAC预测模型
提取完整/截断/剩余三类路径特征，跨路径注意力融合嵌入，联合MSE+成对排序损失预测LAC优化收益，省去大量STA仿真。
### 4 分层LAC采样机制
前期以延时优化变换为主，迭代收敛困难时切换面积优先贪心变换，兼顾双向优化目标。
### 5 完整MCTS近似综合流水线
初始样本生成→排序拆分→叶子选择→Transformer预测采样→性能评估反向传播迭代。

## 实验分析
1. 测试基准：ISCAS85、EPFL算术电路，TSMC28nm工艺，对比HEDALS、TCAD24、DCGWO、VECBEE-S。
2. 优化收益：3%误差率下平均延时降29.84%、面积减23.24%；1.96%NMED下延时降25.51%、面积减15.93%。
3. 帕累托质量：128乘法器基准最优解集完全支配所有对比算法的前沿解。
4. 运行效率：平均迭代耗时33.90分钟，相较基线提速最高4.16倍，时序仿真占比大幅降低。
5. 消融验证：电路排序、Rank-Transformer两大模块缺失后，优化幅度与运行速度显著恶化。

## 研究启发
1. 多目标近似综合不能单一时序或面积导向，需全局帕累托排序划分搜索空间提升解质量。
2. Transformer路径排序预测可替代海量STA仿真，大幅削减LAC筛选的时序评估开销。
3. MCTS搭配分层变换采样，可动态平衡延时、面积两类优化目标，适配不同误差约束场景。
4. 无依赖精准电路模型的排序策略，能规避复杂电路建模误差带来的搜索失效问题。
5. 近似综合迭代瓶颈在于时序仿真，通过模型预测预筛选候选变换是提速核心思路。
