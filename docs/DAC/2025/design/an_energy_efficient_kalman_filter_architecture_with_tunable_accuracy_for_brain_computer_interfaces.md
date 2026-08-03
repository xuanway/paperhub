---
title: "An Energy-Efficient Kalman Filter Architecture with Tunable Accuracy for Brain-Computer Interfaces"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# An Energy-Efficient Kalman Filter Architecture with Tunable Accuracy for Brain-Computer Interfaces

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://sld.cs.columbia.edu/pubs/eichler_dac25.pdf">https://sld.cs.columbia.edu/pubs/eichler_dac25.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 卡尔曼滤波，片上系统，加速器设计，脑机接口，FPGA</p>
</div>

---

## 研究概要
本文面向脑机接口(BCI)运动解码，提出可配置卡尔曼滤波硬件KalmMind。设计高斯精确求逆与牛顿迭代近似交替计算方案，通过寄存器细调精度、时延权衡。基于RISC-V异构SoC在FPGA验证，相较通用处理器能效提升15.3倍，精度最高提升千倍，适配多类神经数据集。

## 背景和动机
1. 植入式BCI电极通道持续增多，高维神经信号需实时卡尔曼滤波解码运动，但植入芯片功耗、散热严格受限，通用处理器无法满足低时延低功耗需求。
2. 卡尔曼滤波核心瓶颈为矩阵求逆，传统高斯消元复杂度高、串行依赖强，现有近似方法精度损失过大，不满足精细肢体控制。
3. 现有卡尔曼硬件面向通用场景，无法适配神经信号时空相关性，缺少精度与时延的可调硬件机制，难以适配不同脑区数据集。
4. BCI系统分为植入采集端与外接中继站，中继站带宽、功耗约束严苛，亟需专用可调滤波加速器。

## 相关工作
1. 软件卡尔曼方案：CPU/GPU执行高斯求逆，算力功耗极高，无法部署于移动BCI中继设备。
2. 通用KF硬件：泰勒、稳态SSKF、无逆IFKF等单一近似架构，仅固定精度，无法动态折中时延误差。
3. 通用矩阵求逆硬件：高斯、乔列斯基、QR分解流水线，计算开销大，未利用神经信号时序相关性做迭代优化。
4. BCI专用计算平台SCALO：仅采用标准高斯求逆，无近似交替加速，算力与能效存在明显短板。

## 本文解决方案
### 1. 卡尔曼算法模块化重构
拆分预测、更新、卡尔曼增益计算模块，解耦矩阵求逆与观测向量运算，实现增益计算与信号加载并行执行，支持替换各类求逆通路。
### 2. 高斯-牛顿交替矩阵求逆机制
利用神经信号强时空相关性，设计两套硬件通路：通路A高斯精确求逆；通路B牛顿迭代近似。通过配置参数calc_freq控制精确计算周期，搭配两种初值种子策略提升收敛精度。
### 3. 全参数可配置硬件架构
加速器分为加载、计算、存储三级，7组内存映射寄存器调控维度、迭代次数、近似层数、求逆切换频率；本地多组双缓存存储状态矩阵，DMA批量读写降低访存开销。
### 4. 异构SoC集成方案
基于ESP瓦片片上网络，搭配CVA6 RISC-V处理器，支持Linux软件调用加速器，兼容32/64位定点、浮点数据通路，提供轻量化极简LITE、SSKF专用子架构。

## 实验分析
1. 实验平台：XCVU440 FPGA，78MHz，三类非人灵长类、大鼠脑电神经数据集，对比i7、裸CVA6与各类KF硬件。
2. 精度表现：可大范围调节MSE误差，牛顿迭代可消除高斯浮点误差，海马数据集精度最高提升78%，存在多组帕累托最优配置。
3. 性能与能效：Gauss-Newton架构相较CVA6能效提升655倍，相较桌面CPU提升15.3倍；SSKF轻量化架构能效最优但精度损失显著。
4. 硬件开销：浮点架构LUT约22k、DSP252，峰值功耗0.185W，全部架构功耗低于200mW，符合BCI中继功耗上限。
5. 扩展性：可适配运动皮层、体感皮层、海马多类数据集，支持自定义迭代层数与精确计算间隔。

## 研究启发
1. BCI专用硬件不能采用固定精度算子，必须设计可配置通路，针对不同脑区神经数据动态折中精度、时延、功耗。
2. 利用神经信号连续帧时空相关性，交替精确/近似矩阵求逆是低开销加速思路，牛顿迭代无除法更适合硬件流水线。
3. 算法模块化解耦设计便于硬件迭代替换求逆通路，兼顾通用性与专用优化收益。
4. 异构RISC-V+专用加速器架构是无线穿戴BCI中继站最优方案，远优于通用CPU/GPU。
5. 硬件设计需提供多档轻量化子架构，可根据假肢控制精度需求灵活选择高能效或高精度模式。