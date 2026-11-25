---
title: "Centralized Training and Decentralized Control through the Actor-Critic Paradigm for Highly Optimized Multicores"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Centralized Training and Decentralized Control through the Actor-Critic Paradigm for Highly Optimized Multicores

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133176">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133176</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 集中式训练，分散式控制，强化学习，温度感知多核优化 </p>
</div>


---

## 研究概要
本文提出集中训练分布式执行的Actor-Critic多核热控DVFS框架，多Actor分应用独立控频，全局Critic评估交互收益，解决分布式控制器观测不全、决策冲突、热耦合干扰问题。基于真实i9处理器测试，相较TP-DQL、Profit平均性能提升20%、24%，峰值提升34%、65%，热违规极少且开销极低。

## 背景和动机
1. 集中式RL资源控制器求解空间随核心数指数膨胀，推理延迟高，不适用于大规模多核。
2. 分布式单智能体控制器仅局部观测，存在信用分配难题，核心热耦合造成决策相互干扰，易出现控频反向升温。
3. 现有分层分布式方案需每轮调用中央仲裁，控制环路延迟敏感，实时性差。
4. 传统多智能体仅共享经验池，缺少全局收益评估，各控制器仅优化本地性能，全局热预算利用率低。
5. 真实开放系统负载动态多变，现有方法泛化弱，无法适配未知多线程应用并发场景。

## 相关工作
1. 集中式RL DVFS：单控制器全局决策，求解规模爆炸，仅适合小规模核心平台。
2. 单核心分布式DQL（TP-DQL）：各核心独立网络，仅本地奖励，忽略跨核热耦合，全局性能受限。
3. 分层Q学习Profit：中央仲裁分配功率预算，仅适配功耗约束，无法处理时空热耦合场景。
4. 自组织多智能体：智能体直接通信交互，频繁数据交换引入大量控制开销。
5. 时序分类LSTM控频：设计时固定模型，动态新负载下泛化能力不足。

## 本文解决方案
### 1 集中训练分布式执行AC架构
每个应用对应独立Actor网络，运行阶段并行独立输出频率；训练阶段汇总所有智能体观测送入全局Critic，离线计算全局价值指导策略更新，运行无中央仲裁交互。
### 2 全局几何均值奖励函数
以多应用IPS几何均值为基础奖励，任意核心超温施加统一惩罚，兼顾系统整体吞吐与公平性，约束全局热上限。
### 3 复合全局Critic状态表征
融合本地观测、其余智能体平均/最大频率、并发应用总数，完整建模跨核热耦合与负载交互关系，采用TD(λ)与目标网络稳定价值估计。
### 4 反事实优势策略梯度更新
基于全局价值计算动作优势，搭配熵正则平衡探索利用，智能体间权重共享降低存储开销。
### 5 轻量实时部署方案
控制周期10ms，每1.3s执行一次集中训练；推理开销仅5.7%，训练开销1.6%，经验缓冲区总内存不超20KB。

## 实验分析
1. 实验环境：Intel i9-12900KF 8性能核，PARSEC/SPLASH-2混合负载，应用到达率2~10/分钟，75℃热阈值，对比TP-DQL、Profit。
2. 性能收益：相较TP-DQL平均性能+20%、峰值+34；相较Profit平均+24%、峰值+65；高并发场景优势收窄。
3. 热稳定性：探索阶段少量违规，利用阶段违规近乎归零，充分利用芯片热预算。
4. 运行开销：单次Actor推理565μs，集中训练单次20ms，内存相较TP-DQL降低99%。
5. 收敛特性：前1小时快速探索收敛，后续持续适配动态负载，损失曲线震荡后稳定低位。

## 研究启发
1. 分布式实时控制无需运行时全局通信，集中式离线训练是平衡实时性与全局最优的有效范式。
2. 多核热耦合属于全局强约束，仅本地观测、本地奖励的单智能体无法实现最优资源分配。
3. 几何均值奖励可兼顾系统吞吐与应用公平，适合多竞争共享资源调度场景。
4. 轻量AC网络、短轨迹缓存能大幅降低多智能体内存与运行开销，适配真实CPU内核部署。
5. 反事实优势函数可精准解决分布式控制器信用分配问题，量化单一频率调整的全局影响。