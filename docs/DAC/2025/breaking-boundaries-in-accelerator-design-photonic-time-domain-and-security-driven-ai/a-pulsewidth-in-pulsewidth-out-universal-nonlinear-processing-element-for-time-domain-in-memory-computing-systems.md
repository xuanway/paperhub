---
title: "A PulseWidth-IN-PulseWidth-Out Universal Nonlinear Processing Element for Time-Domain In-Memory Computing Systems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# A PulseWidth-IN-PulseWidth-Out Universal Nonlinear Processing Element for Time-Domain In-Memory Computing Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2A: In-memory and Near-memory Computing Circuits</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133182">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133182</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 时域存内计算，通用非线性处理单元，神经网络训练，阻变存储器</p>
</div>

---

## 研究概要
本文面向时域存算(TD-IMC)跨域转换能耗高的痛点，提出脉宽输入输出通用非线性单元PIPO-UNPE。设计两层RRAM-ReLU硬件网络，搭配DLRSE训练策略，自研两类脉冲可编程电流源与低偏差VTC。130nm仿真功耗912μW、吞吐10M NOPS，嵌入TD-IMC后能效提升9.5~25倍，推理精度损失低于0.1%。

## 背景和动机
1. 时域存算仅优化MAC线性运算，激活、梯度等非线性计算依赖数字单元，需频繁TDC/ADC跨域转换，功耗开销巨大。
2. 现有模拟非线性单元基于多项式CMOS电路，依赖DAC生成系数，功耗高、支持函数种类少，通用性差。
3. 基础两层ReLU网络拟合精度不足，传统训练参数量庞大，映射硬件后面积、能耗显著上升。
4. 现有VTC电路存在传输延迟偏差，造成脉宽转换误差，降低非线性运算整体拟合精度。

## 相关工作
1. 数字非线性单元（GEBA、NN-LUT、NACU）：全数字实现，需频繁模数转换，能效低、硬件复用性差。
2. 传统模拟多项式电路：依赖DAC配置多项式权重，仅支持少量激活函数，拓展性弱。
3. 早期ReLU拟合网络：朴素反向传播训练，拟合精度低，参数量庞大，不适合硬件映射。
4. 现有TD-IMC加速器（TIMELY）：无线上原生非线性单元，所有激活运算均转出数字域，数据搬运能耗极高。

## 本文解决方案
### 1. DLRSE动态子集增强训练算法
静态均匀锚定数据集+动态损失采样数据集，基于加权核密度估计在高损失区域加密采样，大幅降低ReLU网络参数量，提升函数拟合效率。32隐层仅97个参数，拟合精度显著提升。
### 2. R-PPCS双类型脉冲可编程电流源
R-PPCS-A适配小规模隐藏层阵列，稳定单路电流；R-PPCS-B共享缓冲电路适配大规模输出层阵列，降低MOS与功耗开销，完成时域脉冲乘累加。
### 3. 两类低色散VTC转换电路
DIDO-VTC处理隐藏层差分电压转脉宽，SIDO-VTC处理输出单端电压转脉宽；采用恒定gm比较器抑制传输延迟偏差，六阶多项式补偿转换误差。
### 4. 两级流水线PIPO-UNPE硬件
两层RRAM-ReLU电路级联，分充电保持、转换、复位三阶段；全时域脉宽输入、脉宽输出，无需跨域模数转换，原生支持ELU/GELU/Tanh等12类非线性函数。

## 实验分析
1. 算法消融：DLRSE相较传统训练，权重效率提升近百倍，同等精度参数量仅对比方案1.67%。
2. 器件特性：RRAM动态范围43dB，等效7bit精度，128电导态循环稳定性良好。
3. 单元硬件：130nm工艺面积10516μm²，总功耗912μW，非线性吞吐10M NOPS。
4. 模型测试：MobileViT/YOLOv8等网络使用该单元，精度损失≤0.1%，优于8bit量化激活。
5. 系统增益：集成至TIMELY时域存算，各模型系统能效提升9.5~25倍，大幅削减跨域转换能耗。

## 研究启发
1. 时域存算系统瓶颈不在线性MAC，而在非线性运算的跨模数数据转换，全时域统一非线性单元可根除该开销。
2. 轻量两层ReLU网络可作为通用模拟非线性拟合器，配合动态采样训练能以极低硬件开销实现多激活兼容。
3. 分规模设计存储电流源，大小阵列采用不同缓冲架构，可同时兼顾精度与硬件面积、功耗。
4. VTC转换偏差会大幅降低拟合精度，电路补偿+硬件感知微调训练结合，是低成本精度优化方案。
5. 存算加速器软硬件协同不能只优化线性层，原生模拟非线性单元是提升端到端能效的关键设计环节。