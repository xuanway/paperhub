---
title: "SDISC: A Spike-Driven Human-Machine Interface with In-Situ Computing for Real-Time Low-Power Interaction"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# SDISC: A Spike-Driven Human-Machine Interface with In-Situ Computing for Real-Time Low-Power Interaction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133172">https://ieeexplore.ieee.org/document/11133172</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经形态人机界面，脉冲神经网络，阻变存储器，存内计算，边缘计算</p>
</div>

---

## 研究概要
本文提出SDISC脉冲驱动原位计算人机交互架构，面向EMG肌电信号实时低功耗处理。设计可配置PL-LIF脉冲特征提取、RRAM存内SNN分类器，搭配SAD蒸馏、ALO局部修复缓解器件非理想。实测单样本功耗39.72µW、延迟34µs，长期推理精度稳定约98%。

## 背景和动机
1. 传统帧式人机交互系统缓存大量冗余数据，特征提取功耗占比超41.7%，推理延迟达百毫秒，无法满足穿戴实时需求。
2. 基于ANN的RRAM存内计算依赖稠密帧输入，帧间空闲浪费算力，额外控制器增加能耗。
3. 现有脉冲神经硬件特征提取与分类单元无法复用，电路面积功耗开销大。
4. RRAM电导漂移、长期老化退化会持续降低SNN推理精度，缺少软硬协同长效修复方案。

## 相关工作
1. 帧式RRAM-CIM系统：面向ANN稠密输入，存在大量空闲等待，交互延迟高。
2. 数字脉冲芯片(Xylo/Loihi)：无存内并行MAC，算力与能效远低于RRAM阵列。
3. 差分脉冲编码器：提取与分类模块分离，硬件复用率低，整体成本高。
4. 单一RRAM校正算法：仅短期抑制电导波动，无法解决十余天持续老化退化问题。

## 本文解决方案
### 1 可配置PL-LIF脉冲特征提取模块
简化标准LIF泄漏运算为线性减法，时间常数α可训练复用至提取、分类两层；脉冲编码使数据流稀疏度提升10倍，配套唤醒电路仅在有效信号时启动计算。
### 2 RRAM 1T1R原位SNN分类器
准模拟权重映射，交叉阵列原位完成乘累加，能效4.09TOPS/W；四层PE并行处理，消除数据搬移开销。
### 3 Spike-Activity-Distillation(SAD)蒸馏算法
师生网络两阶段训练，模拟RRAM电导噪声优化神经元时间常数，抵消波动带来脉冲发放偏移。
### 4 Aid-Loser-Only(ALO)局部修复机制
定位精度最差输出神经元对应的存储列，仅修复对应RRAM单元，无需整片重写，大幅降低修复功耗。

## 实验分析
1. 实验平台：180nm工艺8k 1T1R RRAM阵列，Myo八通道EMG手势数据集，对比GPU、传统帧式CIM、数字脉冲芯片。
2. 时延功耗：单样本计算延迟34µW，单样本功耗39.72µs；相较帧式CIM提速9.4倍，GPU快两千余倍。
3. 能效：CIM核心4.09TOPS/W，为GPU的41倍、CPU的430倍。
4. 精度消融：引入SAD后片上精度达98%；连续15天推理搭配AL仅下降0.3%，无修复则跌2.56%。
5. 系统演示：搭建肌电控制小车闭环系统，可实时完成五种手势识别。

## 研究启发
1. 事件脉冲范式天然适配生物时序信号，稀疏编码可从源头削减缓存与计算开销。
2 提取与分类复用同一种脉冲神经元模型，能显著缩减整体硬件面积。
3. RRAM存内计算必须软硬协同，蒸馏预补偿短期噪声、局部修复应对长期老化。
4. 低功耗穿戴交互需分层唤醒机制，空闲时段关闭高算力阵列以降低静态功耗。
5. 面向肌电等时序任务，SNN搭配模拟存内阵列可同时满足低延迟、极低功耗双重边缘需求。
