---
title: "SAPO: Improving the Scalability and Accuracy of Quantum Linear Solver for Portfolio Optimization"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# SAPO: Improving the Scalability and Accuracy of Quantum Linear Solver for Portfolio Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES6: Quantum Computing</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/abstract/document/11133130">https://ieeexplore.ieee.org/abstract/document/11133130</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 量子投资组合优化，约束缩放技术，最小-最大特征值预测模型，HHL算法，Black模型</p>
</div>

---

## 研究概要
本文提出SAPO量子投资组合优化方案，基于HHL算法结合金融均值方差理论。设计约束等价缩放大幅降低拉格朗日矩阵条件数，构建SVR最小/最大特征值预测模型自适应配置量子电路。美股多资产数据集测试，相较基础HHL复杂度降低36.94%，精度相比混合HHL提升1.46倍。

## 背景和动机
1. 经典投资组合优化计算开销巨大，量子算法分为量子伊辛、HHL两类，但均存在明显缺陷。
2. 量子伊辛仅输出是否买入二元结果，无法得到精确资产权重，优化精度极低。
3. 原生HHL求解金融线性系统时，市场数据生成矩阵条件数可达10⁵，电路深度、CNOT门数量爆炸，NISQ设备难以部署。
4. 现有混合HHL仅插入中间测量，未利用金融历史数据，QPE寄存器比特数无法自适应，精度与资源无法平衡。

## 相关工作
1. 量子伊辛类算法（HyQSAT、CAFQA、FrozenQubits）：仅二元投资决策，无精确权重输出，不满足量化金融需求。
2. 基础HHL：直接映射投资线性方程组，无矩阵预处理，电路资源开销极高。
3. 混合HHL：中间测量削减部分受控门，缺少金融数据驱动参数调优，精度提升有限。
4. 通用特征值预估方法：仅协方差矩阵预测或统计数量统计，无法适配HHL完整电路参数配置。

## 本文解决方案
### 1 约束等价缩放变换
基于Black投资模型引入双缩放因子s₁、s₂，等价变换拉格朗日矩阵；采用Nelder-Mead单纯形迭代搜索最优因子，条件数可从10⁵降至10量级，从根源降低HHL复杂度。
### 2 最小-最大特征值SVR预测模型
利用美股历史收益、协方差数据离线训练SVR，仅预测矩阵最小、最大特征值；无需完整特征值分解，大幅削减经典预处理开销。
### 3 自适应量子电路参数配置
依据预测特征值标准化矩阵，固定哈密顿模拟时间为π，推导QPE最小比特数、R_Y归一化常数，实现电路精度与量子资源动态平衡。
### 4 SAPO完整量子求解链路
金融数据构造拉格朗日矩阵→缩放预处理→特征值预测→自适应HHL电路仿真→向量后处理输出最优资产权重。

## 实验分析
1. 实验数据集：AMEX、Nasdaq、NYSE股票历史数据，测试2~6资产规模，对比基础HHL、Qiskit-HHL、混合HHL。
2. 复杂度指标：电路量子比特、深度、CNOT门数综合度量Θ，误差1/4~1/16区间，复杂度平均降低34.64%~36.94%，CNOT门最高缩减99.996%。
3. 优化精度：固定QPE比特下相较Qiskit-HHL精度提升1.52倍，同等资产规模优于混合HHL 1.39倍；4比特QPE精度优于竞品10比特配置。
4. 消融实验：缩放技术是核心增益来源，特征值预测进一步提升1.05~1.54倍精度；资产数量越多缩放适配效果越好。
5. 预测误差：两资产场景特征值预测相对误差最高，但最终优化精度损失仅7.21%，多资产预测稳定性显著提升。

## 研究启发
1. 量子金融算法不能直接套用通用线性求解器，必须结合均值方差等金融理论做矩阵定制预处理。
2. 高条件数矩阵是HHL量子资源爆炸核心诱因，等价缩放是低成本硬件适配关键手段。
3. 无需求解全部特征值，仅预测极值即可完成电路超参配置，大幅降低经典侧预处理成本。
4. 离线金融历史数据训练轻量回归模型，可在线自适应平衡量子比特与求解精度。
5. NISQ受限场景下，算法-领域知识协同设计，能同时提升量子线路可扩展性与优化精度。
