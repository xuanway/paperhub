---
title: "CIMFlow: An Integrated Framework for Systematic Design and Evaluation of Digital CIM Architectures"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# CIMFlow: An Integrated Framework for Systematic Design and Evaluation of Digital CIM Architectures


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.01107">https://arxiv.org/abs/2505.01107</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>数字存内计算，集成框架，指令集架构，编译 </p>
</div>


---

## 研究概要
本文提出CIMFlow一体化数字存内计算设计评估框架，集成分层可扩展ISA、两级编译器、周期精确仿真器。基于DP动态规划划分策略解决SRAM容量瓶颈，覆盖DNN编译到性能全流程评测。对比基线编译方案，推理最高提速2.8倍、能耗降低61.7%，支持多硬件配置设计空间探索。

## 背景和动机
1. 数字SRAM型CIM无ADC/DAC开销、并行度高，但缺乏软硬件协同一体化开发工具，设计迭代成本极高。
2. 现有工具要么仅仿真、要么仅编译，割裂编译与仿真链路，且大多面向模拟CIM，忽略数字CIM片上存储容量约束。
3. SRAM集成密度低，单阵列容量有限，大模型易频繁搬移数据，现有编译划分策略无法平衡并行与传输开销。
4. 缺少分层硬件抽象ISA，难以快速适配不同宏、核、芯片级CIM架构，架构探索灵活性不足。

## 相关工作
1. 纯仿真框架（NeuroSim/MNSIM）：侧重模拟/数字CIM电路级仿真，无完整编译链路，数据通路固定，扩展性差。
2. 专用CIM编译器（CIM-MLC）：仅面向模拟存内架构，未针对数字SRAM容量做分层划分优化，无配套周期仿真。
3. 通用DNN编译工具：不兼容CIM阵列、宏组专属硬件原语，无法生成存内专用指令。
4. 分立编译+仿真流程：工具间无统一ISA接口，数据格式不互通，无法自动化完成端到端评估。

## 本文解决方案
### 1. 三层分层可扩展ISA
芯片/核心/宏单元三级硬件抽象，定义CIM/向量/标量/通信四类统一32位指令，解耦编译与仿真，可快速扩展新型计算单元。
### 2. 两级MLIR编译优化栈
图级CG优化：基于DP动态规划对计算图分块，编码依赖掩码降低计算量，权衡权重复制与片上传输开销；算子OP优化：虚拟映射匹配阵列尺寸，循环分块重排序适配SRAM容量，生成专用CIM指令。
### 3. 周期精确SystemC仿真器
多核心NoC互联建模，三级流水线精确模拟取指/译码/执行，统计延迟、能耗、硬件利用率，输出完整量化评估报告。
### 4. 端到端一体化工作流
输入ONNX模型+硬件配置，自动完成图划分、算子映射、指令生成、周期仿真，一站式完成数字CIM架构选型与编译调优。

## 实验分析
1. 实验配置：64核数字CIM默认架构，测试ResNet/VGG/MobileNet/INT8量化模型，基线为通用映射、CIM-MLC划分方案。
2. 编译收益：DP分层划分最高提速2.8倍，整体能耗下降61.7%，轻量MobileNet类模型优化幅度更突出。
3. 架构探索：宏组MG规模、NoC报文宽度显著影响吞吐与能耗；计算密集模型扩大MG收益高，轻模型带宽开销占比大。
4. 软硬件协同：同一硬件下优化编译可大幅缩小性能-能耗帕累托边界，抵消硬件配置劣势。
5. 工具优势：原生适配数字SRAM容量约束，模块化设计可扩展新型算子与CIM宏电路。

## 研究启发
1. 数字CIM开发必须搭建编译-仿真一体化框架，割裂工具链会大幅拉长架构迭代周期。
2. SRAM容量是数字CIM核心约束，基于依赖掩码的动态规划分块可最优平衡并行度与片外数据搬运。
3. 分层硬件抽象ISA是工具可扩展关键，统一指令层能快速兼容各类新型数字存内宏单元。
4. 不同DNN模型硬件最优配置差异巨大，一体化框架可高效完成大规模设计空间遍历。
5. 编译层优化潜力不亚于硬件电路改进，优秀分块与映射策略可在相同硬件下实现数倍性能提升。