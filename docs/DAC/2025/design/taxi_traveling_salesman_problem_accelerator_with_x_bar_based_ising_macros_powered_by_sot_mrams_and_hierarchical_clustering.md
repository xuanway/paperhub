---
title: "TAXI: Traveling Salesman Problem Accelerator with X-bar-based Ising Macros Powered by SOT-MRAMs and Hierarchical Clustering"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# TAXI: Traveling Salesman Problem Accelerator with X-bar-based Ising Macros Powered by SOT-MRAMs and Hierarchical Clustering

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.13294">https://arxiv.org/abs/2504.13294</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 伊辛机，加速器，存内计算，组合优化问题，自旋轨道转矩MRAM</p>
</div>


---

## 研究概要
本文提出TAXI基于SOT-MRAM交叉条Ising存内加速器，软硬件协同分层聚类分解大规模TSP。采用器件原生随机切换实现自然退火，各聚类子问题在独立Ising宏内并行求解，无需宏间数据搬运。TSPLIB全规模测试，相较主流分层Ising求解平均提速8倍，85900城市实例最优解仅比精确解长20%。

## 背景和动机
1. TSP属于NP难组合优化，冯诺依曼架构海量数据搬运带来严重访存瓶颈，传统精确求解随规模指数级耗时。
2. 现有分层Ising求解器随城市规模扩大解质量大幅下滑，聚类后子问题统一映射至单阵列，互连开销爆炸。
3. CMOS真随机数发生器面积大、速度慢，难以支撑快速退火；RRAM/SONS器件噪声不可控，大规模交叉条稳定性差。
4. 主流存内Ising架构需频繁读写宏外存储，子问题串行执行，并行度低、延迟能耗偏高。

## 相关工作
1. HVC分层聚类Ising：采用K-means聚类，全部子问题映射单阵列，规模扩大后互连复杂度激增。
2. Neuro-Ising：GNN辅助聚类，大规模实例求解精度衰减严重，无原生存内并行硬件。
3. IMA/CIMA存内退火：基于电荷存储器件，自旋状态存于宏外，频繁片外读写拖慢速度。
4. CMOS/TRNG Ising芯片：数字随机单元面积开销大，退火速率受限，能效远低于磁性器件方案。

## 本文解决方案
### 1 SOT-MRAM交叉条Ising宏单元
3T-1M存储单元构建交叉条，划分为权重分区与自旋存储分区；利用器件自旋轨道切换原生随机性生成随机向量，替代大尺寸CMOS RNG。内置叠加、电流镜像、胜者全取ArgMax电路完成Ising能量最小化。
### 2 非线性自然退火机制
依托SOT切换概率S型特性迭代降低写电流，前期快速跳出局部极小、后期稳定收敛全局最优，无需额外数字退火控制电路。
### 3 凝聚式分层聚类算法
采用Ward准则凝聚聚类，自底向上分层拆分；固定簇首尾节点锁定簇间路径，各子簇可分配独立Ising宏完全并行求解。
### 4 宏级并行存内架构
基于PUMA仿真框架改造空间阵列，每个聚类子问题独立映射Ising宏，全程无宏间数据搬移，分治后逐层合并全局路径。

## 实验分析
1. 仿真环境：TSMC 65nm Spectre电路仿真、PUMA周期级架构模拟器，测试TSPLIB 20组76~85900城市实例。
2. 精度表现：12簇4比特配置最优，最大实例85900城市解长度仅为精确解1.2倍，远超Neuro-Ising/CIMA。
3. 性能指标：对比现有分层Ising平均提速8倍；85900城市总运行375.4秒，单CPU精确求解需上百年。
4. 硬件能耗：10600城市仅1.81μJ，33810城市302μJ，同规模竞品能耗高出数倍。
5. 消融对比：12簇、4比特平衡精度与硬件开销，簇尺寸增大延迟与能耗显著上升。

## 研究启发
1. 磁性存储器件原生随机特性可替代昂贵数字TRNG，是Ising退火低成本硬件方案。
2. 分层分治TSP不能共用单阵列，独立Ising宏并行可同时提升速度与路径精度。
3. 聚类算法需硬件适配，固定簇间边界可避免合并阶段路径劣化，兼顾并行度与解质量。
4. 存内计算优化核心是消除宏外数据交换，子问题全本地运算大幅削减传输能耗。
5. 器件固有非线性特性可直接用于退火调度，省去复杂数字控制电路，简化加速器设计。
