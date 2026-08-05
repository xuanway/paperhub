---
title: "MAS-ISP: A Proxy-Free Online Hyperparameter Optimization Framework for ISP Hardware System"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MAS-ISP: A Proxy-Free Online Hyperparameter Optimization Framework for ISP Hardware System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS1: Autonomous Systems (Automotive, Robotics, Drones)</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132763">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132763</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>超参数优化，图像信号处理器，无代理，硬件，多智能体 </p>
</div>

---

## 研究概要
本文提出无代理在线ISP超参优化硬件框架MAS-ISP，基于主从多智能体深度强化学习，无需可微代理模型，解决帧间抖动问题。设计条状卷积核与步感知双缓冲硬件降低CNN开销，FPGA/ASIC分别实现1080P@75/240FPS，图像质量与检测mAP优于代理类SOTA，硬件存储资源大幅削减。

## 背景和动机
1. 自动驾驶ISP需实时动态调参适配光照场景，离线优化方案固定参数，动态画面画质衰减明显，存在安全隐患。
2. 现有在线学习式优化依赖可微代理网络，ISP非线性特性造成代理拟合误差，调参精度不足。
3. 单智能体逐帧调参忽视时序关联，参数频繁震荡，帧间画面不一致，影响机器检测精度。
4. RAW光栅数据流带来巨大CNN中间缓存开销，现有优化硬件BRAM、DSP资源占用高，难以嵌入式部署。
5. 传统无代理进化/DRL方法迭代周期长，无法满足车载实时帧率约束。

## 相关工作
1. 离线ISP优化：CMA-ES等进化算法、离线DRL，仅预训练固定参数，动态场景自适应差，实时性不足。
2. 代理在线Auto-ISP：构建UNet/HFP可微代理拟合ISP，存在模型偏差，训练显存与硬件存储开销巨大。
3. 传统DRL-ISP：单智能体架构，无并行多参数协同机制，调参收敛慢、帧间一致性差。
4. CNN标准卷积硬件：全窗口缓存占用大量片上BRAM，处理光栅RAW数据冗余计算多，吞吐受限。
5. ISP专用流水线：仅处理图像信号，缺少配套实时调参神经网络加速单元。

## 本文解决方案
### 1 无代理主从多智能体DRL优化框架
离线阶段硬件在环训练，直接以ISP输出RGB为奖励，舍弃代理模型；主CNN提取全局隐特征，多个轻量从智能体并行独立优化单路超参，多步动作避免参数震荡；采用帧间增量奖励平滑时序反馈。
### 2 软硬件协同MAS-ISP整体架构
调参智能体加速器与ISP流水线硬件集成，配置转换器映射Q值为参数调整量；图像中心4倍下采样削减CNN计算量，兼顾精度与实时性。
### 3 条状卷积Strip Convolution Kernel
针对步长2的3×3卷积区分单行/双行处理，单输入行完成运算，乘法器数量减少33%，消除冗余窗口计算。
### 4 步感知双缓冲SADB Memory
单行流水线存储结构，复用中间卷积结果，大幅降低BRAM缓存占用与内存访问次数，提升流水线吞吐。
### 5 离线训练+在线推理双流程
离线利用ISP C模型迭代训练多智能体；在线固化网络权重，与ISP同步硬件运行，端到端低延迟调参。

## 实验分析
1. 测试数据集：Kodak静态、OnePlus暗光、BDD100K高速动态驾驶数据集，指标采用PSNR/SSIM/LPIPS/mAP。
2. 画质与检测：静态、动态场景PSNR、mAP全面超越代理Auto-ISP与离线优化方法，动态帧无曝光抖动，目标检测框稳定。
3. 训练开销：模型参量0.0096M，GPU显存仅236M，远低于带代理基线数百兆内存占用。
4. 硬件资源：FPGA BRAM减少57.6%，28nm ASIC总面积1.1296mm²，实现1080P@240FPS；量化画质损失低于0.08dB。
5. 时序性能：8秒长时序曲线收敛更快，静态/动态场景均可稳定维持高画质指标，离线算法持续缓慢爬升。

## 研究启发
1. ISP实时调参可完全抛弃可微代理模型，无代理DRL结合硬件在环能消除拟合带来的精度损失。
2. 主从多智能体并行调参可兼顾多超参协同优化与帧间时序一致性，解决画面震荡痛点。
3. 针对光栅图像步长卷积定制专用算子与单行缓冲，是降低视觉CNN硬件存储开销的核心路径。
4. 增量式时序奖励能平滑相邻帧参数调整幅度，对自动驾驶高速动态场景提升检测稳定性至关重要。
5. 调参神经网络与ISP流水线硬件深度集成，避免跨模块数据搬运，是嵌入式端实现实时自适应ISP的关键。
