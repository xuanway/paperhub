---
title: "3D-CIMlet: A Chiplet Co-Design Framework for Heterogeneous In-Memory Acceleration of Edge LLM Inference and Continual Learning"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# 3D-CIMlet: A Chiplet Co-Design Framework for Heterogeneous In-Memory Acceleration of Edge LLM Inference and Continual Learning


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://engineering.purdue.edu/NanoX/assets/pdf/2025_DAC_3D-CIMlet_AAM.pdf">https://engineering.purdue.edu/NanoX/assets/pdf/2025_DAC_3D-CIMlet_AAM.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> Transformers，内存中心计算，持续学习，异构集成，芯粒</p>
</div>


---

## 研究概要
本文提出3D-CIMlet协同设计框架，面向边缘大模型推理与持续学习，融合RRAM/eDRAM异构存内计算芯粒，搭建热感知、存储可靠性感知多尺度建模工具，配套模型-芯粒映射策略。相较传统2D方案，2.5D、3D架构能效分别提升9.3倍、12倍，EDP最高下降92.5%。

## 背景和动机
1. 边缘设备需同时支持LLM推理与增量持续学习，二者数据流、读写特征差异大，现有硬件难以兼顾两类负载。
2. 单片存内加速器容量受限，无法承载大规模Transformer，传统2D单芯片通信能耗极高，存储墙问题突出。
3. RRAM、eDRAM存储特性天然互补，但缺少异构芯粒协同建模、映射与热分析一体化工具。
4. 现有仿真框架仅支持单芯片或纯推理场景，不支持持续学习反向传播与多工艺芯粒混合设计空间探索。

## 相关工作
1. 单片CIM加速器：基于SRAM/RRAM，仅能部署小型模型，层并行度低，无多芯粒扩展能力。
2. 2.5D芯粒仿真工具SIAM：仅支持RRAM存内推理，缺失持续学习反向传播建模，不兼容eDRAM异构组合。
3. 单芯片设计空间工具Timeloop、AccelTran：局限单片架构，无法建模芯粒间D2D互联与封装热效应。
4. 3D-NeuSim：支持3D堆叠CIM，但芯粒配置单一，缺少存储可靠性感知任务映射策略。

## 本文解决方案
### 1. 3D-CIMlet双层协同建模框架
输入模型与工艺库，覆盖芯内NoC、封装级NoP、2.5D中介层/3D TSV互联，集成有限元热仿真，支持跨尺度功耗、面积、时延评估。
### 2. 异构CIM芯粒模块化架构
采用40nm RRAM、14nm无电容eDRAM两类芯粒：RRAM适配静态权重长期存储；eDRAM用于动态激活、梯度频繁读写，规避RRAM耐久损耗。
### 3. 可靠性感知任务映射策略
推理：静态权重放RRAM，动态注意力激活存入eDRAM；持续学习前向传播复用推理芯粒，反向传播梯度、中间特征全部调度至eDRAM，减少RRAM重复写。
### 4. 通信与存储容量优化
寻优RRAM/eDRAM容量配比（最优比值4）平衡片上/封装网络开销；区分串行、并行学习模式动态分配SRAM/eDRAM缓存存储梯度。

## 实验分析
1. 测试模型：BERT、GPT-2、DeiT文本/视觉大模型，覆盖推理、微调、持续学习三类负载。
2. 推理性能：异构RRAM+eDRAM芯粒相较纯RRAM基线最高提速3.9倍，能效提升1.4倍。
3. 持续学习增益：2.5D、3D堆叠相较2D基准能效提升9.3×、12×，EDP分别降低90.2%、92.5%。
4. 通信开销：RRAM/eDRAM容量比为4时，NoC与NoP总能耗、时延达到全局最优。
5. 热仿真：2.5D封装温度分布均匀，3D堆叠热阻高、热点明显，eDRAM芯粒可缓解局部温升。

## 研究启发
1. 边缘LLM推理与持续学习负载读写特性差异巨大，必须采用NVM+DRAM异构存内芯粒搭配，兼顾留存性与耐久度。
2. 2.5D/3D先进封装可大幅削减芯粒间传输能耗，是突破边缘存储墙的关键路线，但需配套热感知协同优化。
3. 软硬件映射必须结合存储器件可靠性约束，将高频梯度、动态激活分配至易读写存储介质，延长NVM寿命。
4. 完整设计框架需打通算法、芯粒、互联、封装、热多尺度建模，单一维度仿真会低估系统瓶颈。
5. 持续学习存在串行/并行两种调度模式，需动态调整片上SRAM与eDRAM缓存配比以平衡刷新、泄漏能耗。
