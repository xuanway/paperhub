---
title: "Weighted Range-Constrained Ising-Model Decoder for Quantum Error Correction"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Weighted Range-Constrained Ising-Model Decoder for Quantum Error Correction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133309">https://ieeexplore.ieee.org/document/11133309</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量子纠错，伊辛模型，快速解码方法，表面码，变量约简</p>
</div>

---

## 研究概要
本文提出WRIM加权范围约束伊辛解码器用于表面码量子纠错。构建多边形区域圈定故障综合征削减建模变量，分档配置伊辛耦合与外场权重，整体复杂度O(n)。对比传统伊辛方案变量缩减97.8倍，D-Wave退火实现微秒级解码，纠错阈值10.7%~11.0%，优于MWPM解码器。

## 背景和动机
1. 量子退相干严重制约量子计算，表面码是主流容错方案，快速高精度解码是刚需。
2. MWPM解码器复杂度O(n²~n⁷)、内存开销大；UF复杂度O(n log n)仍存在性能瓶颈。
3. 现有标准伊辛解码器建模覆盖全晶格，变量数量庞大、退火耗时高，扩展性受限。
4. 单一固定权重伊辛哈密顿难以适配不同长度错误链，易陷入局部最优，逻辑错误阈值偏低。

## 相关工作
1. MWPM解码器：基于图匹配，精度高但高次复杂度，大码距实时解码困难。
2. UF并查集解码器：近线性速度，但硬件阵列部署受码距限制。
3. 神经网络/张量网络解码器：训练成本高或复杂度O(n²)，落地成本高。
4. 传统伊辛QEC解码器：全局晶格建模，变量多、无分层权重优化，退火效率差。

## 本文解决方案
### 1 范围约束多边形区域生成算法
遍历翻转综合征，自适应划定行/列多边形边界，仅保留故障相关量子比特与综合征，剔除大量无关节点，大幅缩减伊辛建模规模。
### 2 RIM范围约束伊辛基础模型
仅区域内单元构建哈密顿，无需额外辅助变量分解高次项，在保证错误链完备性前提下降低求解规模。
### 3 WRIM多档加权哈密顿优化
按错误链长度分档设置耦合J与外场h多组权重，并行多模型退火，优先返回满足奇偶校验的最短错误链解。
### 4 两级流水线解码流程
先经典侧生成约束区域，再提交量子退火机求解，区域生成复杂度O(kn)，退火阶段最高复杂度O(n⁰·⁹⁷)。

## 实验分析
1. 实验环境：CPU构造伊辛模型，Amplify、D-Wave两套量子退火引擎测试，码距3~9、物理误码0.1%~20%。
2. 变量压缩：同等码距下相比传统伊辛方案变量最高缩减97.8倍，误码越低压缩效果越好。
3. 时间复杂度：整体最坏O(n)，优于UF的O(n log n)；低误码退火迭代近乎常数规模。
4. 解码时延：0.1%、1%低误码场景D-Wave实现微秒级解码，适配超导量子实时纠错需求。
5. 纠错阈值：逻辑误码阈值10.7%~11.0%，突破MWPM最高10.3%的阈值上限。

## 研究启发
1. 量子纠错无需全局晶格建模，基于故障综合征局部区域裁剪可大幅降低伊辛求解开销。
2. 单一哈密顿权重适配性差，按错误链长度分档加权可拓宽能量差，提升全局最优收敛概率。
3. 解码流水线分离经典区域预处理与量子退火，兼顾建模轻量化与硬件加速优势。
4. 相比全局最小错误数，逐链最短错误路径更有利于提升量子纠错容错阈值。
5. 伊辛退火类解码器可实现线性复杂度，有潜力替代MWPM、UF作为大规模表面码高速解码方案。
