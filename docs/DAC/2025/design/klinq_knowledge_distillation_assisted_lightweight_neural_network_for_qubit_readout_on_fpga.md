---
title: "KLiNQ: Knowledge Distillation-Assisted Lightweight Neural Network for Qubit Readout on FPGA"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# KLiNQ: Knowledge Distillation-Assisted Lightweight Neural Network for Qubit Readout on FPGA


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.03544">https://arxiv.org/abs/2503.03544</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 超导量子比特，量子比特读出，知识蒸馏，现场可编程门阵列</p>
</div>


---

## 研究概要
本文提出KLiNQ，面向FPGA设计知识蒸馏轻量化神经网络用于超导量子比特独立读出。搭建大教师网络蒸馏两类定制学生模型，支持电路中间测量。Zynq RFSoC验证，模型参数量削减99%，五比特平均读出保真度约0.91，单比特推理仅32ns，硬件资源开销极低。

## 背景和动机
1. 超导量子比特读出速度慢、误差高，是容错量子计算瓶颈，传统MLP读出模型参数量庞大，FPGA部署资源占用严重。
2. 现有HERQULES等方案必须同步批量读取所有比特，无法支持电路中间测量与实时反馈纠错。
3. 主流网络需额外解调预处理，单比特独立部署后精度大幅衰减；量化压缩方案会显著损失判别保真度。
4. 量子相干时间极短，读出推理延迟必须控制在纳秒级，大网络软件推理时延远超约束。

## 相关工作
1. 基准深层FNN：全并行多比特读出，精度高但百万级参数，硬件部署成本极高，不支持独立测量。
2. HERQULES：融合匹配滤波器轻量化网络，仅适配同步批量读出，单比特拆分后精度下滑。
3. 量化压缩读出网络：仅做数值量化，无知识迁移，大幅降低比特判别准确率。
4. SVM/HMM/匹配滤波传统方案：特征提取能力弱，低信噪比量子信号读出保真度不足。

## 本文解决方案
### 1 师生知识蒸馏训练框架
构建大容量教师FNN学习I/Q时序特征；采用硬标签+软标签混合损失蒸馏轻量化学生网络，完整迁移读出判别知识。
### 2 双规格定制学生网络
高信噪比比特用31输入小型FNN-A，噪声比特采用201输入FNN-B，均搭配匹配滤波器提取增强特征。
### 3 轻量化数据预处理流水线
时序I/Q信号区间均值压缩降维，匹配滤波提取单标量特征；除法移位近似归一化，消除FPGA除法器开销。
### 4 单比特独立FPGA并行架构
每比特分配专属推理流水线，PS+PL异构设计，多级加法树、ReLU流水线并行，100MHz时钟下32ns完成判别。

## 实验分析
1. 实验平台：Xilinx ZCU216 RFSoC，实测5超导比特I/Q读出时序数据集，对比基准FNN、HERQULES。
2. 精度表现：五比特几何平均保真度0.904，短750ns读出序列仍维持0.9以上，优于HERQULES独立读出方案。
3. 模型压缩：教师网络814万参数，学生模型仅数千，参数量削减99.89%。
4. 硬件指标：整套流水线32ns推理，各模块LUT/DSP占用率均低于10%，资源开销可控。
5. 消融验证：匹配滤波、均值压缩、知识蒸馏三者共同保障轻量化下读出精度。

## 研究启发
1. 知识蒸馏可在几乎无损读出保真前提下，极致压缩量子读出神经网络规模，适配FPGA资源约束。
2. 单比特独立推理架构是实现中间电路测量、容错量子纠错的核心硬件思路。
3. 按比特信噪比差异化定制网络尺寸，能平衡判别精度与硬件资源消耗。
4. FPGA实现时用移位替代除法、加法树并行求和，可显著降低延迟与DSP占用。
5. 同步批量读出精度更高，但独立读出是规模化容错量子系统必经折中优化方向。