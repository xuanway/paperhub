---
title: "BlasPart: A Deterministic Parallel Partitioner for Balanced Large-Scale Hypergraph Partitioning"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# BlasPart: A Deterministic Parallel Partitioner for Balanced Large-Scale Hypergraph Partitioning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://numbda.cs.tsinghua.edu.cn/papers/dac251.pdf">https://numbda.cs.tsinghua.edu.cn/papers/dac251.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 平衡划分，确定性并行，大规模超图划分，多层二分法 </p>
</div>


---

## 研究概要
本文提出BlasPart确定性并行超图划分工具，采用两阶段递归二分框架，设计层级自适应平衡约束策略适配大规模多分块场景。区分并行/串行二分流程保证结果确定，优化孤立顶点分配与多解筛选规则。在工业与标准超图测试，4096分块下较Mt-KaHyPar-SDet平均提速3.33倍，划分平衡性显著更优，割质量接近串行hMETIS。

## 背景和动机
1. 现代VLSI、稀疏矩阵、SAT问题超图规模数十亿节点，需要大规模k路划分，传统工具并行时存在非确定性，EDA流程会导致后端重复迭代。
2. 现有确定性并行划分器Mt-KaHyPar-SDet仅约束分块上限，大量场景失衡率超标；BiPart每层采用严格统一平衡系数，割代价大幅上升。
3. 直接k路并行工具随分块数增加运行时间近似指数增长，扩展性差，难以支撑4096等高并行度划分需求。
4. 递归二分传统固定平衡约束对高层二分过于严苛，为满足全局均衡牺牲割优化空间，划分质量下降。
5. 大规模超图存在大量孤立无连接顶点，现有划分器未利用其灵活分配特性优化负载均衡。

## 相关工作
1. 串行多级划分hMETIS/PaToH：划分质量高但无并行加速，超大图耗时难以接受。
2. 非并行流/谱划分HyperSF/SpecPart：精度尚可，完全不支持多核并行。
3. 非确定并行划分Zoltan/Parkway：多核加速，但每次划分结果不同，不满足芯片设计可复现需求。
4. BiPart首款确定并行划分：每层统一严苛平衡系数，割开销高，并行扩展能力弱。
5. Mt-KaHyPar-SDet主流确定并行方案：仅限制分块容量上限，大量测试集失衡突破阈值，k增大后时间膨胀严重。

## 本文解决方案
### 1 两阶段递归二分并行框架
前log(p)层多线程并行二分，快速粗分原图；剩余层级串行二分处理小型子超图，并行瓶颈集中在前序阶段，子图计算开销逐层递减。所有任务按ID排序输出，保证全局确定性。
### 2 层级自适应平衡约束
高层二分放宽上下界约束，底层收紧匹配全局失衡阈值ε；若层级均衡约束无解则强制均分，同时孤立顶点延迟分配至最小分块优化负载。
### 3 串行/二分双流程适配
并行阶段采用并行粗化+多初始解并行求精；串行阶段复用hMETIS成熟FC聚类、GHG初始划分与贪心求精，舍弃不稳定FM算法保证耗时稳定。
### 4 均衡导向多解筛选规则
割值相同时优先选取均衡度更优划分；求精阶段接受零增益但改善负载的顶点移动，同步降低割与失衡双重指标。
### 5 大规模扩展性优化
前序阶段计算量不随k线性膨胀，后序每层子图规模减半，总计算量对数级增长，适配上千分块工业电路超图。

## 实验分析
1. 实验环境：AMD EPYC 64核服务器，Titan23电路、WB/NLPK/SAT/工业6组超大超图，基线hMETIS、BiPart、Mt-KaHyPar-SDet，ε=0.1。
2. 质量对比：相较串行hMETIS平均割值仅高2%；对比Mt-KaHyPar-SDet，高k场景割更优，且绝大多数基准失衡率严格控制在0.1以内。
3. 运行效率：k=4096时比Mt-KaHyPar-SDet平均提速3.33倍，BiPart耗时可达数倍；线程数提升可稳定加速，NLP基准16线程加速6.25倍。
4. 均衡指标：Mt-KaHyPar-SDet在NLPK等基准失衡最高达0.998，BlasPart绝大多数控制≤0.1，仅SAT少量工况0.179。
5. 消融验证：层级自适应约束、孤立顶点后分配、并行有序输出三大模块分别显著提升均衡、降低割、保证确定性。

## 研究启发
1. 递归二分搭配层级可变平衡约束，是大规模高k超图兼顾割质量与分块均衡的有效方案。
2. 并行划分必须严格固定任务输出顺序，才能满足EDA等对结果可复现的硬性需求。
3. 直接k路并行划分时间随分块数快速膨胀，分层二分框架扩展性优势明显。
4. 孤立顶点无需参与前期划分，后置负载调配可在不增加割代价前提下大幅改善均衡度。
5. 并行粗化与串行求精分阶段设计，可平衡多核加速收益与小规模子图求解稳定性。
