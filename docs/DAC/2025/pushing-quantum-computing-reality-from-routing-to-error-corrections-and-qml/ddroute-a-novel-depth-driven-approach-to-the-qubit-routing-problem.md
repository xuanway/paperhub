---
title: "DDRoute: a Novel Depth-Driven Approach to the Qubit Routing Problem"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# DDRoute: a Novel Depth-Driven Approach to the Qubit Routing Problem


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133018">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133018</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量子计算，量子比特映射，量子比特路由，量子电路，深度最小化</p>
</div>


---

## 研究概要
本文提出面向NISQ量子线路的深度驱动布线算法DDRoute，配套DDPlace初始映射策略。设计兼顾线路深度的广义距离代价函数，优先并行SWAP降低时序开销。在多款大规模量子芯片测试，相比主流SABRE、t|ket⟩等工具线路深度最高降低70.4%，编译速度提升92.8倍。

## 背景和动机
1. NISQ量子芯片物理比特拓扑受限，双量子门需插入SWAP完成比特交互，过多SWAP会大幅增加线路深度，超出量子相干时间限制。
2. 现有布线启发式算法以最小SWAP数量为单一目标，忽略并行调度潜力，生成线路时序过深，硬件执行保真度差。
3. 传统最短路径布线仅考量交换步数，未评估SWAP对整体时序堆叠影响，容易造成时间步堆积。
4. 缺少适配不同门执行时长、支持千比特级芯片的可扩展布线方案，大规模线路编译耗时极高。

## 相关工作
1. 精确求解类（整数规划/MaxSAT）：可得到最优解，但复杂度指数级，仅适用小规模量子线路。
2. SABRE、StochasticSwap：启发式增量布线，核心目标减少SWAP总数，不优化并行时序，线路深度开销大。
3. t|ket⟩、Cirq：分层分时间片处理门，仅简单代价函数，未深度挖掘并行交换空间。
4. MQT QMAP：基于A*寻优，侧重门数量优化，对时序深度无定向约束，千比特场景编译效率低。

## 本文解决方案
### 1. DDPlace深度感知初始映射
按线路门深度排序分配物理比特，优先将前后依赖紧密逻辑比特映射至相邻物理位置，减少前期布线交换需求，为DDRoute提供优质初始布局。
### 2. 三层启发式布线核心流程
操作筛选：选取比特深度最低逻辑比特作为交换对象，减少时序堆叠；最优路径：提出含时序、交换步数、未来门收益的综合距离δ，替代传统最短路径；最优交换：分步插入SWAP，最大化并行交换机会。
### 3. 单量子门时序压缩调度
延后单门执行，利用SWAP间隙填充单量子操作，避免额外新增时间步，进一步压低总线路深度。
### 4. 低复杂度可扩展实现
DDPlace复杂度O(g log n)，DDRoute为O(g n^1.5 log n)，支持IBM Condor千比特芯片，编译耗时远低于同类工具。

## 实验分析
1. 测试环境：Sycamore、Aspen、Eagle、Osprey、Condor多款超导芯片，多标准量子线路基准，对比SABRE/t|ket⟩/Cirq/QMAP/StochasticSwap。
2. 深度优化：500比特线路相比SABRE深度降低70.4%，所有芯片场景平均优化幅度超36.8%。
3. 编译效率：几何平均编译提速92.8倍，仅DDRoute与SABRE可通过千比特3小时时限。
4. 门长适配：支持单门/CX/SWAP差异化时长权重，贴合真实硬件门延迟，深度优化效果进一步提升至71.5%。
5. 权衡特性：DDRoute会小幅增加SWAP总数，但以极少交换增量换取大幅时序缩减，适配NISQ相干约束。

## 研究启发
1. 量子布线不能仅以SWAP数量为优化目标，线路深度、并行度是NISQ硬件更关键约束指标。
2. 寻路代价函数必须融合时序、交换开销、后续门依赖多维度指标，单纯最短路径会造成时序堵塞。
3. 初始映射质量直接决定布线深度上限，深度感知布局可从源头减少大量交换操作。
4. 单量子门具备时序填充空间，合理调度可零成本压缩线路总时长。
5. 面向千比特大规模量子芯片，算法复杂度需严格控制，轻量化启发式比精确求解更具工程实用性。