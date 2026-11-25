---
title: "Swift or Exact? Boosting Efficient Microarchitecture DSE via Multi-fidelity Partial Order Prediction"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Swift or Exact? Boosting Efficient Microarchitecture DSE via Multi-fidelity Partial Order Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133073">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133073</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多保真度优化，贝叶斯优化，设计空间探索，偏序预测，微架构设计</p>
</div>


---

## 研究概要
本文提出基于偏序预测的多保真贝叶斯微架构DSE框架，针对架构/RTL/网表三级EDA流程非线性偏差问题。构建非线性高斯融合模型，利用逻辑回归预测PPA排序反转，自适应选择仿真保真度。RISC-V BOOM/Rocket测试，帕累托超体积提升12.9%，收敛速度提升48%，ADRS指标降低57.7%。

## 背景和动机
1. 微架构DSE依赖多级EDA仿真，架构低保真仿真速度快但PPA排序失真，网表高保真精度高但耗时数千CPU小时，全局探索效率极低。
2. 现有多保真DSE多假设高低保真呈线性关联，而芯片面积、功耗、周期指标存在强非线性映射，模型拟合误差大。
3. 传统方法无保真度自适应决策，全部候选都跑完三级仿真，大量低价值样本浪费仿真算力。
4. 多目标帕累托优化缺少排序可信度判断机制，低保真预测颠倒支配关系会遗漏最优硬件配置。

## 相关工作
1. 线性多保真GP（FPL’18）：假设高低保真线性映射，无法适配VLSI多级非线性PPA偏差，探索效果差。
2. 单非线性多目标框架（DATE’21）：仅融合多保真数据，缺少保真度自适应调度，仿真开销巨大。
3. 知识梯度单步寻优（ICML’23）：无偏序支配预测，无法判断低保真结果可信度。
4. 单保真主动学习DSE（ICCAD’21）：全程使用高保真网表仿真，算力消耗极高，大规模参数空间不可行。
5. 信任权重多目标优化（MLST’24）：未针对EDA多级仿真设计自适应保真跳转策略。

## 本文解决方案
### 1 非线性多保真高斯代理模型
将低保真PPA作为输入特征，搭建分层GP拟合三级仿真非线性映射，融合架构、RTL、网表全部采样数据，精准修正低保真预测偏差。
### 2 逻辑回归PPA反转预测器
训练分类模型预测高低保真之间指标排序反转概率，量化当前样本与帕累托前沿点的支配可信度，判断是否需要升级保真仿真。
### 3 多目标偏序判定调度策略
定义多目标支配偏序关系；若预测会出现偏序翻转则进入更高保真仿真，无支配变化则直接终止该样本评估，大幅削减网表仿真量。
### 4 EHVI采集函数引导采样
采用期望超体积提升函数平衡探索/利用，优先选取能扩充帕累托前沿的参数配置，提升同等算力下搜索质量。

## 实验分析
1. 实验平台：Chipyard+Gem5+Synopsys EDA，7nm ASAP7工艺，测试BOOM(20参数)、Rocket(8参数)两款RISC-V核。
2. 指标对比：同等600分钟预算，平均帕累托超体积提升12.9%，ADRS下降57.7%，收敛速度提升48%。
3. 仿真开销：自适应策略大幅减少高保真网表仿真时长，相比线性/单保真方案总仿真时间显著降低。
4. 帕累托质量：所得前沿覆盖范围更广，在功耗、面积、周期三维空间更贴近真实最优解集。
5. 消融：非线性GP与偏序预测为两大核心增益，缺失任意一项均大幅削弱探索效率。

## 研究启发
1. VLSI多级仿真存在强非线性，线性多保真模型无法准确修正低保真偏差，分层非线性GP是拟合关键。
2. 多目标DSE瓶颈不在采样算法，而在无差别高保真仿真，基于排序可信度的自适应保真调度可大幅节约算力。
3. 帕累托支配偏序可作为保真度切换核心判断依据，无需完整指标精确预测，仅判断相对排序即可。
4. 多保真融合与多目标采集函数必须协同设计，单一优化难以同时提升收敛速度与前沿完备性。
5. 面向芯片EDA的DSE不能直接复用通用多保真优化算法，需贴合架构-RTL-网表三级流程定制调度逻辑。
