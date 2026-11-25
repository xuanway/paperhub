---
title: "IRGNN: A Graph-based Framework Integrating Numerical Solution and Point Cloud for Static IR Drop Prediction"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# IRGNN: A Graph-based Framework Integrating Numerical Solution and Point Cloud for Static IR Drop Prediction

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA4: Power Analysis and Optimization</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132887">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132887</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 静态IR压降预测，图神经网络，数值求解器集成，点云特征提取 </p>
</div>


---

## 研究概要
本文提出IRGNN图学习框架用于静态IR压降预测，融合AMG-PCG数值粗解与版图点云特征，构建专属IRGraph供电网图结构；设计距离注意力NDA层+图Transformer层捕获局部与全局拓扑。ICCAD2023等数据集验证，相较CNN基线MAE最高降低38.67倍，推理速度较数值工具PowerRush提升4.6倍，支持全节点细粒度压降预测。

## 背景和动机
1. 先进工艺供电网规模激增，传统AMG-PCG等数值求解精度高但迭代耗时、内存开销巨大，不适合早期设计迭代。
2. IREDGe、MAUnet等CNN类IR预测将版图转为像素图，仅能粗粒度像素输出，无法获取每个金属节点精确压降，难以定位微小热点。
3. CNN模型丢失供电网三维金属层拓扑、电流流向、节点空间距离等关键几何信息，模型泛化性差、极端最坏压降误差高。
4. 纯深度学习黑盒可解释性弱，缺少数值解先验约束，陌生供电网设计预测稳定性不足。
5. 现有图模型未融合点云空间特征，无法量化节点欧氏距离对压降衰减的影响，局部邻域信息聚合效果有限。

## 相关工作
1. 数值求解器（PowerRush）：基于KCL/KVL方程组，全节点高精度，但百万级网格仿真数十秒，迭代成本极高。
2. CNN类IR预测（IREDGe/MAUnet）：速度快，采用2D像素建模，丢失3D拓扑，仅像素级输出，最坏压降误差大。
3. 通用电路GNN：仅编码电路连接关系，未引入供电网三维点云空间距离、金属电阻等专属物理特征。
4. 点云EDA模型：用于拥塞、DRC检查，未结合线性方程组数值解先验，不适用于压降回归任务。
5. ICCAD竞赛基线CNN：多尺度卷积无全局建模，跨工艺供电网迁移性能衰减严重。

## 本文解决方案
### 1 AMG-PCG快速数值粗解前置
减少传统求解迭代次数，得到所有节点近似IR值作为模型输入特征，为神经网络提供物理先验，提升可解释性与泛化能力。
### 2 供电网点云特征提取
将每层金属节点建模为三维点云，标准化x/y平面坐标与z层高度，计算节点偏移向量表征电流流向与空间距离，保留版图三维几何信息。
### 3 IRGraph专用图构建
原始金属连线作为实边；对空间近邻节点增设虚拟距离边；节点嵌入电流、源距离、数值粗解等特征，边携带金属电阻、偏移向量。
### 4 NDA邻域距离注意力层
融合节点、边特征，基于节点欧氏距离设计衰减注意力权重，区分远近邻域对压降的贡献，精准聚合局部供电拓扑信息。
### 5 GT图Transformer全局层
突破局部邻域限制，实现全图节点自注意力交互，捕捉远距离电源、负载之间全局压降耦合，精准预测最坏热点。

## 实验分析
1. 测试数据集：ICCAD2023工业供电网、Nangate/ASAP/Skywater开源工艺基准，指标采用MAE、MIRDE、F1、CC、推理耗时。
2. 对比CNN基线：在大规模测试集IRGNN MAE仅0.46×10⁻⁴V，较MAUnet降低38.67%，热点F1、相关系数CC全面领先。
3. 对比数值工具PowerRush：全节点预测MAE 0.56优于0.71，单设计推理6.64s，相较30.52s提速4.6倍。
4. 迁移测试：Nangate预训练迁移至ICCAD真实设计，MAE 1.68，显著优于所有CNN竞品，跨拓扑泛化更强。
5. 消融实验：数值粗解、点云特征、NDA、GT层均为关键模块，移除后MAE、热点F1大幅退化。

## 研究启发
1. CNN像素化建模丢失供电网三维拓扑，图学习+点云联合建模是实现节点级高精度IR预测的最优路径。
2. 将快速数值粗解作为神经网络输入先验，可解决纯DL模型无物理约束、泛化差、可解释性弱的痛点。
3. 供电压降受节点空间距离显著影响，距离感知注意力能更合理加权邻域电流、电阻特征。
4. 仅局部消息传递会丢失远距离电源耦合，搭配图Transformer捕获全局依赖可大幅降低最坏压降误差。
5. 数值求解与图深度学习融合可平衡精度与速度，适配芯片早期迭代中大规模供电网快速分析需求。
