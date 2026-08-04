---
title: "Chameleon-SAT: An Adaptive Boolean Satisfiability Accelerator Using Mixed-Signal In-Memory Computing for Versatile SAT Problems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Chameleon-SAT: An Adaptive Boolean Satisfiability Accelerator Using Mixed-Signal In-Memory Computing for Versatile SAT Problems


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133416">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133416</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 布尔可满足性，SAT求解器，混合信号，存内处理，加速器</p>
</div>

---

## 研究概要
本文提出Chameleon-SAT混合信号存内ASIC加速器，首款同时支持局部搜索、DPLL、CDCL三类SAT算法。设计自适应算法选择机制与SRAM混合信号存内阵列，适配不同规模、复杂度SAT问题。多基准测试相比CPU提速8.39~90倍，对比现有单算法ASIC，兼容范围与吞吐、能效全面领先。

## 背景和动机
1. SAT广泛用于验证、密码、AI等场景，分完备(DPLL/CDCL)与不完备局部搜索两类算法，不同问题适配最优算法差异极大。
2. 现有SAT硬件加速器仅支持单一算法，无法根据问题变量数、CTV子句变量比自适应切换，多场景适配性差。
3. SAT核心BCP、子句校验操作访存密集，冯诺依曼架构数据搬运开销巨大，软件CPU求解延迟极高。
4. 高CTV相变难例、超大变量规模下传统数字ASIC并行能力不足，缺乏混合信号并行加速手段。

## 相关工作
1. 软件SAT求解器(MiniSAT/Kissat)：纯CPU实现，大规模问题访存瓶颈严重，求解延迟量级偏高。
2. FPGA SAT加速器：可定制但流片成本高，并行规模受限，不适合规模化部署。
3. 单算法ASIC(Snap-SAT/VIP-SAT)：仅支持局部搜索或单一完备算法，无法跨算法自适应调度。
4. 早期SAT存内设计：仅数字电路，无混合信号BCP加速，不兼容CDCL子句学习流程。

## 本文解决方案
### 1. 双模式自适应调度框架
提供用户指定、自动适配两种运行模式；构造时延-能耗加权质量函数，基于变量数量、CTV特征自动择优选择局部搜索/DPLL/CDCL。
### 2. 混合信号SRAM存内计算阵列
SRAM列映射子、单元对存储正负文字；C-2C DAC模拟电路并行完成BCP传播，CL-SAT单元并行计算子句OR，消除频繁内存读写。
### 3. 多算法可重构硬件通路
阵列硬件分时复用：局部搜索仅启用子句并行校验；DPLL叠加BCP与冲突检测；CDCL新增学习子句写入通路，一套硬件兼容三类算法。
### 4. 分层特征聚类策略
按变量规模、CTV阈值将SAT问题划分为30类聚类，预训练时延、能耗特征库，快速计算质量函数完成算法择优。

## 实验分析
1. 实现工艺：28nm CMOS，混合信号SPICE+数字RTL联合仿真，对比CPU与多款主流SAT ASIC。
2. 速度增益：小规模高难问题提速90倍，中等不可满足问题提速19倍，大规模问题提速27倍，各类基准最低提速8.39倍。
3. 架构对比：唯一同时支持完备+不完备SAT硬件，最大支持500变量、2048子句，远超竞品上限。
4. 自适应效果：小问题优选DPLL，高复杂度大规模优选CDLL，低时延场景优选局部搜索，匹配用户时延/能耗权重需求。
5. 硬件代价：总芯片面积18mm²，存内阵列单求解能耗仅nJ级别，兼顾并行吞吐与低功耗。

## 研究启发
1. SAT硬件不能固化单一算法，多算法可重构+自适应调度是覆盖全场景的核心思路。
2. BCP是SAT核心性能瓶颈，混合信号模拟并行存内计算可大幅削减传播操作延迟。
3. 问题规模、CTV相变特征是算法选择关键依据，离线特征库配合加权函数可实现全自动择优。
4. 同一存内阵列分时复用适配三类SAT流程，硬件复用率高，无需多套独立计算单元。
5. 完备与不完备算法硬件需求差异明显，统一混合信号基底可兼顾快速近似求解与严谨逻辑验证需求。