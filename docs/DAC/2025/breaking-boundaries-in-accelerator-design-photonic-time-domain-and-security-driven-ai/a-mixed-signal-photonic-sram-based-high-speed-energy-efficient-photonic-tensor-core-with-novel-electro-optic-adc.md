---
title: "A Mixed-Signal Photonic SRAM-based High-Speed Energy-Efficient Photonic Tensor Core with Novel Electro-Optic ADC"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# A Mixed-Signal Photonic SRAM-based High-Speed Energy-Efficient Photonic Tensor Core with Novel Electro-Optic ADC

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2506.22705">https://arxiv.org/abs/2506.22705</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>光子存储器，存内计算，光子模数转换器，微环谐振器，张量核心 </p>
</div>


---

## 研究概要
本文基于GF45SPCLO工艺，提出混合信号多比特光子张量核。设计差分耦合pSRAM存储权重，利用WDM实现并行光向量乘；独创独热编码光电eoADC完成光模拟信号数字化。整套架构权重更新速率达20GHz，算力4.10TOPS，能效3.02TOPS/W，适配AI矩阵乘运算。

## 背景和动机
1. 传统冯诺依曼架构存在存储墙，电学SRAM/NVM随工艺缩小，互连线电容、电阻恶化，带宽与能效受限。
2. 光子计算依靠波分复用具备高速低串扰优势，但现有光子计算存在短板：MZI面积大、PCM写延迟高、MRR易受温度干扰。
3. 现有光子阵列依赖片外电学ADC，光模拟输出转换环节成为性能瓶颈，缺少片上集成低功耗光电模数转换方案。
4. 多数光子权重存储器件更新速度慢，无法满足大模型在线微调、高频权重刷新场景需求。

## 相关工作
1. MZI光子核心：计算速度快，但器件面积大，难以大规模扩展矩阵运算阵列。
2. PCM基光子存算：可缩小面积，但写入延迟、能耗高，不适合频繁更新权重的任务。
3. MRR光子张量核：集成度高，但无配套片上ADC，模拟光信号需片外转换，吞吐受限。
4. 传统Flash/时分电学ADC：温度计编码激活大量比较器，功耗极高，时分架构存在同步误差，不匹配光子高速数据流。

## 本文解决方案
### 1. 差分耦合pSRAM存储单元
采用双微环谐振器交叉耦合光电锁存结构，差分光波实现快速读写，单次更新仅0.5pJ，权重更新速度20GHz，兼容多比特权重编码。
### 2. WDM混合信号向量乘阵列
基于波分复用，多波长并行输入光强度信号；多级功率分路生成2的幂次缩放输入，MRR由pSRAM控制实现1bit光乘，光电二极管累加得到向量乘模拟光电流。
### 3. 独热编码光电eoADC
多MRR对应不同参考电压阈值，输入电压仅激活单条光路通路，单阈值模块工作大幅降低功耗；搭配TIA、ROM天花板译码电路消除边界编码冲突，采样速率8GS/s。
### 4. 可扩展二维光子张量核
复用向量乘宏单元搭建矩阵计算阵列，多组并行处理；光模拟累加后经eo统一数字化，全光-电片上集成，无需片外转换模块。

## 实验分析
1. 器件仿真：GF45SPCLO工艺验证pSRAM，50ps光脉冲即可完成权重改写，稳定保持存储电平。
2. 向量乘测试：MRR不同环长分离4条无串扰波长通道，归一化光输出与理论乘值高度拟合。
3. eoADC性能：8GS/s采样，单次转换能耗2.32pJ，DNL误差极小无缺失编码，边界输入译码无冲突。
4. 整机指标：16×16张量核算力4.10TOPS，能效3.02TOPS/W；对比同类光子IMC，能效、权重刷新速度大幅领先。

## 研究启发
1. 光子存算系统瓶颈不在光乘阵列，光模拟信号片上模数转换是关键优化靶点，光电一体化设计可消除片外传输开销。
2. 交叉耦合光电存储单元兼顾高速刷新与低能耗，解决传统光子权重器件更新慢的痛点，适配在线训练。
3. 独热编码MRR型ADC相比传统电学ADC，可大幅降低同时激活电路数量，适配光子高速连续模拟数据流。
4. WDM多路并行光运算搭配多级功率分路，能以低成本实现多比特权重混合信号乘法，提升阵列并行度。
5. 单片硅光子工艺可集成存储、计算、转换全套模块，为大模型高吞吐低功耗推理提供可行硬件路线。