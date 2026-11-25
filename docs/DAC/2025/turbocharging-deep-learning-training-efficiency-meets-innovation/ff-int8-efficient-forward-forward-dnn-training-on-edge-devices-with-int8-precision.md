---
title: "FF-INT8: Efficient Forward-Forward DNN Training on Edge Devices with INT8 Precision"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# FF-INT8: Efficient Forward-Forward DNN Training on Edge Devices with INT8 Precision

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2506.22771">https://arxiv.org/abs/2506.22771</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经网络量化，低功耗，低精度训练，资源受限设备 </p>
</div>

---

## 研究概要
本文提出FF-INT8，首个基于前向-前向(FF)算法的INT8边缘低精度训练方案。利用FF分层训练规避反向传播量化误差累积，设计前瞻Look-Ahead损失机制弥补原生FF收敛差缺陷。Jetson Orin Nano实测，对比主流INT8训练，训练提速4.6%、能耗降8.3%、内存减少27%，精度仅小幅损失。

## 背景和动机
1. 传统反向传播BP训练需缓存完整计算图，内存、算力、能耗开销巨大，难以部署低功耗边缘设备。
2. BP直接INT8训练时梯度逐层反向传递，量化误差持续累积，深层网络精度暴跌，现有BP式INT8训练需额外梯度矫正开销。
3. FF算法以双前向替代反向传播，无需存储中间激活，但原生FF仅单分层优化，无法利用后层信息，收敛慢、最终精度偏低，残差网络适配差。
4. 现有低精度训练多为FP16/FP8浮点量化，硬件适配门槛高；INT8整数算力在边缘NPU/GPU普及，但缺少适配FF的完整训练流程。
5. 缺少兼顾INT8低比特与FF分层优势的一体化训练框架，无法同时解决内存、速度、精度三大痛点。

## 相关工作
1. 推理量化：PTQ/QAT仅面向模型部署，不支持训练阶段低比特优化，无法降低训练开销。
2. 浮点低精度训练：MPTraining、Minifloat采用16/8浮点，依赖专用硬件，通用性弱。
3 BP系INT8训练：UI8、DAI8、GDAI8基于反向传播，需梯度裁剪/通道自适应矫正，误差累积问题无法根除，额外计算多。
4 FF基础算法：仅分层好坏函数优化，无跨层信息交互，深层、残差网络效果差，未结合INT8量化。

## 本文解决方案
### 1 FF分层INT8量化训练流水线
采用对称均匀量化SUQ+随机舍入，每层独立INT8前向计算；仅更新本层权重，无需反向梯度回传输入，彻底阻断误差逐层累积；用正负样本构造好坏损失函数做分层优化。
### 2 Look-Ahead前瞻损失机制
改进单层损失，融合后续所有层好坏损失，引入动态平衡系数λ；训练周期逐步提升λ，前期专注单层区分、后期跨层协同优化，适配残差块结构。
### 3 单轮全前向多分层更新策略
一轮完整前向传播计算全部层好坏值，统一计算各层梯度并行更新，不增加反向通路，仅小幅提升内存，大幅缩短收敛轮次。
### 4 INT8专用计算数据流
输入、权重、激活统一INT8存储，MAC采用INT8乘+INT32累加；仅权重梯度量化，舍弃输入梯度计算，削减大量浮点运算。
### 5 边缘适配完整训练框架
无需保存反向计算图，天然削减内存占用；兼容MLP、MobileNet、ResNet等主流CNN，适配带INT8加速的Jetson边缘硬件。

## 实验分析
1. 实验环境：Jetson Orin Nano边缘板，测试MLP/MobileNetV2/EfficientNet-B0/ResNet18，数据集MNIST/CIFAR10。
2 量化误差验证：BP-INT8随层数增加精度断崖下跌；FF分层训练无反向误差累积，多层网络仍保持高准确率。
3 Look-Ahead消融：无前瞻机制ResNet仅60%精度，加入后逼近FP32基线，收敛轮次减少近半。
4 计算量对比：FF-INT单批次MAC运算仅为BP类方案2.6%，INT8硬件加速收益显著。
5 整机指标：对比SOTA GDAI8，平均精度提升0.2%，训练时间-4.6%、能耗-8.3%、内存占用-27%，与FP32精度差距仅0.4%。

## 研究启发
1. 反向传播是INT8训练误差累积根源，FF分层独立优化从数据流层面根除该缺陷，是边缘低精度训练优选范式。
2. 原生FF单分层优化存在跨层信息隔离，前瞻损失可低成本融合深层反馈，完美适配残差现代网络。
3 INT8整数量化更适配边缘硬件，但不能直接套用BP训练逻辑，需搭配无反向的新型训练算法。
4 训练效率不能只看单轮算力，收敛轮次与单轮运算量需综合权衡，FF虽轮次更多但单轮计算量极低，整体更高效。
5 面向端侧在线持续学习场景，FF-INT8无需大缓存，在内存受限嵌入式设备具备极高落地价值。
