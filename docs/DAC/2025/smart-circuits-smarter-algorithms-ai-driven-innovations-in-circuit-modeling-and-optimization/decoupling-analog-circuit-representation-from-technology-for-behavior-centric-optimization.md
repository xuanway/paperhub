---
title: "Decoupling Analog Circuit Representation from Technology for Behavior-Centric Optimization"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Decoupling Analog Circuit Representation from Technology for Behavior-Centric Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133189">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133189</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 模拟电路尺寸设计，柯尔莫哥洛夫-阿诺德网络，知识迁移，行为模型 </p>
</div>

---

## 研究概要
本文提出行为导向模拟电路优化框架BCOA，将电路用晶体管电气特性解耦工艺依赖，设计电气-尺寸映射方法，构建RBF-KAN小样本代理模型，搭配MC-HV帕累托估计加速多目标优化。基于AnalogGym放大器验证，大小信号FOM提升1.73~2.64倍，工艺迁移速度提升3.5~6.2倍，仿真开销大幅降低。

## 背景和动机
1. 模拟电路高度绑定工艺PDK，传统基于管子长宽(W/L)的尺寸优化泛化性差，跨工艺移植需大量重仿真，自动化程度低。
2. 主流RL、贝叶斯、GNN优化以器件尺寸为输入，建模空间复杂，需上万次仿真才能收敛，算力消耗巨大。
3. 经典gm/ID方法依赖预设沟道长度L，工艺缩放后非理想效应加剧，手工查表迭代效率低，多目标优化乏力。
4. 传统超体积HV帕累托评估复杂度随目标数指数上涨，多指标放大器优化耗时极长，易陷入局部最优。
5. 现有代理模型（GP/ANN/GNN）小样本拟合非线性电路能力弱，无法兼顾全局平滑与局部突变特性。

## 相关工作
1. 基于gm/ID的手工优化：依靠查表选取工作区，但必须预设L，工艺适配差，难以自动化多目标寻优。
2. 图神经网络GNN类优化：仅编码拓扑连接，未挖掘电路行为本质，样本需求庞大，跨工艺迁移弱。
3. 高斯过程GP代理：多目标场景计算量爆炸，高维指标下拟合精度快速衰减。
4. 贝叶斯/进化EDA算法：依赖尺寸空间采样，易困局部最优，仿真迭代次数极高。
5. 标准KAN网络：B样条激活对非均匀样本适配差，无法同时捕捉高低频电路非线性特征。

## 本文解决方案
### 1 工艺解耦行为层表征
放弃W/L作为优化变量，采用gm、ft、Vds、ΔVgs大小信号电气参数描述电路行为，消除与特定PDK强绑定，天然支持跨工艺迁移。
### 2 电气参数到器件尺寸映射方法
预仿真多工艺查表，通过ft、ΔVgs、Vds联合推导沟道L，结合gm/ID表反推宽度W，无需手工预设长度，映射误差控制在2%以内。
### 3 RBF-KAN轻量代理模型
用高斯-拉普拉斯径向基替换原生B样条激活，兼顾全局平滑趋势与局部电路突变，数百次仿真即可完成高精度拟合，显著降低仿真开销。
### 4 MC-HV蒙特卡洛帕累托估计
动态调整参考点、曲率自适应加密采样，将多目标复杂度从O(n^m)降至O(n²log n + nm)，超体积计算速度提升97%。
### 5 完整BCOA迭代优化流水线
预生成工艺查表→拉丁超立方初始化行为样本→RBF-KAN预测→MC-HV筛选优质解→参数映射回尺寸仿真，循环收敛，兼容MOEA/D多目标优化器。

## 实验分析
1. 实验平台：RTX4080 GPU、Xeon服务器，测试NMCF/NMCNR/DFCFC三类多级放大器，覆盖90/130/180nm三种工艺。
2. 映射精度：gm、ft映射误差＜1%，Vds、ΔVgs误差＜2%，多工艺下稳定性良好。
3. 代理模型对比：同等仿真次数下RBF-KAN MSE远低于GP/ANN/GNN，行为建模精度优于尺寸建模。
4. 优化性能：相较GNNRL、cVTSBO、gm/ID-RL，FOM_L、FOM_S提升1.73~2.64倍，建立面积、建立时间显著优化。
5. 工艺迁移：跨节点仿真次数减少6.6~7.8倍，迁移速度提升3.5~6.2倍，知识迁移效果显著。

## 研究启发
1. 模拟EDA优化应脱离器件尺寸空间，以电气行为作为核心优化变量，从根源解除工艺绑定，大幅提升可移植性。
2. KAN搭配RBF激活适配模拟电路高低频混合非线性，是小样本EDA代理建模高效路线。
3. 传统HV多目标评估是优化瓶颈，蒙特卡洛自适应采样可大幅降低多指标放大器迭代耗时。
4. gm/ID查表思路可自动化改造，通过多电气参数联合反推尺寸，摆脱人工迭代流程。
5. 行为统一表征+工艺查表映射是实现跨节点模拟电路快速复用、减少重复仿真的通用框架思路。
