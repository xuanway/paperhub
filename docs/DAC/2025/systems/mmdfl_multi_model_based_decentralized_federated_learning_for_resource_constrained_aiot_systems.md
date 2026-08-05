---
title: "MMDFL: Multi-Model-based Decentralized Federated Learning for Resource-Constrained AIoT Systems"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MMDFL: Multi-Model-based Decentralized Federated Learning for Resource-Constrained AIoT Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS4: Embedded System Design Tools and Methodologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133116">https://ieeexplore.ieee.org/document/11133116</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>人工智能物联网，去中心化联邦学习，多模型学习，资源受限，随机梯度下降 </p>
</div>

---

## 研究概要
本文提出MMDFL多模型去中心化联邦学习框架，面向算力带宽受限AIoT设备。引入漫游模型逐设备遍历训练，设计融合数据、资源、遗忘因子的自适应邻居选择策略。仿真与真实嵌入式集群验证，相较主流DFL算法，通信开销大幅下降，IID/非IID场景分类精度、收敛速度均更优。

## 背景和动机
1. 中心化联邦学习存在单点故障、服务器通信瓶颈，去中心化DFL采用P2P通信，但仍受AIoT设备算力、带宽约束。
2. 传统DFL每轮所有邻居模型聚合，弱设备拖慢全局训练，非IID数据易出现权重漂移、精度暴跌。
3. 全邻居同步聚合模式交互复杂，通信量巨大，资源受限终端难以支撑高频完整模型传输。
4. 简单邻居选择易产生掉队设备、灾难性遗忘问题，现有DFL缺少多模型并行知识流转机制。
5. 现有优化方案仍基于全局FedAvg聚合范式，无法解耦设备间绑定关系，知识共享效率低。

## 相关工作
1. 基础去中心化DFL（DFedAvgM、D-PSGD）：每轮向全部邻居完整传模型，通信开销极高，异构设备适配差。
2. 非IID优化DFedSAM、DeSA：通过梯度扰动、特征对齐缓解数据异构，但未解决通信过载。
3. 带宽优化DFedPGP、YOGA：仅传输部分网络层参数，精度损失明显，无多模型流转设计。
4. 异步轻量化LD-SGD：降低同步频率，但未解决邻居选择带来的遗忘、掉队问题。
5. 现有方案均依赖全局平均聚合，无漫游多模型独立遍历的知识分发架构。

## 本文解决方案
### 1 漫游多模型核心架构
摒弃全邻居同步聚合，部署少量漫游模型独立遍历拓扑设备；设备收到多漫游模型时才执行FedAvg聚合，单模型直接复用，大幅减少聚合次数。
### 2 五阶段标准训练流程
模型聚合→本地SGD训练→邻居指标采集→综合打分选最优邻居→漫游模型定向转发，仅向筛选后的设备传输模型。
### 3 三维自适应邻居打分机制
- 数据维度：计算漫游累积分布与邻居数据距离，均衡全局样本；
- 资源维度：结合训练耗时、链路带宽，避开弱终端；
- 遗忘维度：优先久未访问设备，缓解历史知识遗忘；
加权综合得分选取下一跳邻居。
### 4 分布式知识向量维护
漫游模型携带全局类别分布向量，每轮本地训练后更新，用于量化邻居数据异构程度，辅助打分。
### 5 轻量化部署适配
兼容ResNet/VGG/MobileNet等轻量化视觉网络，适配Jetson系列异构AIoT终端，无需中心节点。

## 实验分析
1. 实验环境：仿真20台强弱异构AIoT节点；真实测试床含Jetson Xavier/Nano；数据集CIFAR-10/100、Tiny-ImageNet。
2. 精度表现：IID、α=1.0、α=0.5三类非IID场景下，MMDFL在所有网络数据集上测试准确率高于全部基线算法。
3. 通信与耗时：达到同等精度时，通信量相比基线最高缩减96%，训练时长缩短53%；设备规模10~80均可稳定扩展。
4. 消融实验：三维打分缺一均出现精度下滑，漫游模型数量M=4为精度与开销平衡点。
5. 实测集群：嵌入式异构拓扑下收敛速度、稳定精度显著优于DFedSAM、DFedPGP等主流方法。

## 研究启发
1. 传统全邻居FedAvg聚合是DFL通信与异构性能瓶颈，漫游多模型定向流转可解耦设备绑定关系。
2. 邻居选择不能单一考量数据分布，需融合设备算力、网络、访问时序，同时解决掉队与遗忘两大痛点。
3. 携带全局数据分布向量可低成本量化非IID差异，无需额外全局统计，适配无中心去中心化场景。
4. 少量漫游模型即可完成全拓扑知识扩散，相比全网同步传输大幅降低AIoT终端带宽压力。
5. 去中心化联邦优化需兼顾算法理论与嵌入式硬件约束，轻量化模型+定向通信才适合大规模物联网落地。
