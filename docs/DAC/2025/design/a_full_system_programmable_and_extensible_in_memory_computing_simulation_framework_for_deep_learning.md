---
title: "A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132463">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132463</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 存内计算，仿真框架，深度学习，设计空间探索，信噪比分析</p>
</div>


---

## 研究概要
本文提出全系统可编程存算一体仿真框架IMCsim，兼容SRAM/MRAM/Digital三类存算架构，配套可扩展指令集与SNR精度模型，集成QEMU实现周期级仿真。基于22/28nm实测芯片完成校准，在CNN、大模型、扩散模型多负载开展架构探索，还完成28nm轻量化DiT存算芯片设计与版图验证。

## 背景和动机
1. 存算一体(IMC)缓解冯诺依曼存储墙，但大语言模型、扩散生成模型的硬件设计缺少跨层完整仿真工具。
2. 现有仿真工具仅聚焦交叉阵列电路或小型网络，缺少全系统、周期级运行时建模，无法建模片外访存与器件非理想噪声。
3. 缺少统一仿真平台兼容SRAM、MRAM等多种存算器件，难以完成PPA与计算精度协同权衡。
4. 现有工具不能作为流片前完整设计工具，无法支撑芯片架构迭代、内存规划与版图预估。

## 相关工作
1. 交叉阵列电路仿真器（NeuroSim、RxNN、MNSIM）：仅建模器件电路噪声，无系统级周期仿真，仅支持CNN小规模网络。
2. 专用存算架构模拟器（PUMAsim、PIMulator-NN）：绑定单一存储器件，无通用ISA与运行时性能剖析能力。
3. 设计空间探索工具CiMLoop：缺少周期级时序、噪声精度仿真，不支持完整流片级芯片设计流程。
4. 所有现有工具均无法统一兼容模拟/数字存算，难以端到端评估LLM、DiT等超大生成模型。

## 本文解决方案
### 1. 分层可扩展硬件库
模块化提供IMC阵列、APU、缓存、路由等基础单元，支持自定义稀疏检测、量化硬件扩展，兼容SRAM/MRAM数字/模拟存算器件。
### 2. 可编程软件栈与可扩展ISA
深度学习算子分解映射库，配套RISC风格扩展指令集，支持BF16等新指令与对应硬件模块同步扩展，适配各类AI模型算子。
### 3. 周期级全系统仿真内核
时钟引擎拆解指令为微操作精确计时，集成QEMU整机模拟器，完整建模片外DRAM访存开销；构建SNR量化模型刻画模拟存算噪声误差。
### 4. 运行时多维度剖析器
实时采集周期级硬件利用率、能耗、内存占用，输出吞吐、能效、精度统计，支撑架构瓶颈定位与芯片尺寸约束求解。
### 5. 芯片设计辅助流程
基于工艺参数、面积约束自动求解IMC存储阵列规模、SRAM配比，输出可用于布局的硬件参数，完成完整芯片版图预估。

## 实验分析
1. 仿真校准：采用22nm MRAM、28nm SRAM流片实测数据校准，SNR仿真误差仅约5%，时序、功耗与硬件实测匹配。
2. 多负载架构对比：数字DIMC峰值吞吐高于各类模拟IMC；CNN复用性强吞吐最优，LLM/DiT受KV缓存、全连接层拖累利用率偏低。
3. 阵列规模探索：匹配量化分组的窄行多bank架构可大幅提升硬件利用率，8组DIMC吞吐可达单芯8.1倍。
4. 能耗特征：MRAM写能耗极高，片外访存是全系统能耗主体，多数IMC系统能效不足1TOPS/W。
5. 芯片落地：以28nm、4mm²面积约束完成轻量化DiT存算芯片设计，64组32×32 IMC阵列消除内存溢出，整体延迟降低90%并输出完整版图。

## 研究启发
1. 存算评估不能仅看阵列算力，必须纳入片外访存、器件噪声、时序构成全系统仿真才能真实反映PPA。
2. 大模型量化粒度直接决定IMC阵列利用率，硬件阵列维度需匹配量化分组尺寸以减少空闲周期。
3. 模拟IMC受ADC速率、存储写能耗制约，数字存算更适合大生成类模型高吞吐推理场景。
4. 仿真工具需打通算子、指令、硬件、工艺多层抽象，才能同时完成算法映射与流片前期芯片设计。
5. 多bank细粒度IMC架构优于少数大阵列，多并行单元可掩盖加载空闲，显著提升整体吞吐。