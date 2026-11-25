---
title: "ACRS: Adjacent Computation Resource Sharing among Partitioned GPU Sub-Cores"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ACRS: Adjacent Computation Resource Sharing among Partitioned GPU Sub-Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132550">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132550</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>GPU子核，功能单元共享，操作数收集器阻塞，相邻资源共享，顺序匹配策略 </p>
</div>


---

## 研究概要
本文面向GPU流式多处理器SM子核隔离导致功能单元(FU)利用率低、操作数收集器阻塞问题，提出ACRS相邻计算资源共享框架。设计SF发射、回写两大硬件模块与多种子核配对策略，顺序配对方案效果最优。测试相比基线平均提速14.1%、最高46.4%，能耗降低8.3%，优于现有SOTA调度方案。

## 背景和动机
1. 现代GPU SM拆分为多个独立子核，各子核FU、操作收集器OC硬件隔离，负载不均衡时大量FU空闲，流水线频繁阻塞。
2. OC阻塞高发，统计显示68.4%阻塞场景下同SM相邻子核存在空闲同类型FU，存在巨大资源复用空间。
3. 全局交叉互连共享FU布线面积、时序开销极大，直接新增寄存器写端口会引发写冲突、扩大寄存器面积。
4. 现有调度优化仅优化前端线程分配，无法解决后端FU阻塞与资源闲置的核心瓶颈。

## 相关工作
1. SM间资源共享：聚焦L1缓存、顶层调度器跨SM复用，不涉及单SM内部子核FU共享。
2. Warp/寄存器调度优化（Shuffle+RBA）：缓解分支发散、寄存器体冲突，无法消除OC-FU流水线阻塞。
3. 乱序执行、动态Warp形成：提升指令级并行，但不解决子核硬件隔离造成FU闲置。
4. 全局子核互连方案：采用全交叉网络，硬件复杂度、布线开销呈平方级增长，难以落地。

## 本文解决方案
### 1. ACRS整体硬件架构
采用一对一固定相邻子核配对替代全局交叉，大幅降低布线开销；新增SF ISSUE、SF WriteBack两大跨子核通路，寄存器入口增设4项写缓冲，无需额外寄存器写端口。
### 2. SF ISSUE共享发射模块
监控源子核OC阻塞状态与目标子核FU空闲信号，按类型匹配阻塞指令与空闲FU，跨核指令优先级更高，抢占空闲硬件资源。
### 3. SF WriteBack结果回写模块
携带源子核ID传递运算结果，区分本地/跨核写回；写缓冲仲裁优先调度早生成数据，解决跨核写竞争冲突。
### 4. 四类子核配对策略
提出双配对、三分组、顺序环形、两两互斥四种配对方式，经仿真筛选出Sequential顺序环形配对为最优方案。

## 实验分析
1. 仿真平台：GPGPU-Sim 4.2搭建类Turing架构，测试Rodinia、Parboil等计算/访存混合基准。
2. 性能收益：顺序SS策略平均IPC提升14.1%，计算密集负载最高提速46.4%，相比SOTA调度额外提升12.3%。
3. 资源指标：FU利用率显著上升，OC阻塞周期平均下降27.7%；访存密集负载几乎无性能损耗。
4. 功耗能耗：电路瞬时功耗小幅上升，但总运行时长缩短，整体能耗降低8.3%。
5. 硬件开销：仅少量控制逻辑与512B写缓冲，布线复杂度由交叉O((pw)²)降至线性O(pw)，芯片面积代价极小。

## 研究启发
1. GPU性能瓶颈分前后端，前端调度优化存在上限，后端FU硬件隔离阻塞是计算负载核心短板。
2. 一对一相邻局部共享替代全局互连，可在极低硬件开销下挖掘闲置计算资源，平衡收益与面积成本。
3. 跨核数据通路需配套缓冲仲裁机制，避免寄存器写端口冲突，无需改动寄存器堆主体设计。
4. 负载特性决定优化收益：ACRS对计算密集型程序增益显著，访存受限程序无明显提升。
5. 子核拓扑配对策略直接影响资源复用效率，环形顺序配对可最大化全SM硬件并行潜力。