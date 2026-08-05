---
title: "ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# ParGNN: A Scalable Graph Neural Network Training Framework on multi-GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133102">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133102</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 图神经网络，全批量分布式训练，负载均衡，计算与通信重叠 </p>
</div>

---

## 研究概要
本文提出多GPU全批量GNN训练框架ParGNN，设计PGALB两级图超划分算法缓解负载失衡，搭配子流水线SP重叠计算与通信。在4类大图数据集测试，相较DGL最高提速21.8倍、相较PipeGCN最高提速2.7倍，收敛精度无损，达到目标精度耗时最短。

## 背景和动机
1. 全批量GNN训练精度优于小批量，但多GPU下存在严重负载失衡，METIS仅按顶点/边划分，未考虑SpMM/SDDMM实际计算耗时，失衡率最高超145%。
2. 分布式GNN跨层顶点特征通信开销占训练14%~32%，现有延迟通信策略会损害收敛速度与最终精度。
3. 传统单粒度图划分方案难以适配不同GPU算力，图规模、GPU数量变更时需完整重划分，开销巨大。
4. PipeGCN等流水线方案仅单张子图调度，无法充分隐藏异步通信延迟，硬件利用率偏低。
5. GAT等注意力GNN计算负载远高于GCN，现有划分策略未区分模型计算特性，负载倾斜更严重。

## 相关工作
1. 图划分工具METIS：仅最小割均衡顶点/边，不建模稀疏算子真实运行时延，无法实现算力均衡。
2. DGL分布式GNN：基础同步通信机制，无流水线重叠，通信阻塞严重，训练效率极低。
3. PipeGCN：延迟通信流水线，牺牲模型收敛精度换取通信隐藏，泛化性差。
4. DistGNN：CPU端延迟通信方案，无法适配多GPU NVLINK高速互联架构。
5. 小批量采样GNN：牺牲全局图完整信息，模型表征与收敛精度弱于全批量训练。

## 本文解决方案
### 1 PGALB探查引导两级超划分负载均衡算法
一级粗化原图得到轻量代理图；二级探查各子图真实SpMM/SDDMM运行时延赋予权重，基于权重重分配多子图至各GPU，大幅降低负载失衡率，重划分开销极低。
### 2 多子图超划分部署策略
单个GPU分配多个独立子图，打破单GPU单图限制，为计算通信流水线重叠提供调度空间，适配GCN/GAT差异化计算负载。
### 3 SP子图流水线通信重叠算法
分离计算流与异步通信CUDA流，设置全局顶点接收缓冲区；子图计算完成立即异步发送主顶点特征，通信与后续子图计算完全重叠。
### 4 无精度损失梯度推导机制
重新设计前后向传播梯度计算公式，缓冲区延迟读取顶点特征不破坏求导链式法则，流水线调度不影响模型收敛精度。
### 5 端到端多GPU训练流水线
集成图划分、负载评估、子图调度、异步通信模块，兼容PyTorch，支持GCN/GAT主流全批量图模型。

## 实验分析
1. 实验环境：H10 80GB多GPU服务器，Products/Proteins/Yelp/Reddit四大公开大图，基线DGL、PipeGCN。
2. 负载均衡：PGALB相较METIS失衡率平均降低25%，划分总耗时增幅仅1%左右，额外开销可忽略。
3. 训练速度：相较DGL最高提速21.8倍，相较PipeGCN最高提速2.7倍；通信耗时平均削减近70%。
4. 收敛性能：ParGNN与基线最终精度差距控制在2.5%以内，到达预设精度耗时远短于对比方案。
5. 消融实验：PGALB对GAT加速增益更大；SP流水线是通信开销大幅下降核心，两者协同优化收益叠加。

## 研究启发
1. 图负载均衡不能仅依靠顶点/边数量，需探查稀疏矩阵算子真实运行时延，才能匹配GPU算力差异。
2. 超划分多子图部署是实现计算通信重叠的基础，单GPU单图架构调度空间受限。
3. 异步通信流水线可做到无损隐藏延迟，无需采用牺牲精度的延迟同步策略。
4. GAT与GCN计算负载差异巨大，负载均衡算法需区分模型算子特性针对性调优。
5. 两级粗化重划分架构，可大幅降低图变更、GPU扩容时的重新划分时间，适配动态图持续学习场景。