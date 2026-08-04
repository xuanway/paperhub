---
title: "ResISC: Residue Number System-Based Integrated Sensing and Computing for Efficient Edge AI"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ResISC: Residue Number System-Based Integrated Sensing and Computing for Efficient Edge AI

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132797">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132797</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 余数系统，集成感知与计算，SOT-MRAM，混合基数单元，通道停用</p>
</div>


---

## 研究概要
本文提出基于余数系统(RNS)的端侧感知计算一体化架构ResISC，集成片上余数编码器、SOT-MRAM近存CNN引擎与混合基数单元。设计双通道选择性通道关闭优化，CIFAR-10精度达94.63%，计算量最高缩减89%，相较主流PIM平台功耗提升3.4倍、运行速度最高提速71倍。

## 背景和动机
1. 传统视觉端侧架构传感器、ADC、计算单元分离，模数转换数据量大，带宽与功耗开销严重，依赖云端推理带来延迟与隐私风险。
2. 二进制CNN计算进位链长、乘加时延高，现有RNS加速器需频繁二进制/RNS互转，跨模激活运算硬件开销巨大。
3. 现存近存PIM仅优化存储计算，未从传感器源头减少原始图像数据传输，整体能效提升有限。
4. 主流RNS网络缺少传感器端原生编码方案，前端ADC精度与功耗无法适配余数并行特性。

## 相关工作
1. 感知内计算PIS/PNS：仅在像素内实现简单滤波，无完整RNS CNN推理链路，ADC功耗未优化。
2. 通用MRAM-PIM(SCiMA/IMCE)：基于二进制运算，图像原始数据全部传入内存，前端传输开销高。
3. RNSnet/Res-DNN：仅在内存侧实现RNS卷积，传感器仍输出二进制，跨模激活依赖专用复杂硬件。
4. 嵌套RNS/FPGA-RNN：频繁进制转换抵消并行收益，无法适配端侧低功耗实时场景。

## 本文解决方案
### 1 片上折叠式RNS模数转换器
改造折叠ADC模拟域直接输出余数，省去全局二进制转换；多组折叠电路搭配异或阵列并行生成多模余数，降低ADC功耗与位宽需求。
### 2 两级通道压缩控制单元(CA)
一级关闭冗余RGB色彩通道；二级独立关闭低贡献RNS模通道，对应ADC、计算子阵列同步断电，大幅削减冗余运算。
### 3 SOT-MRAM RNS卷积引擎(RCE)
选用{7,8,15}最优模集，多余数通道并行原位乘加，利用MRAM单周期加法特性，全卷积层驻留余数数据无需进制切换。
### 4 轻量化混合基数单元(MRE)
基于模集特性快速提取符号位实现ReLU，内置缩放单元抑制溢出，统一处理跨模激活、归一化，消除传统跨模巨大硬件开销。

## 实验分析
1. 仿真环境：45nm工艺，ResNet18，测试MNIST/SVHN/CIFAR10/CIFAR100，对比RNSiM、Pinatubo等PIM与RNS加速器。
2. 精度表现：CIFAR10最高94.63%，相比32bit FP仅下降0.37%；关闭单通道精度降幅低于4%。
3. 性能指标：相较SCiMA/IMCE/Pinatubo执行速度分别提升6.4×/30×/71×，整体功耗优化3.4倍。
4. 压缩收益：两级通道关闭最高减少89%计算量，单模关闭可降低40%功耗。
5. 电路开销：MRE为主要功耗单元，ADC相较传统8bit Flash功耗降低19%、延迟缩短50%。

## 研究启发
1. 感知计算一体化优化必须从传感器源头切入，模拟域原生RNS编码可彻底削减图像原始数据传输开销。
2. 适配的专用模集能极大简化跨模激活运算，省去复杂反向转换硬件，释放RNS并行算力优势。
3. 视觉任务RGB与余数通道存在大量冗余，分层动态断电是低成本低功耗优化核心手段。
4. 新型非易失SOT-MRAM与RNS天然适配，并行余数运算可充分发挥存内单周期加法优势。
5. 端侧低功耗视觉推理不能仅优化计算层，传感器、模数转换、近存计算需全链路协同设计。