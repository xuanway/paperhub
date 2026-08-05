---
title: "A Novel Image-Graph Heterogeneous Fusion Framework for Static IR Drop Prediction"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# A Novel Image-Graph Heterogeneous Fusion Framework for Static IR Drop Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA6: Analog CAD, Simulation, Verification and Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132429">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132429</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> IR压降预测，卷积神经网络，图神经网络，异构融合 </p>
</div>

---

## 研究概要
本文提出IGHF图像-图异构融合框架用于静态IR压降预测，CNN分支LLE+HACG提取多尺度空间特征，GNN分支CVA模块聚合异构高阶拓扑信息，双分支特征融合。在CircuitNet数据集测试，相比MAUNet、IREDGe误差分别降低24.6%、55.0%，迁移学习下泛化能力显著提升。

## 背景和动机
1. 先进工艺芯片PDN规模庞大，传统MNA数值求解内存、算力开销极高，难以快速迭代设计。
2. 现有纯CNN IR预测方法仅捕捉像素空间特征，丢失单元拓扑连接、全局电流传导规律，热点误差大。
3. 单一GNN无法提取布局局部、多层级功耗分布图像信息，仅靠拓扑预测精度不足。
4. 现有网络仅处理一阶邻域，忽略高阶单元耦合效应，复杂GPU/NPU芯片压降预测失真。
5. 模型跨电路泛化弱，少量新设计样本下预测误差急剧升高，缺少迁移适配方案。

## 相关工作
1. 数值类IR求解（多重网格、随机游走）：精度高但超大电路求解耗时极长，不适合快速迭代。
2. 纯CNN预测(IREDGe、MAUNet、PowerNet)：依赖图像卷积，缺失PDN非欧拓扑，热点误差大。
3. 基础GNN电路预测：仅建模一阶邻接关系，无法捕捉远距离电流耦合。
4. 单模态CNN/GNN模型：仅利用布局图像或仅利用拓扑，两类互补信息无法融合。
5. 简单图卷积模型：无异构边区分机制，无法区分物理连线与空间虚拟邻接关系。

## 本文解决方案
### 1 双模态输入构建
布局提取功耗、电阻特征图；基于网表构建异构图，区分真实电流边、空间虚拟邻接两类异构关系，PI筛选冗余特征降低输入维度。
### 2 CNN分支：Power ScaleFusion Unet
LLE融合长程大核模块+局部小核模块，同步全局/局部功耗特征；解码器HACG分层+邻接补偿模块，消除上采样信息损失，自适应多尺度融合。
### 3 GNN分支：CVA单元感知图模块
异构注意力区分两类边权重；MixHop传播层聚合一/二阶邻域电压特征，叠加多层残差块捕获远距离单元耦合。
### 4 图像-图异构特征融合
将GNN节点拓扑序列与CNN像素特征对齐，线性层融合双分支输出，联合图像、拓扑损失监督训练。
### 5 迁移学习适配方案
预训练编码器冻结，微调SSF-ADA特征适配器与解码器，少量新电路样本即可大幅降低预测误差。

## 实验分析
1. 实验环境：RTX3090，CircuitNet公开数据集，基线MAUNet、IREDGe，指标MAE、AMMAE、PCC、R²。
2. 基准精度：整体MAE仅0.378mV，对比MAUNet下降24.6%，对比IREDGe下降55.0%，热点AMMAE显著更低。
3. 可视化效果：高低压降热点区域误差图噪点更少，预测版图与黄金数据结构一致性更强。
4. 迁移实验：少量NVDLA/VORTEX样本微调后MAE降幅最高58.7%，优于MAUNet迁移效果。
5. 消融实验：CNN、GNN分支缺一精度大幅下滑；LLE、HACG、CVA均为核心性能增益模块。

## 研究启发
1. IR压降同时依赖布局图像多尺度功耗分布与PDN拓扑连接，单一CNN/GNN均存在信息缺失，异构融合是提升精度关键。
2. 长程+局部并行编码器可同时捕捉全局电流叠加与单元微负载细节，弥补单一感受野缺陷。
3. PDN存在高阶单元耦合，普通一阶GCN不足以建模，MixHop高阶邻域聚合可还原远距离压降干扰。
4. 区分真实布线与空间虚拟两类异构边，能精准建模不同邻接关系对电压的差异化影响。
5. 双分支模型搭配轻量化特征适配器，可在少样本新电路上实现有效迁移，适配工业多样芯片设计。
