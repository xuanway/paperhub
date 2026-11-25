---
title: "SimPhony: A Device-Circuit-Architecture Cross-Layer Modeling and Simulation Framework for Heterogeneous Electronic-Photonic AI System"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# SimPhony: A Device-Circuit-Architecture Cross-Layer Modeling and Simulation Framework for Heterogeneous Electronic-Photonic AI System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132427">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132427</a></p>
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/ScopeX-ASU/SimPhony">https://github.com/ScopeX-ASU/SimPhony</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 电子-光子集成电路，跨层建模与仿真，光子张量核，异构系统架构 </p>
</div>


---

## 研究概要
本文开源SimPhony跨层仿真框架，面向异构光电集成AI芯片，搭建器件库与分层架构生成器，支持多类光子张量核统一建模。融合光学多维并行数据流、数据感知能耗、布局感知面积、光链路预算多模块，可与ONN训练工具协同，在GEMM、Transformer任务验证，仿真指标与真实流片结果高度吻合。

## 背景和动机
1. 光电AI系统跨器件/电路/架构多栈耦合，现有仿真工具仅支持单一固定光子张量核，无法兼容MZI网格、TeMPO阵列等多样拓扑。
2. 光子计算存在波长/偏振等独有多维并行，传统数字加速器数据流模型无法刻画分层模拟累加机制，仿真时延误差巨大。
3. 现有工具仅简单累加器件面积，未考虑光波导走线、器件间距，面积预估严重失真；能耗不关联实际权重数值，精度不足。
4. 缺乏软硬件协同仿真链路，光网络训练与架构评估割裂，无法完成端到端光电协同设计空间探索。
5. 不同光子核重构速度、数值表达范围差异大，缺少统一建模框架量化各类架构时延、能耗开销。

## 相关工作
1. 数字AI仿真器(Timeloop/CACTI)：仅面向纯数字电路，无光电器件模型，不支持光学并行与光链路损耗分析。
2. Albire/CimLoop光子仿真工具：仅固化单一光子架构，拓扑拓展性差，无通用网列表征各类张量核。
3. 专用光子核仿真(TeMPO/Lightening-Transformer)：依附单一架构，不支持异构混合芯片对比，通用性弱。
4. 光电器件仿真(Lumerical)：仅底层器件仿真，无法向上扩展至完整AI加速器系统级评估。
5. ONN训练框架TorchONN：仅完成模型训练，无硬件性能评估模块，训练与架构优化脱节。

## 本文解决方案
### 1 SimPhony-DevLib光电标准化器件库
收录MZI、MRR、DAC/PD等主流光子/电子器件，导入流片实测与Lumerical仿真参数，支持工艺节点、位宽、调制参数灵活缩放，作为系统建模底层基础。
### 2 SimPhony-Arch分层参数化架构生成器
设计有向二引脚光子网表，以最小运算节点为基础单元，自定义缩放规则自动生成阵列、MZI网格等任意光子张量核；输出加权DAG用于链路损耗分析。
### 3 光子专属多维数据流与时延建模
支持空间/光谱/时域多层并行累加，自动补偿数值受限光子核迭代开销、热光/PCM重构时延，分层计算各层总执行周期。
### 4 多维度系统性能分析引擎
- 带宽自适应四级存储建模，自动计算最小SRAM块数；
- 信号流感知布局规划器，贴合真实PIC版图估算芯片面积；
- 数据感知能耗模型，基于权重相位动态计算移相器功耗；
- 光链路预算分析，提取关键损耗路径推导激光最低功率。
### 5 训练-仿真端到端协同链路
对接TorchONN，将数字网络转为光神经网络，提取各层GEMM负载映射至异构光子核，一站式输出面积、时延、能耗完整报告。

## 实验分析
1. 实验环境：TeMPO动态阵列、MZI静态网格、SCATTER稀疏光子核三类架构，测试GEMM、BERT、VGG workload，对标原始论文流片仿真数据。
2. 仿真精度：面积、功耗分解与文献实测偏差极小；无感知面积估算低估72%，本文布局模型贴近真实版图。
3. 架构探索实验：波长增多算力提升但激光器功耗上涨；ADC/DAC位宽越高系统总能耗越大，存在最优平衡点。
4. 异构映射验证：VGG卷积映射SCATTER、全连接映射MZI网格，混合架构可显著降低总能耗。
5. 消融对比：数据感知能耗相较固定模型最高降低60%，光谱并行可大幅削减推理时延。

## 研究启发
1. 光子加速器仿真不能复用数字数据流范式，必须新增波长、偏振等光学维度并行建模逻辑。
2. 统一有向光子网表是兼容多样张量核拓扑的核心，模块化节点+缩放规则可大幅降低新架构建模成本。
3. 器件功耗与输入相位强相关，固定理想功耗模型误差极大，数据感知仿真更贴合真实芯片表现。
4. 版图走线、器件间距不可忽略，仅累加器件面积会严重低估芯片制造成本。
5. 光电协同设计需要训练-仿真一体化链路，才能快速完成算法、光子电路、存储的联合空间寻优。