---
title: "YOCO: A Hybrid In-Memory Computing Architecture with 8-bit Sub-PetaOps/W In-Situ Multiply Arithmetic for Large-Scale AI"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# YOCO: A Hybrid In-Memory Computing Architecture with 8-bit Sub-PetaOps/W In-Situ Multiply Arithmetic for Large-Scale AI

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2312.11836">https://arxiv.org/abs/2312.11836</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存内计算，模拟计算，SRAM-ReRAM混合存储器，深度神经网络加速器 </p>
</div>

---

## 研究概要
本文提出YOCO混合ReRAM-SRAM存内计算架构，设计电荷域原位8位乘算IMA与时域累加器，大幅削减ADC/DAC开销。适配Transformer专属流水线，覆盖CNN与大语言模型。电路层面能效123.8 TOPS/W，吞吐量34.9 TOPS；对比主流IMC，平均能效提升3.9~19.9倍，吞吐提升6.8~33.6倍。

## 背景和动机
1. 冯诺依曼架构存在存储墙，大模型海量矩阵乘搬运能耗极高，传统GPU/TPU能效受限。
2. 模拟存内计算(AiMC)依赖大量ADC/DAC，转换器功耗占比最高达85%，成为性能瓶颈。
3. 单一存储IMC难以兼顾：SRAM速度高但密度低，ReRAM高密度但写开销大，无法同时处理静态权重、动态KV矩阵。
4. Transformer注意力包含Softmax、归一化等复杂算子，现有IMC缺少适配数据流，流水线效率低下。

## 相关工作
1. ISAAC：ReRAM模拟阵列，采用位切片拆分计算，ADC/DAC开销巨大，精度损失高。
2. REALLA：双向切片方案，小幅降低DAC代价，但ADC开销依旧突出，整体能效一般。
3. TIMELY：大块阵列减少切片，依赖分时读出，时域处理简单，无法高效处理注意力计算。
4. C-Ladder/C-2C：SRAM基架构，存储容量受限，难以部署LLM大权重矩阵。

## 本文解决方案
### 1 电荷域原位8位乘算IMA单元
复用阵列内电容完成输入转换、逐位乘、并行累加、加权求和全模拟流程，无需输入/权重位切片，从根源减少转换次数。
### 2 时域累加器TDA
阵列模拟电压经VTC转为时序信号叠加，搭配参考列抵消电路延迟，降低ADC使用数量，提升信号裕度。
### 3 混合ReRAM-SRAM分层存储Tile
SIMA使用ReRAM存储静态网络权重，DIMA采用SR存储动态Q/K/V特征，交叉开关实现两类单元高速数据交互，搭配eDRAM缓存中间KV。
### 4 Transformer专用IMC流水线
拆分QK、KV两级矩阵乘，SFU硬件加速指数Softmax，token级流水线掩盖计算延迟，复用KV缓存减少重复运算。
### 5 四层分层硬件架构
芯片-Tile-IMA-MCC四级层次，阵列可动态电源门控，配套专用函数单元与片上高速互联。

## 实验分析
1. 仿真环境：28nm工艺，Cadence模拟电路仿真+Timeloop架构仿真，测试5CNN、5Transformer共10基准。
2. 电路指标：1024×256 8bit VMM，能效123.8 TOPS/W，吞吐34.9 TOPS，模拟MAC误差低于0.98%。
3. 转换单元优化：DAC面积缩减352倍、能耗降9倍；ADC面积/能耗降低98.4%。
4. 整体性能：相较ISAAC/REALLA/TIMELY，平均能效提升19.9×/4.7×/3.9×，吞吐提升33.6×/20.4×/6.8×。
5. 模型推理：模拟噪声带来推理精度损失低于0.61%；注意力流水线相比逐层计算平均提速2.3倍。

## 研究启发
1. AiMC核心瓶颈是数模转换器，复用阵列电容做全电荷域运算可大幅削减ADC/DAC硬件开销。
2. 单一存储介质无法适配大模型动静两类矩阵，ReRAM+SRAM混合架构兼顾密度与实时计算速度。
3. 时域累加相比传统电压累加拥有更高信号裕度，可降低模拟PVT波动带来的精度损耗。
4. LLM加速不能直接复用CNN存内数据流，需针对注意力KV缓存设计专属流水线与硬件SFU。
5. 电荷域原位多比特计算是突破百TOPS/W能效关口的可行路径，适配边缘与云端大规模AI推理。
