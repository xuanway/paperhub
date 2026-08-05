---
title: "Precon: A Precision-Convertible Architecture for Accelerating Quantized Deep Learning Models across Various Domains Including LLMs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Precon: A Precision-Convertible Architecture for Accelerating Quantized Deep Learning Models across Various Domains Including LLMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133184">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133184</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，量化，脉动阵列，浮点运算，混合精度 </p>
</div>


---

## 研究概要
本文提出Precon可精度转换脉动阵列加速器，设计可拆解指数编码FP16格式，统一MAC单元支持INT4-FP16/INT4-INT8/INT4-INT4三类主流量化模式。复用计算电路、块级移位归一化降低硬件开销，适配LLM、CNN、ViT多模型。全领域测试最高提速4.1倍，能耗降低81.4%，兼顾高精度与极致低比特推理。

## 背景和动机
1. LLM激活存在大量离群值，主流量化分为权重INT4激活FP16（高精度）、全INT低比特（高效）两类，但现有加速器仅支持单一精度组合，通用性差。
2. FIGNA等专用INT-FP硬件仅适配权重量化LLM，无法通用INT4/8纯整数CNN、ViT推理，无法跨域部署。
3. 纯低比特可重构硬件缺少原生FP浮点通路，LLM高精度推理精度大幅衰减。
4. 传统FP/INT两套独立MAC单元硬件面积、功耗开销巨大，缺少逻辑复用的统一计算架构。
5. FP标准格式拆解移位对齐成本高，现有比特拆分方案尾数截断误差大，影响量化推理准确率。

## 相关工作
1. FIGNA：专用INT4-FP16加速器，仅适配LL单权重量化，不支持全整数低比特网络，通用性缺失。
2. BitFusion：比特分片可重构架构，仅面向纯INT计算，无原生FP16浮点通路，LLM精度受损。
3. Sibia：有符号比特切片加速器，仅支持固定整数位宽混合，无法动态切换INT-FP混合运算。
4. 通用FP16脉动阵列：统一浮点计算，低比特权重无法并行利用，算力、存储效率极低。
5. LLM量化算法（AWQ/QQLM）：仅优化数值分布，无配套软硬件协同加速硬件设计。

## 本文解决方案
### 1 指数编码可拆解FP16格式
重构FP16指数域为4倍步进编码，尾数嵌入2bit前导1标识，可拆分为4bit统一数据块；仅损失1bit尾数，指数覆盖范围优于标准FP16，拆解移位仅需4bit固定移位器。
### 2 多模式复用统一MAC计算单元
四组独立4bit乘法器共享通路，区分INT4-FP16/INT4-INT8/INT4-INT4三模式；集成融合对齐加法器，根据指数差自动完成数据块移位累加。
### 3 分块聚合归一化单元
按量化块批量合并多4bit分片，分路径完成整数累加与FP归一化；仅块结束执行归一化，中间计算复用位置寄存器削减归一器功耗。
### 4 输出驻留2D脉动阵列
阵列列末端部署聚合单元，统一/权重双缓冲分离量化权重与激活数据流，片上统一缓冲区减少片外访存频次。
### 5 三模式动态切换流水线
硬件无改动即可切换三类量化计算通路，适配高精度LLM、低比特视觉模型两类推理场景，无需重新综合硬件。

## 实验分析
1. 实验环境：65nm工艺Verilog综合，32×32脉动阵列；测试OPT/LLaMA系列LLM、ResNet、MobileNet、BERT、ViT，对比FP16基线、FIGNA。
2. 精度表现：INT4-FP16模式LLM零样本精度接近全精度，INT4-INT8小幅衰减，纯INT4精度损失明显，符合量化理论预期。
3. 单单元硬件开销：相比纯FP16 MAC面积减少30.1%，功耗降低62.6%；相较FIGNA功耗降低28.6%。
4. 性能与能耗：视觉模型INT4模式最高提速4.1倍，全领域平均能耗降低81.4%；LLM INT4-FP16速度略低于FIG，但通用性更强。
5. 消融验证：指数编码FP16大幅降低拆解误差；块级聚合归一化是削减动态功耗核心优化。

## 研究启发
1. 跨域量化加速器必须同时兼容INT-FP混合与全整数运算，单一精度专用硬件适用场景受限。
2. 改造浮点存储格式实现统一4bit分片，可最大化复用整数计算电路，大幅削减硬件面积开销。
3. 归一化、对齐等高功耗操作可分块延迟执行，仅块输出时触发，能显著降低动态能耗。
4. LLM与视觉网络最优量化位宽存在差异，硬件动态切换精度模式可一套芯片覆盖两类业务。
5. 4bit固定移位器替代可变桶形移位器，是平衡计算误差与硬件成本的轻量化关键设计。