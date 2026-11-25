---
title: "Efficient and Scalable Architectures for Multi-level Superconducting Qubit Readout"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Efficient and Scalable Architectures for Multi-level Superconducting Qubit Readout


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2405.08982v2">https://arxiv.org/abs/2405.08982v2</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>多能级读出，泄漏错误，匹配滤波器，轻量级神经网络，硬件高效架构 </p>
</div>

---

## 研究概要
本文提出适配超导三能级量子比特的可扩展读出架构，融合多类型匹配滤波器与轻量化神经网络。模型规模相较FNN缩减100倍，FPGA资源占用降低60倍，读出时长缩短20%，读出保真度相对提升6.6%，可快速检测泄漏误差，提升量子纠错可靠性。

## 背景和动机
1. 超导Transmon比特易产生|2>泄漏态，泄漏会扩散至相邻比特，严重破坏量子纠错（QEC）奇偶校验结果。
2. 两能级读出方案无法识别泄漏，现有三能级FNN、HERQULES判别模型参数量爆炸，FPGA资源开销巨大、推理延迟高。
3. FNN输出随比特数指数增长，HERQULES三场景判别精度暴跌，二者均难以规模化部署实时泄漏检测。
4. 泄漏检测依赖高精度多级读出，现有方案难以兼顾读出速度、硬件开销与分类保真度，制约容错量子计算落地。

## 相关工作
1. FNN深度读出判别：直接输入原始ADC波形，多能级下参数量指数膨胀，FPGA部署困难但精度尚可。
2. HERQULES混合读出架构：采用基础匹配滤波，仅适配两能级，扩展至三能级后识别准确率大幅下滑。
3. LDA/QDA传统统计判别：硬件开销小，但无法区分弛豫、激发类复杂误差，泄漏识别精度低。
4 专用泄漏抑制电路（LRC）：仅能修复已知泄漏，缺少前端高精度多级读出支撑，修复效果受限。

## 本文解决方案
### 1. 无标定泄漏聚类算法
利用自然泄漏波形均值迹（MTV）谱聚类，无需人工注入泄漏态标定，自动区分|0>/|1>/泄漏|2>三类信号簇。
### 2. 多类型配套匹配滤波器
设计QMF基础态滤波、RMF弛豫误差滤波、EMF激发误差三类滤波器，提取波形特征，最大化信噪比。
### 3. 单比特轻量化NN判别器
放弃全局指数输出，每比特独立小型网络，输入规模多项式增长而非指数，大幅削减参数量与FPGA资源。
### 4. 端到端FPGA读出流水线
解调-滤波-特征提取-轻量化推理全链路硬件适配，缩短单次读出周期，加快QEC循环迭代。

## 实验分析
1. 实验平台：5比特超导芯片实测波形，Xilinx Zynq FPGA综合，45nm工艺功耗仿真，对比FNN、HERQULES、LDA/QDA。
2. 精度表现：五比特联合保真度0.905，相对FNN提升6.6%，单泄漏易出错比特识别精度提升1~6%。
3. 硬件开销：LUT使用量仅为FNN的1/60，FF、BRAM、DSP资源均大幅缩减，运行功耗仅1.561mW。
4. 速度指标：单次读出时长缩短20%，表面码QEC总周期降低17%，泄漏推测准确率由0.914提升至0.947。
5. 扩展性：模型输入随比特数多项式扩张，可支撑大规模多比特量子纠错系统实时读出。

## 研究启发
1. 多级量子读出无需全局巨型神经网络，分治单比特轻量化模型可同时解决精度与硬件规模矛盾。
2. 弛豫、激发误差存在独特波形特征，专用匹配滤波可提前提取关键特征，降低NN学习负担。
3. 依靠自然泄漏波形聚类，省去人工标定流程，降低量子比特校准工程复杂度。
4. 读出延迟是QEC性能核心瓶颈，轻量化判别架构可直接缩短纠错循环，抑制泄漏扩散。
5. 量子控制FPGA硬件设计需规避指数规模模型，多项式扩展架构是规模化容错计算必经路线。
