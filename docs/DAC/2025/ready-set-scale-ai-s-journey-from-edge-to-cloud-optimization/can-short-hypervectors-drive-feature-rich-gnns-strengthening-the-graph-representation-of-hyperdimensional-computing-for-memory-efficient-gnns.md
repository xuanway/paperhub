---
title: "Can Short Hypervectors Drive Feature-Rich GNNs? Strengthening the Graph Representation of Hyperdimensional Computing for Memory-efficient GNNs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Can Short Hypervectors Drive Feature-Rich GNNs? Strengthening the Graph Representation of Hyperdimensional Computing for Memory-efficient GNNs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133067">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133067</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 图神经网络，超维计算，内存，图表示 </p>
</div>


---


## 研究概要
本文提出CiliaGraph轻量超维计算GNN框架，打破万维超长超向量固有范式，提出PRBF编码、差分聚合、拼接组合三类算子，解决编码失真、图结构偏置、中心节点缺失三大缺陷。仅百维短向量即可完成单样本图分类，相比主流GNN内存平均缩减292倍，训练加速最高313倍，精度与SOTA持平。

## 背景和动机
1. 传统HDC-GNN遵循“万维超向量黄金准则”，海量节点搭配超长向量造成严重内存瓶颈，边缘设备难以部署。
2. 现有HDC编码（随机投影/层级映射）用汉明距离替代欧式距离，数值特征空间发生严重失真，模型精度大幅下滑。
3. 原有HDC绑定操作单向聚合，丢失双向边结构信息，引入图结构偏置，无法复刻标准GNN消息传递。
4. 主流HDC合并阶段直接丢弃中心节点超向量，缺失自身特征，进一步削弱图表征能力，只能依靠加长向量弥补缺陷。
5. 高特征图数据（如COIL-RAG含64维属性）下超长向量内存开销爆炸，急需短向量高性能HNN方案。

## 相关工作
1. 传统标准GNN（GCN/GIN/GAT）：精度高，但依赖海量浮点矩阵运算，训练推理时延极高。
2. GraphHD等HDC-GNN：采用上万维超向量，内存占用巨大，编码与聚合存在三类固有噪声，精度显著低于标准GNN。
3. k跳增强GNN（KP-GIN/MAG-GIN）：优化图局部结构，计算量大幅提升，无内存优化手段。
4. 传统HDC编码（随机投影、层级映射）：严格正交约束，数值距离失真，稠密特征量化精度差。
5. 正交环HDC编码：固定比特翻转步长，无法适配非均匀数值分布，特征表达能力不足。

## 本文解决方案
### 1 PRBF塑性随机比特翻转编码
改进正交环机制，按特征数值密度动态调整比特翻转率，引入拟正交替代严格正交；非均匀量化映射数值分布，消除编码距离失真，百维短向量即可承载多维度节点特征。
### 2 差分双向聚合算子
融合特征相似度权重与图连通度构造超权重矩阵，实现边双向对称消息传递；区分中心/邻居贡献，复刻GNN完整聚合逻辑，消除单向绑定带来的结构偏置。
### 3 中心拼接式组合算子
将原始节点超向量与聚合向量等长拼接，完整保留中心节点自身特征，解决传统HDC中心节点缺失问题，不额外带来内存压力。
### 4 CiliaGraph完整推理流水线
特征分布预量化→PRBF生成节点超向量→超权重矩阵差分聚合→拼接融合→全局捆绑分类，全程仅120维短向量，支持单样本一次性推理。
### 5 短向量理论下界推导
推导出满足2n个拟正交向量的最小维度公式，理论证明37~122维即可覆盖全部测试数据集，从数学层面支撑短向量可行性。

## 实验分析
1. 实验环境：RTX4090、AMD EPYC，测试Letter/BZR/AIDS/Synthie/PROTEINS/COIL-RAG多图数据集，对比标准GNN与GraphHD等HNN基线。
2. 内存开销：相较8种SOTA模型平均内存降低292倍，Synth数据集最高缩减2341倍，适配边缘受限硬件。
3. 训练时延：CPU/GPU下训练速度平均提升103倍，最高加速313倍，HDC原生极简运算大幅减少计算量。
4. 模型精度：多数据集精度接近最优标准GNN，COIL-RAG仅落后1.48%，远超GraphHD等传统HDC方案。
5. 消融验证：PRBF编码较传统方法平均提升15%精度；超权重矩阵缺失会造成最高31%精度损失；最优向量维度集中37~122。

## 研究启发
1. HDC无需上万维严格正交超向量，适度放宽至拟正交，百维短向量即可实现充足特征表征，从根源解决内存瓶颈。
2. 传统HDC精度短板来自编码、聚合、合并三步固有噪声，仅加长向量治标，针对性算子改造是治本思路。
3. 图神经网络HDC化必须复刻双向消息传递与中心节点保留机制，单向简化会永久丢失图结构信息。
4. 数值分布非均匀场景需动态比特翻转量化，固定步长正交环无法适配稠密特征区间，表征能力受限。
5. 面向边缘图分类任务，短向量HDC框架兼具低内存、低时延、高鲁棒性，是轻量化部署优选路线。
