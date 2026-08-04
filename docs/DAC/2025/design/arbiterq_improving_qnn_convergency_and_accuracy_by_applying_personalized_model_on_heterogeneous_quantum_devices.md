---
title: "ArbiterQ: Improving QNN Convergency and Accuracy by Applying Personalized Model on Heterogeneous Quantum Devices"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# ArbiterQ: Improving QNN Convergency and Accuracy by Applying Personalized Model on Heterogeneous Quantum Devices


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132786">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132786</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>量子神经网络，异构量子处理器，个性化模型，行为向量，梯度共享 </p>
</div>

---

## 研究概要
本文提出面向异构NISQ量子设备的分布式QNN框架Arbiter。设计模型向量、行为向量统一表征电路硬件特征，提出相似度感知个性化梯度共享训练，以及量子shot细粒度环型调度推理方案。多数据集测试相比SOTA EQC收敛提速4.03倍，训练损失降低7.87%，推理损失减少24.71%。

## 背景和动机
1. NISQ时代单台QPU量子比特有限，分布式并行是扩大QNN规模的必由之路，但不同量子芯片拓扑、门保真度、噪声差异巨大，设备异构性严重破坏训练精度。
2. 现有分布式QNN框架EQ采用全局统一模型权重，异构设备最优参数不一致，梯度相互干扰，收敛慢、损失高。
3. 传统批量并行推理仅单设备处理单样本，硬件噪声不均衡带来巨大预测方差，缺乏细粒度调度机制。
4. 缺少统一量化指标刻画QPU编译后电路噪声与拓扑差异，无法精准分组协同更新梯度。

## 相关工作
1. 分布式变分量子框架EQ：基于集成学习分配投票权重，但全局统一模型不匹配异构硬件，收敛性能差。
2. 通用量子电路向量化工具QuCT：仅优化单设备电路保真度，不支持多设备协同训练调度。
3. 量子噪声缓解算法：面向单芯片误差抵消，未解决多设备异构带来的梯度冲突问题。
4. 量子电路并行划分工作：仅做电路层拆分，未针对QNN权重、shot推理做软硬件协同调度。

## 本文解决方案
### 1. 双向量统一表征体系
定义模型向量存储QNN可训练权重；行为向量拼接上下文向量（门累积误差）、拓扑向量（SWAP附加误差），完整刻画单QPU编译后电路硬件噪声与拓扑特征。
### 2. 相似度感知个性化训练
每台QPU保留专属个性化权重，计算行为向量二范数距离衡量设备相似度；仅同分组设备互传梯度，梯度乘以相似度系数加权更新，规避异构梯度冲突。
### 3. MDS+DFT环型QPU分组降噪
MDS降维行为向量，DFT提取周期特征构建QPU环；环内设备硬件特性差异大，执行shot级噪声补偿，抵消设备固有推理偏置。
### 4. Shot细粒度贪心推理调度
放弃样本级批量并行，将单任务所有测量shot打散分配至多个QPU环；简单任务分配低精度环、困难任务分配高精度环，均衡硬件负载。

## 实验分析
1. 实验平台：ORIGIN实超导72比特QPU、多量子仿真器，测试Iris/Wine/MNIST/HMDB51四类图像视频数据集。
2. 训练效果：对比EQ、全共享、单设备基线，平均收敛速度提升4.03倍，整体训练损失降低7.87%，小数据集精度提升幅度最高达23.23%。
3. 推理性能：shot调度相较传统批量推理平均损失下降24.71%，QPU数量越多降噪收益越明显。
4. 真机验证：2比特小规模实量子芯片测试，收敛速度相较EQ提升1.57倍，损失更低，仿真趋势与真机完全吻合。
5. 消融对比：个性化权重、相似度梯度共享、环型shot调度三者叠加才能实现最优收敛与推理精度。

## 研究启发
1. 异构量子分布式QNN不能共用全局权重，硬件噪声拓扑差异决定每台设备存在专属最优参数，个性化模型是基础优化思路。
2. 行为向量可统一量化量子芯片异构程度，基于向量相似度分组能过滤冲突梯度，大幅提升并行训练效率。
3. QNN推理依赖多次shot采样，样本级并行存在固有精度缺陷，细粒度shot跨设备分配可平滑硬件噪声偏差。
4. 低维映射+频域分析能高效对高维硬件特征聚类，低成本实现多设备噪声互补分组。
5. NISQ分布式量子系统优化需训练、推理全链路协同，仅单一阶段优化无法充分发挥多量子硬件并行增益。
