---
title: "APSQ: Additive Partial Sum Quantization with Algorithm-Hardware Co-Design"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# APSQ: Additive Partial Sum Quantization with Algorithm-Hardware Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.03748">https://arxiv.org/abs/2505.03748</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://github.com/Yonghao-Tan/APSQ">https://github.com/Yonghao-Tan/APSQ</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 硬件感知量化，部分和量化，数据流，深度神经网络，Transformer </p>
</div>


---


## 研究概要
本文提出APSQ增量部分和量化算法与可重构硬件协同架构，针对IS/WS数据流高比特PSUM访存能耗痛点。引入分组策略抑制量化误差，配套RAE可重构引擎。CV/NLP/LLM测试，PSUM压缩至INT8，精度损失最高0.83，访存能耗降低28%-87%，LLaMA2-7B最高节能31.7倍。

## 背景和动机
1. IS、WS数据流下高比特（INT16/32）中间部分和PSUM频繁读写，占总能耗最高69%，现有量化仅优化权重/激活，忽略PSUM压缩。
2. 现有ReRAM类PSQ仅在ADC阶段压缩，缓存仍存储高精度PSUM，无法削减SRAM/DRAM访存开销。
3. 逐次量化会累积舍入误差，直接压缩PSUM造成模型精度大幅下滑，缺少误差缓解方案。
4. 不同模型、数据流最优分组粒度不同，固定硬件无法适配多样网络，灵活性不足。
5. Transformer、大模型FFN层通道数极大，PSUM位宽暴涨，内存能耗瓶颈更突出。

## 相关工作
1. 经典DNN数据流（IS/WS/OS）：仅优化数据复用，未解决PSUM高精度存储带来的能耗问题。
2. 权重/激活量化（INT8/LSQ）：压缩输入输出，不处理累加中间PSUM。
3. ReRAM专用PSQ：仅模数转换阶段压缩，片上缓存仍存高精度PSUM，无访存收益。
4. 固定位宽累加硬件：统一PSUM比特，无法动态适配不同模型误差需求。
5. Transformer专用加速器：优化注意力计算，未针对大规模通道累加的PSUM做软硬件协同压缩。

## 本文解决方案
### 1 增量式APSQ量化算法
递归累加量化，每次将当前乘法结果与上一轮量化增量和合并后再压缩存储，全程仅读写INT8 PSUM，消除高比特缓存读写。
### 2 分组误差抑制策略
将连续PSUM分gs组，每组仅执行一次增量量化，组内仅单次压缩，大幅减少舍入累积误差，平衡精度与访存开销。
### 3 精度感知能耗分析模型
修正传统加速器能耗公式，引入PSUM位宽比例系数β，量化不同数据流、位宽下的内存访问功耗，用于量化收益预估。
### 4 RAE可重构APSQ硬件引擎
搭载多组PSUM缓存、移位缩放单元、多路选择器，通过配置位动态切换gs分组尺寸，仅增加3.21%芯片面积。
### 5 量化感知训练适配
采用LSQ可学习缩放因子，缩放值设为2的幂次，量化/反量化仅用硬件移位，无乘法额外开销。

## 实验分析
1. 实验平台：28nm工艺加速器，测试BERT、Segformer、EfficientViT、LLaMA2-7B，GLUE/ADE20K/零样本常识评测。
2. 精度表现：最优gs配置下BERT精度降0.16%，Segformer mIoU降0.61%，LLaMA2平均精度仅损失0.59%。
3. 能耗收益：IS数据流节能28%~42%；WS场景CV模型最高降低87%能耗，LLaMA2-7B WS模式节能31.7倍。
4. 硬件开销：RAE引擎仅增加86410μm²总面积，整体加速器面积提升3.21%，无显著时序损耗。
5. 消融验证：gs=1误差最大，gs=2~4为通用最优区间；INT4/6精度损失严重，INT8是最优折中方案。

## 研究启发
1. 现有量化研究普遍忽视PSUM能耗，中间累加缓存是IS/WS架构核心功耗优化突破口。
2. 增量递归量化可全程低比特存储中间结果，从根源减少SRAM/DRAM读写次数。
3. 分组机制能显著抑制多次量化带来的累积舍入误差，无需大幅提升硬件开销。
4. 可重构硬件适配多分组粒度，才能兼顾CNN、Transformer、大模型多样化需求。
5. 大语言模型自回归解码单次输出向量，WS数据流下PSUM压缩节能增益极其显著。