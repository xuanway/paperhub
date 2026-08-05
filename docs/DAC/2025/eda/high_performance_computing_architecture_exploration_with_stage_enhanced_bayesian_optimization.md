---
title: "High-Performance Computing Architecture Exploration with Stage-Enhanced Bayesian Optimization"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# High-Performance Computing Architecture Exploration with Stage-Enhanced Bayesian Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11132525">https://ieeexplore.ieee.org/abstract/document/11132525</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高性能计算，设计空间探索，贝叶斯优化，集成学习 </p>
</div>


---

## 研究概要
本文提出三阶段增强贝叶斯优化算法SEBO，面向7nm Arm Neoverse V1多核处理器PPA多目标架构探索。采用Hammersley转导采样、多核集成信任域高斯代理、并行批量NEHVI采集函数，搭配VPSim+改良McPAT仿真流。STREAM等HPC基准测试，帕累托超体积优于SOTA 1~7%，解集多样性提升最高24%，运行效率翻倍。

## 背景和动机
1. 高性能多核处理器架构参数组合爆炸，系统级TLM仿真耗时极长，全遍历探索完全不可行。
2. 遗传算法等无模型DSE方法采样效率低，大量仿真预算下才能获得优质帕累托解集。
3. 传统贝叶斯优化存在三大短板：随机初始化样本信息不足、单一核代理拟合离散架构能力弱、单目标采集易丢失非凸帕累托解。
4. 现有BOOMExplorer、HyperMapper等缺少并行批量采样机制，大规模多核探索迭代缓慢。
5. 商用求解器解集多样性差，难以给架构师提供丰富折中设计方案；缺少适配7nm FinFET的完整PPA联合仿真链路。

## 相关工作
1. 无模型DSE：Platune、SPEA2遗传算法，依赖大量仿真样本，小预算下效果差。
2. 强化学习探索：MDP、蒙特卡洛树搜索，采样成本高，不适合昂贵电路仿真场景。
3. 基础贝叶斯优化：HyperMapper随机森林代理，无多目标批量并行能力；BOOMExplorer单核GP，初始化依赖先验知识。
4. TuRBO/MORBO信任域BO：仅单一核，未集成多核集成与转导采样初始化。
5. 商用Hexaly求解：无并行仿真支持，输出帕累托解集覆盖范围窄。
6. 仿真工具链：原生McPAT仅支持老工艺，缺少7nm FinFET缩放模型适配。

## 本文解决方案
### 1 两阶段Hammersley转导实验设计初始化
先低差异Hammersley粗采样全域，再基于岭回归最小预测方差筛选高信息样本；无需架构先验，解决随机采样样本不均衡、模型偏置问题。
### 2 信任域+多内核集成高斯代理模型
采用重叠/变换重叠/字典汉明三类核组合，留一交叉验证自动优选核；划分局部信任域并行训练多个GP，降低单模型拟合偏差，适配离散架构参数。
### 3 并行批量NEHVI采集函数
采用含噪声期望超体积改进指标，蒙特卡洛近似求解；多信任域并行多起点局部搜索，批量输出待仿真配置，支持多仿真同时运行，避免丢失非凸帕累托点。
### 4 7nm完整PPA仿真链路
VPSim获取延迟、访存性能指标；改良McPAT集成FinFET缩放参数，统一输出功耗、面积，构成黑盒多目标评估器。
### 5 端到端SEBO探索流水线
初始化采样并行仿真→分信任域集成GP训练→批量采集候选→多配置并行评估→更新帕累托前沿，循环至仿真预算耗尽。

## 实验分析
1. 实验设置：7nm Neoverse V1，参数覆盖核数/缓存/NoC，STREAM、DGEMM、waLBerla三类HPC负载，对比BOOMExplorer、HyperMapper、Hexaly。
2. 精度指标：同等1000仿真预算，SEBO帕累托超体积领先基线1%~7%；相比商用Hexaly解集多样性提升24%。
3. 运行效率：相较BOOMExplorer速度提升2倍，集成多核开销被并行信任域完全抵消。
4. 设计规律：实验验证核数、缓存存在收益拐点，超大架构不会持续降低延迟；提供功耗/延迟/面积三类典型最优配置。
5. 消融验证：移除转导采样、多核集成、批量并行任一模块，超体积与多样性指标显著下滑。

## 研究启发
1. 硬件DSE属于昂贵黑盒优化，贝叶斯优化相比进化算法具备天然采样效率优势。
2. 高质量初始化样本是代理模型精准的前提，低差异采样结合转导设计可摆脱领域先验依赖。
3. 离散架构参数不能仅用单一核函数，多内核集成搭配局部信任域可大幅提升拟合能力。
4. 多目标优化不能采用标量化简化，NEHVI超体积采集可保留全部折中设计，拓宽架构选择空间。
5. 并行批量候选生成+多仿真同步执行，是缩短大规模多核架构探索周期的关键工程手段。
