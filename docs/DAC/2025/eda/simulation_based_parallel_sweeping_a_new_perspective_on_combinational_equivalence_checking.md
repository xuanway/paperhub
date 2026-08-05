---
title: "Simulation-based Parallel Sweeping: A New Perspective on Combinational Equivalence Checking"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Simulation-based Parallel Sweeping: A New Perspective on Combinational Equivalence Checking

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA2: Design Verification and Validation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133204">https://ieeexplore.ieee.org/document/11133204</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 组合等价性检查，并行扫描，GPU加速，穷举仿真 </p>
</div>


---

## 研究概要
本文提出基于GPU并行穷举仿真的组合等价检查框架Simulation-based Parallel Sweeping，区别传统SAT Sweeping。设计三维并行穷举仿真、窗口合并、多轮优先割局部函数校验模块，分多阶段迭代化简Miter。EPFL/IWLS大规模电路测试，4组可独立完成验证；GPU引擎搭配ABC平均提速4.89倍，相较商用LEC提升4.88倍。

## 背景和动机
1. 组合等价检查(CEC)属于co-NP完全问题，主流SAT Sweeping依赖串行SAT求解，大规模算术/控制电路验证耗时极长，部分案例超时数月。
2. SAT求解天然并行度低，现有并行CEC仅对SAT任务多线程分发，未从底层验证范式重构并行计算架构。
3. 大支持集节点全局穷举仿真指数开销不可控，缺少基于割的局部函数校验机制降低仿真规模。
4. 传统随机仿真仅粗分等价类，无法完整证明节点等价，只能作为SAT前置过滤手段。
5. 现有GPU辅助CEC仅分担局部匹配，核心等价证明仍依赖CPU SAT，GPU算力未充分释放。

## 相关工作
1. BDD等价检查：内存爆炸，无法适配千万节点级大规模电路，现已淘汰。
2. SAT Sweeping系列：以SAT求解为核心，优化仿真样本、并行SAT任务，但并行上限低，超大电路效率差。
3 CPU多线程CEC：仅并发SAT调用，仿真未大规模并行，算力利用率有限。
4 早期GPU辅助验证：GPU仅做简单仿真匹配，等价判定仍交给CPU SAT，无完整穷举仿真证明能力。
5 代数CEC：仅适配专用算术电路，通用数字设计泛化能力不足。

## 本文解决方案
### 1 五模块GPU并行CEC整体架构
包含Miter管理器、等价类EC管理器、随机局部仿真器、割生成器、核心穷举仿真器，全部计算GPU加速，仅窗口合并少量CPU处理。
### 2 三维并行穷举仿真算法
单真值字并行、同层级节点并行、多仿真窗口并行；多轮分片计算长真值表，窗口合并减少重复电路仿真开销。
### 3 多层级割生成与局部校验机制
拓扑分层枚举优先割，三套割筛选准则轮换生成公共割；利用内部无关项SDC，用局部函数等价替代全局真值比对，大幅缩减输入变量规模。
### 4 三阶段迭代化简流水线
输出PO校验→全局仿真化简→多轮局部割校验，每轮合并等价节点压缩Miter；无法判定则输出简化网表移交SAT工具。
### 5 等价类迭代更新机制
随机仿真初始化等价类，反例CEX拆分错误等价簇，每轮仿真后同步更新Miter与节点等价关系。

## 实验分析
1. 测试环境：RTX A6000 48G GPU，EPFL/IWLS基准经ABC double放大生成超大AIG Miter。
2 独立验证能力：9组大规模电路中4组仅靠GPU仿真引擎即可完全证明等价，log2案例从4个月缩短至1.4天。
3 速度对比：GPU引擎+ABC混合流程相对原生ABC平均提速4.89倍，对比16线程商用Conformal LEC提速4.88倍。
4 消融表现：PO、全局、局部三阶段缺一不可，局部割校验是处理大支持集电路核心手段。
5 短板场景：VGA等拥塞电路GPU化简幅度低，混合流程仅小幅优于原生ABC。

## 研究启发
1 CEC不只有SAT一条技术路线，穷举仿真具备天然GPU大规模并行优势，可作为独立验证引擎或SAT前置化简工具。
2 全局仿真指数复杂度瓶颈可通过公共割局部校验破解，利用电路内部无关项SD大幅降低仿真输入维度。
3 多维度并行+窗口合并能充分挖掘GPU内存合并访存优势，削减重复电路仿真冗余计算。
4 混合验证范式具备实用价值：GPU处理易验证节点，SAT处理仿真无法判定的复杂结构，兼顾速度与完备性。
5 电路拓扑分层生成优先割，搭配多套筛选准则可提升公共割质量，显著提高局部函数等价证明成功率。