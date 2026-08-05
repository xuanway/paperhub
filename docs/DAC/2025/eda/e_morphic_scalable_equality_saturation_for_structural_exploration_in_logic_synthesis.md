---
title: "E-morphic: Scalable Equality Saturation for Structural Exploration in Logic Synthesis"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# E-morphic: Scalable Equality Saturation for Structural Exploration in Logic Synthesis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.11574">https://arxiv.org/abs/2504.11574</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 等式饱和，逻辑综合，结构探索，模拟退火提取 </p>
</div>


---

## 研究概要
本文提出E-morphic可扩展等式饱和逻辑综合框架，解决传统e-graph工具规模受限、提取易陷入局部最优问题。设计DAG直转、解空间剪枝、模拟退火多线程提取、GNN快速代价评估四大核心技术。EPFL基准测试相较工业延迟优化流程，平均面积缩减12.54%、延迟降低7.29%，大电路无超时崩溃。

## 背景和动机
1. 传统ABC重写存在结构偏差，初始AIG拓扑直接决定映射结果，难以探索等价优质电路结构，仅少量等价节点可供选择。
2. 现有E-Syn等e-graph工具依赖S表达式中间层，大电路转换内存/时间爆炸，4万以上e节点即超时，无法处理大规模设计。
3. e-graph标准贪心提取易陷入局部最优，无法跳出次优拓扑，缺乏全局搜索机制平衡面积与时序。
4. 每次提取完整工艺映射评估耗时极高，缺少轻量预测模型加速海量候选拓扑筛选。
5. 等式饱和迭代后冗余等价节点泛滥，全量遍历提取计算开销巨大，缺少剪枝手段。

## 相关工作
1. ABC传统逻辑重写：基于局部变换，等价结构探索能力弱，存在严重结构偏差。
2. E-Syn等式饱和综合：依赖S表达式做电路与e-graph转换，大规模电路内存溢出、运行超时。
3. egg基础e-graph库：仅提供基础重写框架，无面向综合的高效提取、剪枝策略。
4. 基于SA的表达式优化：未适配AIG电路DAG结构，不支持多层时序/面积代价联合优化。
5. HOGA电路GNN：仅用于拓扑预测，未嵌入e-graph饱和提取流水线。

## 本文解决方案
### 1 无中间层DAG直转机制
摒弃S表达式序列化冗余开销，设计专用DSL直接完成AIG与e-graph双向映射，节点一一对应，百万级电路转换秒级完成，规避内存溢出。
### 2 解空间剪枝提取算法
维护每等价类最小代价缓存队列，跳过高冗余e节点，仅遍历具备优化潜力单元，大幅削减提取遍历规模。
### 3 模拟退火多线程并行提取
自底向上生成初始拓扑，Metropolis准则允许代价小幅上升跳出局部最优；多线程并行生成多候选解，择优输出。
### 4 双模式代价评估体系
1）质量模式：调用ABC标准单元映射精确评估面积延迟；2）速度模式：HOGA GNN快速预测拓扑代价，大幅减少完整映射次数。
### 5 完整综合插入流程
放置于工艺无关优化与工艺映射中间，少量饱和迭代生成多等价拓扑，完成重综合后再执行单元映射，缓解结构偏差。

## 实验分析
1. 实验环境：双Xeon服务器256G内存，Rust实现对接egg，EPFL大小混合基准，ASAP7nm工艺，对比ABC工业延迟优化流、E-Syn。
2. 转换效率：E-Syn数万节点即超时，E-morphic百万节点双向转换均在数秒内完成。
3. QoR指标：相较基线，全部电路延迟下降，平均面积-12.54%、延迟-7.29%；启用GNN后总运行时间平均缩减28%。
4. 规模适配：hyp等超大电路无内存溢出，仅小幅增加综合总耗时，开销可控。
5. 消融验证：DAG直转、剪枝、SA并行、GNN四项技术缺一不可，任一移除指标大幅退化。

## 研究启发
1. 等式饱和落地逻辑综合的核心瓶颈是图转换效率，去除S表达式冗余层才能支撑大规模工业电路。
2. 贪心提取天然存在局部最优缺陷，模拟退火随机扰动是低成本全局拓扑探索方案。
3. 解空间剪枝可过滤大量无收益等价节点，在不损失QoR前提下显著降低提取耗时。
4. GNN轻量代价预测可作为完整工艺映射的前置筛选，平衡优化质量与运行速度。
5. 在工艺无关优化与映射间插入e-graph重综合，是消除拓扑结构偏差的有效标准流程改造方案。
