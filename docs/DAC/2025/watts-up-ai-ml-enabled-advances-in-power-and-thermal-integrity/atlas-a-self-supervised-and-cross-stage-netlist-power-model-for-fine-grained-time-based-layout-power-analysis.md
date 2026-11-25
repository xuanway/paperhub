---
title: "ATLAS: A Self-Supervised and Cross-Stage Netlist Power Model for Fine-Grained Time-Based Layout Power Analysis"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# ATLAS: A Self-Supervised and Cross-Stage Netlist Power Model for Fine-Grained Time-Based Layout Power Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA4: Power Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://zhiyaoxie.com/files/DAC25_ATLAS.pdf">https://zhiyaoxie.com/files/DAC25_ATLAS.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 时序功耗预测，网表功耗模型，自监督预训练，跨阶段对齐 </p>
</div>

---

## 研究概要
本文提出ATLAS自监督跨层级网表功耗预测框架，基于轻量化图Transformer编码器，设计五类电路自监督预训练任务，分三类轻量模型微调，仅需综合网表即可预测逐周期版图级功耗。6款300K~600K单元CPU电路验证，总功耗MAPE低于1%，推理速度较传统布局+PTPX流程快千倍。

## 背景和动机
1. 传统精确逐周期功耗必须完成布局布线+寄生仿真，大规模电路耗时数天，早期综合阶段无法获取真实功耗用于优化。
2. 现有ML功耗模型存在短板：专用模型仅适配单设计，通用模型只能输出平均功耗，无法生成逐周期时序功耗曲线。
3. 多数模型以门级仿真为标签，忽略CTS、缓冲插入等版图优化带来巨大功耗偏差，时钟树功耗预测完全失效。
4. 电路逻辑锥划分存在重叠问题，叠加后总功耗失真，缺少无重叠子模块细粒度划分方案。
5. 缺少能对齐综合/版图两级、适配动态负载的通用电路表征学习方法。

## 相关工作
1. 设计专属功耗模型(PRIMAL/APOLLO)：支持逐周期功耗，但每款电路需重新采集标签训练，复用性极差。
2. 跨设计平均功耗模型(SNS V2/PowPredicCT)可泛化新电路，但仅输出平均功耗，无法刻画峰值与时序波动。
3. 图电路表征学习(DeepGate系列)仅针对纯组合逻辑，未覆盖时序单元、时钟树，无跨版图对齐学习。
4. 商用门级PTPX：无版图RC信息，时钟树功耗预测误差100%，组合逻辑误差超65%。
5. 传统GNN电路模型：大图算力开销高，无法支撑百万级单元电路快速推理。

## 本文解决方案
### 1 无重叠子模块网表预处理
将综合网表、等价变换网表、版图网表统一拆分为互不重叠子图；提取单元类型、逐周期翻转率、lib固有功耗三类节点特征，构建有向图输入。
### 2 五类联合自监督预训练任务
基于SGFormer线性复杂度图Transformer编码器，同时完成掩码翻转预测、掩码单元分类、子规模回归、同功能对比学习、综合-版图跨层对齐对比学习，无需功耗标签。
### 3 三分支轻量化微调预测
将总功耗拆组合逻辑、寄存器、时钟树三类，分别训练XGB轻量模型；时钟树仅依赖编码向量，组合/寄存器补充单元数量、电容等网表原生特征求和得到全电路逐周期功耗。
### 4 跨设计泛化推理流程
预训练编码器一次性离线完成；新电路仅做子图划分与特征提取，直接推理逐周期版图功耗，无需布局、寄生抽取与时序仿真。
### 5 内存功耗独立简易模型
SRAM宏单元结构布局无变化，单独基于端口翻转率建立简易查表模型，不参与ATLAS主框架训练。

## 实验分析
1. 实验环境：TSMC40nm工艺，6款300K~600K乱序CPU电路，C1/C3/C5/C6训练、C2/C4测试，基线为门级PTPX完整后端流程。
2. 预测精度：整体总功耗平均MAPE仅0.78%；时钟树0.58%、寄存器0.45%、组合逻辑5.12%，门级PTPX总误差超26%，时钟树完全失效。
3. 推理效率：传统布局+PTPX单组负载平均8万秒，ATLAS预处理+推理仅76秒，提速超1000倍。
4. 细粒度能力：支持CPU前端、LSU等子模块单独功耗输出，组件MAPE普遍低于5%。
5. 消融验证：跨层对齐与翻转掩码两大预训练任务是缩小版图功耗误差的核心模块。

## 研究启发
1. 电路功耗预测必须建立综合到版图的映射表征，仅依赖门级信息会带来巨大时钟、互连功耗偏差。
2. 多任务自监督图学习可在无功耗标签下捕获版图优化带来的电路结构变化，大幅提升跨设计泛化能力。
3. 拆分组合/寄存器/时钟树三类独立功耗分支，可针对性降低各类电路预测误差，时钟树无法仅依靠门级原始特征推导。
4. 无重叠子模块划分解决逻辑锥叠加失真问题，实现组件级细粒度功耗反馈，方便前端低功耗迭代。
5. 线性复杂度图Transformer适配百万级大规模电路，是后端加速类EDA模型的优选骨干网络。
