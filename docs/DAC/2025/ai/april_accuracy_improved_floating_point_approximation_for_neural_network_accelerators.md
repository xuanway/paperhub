---
title: "April: Accuracy-Improved Floating-Point Approximation For Neural Network Accelerators"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# April: Accuracy-Improved Floating-Point Approximation For Neural Network Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://soldierchen.github.io/assets/pdf/April-DAC25.pdf">https://soldierchen.github.io/assets/pdf/April-DAC25.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://github.com/CLabGit/April">https://github.com/CLabGit/April</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 浮点近似，现场可编程门阵列 </p>
</div>


---

## 研究概要
本文提出April软硬件协同框架，基于对数近似FPMA浮点乘法，设计下采样误差补偿与灵活偏置机制，配套可配置脉动阵列。适配FP8/FP16/BF16多种浮点格式，FPGA实测相较INT8阵列面积降低34%-52%，矩阵RMSE最高下降96%，图像模型精度持平甚至优于INT8方案。

## 背景和动机
1. 神经网络浮点乘法硬件开销巨大，Mitchell对数近似FPMA可将乘法转为整数加法，但原生FPMA误差严重，模型精度大幅下跌。
2. 现有细粒度误差补偿存储开销极高，轻量补偿方案校正能力不足，无法兼顾精度与硬件成本。
3. 权重、激活数值分布差异显著，统一指数偏置无法适配两类数据，进一步放大计算误差。
4. 暂无完整硬件架构融合优化FPMA，缺乏自动化设计工具平衡精度、面积、位宽三者折中。
5. 各类FP8/E2M5~E4M3等格式误差分布特性不同，缺少通用自适应校正方案。

## 相关工作
1. 基础Mitchell FPMA：仅利用对数近似简化乘法，无误差校正，各类网络精度衰减严重。
2. 细粒度查表补偿：逐mantissa组合存储修正值，存储随尾数位数爆炸，硬件LUT开销极高。
3. 固定偏置浮点近似：权重与激活共用指数偏移，无法匹配两者数值分布，误差偏大。
4. INT8量化加速器：依靠整数乘加，乘法单元面积远大于优化后FPMA阵列。
5. 单一浮点格式专用硬件：无跨FP8/BF16/FP16通用适配能力，可移植性差。

## 本文解决方案
### 1 下采样式误差补偿算法
利用误差热力图局部相似性，将尾数空间分K×K窗口，窗口均值作为统一补偿值；仅存储压缩后小尺寸LUT，k=3时仅需单LUT6，大幅削减存储开销，全浮点格式通用。
### 2 自适应灵活偏置机制
分别为权重、激活配置独立指数偏置，匹配两者数值分布区间；推导带差异化偏置的对数近似公式，保证近似计算数学自洽，缩小数值截断误差。
### 3 优化FPMA-MAC脉动单元
输出驻留脉动阵列，每个MAC集成三元加法器、压缩补偿LUT、灵活偏置模块；提取尾数高k位索引查表，补偿值直接并入加法链路，无额外流水线延迟。
### 4 April软硬件协同生成框架
四步自动化流程：①按张量分布选最优偏置；②生成不同k值补偿表；③精度仿真筛选折中参数；④输出可综合RTL脉动阵列代码。
### 5 多浮点格式统一适配
框架原生支持FP8(E2M5/E3M4/E4M3/E5M2)、FP16、BF16，自动匹配对应误差热力与补偿窗口尺寸。

## 实验分析
1. 实验平台：RTX3090仿真精度，AMD Alveo U250 FPGA评估硬件，测试MobileNetV2、FastViT、DeiT等ImageNet模型。
2. 误差指标：补偿后平均绝对误差下降74%~81%，FP8-E4M3可完全消除计算误差，大位宽浮点RMSE最高降低96%。
3. 硬件开销：同等并行度下，April阵列比INT8节省34%~52% LUT；相较细粒度补偿方案硬件开销线性增长，无爆炸式上升。
4. 模型精度：优化FPMA搭配灵活偏置后，网络Top-1精度接近FP8基准，多数场景优于INT8量化推理。
5. 参数消融：补偿因子k越大精度越高，但LUT开销上升，k=3为通用最优折中配置。

## 研究启发
1. FPMA近似误差具备空间局部性，下采样均值查表是低硬件开销高精度补偿新思路。
2. 权重与激活数值分布天然分离，差异化指数偏置能显著提升近似浮点整体表达能力。
3. 对数近似乘法单元面积远小于标准浮点与INT8乘法器，是边缘FPGA轻量化加速优选路线。
4. 软硬件协同自动化框架可快速遍历精度-面积设计空间，降低专用加速器开发门槛。
5. 不同尾数位宽浮点误差特征差异大，补偿机制需支持自适应窗口尺寸，不可一套方案通用。
