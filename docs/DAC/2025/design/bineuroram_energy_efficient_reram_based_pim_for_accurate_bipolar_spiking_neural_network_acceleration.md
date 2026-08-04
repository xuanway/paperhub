---
title: "BiNeuroRAM: Energy-Efficient ReRAM-Based PIM for Accurate Bipolar Spiking Neural Network Acceleration"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# BiNeuroRAM: Energy-Efficient ReRAM-Based PIM for Accurate Bipolar Spiking Neural Network Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132454">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132454</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经形态硬件，脉冲神经网络，存内处理，异步电路，双极神经元</p>
</div>


---

## 研究概要
本文提出BiNeuroRAM，首款支持ST-BIF双极性神经元的ReRAM存内计算SNN加速器。设计低功耗电压灵敏放大器LPVSA与异步自触发转换器STC，采用无全局时钟微架构，搭配输入/权重稀疏优化。ImageNet ResNet-50准确率达80.9%，相较SOTA吞吐量、能效分别提升2.08倍、2.09倍。

## 背景和动机
1. 传统IF/LIF脉冲神经元硬重置膜电位，存在过发放问题，ANN-SNN转换精度大幅损失，现有硬件无法适配新型ST-BIF双极性神经元。
2. 现有ReRAM-PIM采用电流灵敏放大器CSA或ADC，小阵列读功耗高、面积开销大，制约能效提升。
3. 主流SNN加速器为同步全局时钟架构，脉冲事件稀疏时产生大量无效空转功耗，与事件驱动特性不匹配。
4. 缺乏面向ST-BIF神经元的完整存内计算电路，正负脉冲同步累加、软重置机制难以在模拟阵列实现。

## 相关工作
1. SRAM型SNN-CIM（Neuro-CIM）：无ADC电荷累加，但依赖同步时钟，功耗高，仅支持单极性IF神经元。
2. ReRAM加速器NeuRRAM：搭载高精度ADC，面积功耗代价巨大，不兼容双极性脉冲运算。
3. Tempo-CIM：时域转换存内计算，仅实现LIF神经元，转换后识别精度偏低。
4. 异步数字SNN处理器ANP-I：无存内并行计算能力，访存墙显著，难以部署大规模视觉网络。

## 本文解决方案
### 1. ST-BIF双极性神经元专用异步电路
基于Click握手异步控制器，实现膜电位正负电荷分开累加，支持软重置与脉冲追踪器，生成正负双向脉冲，消除过发放误差，保障ANN-SNN转换精度。
### 2. LPVSA低功耗电压读出放大器
替换传统CSA，采用弱静态电流通路，HRS/LRS读取功耗降低14.7~58.2倍，大幅缩减读出电路面积。
### 3. 无ADC自触发转换器STC
异步脉冲式电荷计数替代模数转换器，分正负两路累加电荷，输出数字膜电位，消除时钟驱动ADC功耗开销。
### 4. 双层稀疏软硬件协同优化
输入脉冲空闲时对CSU功率门控；权重0比特占比高，将低阻HRS映射零权重，降低阵列整体读出能耗。
### 5. 权重固定异步数据流PE架构
8×8网状NoC连接处理单元，ReRAM阵列常驻权重，多时间步异步迭代累加膜电位，充分复用存储带宽。

## 实验分析
1. 实现工艺：28nm CMOS，模拟电路Spectre仿真，数字RTL综合、PrimeTime功耗分析，ReRAM采用实测校准模型。
2. 精度表现：MNIST 99.2%、CIFAR-10 ResNet12达93.7%，ImageNet ResNet-50准确率80.9%，领先同类SOTA最高8.4%。
3. 电路消融：LPVSA相较传统VSA/CSA功耗分别降低14.7/58.2倍；STC替代ADC后系统能效提升46.1倍。
4. 系统性能：对比主流SNN加速器，吞吐量密度提升2.08×，能效提升2.09×，单张ImageNet推理能耗仅2.29μJ。
5. 稀疏收益：输入脉冲平均稀疏度87%，功率门控降低9.2倍空闲功耗；权重比特稀疏进一步削减阵列读出能耗。

## 研究启发
1. IF/LIF神经元存在固有精度缺陷，硬件原生支持ST-BIF双极性脉冲是提升SNN图像识别精度关键路径。
2. 小尺寸ReRAM阵列不宜使用电流读出，电压型灵敏放大器可同时降低功耗与硬件面积。
3. 去除全局同步时钟、采用握手异步电路，能匹配SNN事件驱动本质，消除无效周期功耗。
4. 电荷累加无需昂贵ADC，异步脉冲计数式STC可低成本完成模拟到数字转换。
5. 存内计算优化需结合网络权重、脉冲双层稀疏特性，软硬件协同才能最大化能效收益。