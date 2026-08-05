---
title: "Contention-Aware Forecasting of Energy Efficiency through Sequence-Based Models in Modern Heterogeneous Processors"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Contention-Aware Forecasting of Energy Efficiency through Sequence-Based Models in Modern Heterogeneous Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132825">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11132825</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 能源效率预测，资源争用感知，基于序列的模型，异构处理器</p>
</div>


---

## 研究概要
本文提出EffiCast序列预测框架，面向Intel混合异构处理器实现感知资源竞争的能效预测。通过实测分析程序阶段、簇内/簇间竞争对IPJ能效的影响，构建分层时序特征，采用LSTM与Transformer时序模型。真实平台批量推理仅1.82ms，预测RMSE低至1.14，显著优于XGB、浅层神经网络基线。

## 背景和动机
1. 异构P/E混合处理器依靠核映射、DVFS优化能效，但不同程序、执行阶段最优配置差异极大，启发式调度难以适配动态负载。
2. 程序能效具备强时序波动，存在突发能效尖峰，静态单时刻模型无法捕捉阶段变化，决策滞后。
3. 处理器L2/L3共享缓存带来簇内、跨簇多级资源竞争，并发任务相互干扰，现有预测方案未建模竞争影响。
4. 传统ML预测仅拟合当前时刻指标，无法预判迁移、调频后的未来能效，难以支撑主动资源管理。
5. 多数方案依赖源码插桩，工业场景无源码时无法部署，基于硬件PMC的时序预测方案仍存在精度短板。

## 相关工作
1. 源码插桩类优化：依赖编译器/内核追踪，需要程序源代码，封闭软件场景无法使用。
2. 同构平台功率预测：仅针对单一核心架构，不区分P/E核，无法适配混合异构集群。
3. 浅层树/基础NN模型：只能静态单点预测，缺失时序依赖，负载突变场景误差激增。
4. 仿真平台LSTM功耗预测：仅在模拟器验证，未在真实商用异构CPU落地，无多级缓存竞争建模。
5. 单维度DVFS预测：只关注频率调节，未联合任务迁移、多簇资源竞争联合建模。

## 本文解决方案
### 1 异构平台全维度能效影响量化分析
基于Alder Lake i9实测PARSEC/SPLASH2，量化核心类型、V/F频率、程序执行阶段、簇内/跨簇缓存竞争四类因素对IP能效的波动规律，证实时序与竞争是核心干扰项。
### 2 分层时序特征工程体系
三层特征：目标程序PMC细粒度指标、同簇并发元应用聚合指标、全局系统能耗；区分E核L2、P核L3竞争差异，编码待迁移/调频目标配置，按5周期构建时序序列输入。
### 3 完整EffiCast数据生成流水线
随机生成2–16并发任务负载，1.5–3.5GHz多频率遍历，每100ms采集PMC与RAPL能耗，以配置变更后的下一周期IPJ为标签，构建181万时序样本集。
### 4 双时序预测模型架构
- Transformer：多头注意力捕捉长时序依赖，嵌入配置参数做回归预测；
- 双层堆叠LSTM：通过时序隐状态记录阶段变化，轻量化推理；
两者均以MSE为损失，早停防止过拟合。
### 5 oneDNN批量推理加速
训练离线完成，线上批量推理优化，单序列推理时延由94ms降至1.82ms，远低于100ms采样周期，满足实时调度要求。

## 实验分析
1. 实验平台：12代Alder Lake i9异构处理器，16核分为1P+2E三簇，数据集7:1.5:1.5划分训练/验证/测试。
2. 单时刻预测：XGB、浅层NN精度尚可，但预测未来周期误差大幅飙升，无法用于主动调度。
3. 时序预测精度：LSTM RMSE=1.14、Transformer RMSE=1.87，残差趋近于0，在未见过的并发负载上趋势预测无反向偏差。
4. 泛化测试：14任务并发陌生负载，四类波动程序的预测曲线与真实IPJ高度贴合，可适配周期性、突发型能效变化。
5. 推理开销：批量推理1.82ms/样本，不足采集周期2%，不会抢占调度计算资源。

## 研究启发
1. 异构CPU能效预测必须同时建模程序时序阶段与多级缓存资源竞争，单一静态特征精度不足。
2. 时序深度学习（LSTM/Transformer）是实现主动预判的关键，静态树模型仅适合事后评估。
3. 基于硬件PMC无侵入采集数据，无需源码，更适配商用封闭软件的资源调度场景。
4. 离线训练+线上批量推理的分离架构，可平衡模型精度与实时性开销。
5. 主动调度不能仅看当前负载，提前预判调频、迁移后的系统能效，才能充分挖掘混合架构节能潜力。
