---
title: "Towards In-Situ Neuromorphic Computing Architecture for Event Stream Super-Resolution"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Towards In-Situ Neuromorphic Computing Architecture for Event Stream Super-Resolution

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11133248">https://ieeexplore.ieee.org/abstract/document/11133248</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 脉冲神经网络，硬件加速器，超分辨率，事件相机 </p>
</div>


---

## 研究概要
本文面向低分辨率事件相机，首个软硬件协同设计脉冲神经网络超分辨加速器。算法简化SRM神经元、重排卷积时序、定点量化；硬件提出分层架构、KCTR数据流与双流水线实现原位计算，消除层中间存储。28nm流片500MHz，相较GPU提速95.6%，突触操作能耗仅0.546pJ，下游分类精度超98.8%。

## 背景和动机
1. 事件DVS相机具备高时序、高动态范围，但像素电路占用面积大，空间分辨率普遍偏低，限制视觉任务性能。
2. 现有事件流超分辨仅停留在GPU软件算法，无专用神经形态硬件，边缘端实时、低功耗需求无法满足。
3. SRM神经元指数核硬件实现复杂，时空卷积计算顺序原始设计访存、计算开销巨大。
4. 脉冲网络层间脉冲中间缓存量大，片上存储与数据搬移带来显著时延、功耗损耗。
5. 缺少适配事件三维时空数据的并行硬件数据流，传统NPU无法兼顾事件稀疏与时序特性。

## 相关工作
1. 事件超分辨软件算法(Neurocomputing/ICCV)：基于GPU浮点SNN，推理耗时数十毫秒、功耗30W，不适配边缘嵌入式设备。
2. 通用SNN神经形态加速器：面向图像/关键词分类，无事件流上采样、插值专用模块，不支持3D时空事件处理。
3. LIF基础脉冲硬件：精度不足，未采用带不应期SRM神经元，难以完成精细事件重建任务。
4. 帧图像超分辨ASIC：输入为稠密帧，无法适配异步稀疏事件脉冲数据流。
5. 事件相机处理芯片：仅做基础滤波，无SNN超分辨推理计算通路。

## 本文解决方案
### 1 硬件友好SNN超分辨算法
采用SRM神经元；调换时空卷积计算顺序降低累加开销；指数响应核离散截断为有限序列；权重8bit定点量化，近邻插值完成4倍上采样。网络含2卷积+1反卷积+插值融合模块。
### 2 分层并行硬件架构
三级分层设计：顶层全局控制；中层多通道并行PE阵列；底层卷积/神经元/插值专用计算单元，多通道独立权重寄存器复用时序核存储。
### 3 KCTR四维有序数据流
按核-通道-时间戳-行顺序调度事件数据，配套四层计数器同步流水线，逐行滑动分块并行卷积，统一地址生成减少重复读取。
### 4 双层双流水线原位计算
层内微流水线完成单卷积-神经元串行运算；层间宏流水线实现多层并行处理，无需缓存完整中间脉冲，仅按行分段存储，大幅削减SRAM占用。
### 5 事件双通道分离处理
正负亮度事件分为两路独立流并行计算，插值与卷积分支结果融合输出高分辨率事件流。

## 实验分析
1. 实验环境：28nm CMOS，0.9V 500MHz；测试N-MNIST、ASL-DVS事件数据集，对比GPU软件SNN与多款SNN专用ASIC。
2. 重建精度：ASL-DVS RMSE低至0.121，N-MNIST为1.296；下游分类精度分别达99.73%、98.84%。
3. 速度性能：N-MNIST单样本1.69ms、ASL-DVS 22.37ms，相比GPU提速86.4%/95.6%。
4. 硬件指标：芯片面积3.61mm²，片上内存21.45kB，单突触运算能耗0.546pJ，优于同工艺主流SNN加速器。
5. 消融对比：KCTR数据流+双流水线协同可减少70%层间脉冲存储，原位计算是低时延核心。

## 研究启发
1. 事件相机超分辨必须软硬件协同，仅GPU浮点算法无法满足边缘低功耗实时约束。
2. SRM神经元指数核可离散截断量化，在几乎无损精度下大幅降低硬件计算复杂度。
3. 面向三维时空稀疏事件，定制四维有序数据流能最大化PE并行度，减少重复访存。
4. 分层双层流水线实现原位计算，是削减脉冲中间缓存、降低存储功耗的关键思路。
5. 神经形态硬件需配套专用上采样插值单元，通用SNN加速器无法适配事件超分辨重建需求。
