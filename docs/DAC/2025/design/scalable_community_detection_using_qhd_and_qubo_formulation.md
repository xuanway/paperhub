---
title: "Scalable Community Detection Using QHD and QUBO Formulation"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Scalable Community Detection Using QHD and QUBO Formulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://par.nsf.gov/servlets/purl/10663211">https://par.nsf.gov/servlets/purl/10663211</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>量子哈密顿下降，二次无约束二值优化，社区检测 </p>
</div>


---

## 研究概要
本文提出基于量子哈密顿下降(QHD)的分层社区检测算法，将图模块度优化转化为QUBO问题。设计粗化-求解-细化分层流程，依托GPU并行模拟量子隧穿跳出局部最优。多真实图测试，中等密度网络模块度最高提升5.49%，大规模场景相较GUROBI求解速度大幅领先。

## 背景和动机
1. 社交、生物等大规模图的社区检测属于非凸组合优化，传统算法易陷入局部最优，大图计算开销爆炸。
2. 经典整数求解器GUROBI在千变量以上大图易超时，难以兼顾模块度与运行效率。
3. 量子退火类方案需专用量子硬件，落地成本高，缺少纯GPU可运行的类量子优化方案。
4. 现有QUBO社区建模未均衡社区规模，单层求解无法处理超大规模稀疏图，扩展性差。

## 相关工作
1. 传统社区检测：谱聚类、分层聚类、METIS分层划分，仅依赖局部贪心，极易困在局部极值。
2. 精确整数求解器GUROBI：小规模图可求最优解，大规模图迭代耗时极高，资源开销巨大。
3. 量子退火社区方案：依赖量子硬件嵌入，硬件约束强，无法在通用GPU部署。
4. 基础QHD优化工具QHDOPT：仅通用数值求解，未针对社区检测设计分层图适配流程。

## 本文解决方案
### 1 多约束社区检测QUBO建模
以最大化模块度为目标，增加节点唯一分配、社区规模均衡两类惩罚项，构建完整二次无约束二元目标函数，适配任意分社区数量k。
### 2 三层分层大图处理框架
粗化层采用重边匹配聚合节点压缩图规模；粗图执行QUBO求解；逐层反投影并细化微调，大幅降低单次优化变量规模。
### 3 GPU加速QHD求解器
离散薛定谔方程模拟量子隧穿效应，仅依靠矩阵乘运算，基于cuSPARSE、PyTorch实现多卡并行，无需线性方程组求解。
### 4 迭代细化微调机制
每层反投影后遍历节点，尝试更换社区并更新模块度，无增益则停止迭代，逐层提升划分质量。

## 实验分析
1. 实验平台：4张A5000多GPU，对比GUROBI求解器，测试小型基准图、Facebook等大型真实社交网络。
2. 小规模图：10组基准中8组模块度优于GUROBI，计算耗时仅为其20%，75.4%场景可匹配最优解。
3. 大规模图：中等密度Facebook网络模块度提升5.49%；极稀疏LastFM场景GUROBI小幅占优。
4. 求解器对比：739个超千变量实例中71.4% QHD模块度更优，同等时间限制下收敛质量更强。
5. 扩展性：分层机制有效压缩变量，多GPU并行随图规模稳定提速，适配万级节点网络图。

## 研究启发
1. 量子启发优化无需量子硬件，通过经典模拟隧穿效应即可突破传统贪心局部最优缺陷。
2. 大规模图组合优化必须分层降维，单层QUBO建模变量爆炸无法实用。
3. QUBO建模不能仅考虑模块度，加入分配、规模均衡约束可避免无意义平凡解。
4. 基于矩阵乘的优化算法天然适配GPU稀疏并行，相比传统分支切割求解器扩展性更强。
5. 算法效果与图密度强相关，中等稠密网络量子启发优化增益最显著，极稀疏图仍需结合经典精确求解思路。
