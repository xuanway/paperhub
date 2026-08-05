---
title: "Enabling On-Tiny-Device Model Personalization via Gradient Condensing and Alternant Partial Update"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Enabling On-Tiny-Device Model Personalization via Gradient Condensing and Alternant Partial Update

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132925">https://ieeexplore.ieee.org/document/11132925</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 设备端模型个性化，梯度凝缩，交替部分更新，资源受限环境</p>
</div>

---

## 研究概要
本文提出TinyMP端侧模型个性化协同优化框架，包含梯度压缩GC与交替局部更新APU两大核心模块。GC压缩梯度图降低反向传播算力与内存开销且误差有界；APU在线动态筛选关键卷积核交替更新。在OpenMV-H7微型MCU实测，最高提速2.4倍，内存节省80.8%，下游任务精度最高提升30.3%。

## 背景和动机
1. 微型IoT设备仅MB级存储算力，传统云端微调存在数据上传隐私、传输能耗问题，本地训练反向传播内存算力开销巨大。
2. 现有局部更新方案分离线搜索、静态固定微调、在线梯度乘积筛选三类：离线搜索耗资源，静态策略易过拟合，在线方法缓存梯度占用大量SRAM。
3. 梯度量化、池化等反向优化会引入不可控精度损失，无法平衡训练开销与模型准确率。
4. 现有方案无法同时解决梯度计算高负载与参数动态筛选双重痛点，难以在极小MCU落地完整本地个性化微调。

## 相关工作
1. 静态局部微调（Full-FT、LinearOnly、TinyTL）：固定更新全层/线性层/偏置，无法适配动态数据分布，易产生过拟合。
2. 离线稀疏更新SU：云端进化搜索确定待更新通道，部署后不可动态调整，不支持实时自适应。
3. 在线参数筛选TinyTrain：通过梯度-激活乘积评估核重要度，需缓存全部特征，内存占用极高。
4. 梯度压缩优化GF-FT：采用池化压缩梯度，无误差边界约束，会造成明显精度衰减。
5. 轻量化推理框架TF Micro：仅支持前向推理，未提供端训练反向传播优化方案。

## 本文解决方案
### 1 梯度压缩GC机制
前向传播压缩特征图至卷积核尺寸，反向将梯度图压缩为均值标量；用区域均值乘积近似卷积梯度推导，严格给出梯度误差上界，大幅削减中间特征、梯度缓存内存与卷积FLOPs。
### 2 交替局部更新APU
每轮推理阶段利用少量样本计算马氏相似度衡量卷积核时序变化，定义带动量的核重要度分数；仅选取高分核参与反向更新，低分核跳过梯度计算，无需存储完整梯度图。
### 3 端侧协同训练流水线
先APU在线筛选本轮待更新卷积核，再基于GC完成压缩式前向与反向传播；交替更新不同子集参数，降低单轮训练负载，适配1MB SRAM微型MCU。
### 4 误差可控梯度近似推导
数学证明特征、梯度压缩带来均方误差存在理论上界，小尺寸嵌入式网络天然压缩误差更小，保障微调后模型精度不会显著下降。

## 实验分析
1. 实验平台：OpenMV-H7（Cortex-M7，1MB SRAM/2MB Flash），基准模型MobileNetV2、MCUNet；测试多域小样本下游数据集。
2. 精度表现：相比GF-FT、Full-FT最高提升30.3%，多数跨域任务平均精度优于SU、TinyTrain。
3. 资源开销：峰值内存相较SOTA降低80.8%，训练时延最高2.4倍加速，完美适配极小内存设备。
4. 消融实验：APU单独使用可缓解过拟合，GC独立使用开销显著下降；二者结合兼顾精度、内存、速度。
5. 横向对比：现有方法普遍存在精度/内存/时延三角权衡，TinyMP可三者同时优化。

## 研究启发
1. 微型设备端训练不能单一优化参数更新或梯度计算，算法+系统协同才能突破内存算力双重瓶颈。
2. 梯度压缩可通过区域均值近似卷积运算，只要给出误差理论边界，就能在几乎无损精度前提下削减海量中间缓存。
3. 在线参数重要度评估可放在推理阶段完成，无需额外梯度存储，大幅降低MCU内存占用。
4. 交替式局部更新可避免静态微调策略的过拟合问题，适配动态用户个性化数据分布。
5. 面向MCU的端侧微调方案需放弃全精度梯度完整计算，轻量化梯度近似是落地关键技术路线。
