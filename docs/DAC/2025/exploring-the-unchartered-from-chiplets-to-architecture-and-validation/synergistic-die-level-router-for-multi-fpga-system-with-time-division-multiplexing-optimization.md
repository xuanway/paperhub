---
title: "Synergistic Die-Level Router for Multi-FPGA System with Time-Division Multiplexing Optimization"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Synergistic Die-Level Router for Multi-FPGA System with Time-Division Multiplexing Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA1: Design Methodologies for System-on-Chip and 3D/2.5D System-in Package</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://yibolin.com/publications/papers/ROUTE_DAC2025_Wang.pdf">https://yibolin.com/publications/papers/ROUTE_DAC2025_Wang.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 多FPGA系统，裸片级布线，时分复用，关键连接延迟 </p>
</div>


---

## 研究概要
本文面向时分复用多FPGA系统提出协同裸片级布线器，分均衡初布线、拉格朗日TDM分配两大阶段。设计时延-拥塞平衡寻路、多线程松弛求解、余量感知合法化算法。2023裸片路由竞赛基准测试，相较SOTA关键连接时延降低7.6%，运行速度提升5.761倍。

## 背景和动机
1. 大规模原型验证多FPGA采用多裸片架构，跨裸片SLL长线与跨片TDM互联存在复杂时序、容量约束。
2. 传统FPGA级布线仅粗划分芯片，无法精准管控裸片内部/之间拥塞，易产生SLL资源冲突与时序恶化。
3. 现有裸片级布线仅最小化布线总量，忽视关键路径时延，TDM分配未区分SLL、TDM差异化时序模型。
4. 主流TDM优化动态规划随电路规模扩展性差，缺少多线程加速方案，超大网表耗时极高。
5. 缺少拓扑与TDM比值协同优化一体化裸片布线框架，拓扑与时分分配割裂导致全局次优。

## 相关工作
1. FPGA级系统布线（ICCAD2019系列）：以FPGA为划分单元，不区分内部裸片，无法管控裸片级SLL拥塞，适配裸片场景易非法重叠。
2. 最小斯坦纳树布线：仅缩减总线资源，会拉长关键路径连接时延，难以满足系统最高频率需求。
3. 最短路径布线：降低单连接时延，但大量占用SLL造成布线拥塞，TDM比值激增。
4. 拉格朗日松弛TDM优化：仅适用于FPGA层级，未适配裸片SLL专属容量与时序约束。
5. 现有裸片布线方案：拓扑与TDM分配解耦，动态规划求解大规模电路效率低下。

## 本文解决方案
### 1 时延-需求均衡初始布线
网拆分为裸片间连接，Floyd-Warshall计算路径权重按优先级布线；动态更新SLL/TDM代价，迭代消解长线重叠，同时平衡连接时延与边占用量。
### 2 多线程拉格朗日松弛TDM初分配
构建以最大时延为目标的松弛优化模型，基于KK条件推导出单边最优TDM比值；OpenMP多线程并行计算各边η系数、更新拉格朗日乘子加速迭代。
### 3 余量感知TDM比值合法化与线分配
将浮点TDM比值向上取整为步长整数；基于连接临界度优先缩减高时延网络比值，双向物理线容量均衡分配，充分利用互联余量。
### 4 两阶段协同整体流程
阶段一完成无重叠裸片拓扑布线；阶段二迭代优化全网TDM比值并完成物理线绑定，拓扑与时分参数联合优化。

## 实验分析
1. 测试平台：Xeon 10核CPU、320GB内存，采用2023裸片路由竞赛10套工业基准，对比竞赛前三名与现有裸片SOTA工具。
2. 时延与速度：相较文献SOTA关键时延降低7.6%，整体运行提速5.761倍；对比竞赛冠军标准化时延降至1.0，速度提升1.557倍。
3. 鲁棒性：全部测试用例SLL无重叠冲突，传统FPGA级布线适配多套基准出现布线失败。
4. 消融实验：单独替换本文TDM优化可降低基线时延0.3%~10.3%，初布线模块是核心性能增益来源。
5. 耗时拆解：初始布线占总耗时70.39%，拉格朗日分配19.50%，合法化模块仅10.12%。

## 研究启发
1. 多FPGA原型系统必须采用裸片精细布线流程，FPGA粗划分无法预判片内长线拥塞与时序瓶颈。
2. 布线拓扑与TDM时分比值不可分开优化，协同设计可同时降低关键路径时延与互联资源占用。
3. 单一最短/最小树策略存在短板，时延-拥塞均衡代价函数能兼顾频率与布线可实现性。
4. 拉格朗日松弛搭配多线程并行可解决大规模网表TDM优化效率瓶颈，优于动态规划方案。
5. TDM比值合法化需预留容量余量，基于路径临界度贪心微调可进一步压缩系统最大传输时延。
