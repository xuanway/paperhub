---
title: "INSIGHT: A Universal Neural Simulator Framework for Analog Circuits with Autoregressive Transformers"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# INSIGHT: A Universal Neural Simulator Framework for Analog Circuits with Autoregressive Transformers

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11133292">https://ieeexplore.ieee.org/abstract/document/11133292</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模拟电路性能预测，自回归Transformer，数据高效学习，通用神经仿真器 </p>
</div>


---

## 研究概要
本文提出INSIGHT通用自回归Transformer神经模拟仿真框架，将模拟电路性能预测建模为序列生成任务，设计贪心指标排序策略，搭配LoRA低秩微调实现跨工艺迁移。运放、TIA、LDO等多电路测试，预测R²≥0.95；跨工艺训练数据减少60%，内存降低42%，嵌入RL尺寸优化后SPICE仿真调用量降低100~1000倍。

## 背景和动机
1. 传统SPICE仿真计算开销巨大，模拟电路尺寸优化循环仿真成本极高，设计迭代缓慢。
2. 现有代理模型（全连接、对比回归）难以捕捉多性能指标间强耦合关系，复杂电路预测精度低、数据需求量大。
3. 不同工艺、拓扑模拟电路物理规律相通，但现有模型无法高效跨工艺迁移，新工艺需完整重训。
4. 全量微调迁移学习显存与训练耗时高，缺少参数高效微调方案适配EDA快速迭代需求。
5. 现有网络输入输出维度固定，无法兼容参数、指标数量可变的各类模拟拓扑，通用性差。

## 相关工作
1. 解析建模方法：依赖人工推导公式，先进工艺精度差，复杂拓扑难以扩展。
2. 全连接集成代理（CRONuS）：仅拟合单点映射，忽略指标依赖，小样本R²不足0.8。
3. 对比回归LbC：引入合成数据增强，但未建模指标序列依赖，复杂瞬态指标预测偏差大。
4. RNN类时序模型：梯度消失，并行训练效率低，不适合EDA大批量参数推理。
5. RL模拟优化（AutoCkt）：无高精度代理，迭代需大量真实SPICE仿真，算力成本极高。

## 本文解决方案
### 1 自回归Transformer预测建模
把电路参数、已预测性能作为上下文，逐一生成剩余指标；采用仅解码器轻量Transformer，无分词直接处理连续电路数值，自适应可变参数/指标长度。
### 2 贪心信息增益指标排序算法
按仿真开销升序排序，迭代选取信息增益最大指标后置，先用低成本静态指标辅助预测高代价瞬态指标，大幅提升数据效率。
### 3 LoRA低秩参数迁移学习
预训练主干权重冻结，仅更新低秩分解矩阵微调新工艺；大幅减少可训练参数，压缩显存、缩短训练时长。
### 4 MLE极大似然损失训练
基于序列联合概率构造负对数似然损失，精准建模各性能指标条件依赖关系，捕捉电路内部物理耦合。
### 5 INSIGHT+PPO协同尺寸优化流水线
预训练代理替代绝大多数SPICE调用，仅少量样本用于校正，大幅削减优化循环仿真开销。

## 实验分析
1. 测试对象：两级运放、TIA、折叠共源共栅、LDO等，覆盖45/90/130nm工艺，对比CRONuS、LbC。
2. 预测精度：全电路测试集R²均≥0.95，MSE远低于两类基线；贪心排序相比逆序平均R²提升5%。
3. 迁移性能：跨工艺微调仅需40%原始训练样本，同等精度数据需求降低60%。
4. LoRA收益：可训练参数减少42%，训练耗时下降25%，预测精度无明显损失。
5. 优化效率：结合PPO强化学习后，优化所需真实SPICE仿真仅2~15次，相比基线减少百倍至千倍。

## 研究启发
1. 模拟电路各项性能存在强条件依赖，自回归序列建模可充分利用指标关联，显著提升代理模型数据效率。
2. Transformer自注意力天然适配可变维度电路数据，相比固定FC/RNN更适合通用模拟仿真代理。
3. 按仿真成本与信息增益排序性能指标，是低成本提升预测精度的工程化策略。
4. LoRA类参数高效微调解决跨工艺迁移痛点，避免全量重训带来的算力浪费。
5. 高精度神经代理嵌入强化学习优化闭环，可从根源削减昂贵SPICE仿真调用次数，加速模拟自动化设计。
