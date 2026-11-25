---
title: "Hydra: Harnessing Expert Popularity for Efficient Mixture-of-Expert Inference on Chiplet System"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Hydra: Harnessing Expert Popularity for Efficient Mixture-of-Expert Inference on Chiplet System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133023">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133023</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合专家模型，芯粒，大语言模型 </p>
</div>

---

## 研究概要
本文面向芯粒架构MoE推理提出软硬件协同Hydra加速器。软件端基于层间专家选择条件概率做热度感知映射，减少全互联通信；硬件采用CAM消除重排稀疏矩阵运算，混合跳过Softmax冗余计算。22nm工艺下，相较RTX3090延迟降低14.2倍、功耗减少169.1倍，优于FLAME等SOTA加速器。

## 背景和动机
1. 超大MoE模型无法单片集成，芯粒专家并行会产生大量片间全互联传输，通信占总运行74.9%，成为首要瓶颈。
2. MoE的置换/逆置换依赖高复杂度稀疏矩阵乘，门控Softmax存在大量指数、除法冗余运算，计算开销占62.7%。
3. 现有MoE优化仅侧重单芯片预取，未利用层间专家选择相关性，无法缓解芯粒间流量不均衡问题。
4. 传统置换模块硬件复杂度高，缺少并行检索专用硬件消除矩阵运算开销。
5. 通用Softmax引擎无稀疏门控适配跳过机制，未区分模型并行带来的重复计算。

## 相关工作
1. Pre-gated MoE、FLAME：仅优化单芯片专家预取，未解决芯粒间全互联通信瓶颈。
2. 分布式MoE框架（Tutel、Gshard）软件分片，无芯粒专用硬件加速置换、门控算子。
3. 通用DNN芯粒加速器Simba：未针对Mo稀疏门控、token重排定制专用计算单元。
4. 单芯片MoE硬件：仅优化FFN计算，忽略置换与Softmax两大计算瓶颈。
5. 分布式多GPU MoE：通信开销巨大，能效远低于专用芯粒加速器。

## 本文解决方案
### 1 热度感知专家映射（软件层）
挖掘连续层专家选择条件概率预测各芯粒专家访问热度，以模拟退火求解最小跳数通信映射方案，推理时提前预加载下一层专家，片间流量大幅削减。
### 2 CAM并行置换硬件引擎
采用9T CAM阵列并行检索token-专家映射关系，把原O(S²M)稀疏矩阵重排降至O(E)检索开销，省去中间稀疏矩阵存储。
### 3 混合冗余跳过Softmax单元
双维度跳过机制：模型并行下分片token计算跳过；稀疏门控仅保留选中专家做除法，无精度损失，大幅削减指数、除法运算量。
### 4 4×4可扩展芯粒硬件架构
单芯粒集成多PE阵列、CAM置换引擎、优化Softmax、映射求解器，芯粒间100Gbps NoC互联，支持混合专家/模型并行调度。

## 实验分析
1. 实验配置：22nm 500MHz工艺，4×4 Hydra芯粒；基线RTX3090、A100多卡、FLAME/Pre-gated MoE；测试Switch-base8/16模型。
2. 整体PPA：对比GPU延迟降14.2倍、功耗降169.1倍；对比FLAME延迟3.5倍、能效18.9倍。
3. 消融实验：热度映射单独提速1.49倍，CAM置换提速1.59倍，Softmax跳过额外提速1.22倍，三者协同收益最高。
4. 扩展性：芯粒数量提升时映射策略持续均衡流量，吞吐量稳定上升，无通信拥塞衰减。
5. 多GPU对比：相较4/8卡A100吞吐量提升11倍以上，能效提升数百倍。

## 研究启发
1. MoE层间专家选择存在强相关性，可提前预测访问热度，从映射层面根治芯粒全互联通信瓶颈。
2. Token置换稀疏矩阵运算可通过CAM并行检索硬件完全替代，是低开销硬件优化关键路径。
3. MoE稀疏门控+模型并行天然存在两类Softmax冗余，无损跳过机制可显著降低算术单元功耗。
4. 面向MoE的芯粒系统不能复用通用DNN芯粒设计，必须配套专用置换、门控硬件单元。
5. 软件映射优化与硬件算子加速具备叠加增益，软硬件协同是芯粒MoE极致能效的核心路线。
