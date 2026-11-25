---
title: "Mixed Structural Choice Operator: Enhancing Technology Mapping with Heterogeneous Representations"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Mixed Structural Choice Operator: Enhancing Technology Mapping with Heterogeneous Representations

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.12824">https://arxiv.org/abs/2504.12824</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 逻辑综合，技术映射，结构偏差，结构选择，异构表示 </p>
</div>


---

## 研究概要
本文提出混合结构选择算子MCH，融合AIG/XMG/MIG等异质逻辑图构建多选网络，按路径分层采用多策略生成等价候选，打通逻辑优化与工艺映射协同。ASIC映射面积降3.73%、延迟降8.94%；FPGA LUT映射刷新EPFL基准多项最优，同时可突破局部最优用于逻辑重构。

## 背景和动机
1. 传统综合将工艺无关优化与工艺映射割裂，单一逻辑图存在结构偏置，同等布尔函数映射PPA差异巨大。
2. 现有结构选择（DCH）仅基于单一图生成候选，无法复用XOR/多数图的结构优势，优化上限低。
3. 异构综合工具转换统一图后丢失多图优势，候选多样性不足，易陷入局部最优解。
4. 缺乏面向关键/非关键路径的分层候选生成策略，统一优化无法同时兼顾延迟与面积目标。
5. 现有方法无法在映射阶段动态评估多类逻辑结构的工艺代价，难以选出最优电路拓扑。

## 相关工作
1. 单一结构选择DCH/LCH：仅在AIG内部生成等价子图，不支持异质逻辑表示，结构偏置问题无法根治。
2. LSOracle异构综合：电路分段分别优化后统一转单一图，丢失多图原生结构收益。
3. E-Graph重写：等价图搜索空间大，大规模电路运行效率低下。
4. AIG/MIG/XMG独立优化：各工具单独运行，无统一候选网络供映射择优。
5. 常规工艺映射：仅基于输入单张逻辑图切割匹配，缺少多等价结构对比筛选机制。

## 本文解决方案
### 1 混合结构选择(MCH)异构候选网络
以AIG为基底一对一映射生成MIG/XMG/XAG等价图，原图与异构图共存作为可选代表/选择节点，完整保留各类图结构优势。
### 2 路径感知多策略候选生成算法
区分关键路径节点采用层数优先重写（优化延迟）；非关键路径基于MFFC执行面积优先化简，生成多样化等价子图候选，不替换原图仅做备选。
### 3 MCH协同工艺映射流程
将选择节点切割合并至原图节点候选切割集，映射时按面积/延迟目标排序切割，依据工艺库代价自动择优匹配ASIC单元或FPGA LUT。
### 4 基于MCH的迭代逻辑重构
以混合选择网络为中间载体，多轮跨图映射重构，持续跳出传统单一图的局部最优，同步优化节点数量与时序深度。
### 5 开源工具集成
在also综合工具实现MCH完整命令，兼容EPFL标准电路与ASAP7工艺库，支持面积/延迟均衡、时延优先、面积优先三类映射模式。

## 实验分析
1. 测试基准：EPFL组合电路集，ASAP7 7nm工艺ASIC、6输入FPGA LUT两种映射场景。
2. ASIC结果：均衡模式面积-3.73%、延迟-8.94%；时延优先延迟降20.35%；面积优先面积降21.02%，优于DCH基线。
3. FPGA结果：MCH刷新EPFL Best Challenge多条电路6-LUT最小节点记录，无需前置重优化即可提升结果。
4. 逻辑重构消融：MCH辅助图映射平均节点减11.56%、时序深度降18.59%，部分电路指标降幅超50%。
5. 开销对比：候选网络带来少量运行时间增加，大规模算术电路相较传统映射反而速度更快。

## 研究启发
1. 单一逻辑图存在固有结构偏置，必须共存多种异构等价图才能释放工艺映射最优潜力。
2. 关键路径与普通路径分层差异化优化，可同时兼顾时序与面积两类设计目标。
3. 逻辑优化不能独立于工艺库，把工艺代价引入候选筛选可实现前后端协同优化。
4. 混合选择网络可作为通用中间层，同时适配ASIC标准单元与FPGA LUT两类映射场景。
5. 传统单图优化极易陷入局部最优，多等价候选并行搜索是低成本提升综合QoR的有效路径。