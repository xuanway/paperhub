---
title: "ALLMod: Exploring \underline{A}rea-Efficiency of \underline{L}UT-based \underline{L}arge Number \underline{Mod}ular Reduction via Hybrid Workloads"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ALLMod: Exploring Area-Efficiency of LUT-based Large Number Modular Reduction via Hybrid Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.15916v2">https://arxiv.org/abs/2503.15916v2</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>大数模约简，查找表，混合工作负载，面积效率，现场可编程门阵列 </p>
</div>


---

## 研究概要
本文提出ALLMod混合负载大数模约简架构，融合LUT查表法与迭代减法法，将输入高位分配查表、低位迭代运算，设计均衡负载硬件模板与约束驱动设计空间搜索。FPGA验证表明，128/8192比特下面积效率相较传统查表法分别提升1.65倍、3倍，大幅削减BRAM与加法器硬件开销。

## 背景和动机
1. 同态加密、零知识证明隐私计算依赖高比特模约简，Barrett/Montgomery乘法硬件复杂度随位宽激增。
2. 纯LUT查表法延迟低、吞吐高，但位宽提升后BRAM、加法树面积爆炸，面积效率极差。
3. 纯迭代减法硬件开销极小，但迭代周期随模数线性增长，延迟过高，无法满足实时加密需求。
4. 现有方案只能单一选用查表或迭代，缺少二者融合均衡硬件框架，无自动化寻优手段适配面积/延迟多约束。

## 相关工作
1. 乘基模约简（Barrett/Montgomery）：依赖高位宽乘法器，超大模数硬件实现难度大。
2. 标准LUT模约简：分段预存模值并行查表，仅小幅优化LUT复用，无法解决BRAM资源膨胀问题。
3. LUTMR优化：复用FPGA原生LUT降低少量存储开销，面积效率提升不足5%，无架构层面改进。
4. 迭代减法模约简：仅用减法器，硬件极简，但数千比特模数下延迟极长，吞吐受限。

## 本文解决方案
### 1. 混合负载分段融合算法
2n比特输入拆分：高n−m比特采用并行LUT查表，低n+m比特串行迭代减法，参数m均衡两路运算周期，并行执行两类负载，结果串行融合修正。
### 2. 均衡负载标准化硬件模板
分为并行查表、串行累加、迭代减法、结果融合、最终校正五级流水线；复用加法/减法单元减少冗余硬件，推导最优m使两路周期匹配，消除资源闲置。
### 3. 多约束设计空间自动搜索
枚举分段参数m与加法树规模，计算对应BRAM、加法器、减法器资源与总延迟，筛选满足吞吐、面积、延迟约束的帕累托最优设计。
### 4. 双场景适配调优策略
严苛延迟约束时增大查表负载、引入小型加法树加速累加；严苛面积约束时扩大迭代负载、复制减法单元保障吞吐。

## 实验分析
1. 实验平台：Xilinx Vivado综合，200MHz FPGA原型，统一Ops/十亿LUT为面积效率指标。
2. 资源收益：8192比特场景相比纯查表法，BRAM节省30%以上，加法器削减66%。
3. 面积效率：128bit提升1.65倍，8192bit最高提升3倍，位宽越大优化增益越显著。
4. 延迟特性：远低于纯迭代法，仅小幅高于纯查表，兼顾低延迟与小面积。
5. 设计空间：自动搜索快速输出多吞吐下帕累托解集，超大模数寻优耗时仅十分钟。

## 研究启发
1. 模约简硬件存在面积-延迟固有权衡，单一算法难以兼顾，异构融合混合负载是突破关键。
2. 负载均衡是混合架构核心，通过分段参数匹配两路运算周期，可最大化硬件利用率。
3. 超大比特隐私加密场景，硬件瓶颈不再是计算延迟，而是存储资源（BRAM）占用。
4. 标准化硬件模板搭配自动化设计搜索，可快速适配不同芯片、加密算法的多约束需求。
5. 复用流水线内加法、减法运算单元，能在不损失吞吐前提下显著降低整体硬件面积。
