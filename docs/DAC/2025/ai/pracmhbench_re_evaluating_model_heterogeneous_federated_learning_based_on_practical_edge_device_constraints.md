---
title: "PracMHBench: Re-evaluating Model-Heterogeneous Federated Learning Based on Practical Edge Device Constraints"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# PracMHBench: Re-evaluating Model-Heterogeneous Federated Learning Based on Practical Edge Device Constraints

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2509.08750">https://arxiv.org/abs/2509.08750</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 联邦学习，平台，模型异质性 </p>
</div>

---

## 研究概要
本文提出首个面向真实边缘约束的模型异构联邦学习评测基准PracMHBench，划分宽度/深度/拓扑三层异构，覆盖CV/NLP/HAR多任务，构建算力/通信/内存三类边缘受限场景。以全局精度、收敛时长等多指标系统评测现有MHFL算法，给出不同硬件约束下最优方案选择指南。

## 背景和动机
1. 现有模型异构联邦学习(MHFL)算法仅按模型比例缩放做实验，未考虑Jetson、树莓派等真实边缘设备算力、内存、带宽差异，同等缩放比例资源开销差距极大，对比不公平。
2. 缺少统一基准平台，无法在多任务、多硬件约束下横向对比宽度、深度、拓扑三类异构算法的综合性能。
3. 边缘设备普遍存在单一资源瓶颈（算力/带宽/内存其一受限），现有研究未分场景量化各算法适配性，工程落地缺少参考依据。
4. 现有FL基准聚焦数据异构、硬件同构，未针对模型异构、真实边缘资源约束做系统化测试与结论归纳。
5. 不同MHFL算法内存、算力开销差异显著，内存敏感场景下部分主流方法性能大幅衰退，缺乏定量分析。

## 相关工作
1. 传统联邦学习基准(LEAF/FedEval)：侧重数据非独立同分布评测，不支持模型异构与边缘硬件约束仿真。
2. 硬件异构FL平台：仅评估设备算力差异，未区分宽度/深度/拓扑三类模型异构范式。
3. MHFL算法（SHeteroFL/DepthFL/FedProto）：各自在自定义简易设置下验证，缺少统一公平对比平台。
4. 边缘联邦优化工作：仅做单一算法落地，未系统性横向评测各类异构策略优劣。
5. 稀疏/剪枝联邦方案：不区分模型异构层级，无法为受限设备提供选型指导。

## 本文解决方案
### 1 三层模型异构分类体系
将MHFL划分为宽度异构（通道缩放）、深度异构（层数裁剪）、拓扑异构（完全不同网络），收录Fjord、DepthFL、FedProto等代表性算法归入对应层级。
### 2 多领域多任务评测数据集
覆盖CV(CIFAR10/100)、NLP(AG-News/StackOverflow)、HAR(UCI-HAR/HAR-BOX)，同时支持IID与真实用户划分非IID数据分布。
### 3 三类真实边缘约束仿真场景
基于Jetson Orin/Nano、树莓派实测数据构建：算力受限（统一单轮训练时长）、通信受限（统一传输耗时）、内存受限（匹配设备最大可训练模型）。
### 4 四维综合评测指标
全局精度、Time-to-Acc（达标耗时）、设备精度方差（稳定性）、相较同质基线精度提升（有效性），全面衡量算法综合收益。
### 5 标准化可复现评测流水线
统一客户端采样、训练轮次、硬件仿真逻辑，支持单约束/多约束混合、不同客户端规模、非IID强度消融实验。

## 实验分析
1. 实验环境：Jetson Orin/Nano、树莓派实测模型算力/内存参数，客户端规模30~500，每组实验重复3次取均值，训练1000轮至收敛。
2. 算力/通信受限场景：深度异构算法DepthFL、SHeteroFL全局精度与收敛速度最优，各数据集表现稳定；宽度类、拓扑蒸馏类性能垫底。
3. 内存受限场景：DepthFL内存开销大，性能大幅下滑，FeDepth轻量化方案表现最优；各算法设备精度稳定性出现反转。
4. 多约束混合场景：SHeteroFL分层缩放算力/内存/通信开销均衡，复合瓶颈下综合表现最佳。
5. 消融结论：非IID数据不会改变算法优劣排序；宽度异构客户端扩容收敛衰减最小，扩展性最优。

## 研究启发
1. 仅依靠模型参数比例缩放做MHFL对比存在严重偏差，必须结合真实边缘算力、内存实测数据保证实验公平性。
2. 算力、带宽瓶颈优先选用深度异构方案；内存紧缺场景需避开DepthFL等高内存算法，选用轻量化深度变体。
3. 拓扑异构知识蒸馏虽适配多样网络，但算力、通信开销大，仅适合高性能边缘集群，低端设备不推荐。
4. 不同资源约束下最优算法不统一，不存在万能MHFL方案，需根据设备核心瓶颈选型。
5. 宽度异构策略客户端扩容鲁棒性更强，大规模边缘集群部署优先考虑宽度类异构算法。
