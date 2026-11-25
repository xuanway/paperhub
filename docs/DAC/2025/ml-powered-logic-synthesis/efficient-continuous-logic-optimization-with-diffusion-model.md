---
title: "Efficient Continuous Logic Optimization with Diffusion Model"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Efficient Continuous Logic Optimization with Diffusion Model

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA5: RTL/Logic Level and High-level Synthesis</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://personal.hkust-gz.edu.cn/yuzhema/papers/DAC2025-DiffSyn.pdf">https://personal.hkust-gz.edu.cn/yuzhema/papers/DAC2025-DiffSyn.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 连续优化，扩散模型，代理模型，逻辑综合序列优化 </p>
</div>


---

## 研究概要
本文提出基于扩散模型的连续逻辑优化框架，将离散变换序列映射至连续隐空间。依托多任务代理模型获取QoR梯度，扩散模型约束隐变量贴合合法变换分布，规避优化后映射失真。EPFL、ISCAS基准测试，相较RL、贝叶斯等离散搜索方法，运行速度提升5~130倍，面积、时序QoR同步更优。

## 背景和动机
1. 逻辑优化变换序列组合空间呈指数级，传统DRiLLS、BOiLS等离散搜索方法迭代开销巨大，大电路收敛极慢。
2. 连续梯度优化思路存在致命缺陷：仅基于QoR梯度更新会让隐变量偏离合法变换嵌入，映射回有效优化序列时QoR大幅退化。
3. 现有方法缺少统一框架同时兼顾时序/面积优化与隐空间分布约束，分开优化导致流程割裂、效果受损。
4. 各类电路GNN、CNN代理模型仅用于单独预测，未和生成式模型联合做端到端隐空间优化。
5. 离散搜索每次迭代需调用ABC综合工具，反复仿真带来高额时间成本，工业大设计迭代周期难以接受。

## 相关工作
1. 强化学习类序列优化（DRiLLS、abcRL）：逐次离散决策，海量迭代调用综合工具，耗时极高。
2. 多臂老虎机FlowTune：离散空间采样寻优，搜索效率有限，复杂电路提升幅度小。
3. BOiLS贝叶斯优化：基于采集函数离散采样，随序列长度增长算力爆炸。
4. 电路QoR代理模型（ASAP、LOSTIN、CNN预测）：仅做结果预估，未参与隐空间连续优化。
5. 单纯连续梯度优化：无分布约束，优化后隐变量与合法嵌入偏差大，映射后性能严重下滑。

## 本文解决方案
### 1 双模型联合训练流水线
离线并行训练代理模型与一维U-Net扩散模型；代理输入电路+序列嵌入预测面积/延迟并输出梯度，扩散学习所有合法变换的隐空间分布。
### 2 融合双目标的隐空间迭代更新
优化目标同时最小化预测QoR与隐变量和合法嵌入分布偏差；每轮迭代叠加代理梯度损失与扩散去噪修正项，借助重参数技巧精准计算梯度。
### 3 扩散模型去噪约束机制
前向扩散逐步对合法嵌入添加高斯噪声，反向去噪步骤拟合真实数据分布；优化全程嵌入去噪校正，保证最终隐变量可直接映射为有效变换序列。
### 4 通用序列检索策略
优化收敛后隐变量贴合合法变换嵌入，采用近邻匹配快速还原完整逻辑优化序列，无需额外复杂解码流程。
### 5 通用适配架构
兼容GNN、CNN、多任务三类代理模型，适配rw/rf/rs等全部标准逻辑变换，可直接对接ABC综合工具链。

## 实验分析
1. 实验环境：EPFL、ISCAS基准，ASAP7工艺，RTX3090+AMD EPYC，对比DRiLL、abcRL、BOiLS、FlowTune。
2. QoR指标：几何均值面积降低23.3%、时序延迟降低15.5%，各类规模电路均稳定优于所有离散基线。
3. 运行效率：单轮序列优化仅44秒，相比最慢abcRL提速130倍，相比FlowTune提速近6倍。
4. 消融验证：移除扩散模型后面积平均提升90%，无论搭配哪种代理模型性能均大幅倒退。
5. 泛化能力：GNN/CNN/多任务代理搭配扩散均可稳定提升，框架具备通用性。

## 研究启发
1. 逻辑优化离散组合问题可转为连续隐空间梯度优化，但必须引入生成模型约束分布，否则映射失效。
2. 扩散模型天然适配EDA嵌入分布拟合，能低成本消除连续优化与离散变换间的鸿沟。
3. 离线预训练双模型、在线快速隐空间迭代，可大幅减少综合工具重复调用开销。
4. 单纯代理梯度优化存在局部最优与分布偏移缺陷，多目标联合损失是可靠解决方案。
5. 生成式深度学习与电路代理预测结合，是破解逻辑序列指数搜索复杂度的高效新路线。