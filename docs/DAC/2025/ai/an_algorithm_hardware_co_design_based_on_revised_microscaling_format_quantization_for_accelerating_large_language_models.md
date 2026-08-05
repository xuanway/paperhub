---
title: "An Algorithm-Hardware Co-design Based on Revised Microscaling Format Quantization for Accelerating Large Language Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# An Algorithm-Hardware Co-design Based on Revised Microscaling Format Quantization for Accelerating Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132485">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132485</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，微缩放格式，加速器，两级量化 </p>
</div>


---

## 研究概要
本文提出软硬件协同LLM加速方案RMFQ量化算法与RMFA专用加速器。设计两层修正微缩放RMX格式，创新分组方向适配通道离群值；配套适配脉动阵列与硬件编码器。OPT/LLaMA等模型验证，4/6比特量化达到SOTA精度，RMFA相较OliVe提速1.28倍、能耗降低31%，硬件面积开销仅2%。

## 背景和动机
1. LLM激活存在少量极端离群值，传统INT低精度量化精度严重衰减，8bit量化存储与算力开销仍偏高。
2. 现有离群感知量化采用坐标/OVP配对存储，内存非对齐、控制单元面积开销大，硬件适配性差。
3. 原生MX微缩放格式仅单层分组，等效位宽偏高，且缺乏配套专用硬件架构，GPU仿真落地困难。
4. 主流逐token分组无法适配通道级离群分布，矩阵乘硬件GEMM内核难以兼容通道分组逻辑。
5. 现有量化加速器未针对微缩放共享指数做MAC定制，指数移位计算带来额外时延与能耗。

## 相关工作
1. 传统整数量化（INT8/4）：逐张量缩放，无法处理通道离群，大模型困惑度暴涨。
2. 离群感知量化GOBO/OLAccel：坐标列表存储离群，内存访问不对齐，硬件面积开销超50%。
3. OliVe：OVP成对量化，硬件开销降至4%，但未采用微缩放格式，压缩上限有限。
4. MX微缩放标准：单层分组，等效位宽高，无面向LLM的通道分组优化，无专用加速硬件。
5. ANT自适应数据类型：每层切换数值格式，但未设计两层缩放，共享指数硬件支持缺失。

## 本文解决方案
### 1 RMX修正微缩放数据格式
双层缩放架构：全局张量缩放+分组共享指数；支持混合INT/Float4/6比特，引入等效位宽指标优化存储，大幅降低分组指数开销。
### 2 RMFQ两层后训练量化算法
第一层全局张量缩放压缩数值区间；第二层沿通道分组提取共享指数，针对性处理通道离群；以MSE为损失搜索每层最优RMX精度，无需重训练。
### 3 RMFA自适应脉动阵列硬件
阵列按最小分组分Tile并行计算；MAC单元集成三输入移位器，合并权重与激活共享指数统一移位，流水线传递分组指数降低通信。
### 4 硬件友好RMX编码器
FP16非线性输出经截断、前导1检测生成4bit共享指数；分组移位后截断至目标位宽，编码逻辑轻量化，面积仅0.03mm²。
### 5 完整软硬件协同链路
软件完成分层混合精度量化与分组预处理；硬件脉动阵列+片上三级缓存配合编码器，统一处理4/6bit RMX推理，兼容主流Transformer。

## 实验分析
1. 实验配置：OPT/GPT2/LLaMA系列大模型、ResNet；28nm工艺DC综合，cycle级Dnn Weaver仿真，基线ANT/OliVe/OLAccel。
2. 量化精度：6bit RMFQ接近FP16基线，困惑度涨幅<3.4%；4bit全面超越现有4bit量化方案，小模型精度优于INT8。
3. 硬件指标：RMFA总面积3.09mm²，功耗472.5mW，相比OliVe面积开销减半至2%。
4. 性能能耗：同精度下相对OliVe提速1.28倍，能耗下降31.4%；对比ANT提速3.13倍、能耗降58%。
5. 消融验证：分组尺寸8–64精度损失极小；通道分组比token分组更适配离群场景，编码器硬件开销可忽略。

## 研究启发
1. 双层张量+分组缩放的微缩放格式，可在无损精度前提下降低等效存储位宽，优于单层MX。
2. LLM离群值集中在通道维度，激活采用通道分组是低比特量化精度提升关键。
3. 微缩放共享指数需定制移位MAC单元，通用脉动阵列无法充分发挥压缩收益。
4. 软硬件协同设计要同步优化量化分组逻辑与硬件数据流，单一算法或硬件优化增益有限。
5. 轻量化前导1硬件编码器可在线生成分组指数，避免离线存储大量缩放参数，降低片上缓存压力。
