---
title: "iG-kway: Incremental k-way Graph Partitioning on GPU"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# iG-kway: Incremental k-way Graph Partitioning on GPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132904">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132904</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 增量k路图划分，GPU并行，增量感知数据结构，分区平衡，并行细化</p>
</div>

---

## 研究概要
本文提出首个GPU增量k路图划分器iG-kway，面向CAD动态电路图迭代优化。设计桶列表GPU原生图存储、伪分区均衡与并行细化内核，仅修改受影响顶点。工业与DIMACS图测试，相较全重划分G-kway平均提速84倍，切割质量基本持平。

## 背景和动机
1. RTL时序优化、仿真等CAD流程需上万次迭代动态图修改，传统GPU划分器仅支持全图重划分，每次重构CSR开销极大。
2. CSR静态数组不支持GPU原位增删顶点/边，修改需CPU重建并迁移数据，迭代场景时延爆炸。
3. 动态修改后分区失衡，现有细化内核遍历全部边界顶点，无法限定局部受影响区域。
4. CPU增量划分方案无法适配GPU大规模并行架构，线程负载不均、同步开销高。

## 相关工作
1. G-kway/Jet等GPU全图划分：多级并行划分性能优异，但无增量更新能力，每次迭代重建图结构。
2. Metis/mt-metis：CPU多级划分，大图单次划分耗时数分钟，迭代场景不可用。
3. CPU增量划分IOGP/LP方案：面向分布式数据库或串行求解，不兼容GPU线程并行模型。
4. 传统GPU细化算法：遍历全部边界顶点，未区分修改带来的局部影响，冗余计算多。

## 本文解决方案
### 1 约束粗化全图预处理
改进G-kway合并策略，按迭代标签分组粗化顶点，均衡粗块权重，保障初始划分切割质量。
### 2 桶列表GPU动态图结构
对齐32线程warp预分配存储，原位增删顶点/边，无需重建数组；利用warp原语快速检索空槽，消除CPU-GPU数据迁移。
### 3 增量分区均衡机制
新增伪分区缓存受影响顶点，区分直接修改点与邻接扰动点，过滤无优化价值顶点，集中至统一缓冲区均衡GPU线程负载。
### 4 无冲突并行细化内核
筛选互不相邻顶点并行迁移，分段扫描约束分区权重，批量执行顶点重分配，在控制切割损失前提下并行降割。

## 实验分析
1. 测试环境：A6000 GPU，10组工业电路+DIMACS大图，每组执行100轮增量迭代，基线为每次全重划分G-kway†。
2. 速度表现：平均提速84倍，k=2最高98倍；划分分块数k越大、单轮修改顶点越多，加速比略有下降。
3. 划分质量：切割值与基线差距±3%，迭代越多优势越明显。
4. 扩展性：单轮修改量50以内收益最大；单次修改超原图50%时增量收益衰减，建议切换全划分。
5. 硬件开销：桶列表预分配内存可控，warp原语大幅降低分支发散，修改阶段耗时几乎不随图规模增长。

## 研究启发
1. GPU动态图处理不能依赖CSR静态存储，对齐warp的预分配桶结构可实现原位增量更新。
2. 增量划分核心是限定受影响顶点，避免全图边界遍历，伪分区机制能同时解决失衡与负载不均问题。
3. 并行顶点迁移需规避相邻顶点同步冲突，筛选独立顶点批量执行可大幅减少同步代价。
4. CAD迭代优化场景专用增量划分相比反复全重划分存在数量级性能优势。
5. 算法预处理粗化质量直接决定增量细化上限，初始均衡划分能降低迭代切割损失。
