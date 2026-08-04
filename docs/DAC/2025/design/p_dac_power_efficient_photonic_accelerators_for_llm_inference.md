---
title: "P-DAC: Power-Efficient Photonic Accelerators for LLM Inference"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# P-DAC: Power-Efficient Photonic Accelerators for LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132618">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132618</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>光子加速器，大语言模型推理，马赫-曾德尔调制器，数模转换器，光子数模转换器，高能效 </p>
</div>


---

## 研究概要
本文提出P-DAC光子数模转换器，替换光Transformer加速器传统电子DAC，依托光信号加权近似驱动MZM调制器，省去电域转换功耗。数学推导验证误差可控，集成Lightening-Transformer后，8bit场景整机功耗降低47.7%，BERT/DeiT推理能耗最高削减35.4%。

## 背景和动机
1. 光子加速器依托MZM实现模拟点积，但传统电子DAC为整机功耗瓶颈，8bit精度下DAC功耗占比超50%，精度越高能耗问题越严重。
2. 传统方案需控制器计算MZM驱动电压，额外引入计算开销，电数模转换链路功耗、延迟双重损耗。
3. LLM推理包含注意力、全连接层大量矩阵乘，对数值误差具备天然容忍度，适配近似型光子信号转换方案。
4. 现有光计算架构未利用WDM波分复用简化DAC链路，无法从底层消除电DAC功耗开销。

## 相关工作
1. 通用光子互联SPRINT/SPACX/CAMON：仅优化片上光传输，未解决MZM驱动DAC功耗问题。
2. 卷积光子加速器Albireo：基于MZI阵列，依赖电子DAC做信号调制，无光子原生DAC优化。
3. Lightening-Transformer：面向Transformer动态点积光子架构，性能优异，但电子DAC功耗占比极高，是核心能效短板。
4. 各类电子DAC芯片：纯电学转换，多比特下功耗激增，不匹配光子计算超低功耗诉求。

## 本文解决方案
### 1 P-DAC硬件架构设计
移除传统电DAC与控制单元，采用MRR波分接收多波长光数字信号，搭配差异化权重TIA阵列叠加模拟电压直接驱动MZM，全光前置转换。
### 2 分段线性近似映射模型
针对MZM非线性余弦传输方程，分段拟合arccos函数，两段线性近似压缩转换误差，最大数值误差仅8.5%，适配LLM容错特性。
### 3 原生WDM协同数据流
复用多比特EO光接口输出光数字信号，经由WDM多路并行送入P-DAC，无需逐路电DAC转换，提升并行度同时削减转换能耗。
### 4 整机协同集成方案
P-DAC分别集成全局存储输出与阵列输入缓冲接口，适配权重驻留、输入流式两类LLM数据流，兼容DDot光点积单元。

## 实验分析
1. 测试基准：对比原生Lightening-Transformer，负载采用BERT-base、DeiT图像Transformer，分4/8bit两种量化精度。
2. 功耗指标：4bit整机功耗下降19.9%，8bit下降47.7%；原架构DAC最高50.94W，P-DAC方案降至26.64W。
3. 推理能耗：8bit下BERT总能耗降低32.3%，注意力层最高节省42.1%；DeiT整体能耗降幅32.3%。
4. 误差验证：转换最大误差8.5%，模型困惑度、分类精度无明显衰减，满足LLM推理精度需求。
5. 瓶颈拆解：优化后激光器成为新功耗主体，为后续光器件优化指明方向。

## 研究启发
1. 光子加速器能效瓶颈并非光计算核心单元，MZM配套电子DAC是易被忽视的高功耗模块，可通过全光转换替代。
2. 利用模型数值容错特性，采用分段线性近似能大幅简化光-模拟转换电路，硬件代价极低。
3. WDM波分复用不仅用于数据传输，还可复用为并行数模转换通道，消除多路独立DAC开销。
4. 光计算软硬件协同需打通存储-调制-计算全链路，单一计算单元优化收益有限。
5. 高精度量化场景下电子DAC功耗膨胀更显著，P-DAC类光子原生转换架构收益随位宽提升持续放大。