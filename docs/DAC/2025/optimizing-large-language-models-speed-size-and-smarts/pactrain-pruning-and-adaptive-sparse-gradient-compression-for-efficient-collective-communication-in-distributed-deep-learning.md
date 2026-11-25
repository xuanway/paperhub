---
title: "PacTrain: Pruning and Adaptive Sparse Gradient Compression for Efficient Collective Communication in Distributed Deep Learning"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PacTrain: Pruning and Adaptive Sparse Gradient Compression for Efficient Collective Communication in Distributed Deep Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2505.18563">https://arxiv.org/abs/2505.18563</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 分布式深度学习，梯度压缩，模型剪枝 </p>
</div>

---

## 研究概要
本文提出PacTrain分布式训练框架，融合模型剪枝与自适应稀疏梯度压缩。设计梯度稀疏约束GSE与掩码追踪器，各工作器共享全局稀疏掩码，兼容AllReduce原语；搭配三元梯度量化进一步压缩。在带宽受限场景下，相较主流压缩方案训练吞吐提升1.25~8.72倍，最高提速8.72倍，精度损失可控。

## 背景和动机
1. 大模型分布式训练梯度聚合通信开销巨大，低带宽多机集群通信成为核心瓶颈，拉长收敛至精度(TTA)时间。
2. 现有TopK、TernGrad等梯度压缩方法存在缺陷：要么破坏AllReduce兼容性，要么引入大量误差、收敛变慢。
3. 传统稀疏集体通信方案依赖全局稀疏索引传输，无法适配PyTorch DDP等主流分布式框架，改造成本高。
4. 模型剪枝多用于推理加速，未结合训练梯度压缩，剪枝后权重稀疏特性未用于降低同步流量。
5. DDP会扁平化梯度张量、丢失层权重映射关系，难以统一跨节点稀疏掩码，无法实现无损稀疏同步。

## 相关工作
1. 梯度压缩类：TopK、DGC依靠梯度幅值筛选，需AllGather不兼容AllReduce；TernGrad量化误差大，收敛速度受损。
2. 稀疏集体通信：OmniReduce、Zen需要专用稀疏聚合流程，无法对接原生DDP通信原语。
3. 模型剪枝：传统train-prune-fine-tune仅优化推理；LTH、动态稀疏训练未面向分布式通信做协同设计。
4. 联邦稀疏训练Fed系列：面向端侧受限场景，不针对多GPU数据并行AllReduce优化。
5. 张量同态压缩THC：压缩计算开销高，带宽收益难以抵消额外运算耗时。

## 本文解决方案
### 1 梯度稀疏约束GSE算法
每轮训练将零权重对应梯度强制置零，让梯度与权重共享稀疏分布，统一各GPU稀疏模式，天然适配剪枝后的稀疏网络。
### 2 掩码追踪器Mask Tracker
解决DDP梯度扁平化映射难题，持续记录权重-梯度稀疏对应关系；掩码稳定后仅传输非零梯度，不稳定时全量同步保障收敛。
### 3 全局共享稀疏无损压缩
所有工作器共用一套剪枝掩码，稀疏梯度重排为稠密张量走标准AllReduce，无需额外索引传输，无解压重计算开销。
### 4 剪枝+三元量化联合优化
基于GraSP梯度流得分筛选关键权重，剪枝后对剩余梯度做三元量化；引入随机扰动帮助模型跳出局部极小值。
### 5 轻量化DDP插件实现
基于PyTorch DDP通信钩子开发，无需重构分布式底层，适配NCCL/TCP通信链路，兼容CNN、ViT主流视觉模型。

## 实验分析
1. 实验环境：8×A40虚拟GPU集群，带宽100M/500M/1Gbps，测试VGG19/ResNet152/ViT，对比FP16、TopK基线。
2. 收敛性能：带宽受限场景TTA最高提速8.72倍，相比FP16、TopK提升1.25~7.05倍，同等精度收敛更快。
3. 剪枝鲁棒：剪枝比例≤80%时各类模型精度下降小于2%，超高稀疏仍可维持有效训练。
4. 消融对比：掩码稳定压缩、GSE稀疏约束是两大核心增益；仅量化无剪枝时通信缩减效果微弱。
5. 带宽适配：带宽越低加速优势越明显，1Gbps高带宽场景仍优于传统梯度压缩方案。

## 研究启发
1. 模型剪枝不仅服务推理，可主动塑造梯度稀疏分布，作为分布式梯度压缩前置核心手段。
2. 跨节点统一稀疏掩码是兼容AllReduce的关键，避免稀疏索引额外通信开销。
3. DDP扁平化梯度会破坏权重映射，专用掩码追踪模块可低成本打通稀疏同步链路。
4. 剪枝与梯度量化可协同增效，量化随机性弥补剪枝带来的优化空间收缩问题。
5. 梯度压缩方案不能只看压缩率，必须兼顾AllReduce兼容性与收敛速度，TTA是更全面评估指标。
