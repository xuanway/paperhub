---
title: "Logic Optimization Meets SAT: A Novel Framework for Circuit-SAT Solving"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Logic Optimization Meets SAT: A Novel Framework for Circuit-SAT Solving

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2403.19446">https://arxiv.org/abs/2403.19446</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 电路SAT求解，逻辑综合，强化学习，查找表映射 </p>
</div>


---

## 研究概要
本文面向电路可满足性CSAT提出EDA协同预处理框架，将逻辑综合建模为强化学习MDP，设计以SAT分支复杂度为目标的定制LUT映射。工业LEC/ATPG基准测试，搭配Kissat、CaDiCaL求解器，总求解时长最高降低63%，可无缝兼容主流CDCL SAT工具。

## 背景和动机
1. 主流SAT求解器适配CNF格式，电路直转CNF会破坏原生拓扑，产生大量冗余子句，CSAT求解耗时爆炸。
2. 现有电路预处理仅优化面积/延迟，不面向SAT分支复杂度，无法减少求解器分支搜索开销。
3. 传统逻辑综合流程固定，依赖人工编排变换序列，难以针对不同电路自适应生成最优化简方案。
4. 标准LUT映射以面积为代价函数，XOR等高分支成本逻辑未被抑制，生成实例求解难度偏高。
5. 缺少融合电路表征学习与强化学习的自动化预处理流水线，工业大规模电路验证效率受限。

## 相关工作
1. CNF预处理算法：基于消解、变量消去简化子句，不利用电路AIG原生拓扑，优化上限低。
2. 传统电路预处理：仅做面积最小化综合，未考虑SAT分支开销，无法缩短求解时间。
3. 固定流程逻辑综合：rewrite/refactor等操作顺序人工固定，无自适应决策机制。
4. 标准LUT映射：代价函数以面积、延迟为主，忽略不同LUT带来的SAT分支复杂度差异。
5. 电路表征DeepGate系列：提取门电路拓扑嵌入，但未结合RL优化SAT专用综合流程。

## 本文解决方案
### 1 整体EDA预处理流水线
输入AIG电路，RL智能体迭代选择综合操作化简，再执行分支感知LUT映射，最终转为轻量化CNF供给SAT求解器。
### 2 基于DQN的RL逻辑综合智能体
将综合序列建模MDP；状态融合电路规模特征+DeepGate预训练拓扑嵌入；动作集包含rewrite、balance等标准综合操作；奖励定义为SAT分支数减少量，训练自适应化简策略。
### 3 分支复杂度定制LUT映射
定义LUT分支代价：扇出取0/1时输入组合总数作为成本；修改映射工具代价函数，优先生成低分支开销4-LUT，抑制XOR类难求解逻辑。
### 4 AIG标准化转换模块
依托ABC工具统一各类电路至AIG格式，保证输入图结构统一，便于RL提取标准化电路特征。
### 5 LUT转CNF适配接口
完成映射后标准化编码，输出兼容Kissat、CaDiCaL的CNF文件，无需修改SAT求解器内核。

## 实验分析
1. 测试数据集：200组训练简易CSAT实例，300组工业LEC、ATPG难例，门规模60~24k。
2. 总耗时对比：基线管道总耗时19422s，同类电路预处理对比方案11073s，本文仅7179s，降幅63.03%。
3. 消融实验：随机综合序列相比RL智能体耗时上升11.95；传统面积LUT映射比定制分支映射耗时增加50.8%。
4. 求解器兼容性：Kissat、CaDiCaL两款主流工具均获得显著加速，无兼容性问题。
5. 扩展性：大规模多输入数据通路电路收益最明显，难XOR密集实例优化提升幅度最大。

## 研究启发
1. 电路优化目标不能仅局限PPA，面向SAT分支复杂度的专用综合可大幅削减验证计算开销。
2. 强化学习可自适应编排逻辑综合变换序列，替代人工固定流程适配多样化工业电路。
3. LUT映射代价函数需贴合后端求解特性，抑制高分支代价逻辑是降低CSAT难度关键手段。
4. 电路拓扑嵌入与RL结合，能充分利用AIG原生结构，弥补纯CNF预处理的信息丢失缺陷。
5. EDA前端逻辑处理与后端SAT求解协同设计，是提升等价检查、ATPG等验证任务效率有效路线。