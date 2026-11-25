---
title: "3D-Flow: Flow-based Standard Cell Legalization for 3D ICs"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# 3D-Flow: Flow-based Standard Cell Legalization for 3D ICs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132587">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132587</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 三维集成电路，标准单元合法化，网络流，最小位移 </p>
</div>

---


## 研究概要
本文提出3D-Flow，首款面向3D IC的网络流标准单元合法化工具。构建三维网格流图，采用分支定界搜索最短增广路径消解bin溢出；搭配消圈后优化降低最大位移。基于ICCAD22/23 3D布局基准测试，同等运行速度下平均位移降低13%、最大位移降低43%，线长增量更优。

## 背景和动机
1. 传统合法化算法仅在单层二维die内移动单元，无法利用3D堆叠垂直空间，单元位移量大、线长恶化严重。
2. 贪心类工具（Tetris/Abacus）按固定顺序挪动单元，易产生大幅偏移，高拥塞带/宏模块场景效果差。
3. 二维流合法化BonnPlaceLegal仅支持同层边，无法处理层间垂直迁移，且Dijkstra适配负代价路径效率低下。
4. 现有True-3D布局工具先固定die分配再二维合法化，丢失三维全局优化空间。
5. 3D面对面键合异构die行高、单元宽度不同，跨层移动存在特殊代价约束，缺少适配流模型。

## 相关工作
1. 贪心合法化(Tetris/Abacus)：逐行移动单元，实现简单但位移开销大，无全局视野。
2. 二维网络流合法化(BonnPlaceLegal)：仅单层网格，不支持跨die迁移，负代价路径计算效率低。
3. 扩散式合法化：基于力导向迭代，收敛慢，难以适配大规模3D设计。
4. 伪3D布局：分块+二维布局分离流程，无法同步优化die分配与单元坐标。
5. 纯3D解析布局：仅全局松弛，无配套三维专用合法化流程，落地存在冲突重叠。

## 本文解决方案
### 1 三维网格最小代价流建模
将上下异构die划分为bin网格，同层相邻加平面边、垂直重叠bin增设D2D跨层边；区分源溢出bin与需求空闲bin，跨层移动引入额外代价惩罚。
### 2 分支定界最短增广路径算法
改进BFS替代Dijkstra适配负代价，设定代价阈值剪枝冗余分支；区分同层可分块、跨层完整单元两种移动规则，最小化单次迁移位移。
### 3 分层单元移动消解溢出
按供给量降序处理溢出源bin，回溯最优路径批量迁移单元，逐层消除bin内面积过载。
### 4 行内精细化合法校正
溢出消解后采用Abacus PlaceRow消除单行单元重叠，保持局部位移最小。
### 5 消圈后优化策略
筛选大幅偏移单元构造负代价循环，向原始坐标回移并增量重流优化，显著降低全局最大单元位移。

## 实验分析
1. 实验环境：C++实现，Intel Xeon平台，ICCAD22纯标准单元、ICCAD23含宏块3D基准，对比Tetris/Abacus/BonnPlaceLegal。
2. 位移指标：相比主流二维工具平均位移降13%，最大位移最高降低43%；少量跨层单元即可大幅释放单层空闲空间。
3. 线长表现：HP线长增量显著低于所有基线，宏分割复杂场景优势更突出。
4. 运行效率：速度接近贪心Tetris，比BonnPlaceLegal快3~8倍，大规模电路可稳定扩展。
5. 消融验证：关闭跨D2D迁移后平均位移上升6.8%、最大位移上升19%；消圈优化是降低峰值偏移关键。

## 研究启发
1. 3D合法化不能局限单层优化，跨die垂直迁移是释放布局空闲、削减单元位移的核心手段。
2. 传统Dijkstra不适合存在负位移代价的三维网格，分支定界BFS可兼顾精度与运行速度。
3. 流模型需区分同层分片、跨层整块单元两种移动逻辑，才能贴合标准单元物理约束。
4. 全局流消解溢出后叠加局部消圈微调，可同时优化平均与最大两类位移指标。
5. 面向异构3D堆叠需定制跨层代价函数，平衡跨层迁移收益与垂直互连开销。