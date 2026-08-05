---
title: "DSPlacer: DSP Placement for FPGA-based CNN accelerator"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# DSPlacer: DSP Placement for FPGA-based CNN accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132920">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132920</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> DSP布局，图卷积网络，最小费用流，级联约束合法化 </p>
</div>


---

## 研究概要
本文提出DSPlacer面向FPGA CNN加速器的数据通路DSP专用布局框架，采用GCN区分数据/控制DSP，IDDFS构建通路图，最小费用流求解DSP分配，双层ILP完成级联合法化。在ZCU104平台测试，相较Vivado、AMF-Placer，WNS分别提升32.5%、65.8%，布线规整度显著改善。

## 背景和动机
1. CNN加速器大量DSP构成规整数据流，商用Vivado布局忽视数据通路拓扑，布线绕路严重，时序裕量恶化。
2. 现有数据通路布局依赖图同构提取，仅捕获局部规则，无法区分数据/控制类DSP，布局紧凑度不足。
3. 传统ILP全局求解全部硬件规模过大，求解耗时爆炸，难以适配万级DSP神经网络设计。
4. FPGA列式DSP阵列存在严格级联放置规则，通用布局器无专属约束处理，产生大量DR违规。
5. Zynq系列PS处理器固定位置，数据总线有固定走向，现有工具未建模PS-PL传输布线偏好。

## 相关工作
1. PADE布局：基于SVM图同构识别数据通路，仅提取局部规则，全局DSP分类精度低。
2. R-SAD脉动阵列布局：仅适配单一 systolic 架构，通用性差，无法覆盖多样化CNN PE结构。
3. AMF-Placer通用FPGA布局：无DSP级联约束建模，不区分数据流与控制单元，时序优化有限。
4. 全局ILP数据通路布局：变量规模庞大，大规模DNN设计求解不可行。
5. 商用Vivado布局：无数据流感知DSP分配，随机放置易破坏PS-PL总线布线路径。

## 本文解决方案
### 1 GCN数据通路DSP识别模块
提取介数、接近中心性、偏心率等全局图特征构建节点向量；双层图卷积+全连接网络做DSP二分类，加权损失缓解样本不均衡，分类精度达96%。
### 2 IDDFS数据通路图构建
迭代深度优先搜索计算DSP间最短路径，过滤控制类DSP，仅保留纯数据流DSP构建拓扑图，缩减优化规模。
### 3 最小费用流DSP分配模型
将原始二次0-1规划线性近似转化为MCF问题；新增PS-PL总线角度软惩罚、DSP级联损失项，最小化互连距离。
### 4 双层ILP级联合法化
先列级ILP调整DSP所属列，满足级联单元同列约束；再逐列并行行分配，保证级联DSP垂直相邻，最小位移修正。
### 5 交替迭代增量布局
固定DSP优化其他逻辑、再固定逻辑重排DSP，循环迭代消除跨模块布线冲突，兼容主流FPGA布局工具。

## 实验分析
1. 实验环境：Zynq ZCU104，iSmartDNN、SkyNet、多版本SkrSkr CNN基准，对比Vivado2020.2、AMF-Placer2.0。
2. DSP识别：GCN相较PADE SVM精度提升15%，各类网络泛化能力更强。
3. 时序指标：相较Vivado平均WNS提升32.5%，对比AMF-Placer提升65.8%，总负TNS大幅缩减。
4. 布线与开销：总线长小幅上浮，布局总运行开销主要来自通用逻辑，DSP优化阶段仅占总耗时2%。
5. 可视化对比：DSPlacer数据流排布更规整，PS到PL传输通道布线更顺畅，无长绕路。

## 研究启发
1. CNN FPGA布局必须单独识别数据流DSP，控制单元可交由通用工具处理，能大幅降低优化复杂度。
2. 大规模DSP分配不可直接全局ILP，线性化转最小费用流可在精度损失极小前提下大幅提速。
3. FPGA DSP级联约束需分列、行两步合法化，并行逐列求解能平衡修正质量与运行时间。
4. 布局需建模PS-PL固定总线走向作为软约束，从源头减少跨模块长布线与时序违例。
5. 数据流专用DSP布局可与通用布局器协同迭代，无需重构完整P&R流程，工业适配成本更低。
