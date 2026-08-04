---
title: "EPOC: A Novel Pulse Generation Framework Incorporating Advanced Synthesis Techniques for Quantum Circuits"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# EPOC: A Novel Pulse Generation Framework Incorporating Advanced Synthesis Techniques for Quantum Circuits


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2405.03804">https://arxiv.org/abs/2405.03804</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>量子最优控制，量子编译，量子电路优化 </p>
</div>


---

## 研究概要
本文提出EPOC高效量子脉冲生成框架，融合ZX演算、贪心分块、单元门合成与均衡重组优化QOC流程。先图化简压缩电路深度，再平衡分块单元规模，解决细粒度门脉冲时延堆积问题。基于QASMBench测试，相较PAQOC时延降31.74%、传统门基方案降76.80%，整体保真度显著提升。

## 背景和动机
1. NISQ设备相干时间短，量子最优控制QOC生成微波脉冲计算开销巨大，现有编译流程时延高、保真度差。
2. 传统编译直接对基础门做脉冲转换，无等价电路化简，大量短脉冲叠加累积噪声与执行延迟。
3. AccQOC、PAQOC粗粒度分块仅按门分组，未做电路拓扑等价变换，分块粒度固定无法平衡合成与QOC收益。
4. 直接合成极小可变单元门VUG后单独生成脉冲，粒度过细导致脉冲序列过长、误差累积严重，缺少重组均衡策略。

## 相关工作
1. 传统门基脉冲编译：逐层分解硬件基门，逐门调用QOC，脉冲数量多、总时延极高，无电路等价优化。
2. AccQOC粗粒度分块：固定2量子比特子电路构建脉冲库，不做拓扑化简，分块粒度单一，并行优化空间有限。
3. PAQOC子图挖掘分块：挖掘重复门模式生成脉冲，仍缺少ZX图层面全局化简，细粒度门脉冲堆积问题未解决。
4. 量子电路合成工具（BQSKIT/QSearch）：仅最小化门数量，未对接QOC脉冲生成，忽略细粒度门带来的时延开销。

## 本文解决方案
### 1. ZX图全局电路化简
将量子电路转为ZX图，利用蜘蛛融合、门交换规则合并可交换门，大幅压缩原始电路深度，平均缩短1.48倍。
### 2. 贪心均衡电路分块
水平+垂直双向切割，控制单块最大门数量，在化简后均匀划分，为后续合成提供规整子电路。
### 3. VUG可变单元门合成
基于A*搜索分解分块酉矩阵为VUG+CNOT混合电路，降低二量子门数量，简化脉冲求解目标。
### 4. 酉矩阵均衡重组策略
核心创新：不直接对单个VUG生成脉冲，将多个小型单元重组为适中规模酉矩阵，平衡QOC并行收益与计算开销。
### 5. 带全局相位匹配GRAPE脉冲库
复用历史优化脉冲，支持酉矩阵全局相位模糊匹配，提升缓存命中率，采用GRAPE梯度算法优化脉冲波形。

## 实验分析
1. 实验环境：8节点Linux集群，17组QASMBench标准量子电路，对比门基、AccQOC、PAQOC三类基线。
2. 时延指标：相比PAQOC平均时延降低31.74%，相较传统门基方案降低76.80%；重组步骤仅增加7.11%编译耗时。
3. 保真度：全局累积保真度平均提升33.77%，EPOC平均整体保真0.974，优于AccQOC的0.890。
4. 消融对比：仅合成不重组会造成大量短脉冲堆叠，时延与保真度大幅劣化，重组是核心增益模块。
5. 扩展性：可支撑160比特超大深度量子程序，分块与合成流程可并行执行，具备大规模量子程序编译能力。

## 研究启发
1. QOC脉冲优化不能仅局限于分块，必须先通过ZX图做全局拓扑化简，从源头减少脉冲总数量。
2. 电路合成追求门最小化不等于脉冲最优，细粒度单元门会叠加时延误差，需要重组平衡酉矩阵规模。
3. 分块粒度存在最优平衡点，过小脉冲堆积、过大酉矩阵计算爆炸，折中重组是兼顾时延与编译开销关键。
4. 脉冲缓存需兼容酉矩阵全局相位等价匹配，能大幅减少重复QOC梯度优化计算。
5. 量子编译前端图化简、中端分组合成、后端脉冲优化需全链路协同，单阶段优化无法实现最优硬件执行效率。
