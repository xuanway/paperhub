---
title: "Enhancing Parallelism and Energy-Efficiency in SOT-MRAM based CIM Architecture for On-Chip Learning"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Enhancing Parallelism and Energy-Efficiency in SOT-MRAM based CIM Architecture for On-Chip Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11424425">https://ieeexplore.ieee.org/abstract/document/11424425</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 自旋轨道力矩，多端口存储器，片上学习，神经网络，存内计算</p>
</div>


---

## 研究概要
本文面向片上学习场景，提出多端口SOT-MRAM存内计算架构。设计1写6读新型单元，配套批量写权重更新机制、多向量并行推理调度。45nm工艺仿真，相比传统单端口SOT-CIM，时延降低5.82倍、能效提升3.20倍，仅小幅增加芯片面积。

## 背景和动机
1. 冯诺依曼内存墙制约边缘AI实时学习，SOT-MRAM兼具高速、非易失优势，但传统单端口CIM并行度极低。
2. 现有SOT-CIM训练时逐单元更新权重，写周期极多；推理单次仅处理一组向量，阵列硬件利用率差。
3. STT/ReRAM器件读写电流不对称，难以实现批量并行写，而SOT读写通路天然隔离、电流对称，潜力未被挖掘。
4. 现存多端口存储设计仅面向缓存，未适配DNN前向传播、反向梯度、权重更新全链路并行需求。

## 相关工作
1. 单端口SOT-MRAM CIM：单元读写串行，训练权重逐次编程，推理向量串行计算，吞吐与能效偏低。
2. ReRAM并行MAC架构：器件读写电流不对称，无法大规模批量写，仅提升推理并行、不优化训练。
3. 多端口SRAM存内学习：存储密度低，片上模型容量受限，功耗高于自旋器件。
4. 专用转置存储学习核：寄存器阵列面积开销大，多轮梯度计算访存频繁，实时性差。

## 本文解决方案
### 1. 1写6读多端口SOT存储单元
新增多路读晶体管，读写通路完全分离；利用SOT电流对称特性，支持6组向量并行点积，45nm版图面积可控。
### 2. 批量写权重更新机制
统计待翻转权重单元，动态匹配最优并行写数量，自适应调节驱动电流；分批次批量置1/置0，大幅缩减反向传播更新周期。
### 3. 多向量并行推理调度
多组输入同时接入不同读端口，阵列并行执行多路VMM，搭配5bit SAR ADC、分层累加单元同步汇总计算结果。
### 4. 全链路控制调度电路
集成输入编码、梯度计算、批量写控制有限状态机，统一调度前向、误差、梯度、权重更新四阶段操作。

## 实验分析
1. 仿真环境：45nm GPDK工艺，128×128 SOT阵列，VGG8+CIFAR10，DNN+Neurosim仿真框架。
2. 并行上限：单单元最多同步6路读写，批量写单次可并行6个存储单元，驱动电流953μA。
3. 性能对比：相比传统1R1W架构，总时延下降5.82倍，推理能效提升3.20倍，推理吞吐达3.17 TOPS。
4. 硬件代价：阵列总面积提升2.67倍，权重梯度计算仍是能耗与时延主要占比模块。
5. SOTA对比：训练能效3.49 TOPS/W，优于SRAM与标准SOT-MRAM同类CIM方案。

## 研究启发
1. SOT-MRAM读写电流对称、通路隔离是实现批量并行写的独特硬件优势，区别于STT、ReRAM等器件。
2. 片上学习瓶颈集中在权重更新阶段，仅优化推理并行无法大幅提升整体性能，训练写并行是关键突破口。
3. 多端口单元可多路并行VMM，充分挖掘交叉阵列并行潜力，适合多输入、多特征视觉推理任务。
4. 并行端口数量存在硬件边界，过多读端口会缩小读出裕度，6路是精度与吞吐最优平衡点。
5. 器件单元电路创新搭配顶层调度控制，才能同时解决训练、推理两端的并行度短板。
