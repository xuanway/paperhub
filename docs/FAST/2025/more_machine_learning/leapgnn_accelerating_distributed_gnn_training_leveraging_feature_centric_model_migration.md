---
title: "LeapGNN: Accelerating Distributed GNN Training Leveraging Feature-Centric Model Migration"
description: "FAST 2025 · More Machine Learning · 把 GNN 模型搬到顶点特征所在服务器，微图调度让分布式训练比 P3 最高快 4.2 倍"
tags:
  - "FAST2025"
  - "More Machine Learning"
  - "distributed GNN training"
  - "feature-centric"
---

# LeapGNN: Accelerating Distributed GNN Training Leveraging Feature-Centric Model Migration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">分布式 GNN 训练以模型为中心，要把海量顶点特征搬到模型侧，远程特征聚合占训练时间 44%–83%。LeapGNN 反过来把模型迁到特征所在的服务器，用微图训练单元、特征预聚合与微图合并压缩远程取数与同步开销，在五个数据集、五个模型上相对 P3 最高加速 4.2 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · More Machine Learning</p>
</div>

**中文标题**：LeapGNN：借助以特征为中心的模型迁移加速分布式 GNN 训练

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/chen-weijian-leap](https://www.usenix.org/conference/fast25/presentation/chen-weijian-leap)

**论文 PDF**：[fast25-chen-weijian-leap.pdf](https://www.usenix.org/system/files/fast25-chen-weijian-leap.pdf)

**作者**：Weijian Chen、Shuibing He、Haoyang Qu（Zhejiang University）；Xuechen Zhang（Washington State University Vancouver）

**会议**：FAST 2025 · Santa Clara, CA · 第 255–270 页

**Session**：More Machine Learning · 2025-02-26 09:00–10:20 · Chair：Ali R. Butt（Virginia Tech）

**所属 Session**：[More Machine Learning](index.md) · [FAST 2025](../index.md)

**关键词**：distributed GNN training, feature-centric, model migration, micrograph, communication optimization

---

## 英文摘要

Distributed training of graph neural networks (GNNs) has become a crucial technique for processing large graphs. Prevalent GNN frameworks are model-centric, necessitating the transfer of massive graph vertex features to GNN models, which leads to a significant communication bottleneck. Recognizing that the model size is often significantly smaller than the feature size, we propose LeapGNN, a feature-centric framework that reverses this paradigm by bringing GNN models to vertex features. To make it truly effective, we first propose a micrograph-based training strategy that leverages a refined structure to enhance locality, combined with the model migration technique, to minimize remote feature retrieval. Then, we devise a feature pre-gathering approach that merges multiple fetch operations into a single one to eliminate redundant feature transmissions. Finally, we employ a micrograph-based merging method that adjusts the number of micrographs for each worker to minimize kernel switches and synchronization overhead. Our experimental results demonstrate that LeapGNN achieves a performance speedup of up to 4.2× compared to the state-of-the-art method, namely P 3 .

## 中文摘要

图神经网络的分布式训练已成为处理大图的关键技术。主流框架以模型为中心，需要把海量顶点特征搬到模型所在的服务器，形成明显的通信瓶颈。注意到模型参数规模通常远小于特征规模，LeapGNN 把范式反过来，做成以特征为中心的框架：让 GNN 模型迁移到顶点特征所在的位置。为让这一思路真正有效，它首先提出基于微图（micrograph）的训练策略，用更精细的结构提升局部性，并结合模型迁移把远程特征取回降到最低；其次设计特征预聚合（pre-gathering）方法，把多次取回操作合并为一次，消除冗余的特征传输；最后提出基于微图的合并方法，为每个 worker 调整微图数量，以减少 kernel 切换与同步开销。实验表明，LeapGNN 相对当前最优方法 P3 取得最高 4.2 倍的性能加速。

## 一句话总结

> 模型参数远小于顶点特征，于是把模型搬到特征一侧，再用微图把一次迁移要取的特征压到最少。

## 研究背景与问题

- **特征搬运就是瓶颈**：图数据集很容易超出单机内存（Pinterest 18 TB、ByteDance 100 TB），训练要在多台服务器间切分拓扑与特征；实测远程顶点特征聚合占训练时间的 44%–83%，采样与计算合计平均只有 11%。
- **模型中心方案各有代价**：近似采样类工作提升本地命中率却牺牲精度，而推荐系统中 0.1% 的精度下降就可能造成数百万美元损失；用 GPU 显存放热点特征则受缓存容量限制；P3 用随机哈希分区结合模型并行与数据并行，但面向隐维度小的 GNN，层数增加后收益衰减。
- **换向的动机**：每轮迭代从远端取回的数据量与模型参数规模之比 α 在 13.4 到 2368.1 之间，112 层的 DeeperGCN 达到 2368.1——搬模型比搬特征便宜。
- **朴素换向会反噬**：直接实现会引入中间数据（部分聚合结果、激活）的传输，数据移动量反而比模型中心方案最多增加 2.59 倍。

## 核心贡献

- **特征中心的训练范式**：以模型迁移替代特征搬运来降低特征通信开销，是首个按此思路设计的分布式 GNN 训练框架。
- **微图（micrograph）训练单元**：用比 subgraph 更细的粒度组织训练，提升根顶点与其 fanout 邻居同机的概率，配合模型迁移减少远程取特征与中间数据。
- **特征预聚合与微图合并**：前者把多次特征取回合并为一次以消除冗余传输，后者按 worker 自适应分配微图数量以减少模型迁移、kernel 切换与同步开销。
- **无损精度的工程实现**：在 DGL 上实现并在五个数据集、五个模型上验证，三项技术均不改变模型精度。

## 方法与技术要点

- **以微图为训练单位**：每个 worker 按微图组织训练，逐微图把模型迁到特征所在服务器并在本地完成前向与反向，聚合结果更少跨机往返；模型在每个迭代结束时回到原服务器。
- **模型迁移与梯度处理**：迁移的是模型参数而非特征，各服务器收到多份部分梯度后与已有梯度原地累加，因此显存占用与 DGL 相当。
- **特征预聚合（pre-gathering）**：把同一批内的多次特征取回操作合并成一次通信，减少重复传输与往返次数。
- **微图合并（micrograph merging）**：为每个 worker 动态调整微图数量，减少迭代内的模型迁移次数，从而减少 kernel 切换与同步开销。
- **实现约束**：不修改 DGL 的 GNN 计算 kernel，兼容 sum、max、LSTM 等聚合；效果依赖微图的局部性，适用于有局部性的分区算法，不适用于随机分区。

## 评估与主要结果

- **加速比**：基于 DGL 实现，在五个数据集、五个 GNN 模型、分布式 GPU 集群上，相对当前最优方法 P3 最高加速 4.2 倍。
- **迁移开销**：相较 DGL，模型与梯度跨机迁移带来的额外通信平均只占总训练时间的 4.6%，计入该开销后训练时间仍优于其他方案。
- **含分区的端到端对比**：把分区时间计入总时间后，GAT 在典型 200 epoch 训练中仍比 P3 快 1.6 倍。
- **内存与恢复**：原地累加部分梯度使内存占用与 DGL 相当；模型在迭代末回到原机，因此只在迭代结束时做 checkpoint，与常规做法一致。

## 代码与研究制品

- [代码仓库](https://github.com/ISCS-ZJU/LeapGNN-AE)

[返回 More Machine Learning](index.md) · [返回 FAST 2025](../index.md)
