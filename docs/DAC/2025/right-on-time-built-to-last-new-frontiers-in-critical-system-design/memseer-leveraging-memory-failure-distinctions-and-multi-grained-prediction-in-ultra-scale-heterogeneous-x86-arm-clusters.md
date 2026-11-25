---
title: "MemSeer: Leveraging Memory Failure Distinctions and Multi-Grained Prediction in Ultra-Scale Heterogeneous X86/ARM Clusters"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MemSeer: Leveraging Memory Failure Distinctions and Multi-Grained Prediction in Ultra-Scale Heterogeneous X86/ARM Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS6: Time-Critical and Fault-Tolerant System Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132417">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132417</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> DRAM可靠性，存储器故障，预测，异构集群</p>
</div>

---

## 研究概要
本文基于超大规模x86/ARM异构集群真实内存故障日志，提出MemSeer多粒度内存故障预测框架。区分两类架构故障时空差异，分层实现DIMM、服务器、页/行三级预测，设计四类特征与规则融合预测器。实测F1相较SOTA提升17.3%，线上集群VM中断平均降低24.2%。

## 背景和动机
1. 数据中心内存故障占服务器宕机57%，x86与ARM平台ECC、日志机制不同，CE/UE时空演化规律存在显著差异，单一模型跨架构预测效果极差。
2. 现有内存预测仅面向x86，缺少适配ARM的特征体系，长预警时长下精确率、召回率大幅下滑，难以支撑VM迁移、页下线等运维动作。
3. 主流方案仅支持DIMM单一层级预测，无法定位页、行级微观故障，页下线策略开销过高、故障规避能力弱。
4. ARM服务器缺少比特级错误寄存器，现有比特特征方案无法复用，缺少异构场景专用特征工程与采样机制。
5. 传统固定窗口采样忽略CE突发时序，样本分布失衡，模型训练偏置，无法适配线上流式日志。

## 相关工作
1. 单架构DRAM故障预测（HiMFP、Risky CE）：仅适配x86，依赖比特级日志，无ARM兼容特征，跨集群泛化差。
2. 机器学习故障模型：随机森林、LSTM等仅做DIMM粗粒度分类，不支持页/行微观定位，无法指导精细化内存隔离。
3. 内存容错运维策略：页下线、VM迁移研究缺少配套分层预测输入，难以平衡隔离开销与故障阻断效果。
4. 数据中心故障特征分析：仅统计故障占比，未挖掘x86/ARM时空分布、CE累积演化核心差异。
5. 流式日志采样方案：固定时间窗口采样，忽略CE风暴事件驱动特性，正负样本不均衡影响模型精度。

## 本文解决方案
### 1 异构集群故障特征体系
设计静态、空间、时序、比特四类特征；x86完整使用比特维度，ARM舍弃比特特征强化空间统计特征，适配两类硬件日志差异。
### 2 事件驱动流式采样标注
摒弃固定窗口，CE数量触发样本采集；基于预警时长、观测窗口正负样本标注，缓解样本不均衡问题，适配线上AIOps数据流。
### 3 三层分层预测架构
- DIMM层：XGBoost树模型做二分类故障预测，适配异构特征集；
- 服务器层：基于DIMM预测结果“至少一故障”集成判定，支撑整机VM迁移；
- 微观页/行层：四类规则集成预测器，依靠CE/巡检UE阈值定位高危内存单元。
### 4 跨架构适配优化
针对ARM无比特日志缺陷，强化bank/行CE分布空间特征；区分长短预警窗口模型，兼顾短时快速迁移、长时硬件更换运维需求。
### 5 分层运维联动机制
粗DIMM预警触发虚拟机热迁移；细页/行预测驱动操作系统页下线，分层阻断不可纠正UE故障。

## 实验分析
1. 数据集：华为3年真实日志，近200万条DIMM记录，分x86、ARM两套独立数据集，复现HiMFP、Risky CE基线。
2. 预测精度：同预警时长下MemSeer F1提升17.3%，ARM场景召回平均提升27%；树模型优于神经网络。
3. 特征消融：x86比特特征贡献最高，ARM空间特征为核心关键指标，删除后指标大幅衰减。
4. 运维收益：x86集群VM中断降低40.2%，ARM降低20.7%；线上半年运行平均减少24.2%VM故障中断。
5. 微观页下线：规则融合方案可减少单位故障隔离页面开销55%，同时提升规避UE数量110%。

## 研究启发
1. x86与ARM内存ECC、硬件日志机制差异巨大，统一预测模型必须做差异化特征裁剪，不能直接迁移x86方案。
2. 单粒度DIMM预测不足以支撑精细化容错，分层粗/细粒度预测可分别适配VM迁移、内存页下线两类运维手段。
3. CE事件驱动采样优于固定时间窗口，能均衡正负样本分布，显著提升线上流式日志训练模型泛化能力。
4. 无比特日志的ARM平台可依靠行、bank空间CE分布特征弥补预测精度损失，空间特征具备跨架构通用性。
5. 多粒度预测框架可落地AIOps运维系统，从故障预测到主动隔离形成完整闭环，有效降低云服务SLA损失。
