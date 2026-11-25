---
title: "Principle-based Dataflow Optimization for Communication Lower Bound in Operator-Fused Tensor Accelerator"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Principle-based Dataflow Optimization for Communication Lower Bound in Operator-Fused Tensor Accelerator

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132765">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132765</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>数据流，张量，原理，融合，处理单元 </p>
</div>


---

## 研究概要
本文提出基于四条理论准则的数据流优化方法，给出访存下界解析解，并设计FuseCU融合张量加速器。区分同/异NRA融合收益，支持Tile/Column两种融合映射。在BERT、LLaMA2等Transformer测试，相比TPUv4i访存减少63.6%、提速1.33倍，硬件面积仅增12%。

## 背景和动机
1. Transformer张量计算中外存访存是性能与功耗核心瓶颈，算子融合可消除中间张量片外读写。
2. 现有数据流优化依赖DSE搜索，空间爆炸、耗时久，缺少数学理论下界与架构指导。
3. 传统加速器仅支持内存层算子融合，无法在PE阵列实现计算级融合，大量融合方案无法落地。
4. 跨算子融合易破坏单算子最优分块调度，部分融合反而增加总访存，缺少收益判定标准。

## 相关工作
1. 单算子数据流工具(MAESTRO/Timeloop)：仅优化卷积/矩阵乘内部分块，不支持跨算子融合。
2. 内存层融合框架(DAT/FLAT/Chimera)：仅在片上缓存完成融合，无法映射至PE阵列。
3. 空间加速器(TPUv4i/Gemmini/Planaria)：PE数据流模式固定，缺少灵活融合通路。
4. 搜索式优化：遗传/整数规划遍历设计空间，收敛慢且无架构可复用理论结论。

## 本文解决方案
### 1 四层访存下界优化准则
依据片上缓存大小划分Single/Two/Three-NRA三类数据流，给出分块、调度最优策略；准则4判定仅相同NRA算子融合才有收益。
### 2 两类融合硬件映射
Tile融合：中间张量作为PE驻留瓦片；Column融合：PE阵列拆分分段流水处理中间张量，覆盖全部高效融合模式。
### 3 XS可配置PE单元
增加多路选择器，动态切换输入/输出驻留数据流，适配各类融合流水线。
### 4 FuseCU融合计算单元
由4个可配置CU组成，互连MUX切换阵列宽窄/方形布局，无需修改原有乘加逻辑，兼容现有空间加速器。

## 实验分析
1. 测试负载：BERT、GPT2、LLaMA2等7类Transformer，对比TPUv4i、Gemmini、Planaria、DAT。
2. 理论验证：准则解析最优访存与DAT搜索结果持平，部分场景更优，无搜索耗时。
3. 性能指标：相较TPUv4i访存降低63.6%、吞吐提升1.33倍；相比Gemmini、Planaria分别提速1.25×、1.14×。
4. 硬件开销：28nm综合面积仅增加12%，互连与控制逻辑开销不足0.1%。
5. 序列敏感性：长文本场景融合收益进一步放大，短序列仍保持稳定优化效果。

## 研究启发
1. 数据流优化可脱离暴力搜索，通过缓存与张量维度数学推导直接得到理论最优方案。
2. 算子融合存在收益边界，仅保持相同非冗余访问模式的融合能降低总访存。
3. 灵活驻留PE与可重构阵列互连是实现计算级算子融合的最小硬件代价方案。
4. 分块、调度、映射三层数据流必须协同优化，单一维度调整易抵消融合收益。
5. 面向大模型的加速器设计，跨PE算子融合是降低片外带宽需求的关键低成本手段。
