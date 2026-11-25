---
title: "MIA-aware FinFlex Cell Legalization with Power-Driven Cell Version Substitution"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# MIA-aware FinFlex Cell Legalization with Power-Driven Cell Version Substitution

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133187">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133187</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 最小注入面积感知，FinFlex单元合法化，单元版本替换，功耗优化 </p>
</div>


---

## 研究概要
本文面向3nm FinFlex混合行高单元，提出兼顾MIA约束与功耗驱动的合法化算法。分为预处理、DAG布局、DP后处理三阶段，支持同时序功率组内单元版本替换。ICCAD基准测试，相比SOTA总位移平均降低53%，运行时间缩减34%，MIA违规最多消除94%。

## 背景和动机
1. 3nm FinFlex工艺含S/W/T/C四类单元、H/S/L多阈值，混合高低行高布局，版本替换可折中功耗时序，但布局合规难度陡增。
2. 现有混合行高合法化仅做单元尺寸替换，未结合VT阈值，易产生大量MIA最小注入面积违规。
3. 仅替换单元不控制功率，低VT高漏功耗单元泛滥，难以达成功耗收敛目标。
4. 传统方案分阶段做版本替换与布局，无法联动优化，单元整体位移大、版图密度偏高。
5. MIA分行间/行内两类违规，现有修复仅靠填充单元，缺少聚类、版本替换协同优化手段。

## 相关工作
1. 混合行高全局布局：仅优化宏观排布，不处理合法化阶段MIA与单元版本选择。
2. HRH合法化SOTA：支持单元尺寸替换，但忽略VT阈值与MIA规则，功耗无约束。
3. MIA感知布局工具：仅适配固定高度标准单元，不兼容FinFlex跨行COMBO单元。
4. 阈值优化布局：未结合FinFlex多版本替换机制，时序功率权衡空间小。
5. 传统DP精细化布局：仅处理单元移位，无填充、版本替换联合修复MIA违规。

## 本文解决方案
### 1 预处理：填充感知聚类消除行内MIA
基于四叉树计算局部密度构建聚类图，高密度区域同时序功率单元聚类，低密度插入填充单元；按宽度、密度、候选版本数给单元分配布局优先级。
### 2 DAG导向一体化合法化
构建水平约束有向图，遍历候选区间合并位移曲线；布局时同步选择单元版本，预判行间MIA风险施加惩罚，兼顾COMBO跨行单元合法排布。
### 3 DP后处理消除行间MIA
构建单元依赖图，枚举移位+填充多类单元状态；动态规划全局最小化位移与MIA违规，稠密区域分治降低计算开销。
### 4 时序功率分层约束
将多尺寸+VT组合划分为5性能层级，单元仅可在同层级内切换版本，保证时序不恶化、抑制漏功耗。
### 5 完整三阶段流水线
预处理消行内MIA→DAG同步选版本+最小位移布局→DP优化消除剩余行间MIA，全程联动单元替换与合规修复。

## 实验分析
1. 测试数据集：ICCAD多高度合法化竞赛基准，适配FinFlex S/W/T/C四类单元与三阈值VT。
2. 位移与效率：对比增强版SOTA，总单元位移平均降至0.473倍，运行时间缩减至0.622倍，版图密度下降10%。
3. MIA修复效果：合法化后行间违规数量可控，DP后处理最多消除94%初始行间MIA违规；布局预判可进一步降低违规基数。
4. 消融对比：MIA预判模块可显著减少后处理压力；聚类+版本替换协同优于单纯填充修复。
5. 版图特性：稠密、稀疏电路均稳定优化，兼顾COMBO跨行特殊单元合规性。

## 研究启发
1. FinFlex工艺合法化必须将单元版本替换、VT阈值、MIA三类约束联合优化，分阶段处理会损失优化空间。
2. 行内MIA可通过密度感知聚类替代单纯填充，有效降低版图面积开销。
3. DAG布局时提前预判行间违规，能大幅减轻后处理DP修复压力。
4. 按时序功率分组限制版本替换范围，可在布局优化时同步实现功耗收敛。
5. 动态规划同时支持单元移位与填充插入，是低成本消除行间MIA违规的高效手段。