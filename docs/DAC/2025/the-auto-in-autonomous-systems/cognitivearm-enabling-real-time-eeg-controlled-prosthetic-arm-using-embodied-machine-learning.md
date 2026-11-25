---
title: "CognitiveArm: Enabling Real-Time EEG-Controlled Prosthetic Arm Using Embodied Machine Learning"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# CognitiveArm: Enabling Real-Time EEG-Controlled Prosthetic Arm Using Embodied Machine Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS1: Autonomous Systems (Automotive, Robotics, Drones)</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2508.07731">https://arxiv.org/abs/2508.07731</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 脑电控制，实时处理，嵌入式机器学习，模型优化</p>
</div>

---

## 研究概要
本文提出CognitiveArm嵌入式脑控假肢系统，基于实境机器学习实现实时EEG运动想象分类。采用进化搜索获取帕累托最优模型，搭配剪枝/量化压缩，集成Whisper语音指令切换模式。搭载3自由度3D打印假肢，边缘端推理精度最高90.1%，单帧推理低至0.071s，低成本适配肢体残障人群。

## 背景和动机
1. sEMG假肢依赖残余肌肉，ALS、脊髓损伤患者无可用肌电信号，无法正常控制肢体。
2. 现有EEG脑控方案依赖PC/云端运算，传输延迟高、隐私泄露风险大，难以实时交互。
3. 深度学习EEG模型参数量大，边缘嵌入式设备算力/内存受限，精度与延迟难以兼顾。
4. 现有系统缺少完整软硬件一体化原型，仅停留在信号分类仿真，无法落地日常抓取、握手等动作。
5. 单一脑控模式操作单一，缺少语音辅助切换自由度，多任务操控灵活性不足。

## 相关工作
1. 侵入式脑机（Neuralink）：精度高但手术成本、创伤风险极高，普及性差。
2. 传统非侵入EEG假肢：模型未做边缘优化，推理时延高，分类精度仅75%-87.5%。
3. sEMG商用假肢（BeBionic、LUKE Arm）：售价数万美金，依赖肌肉信号，适用人群狭窄。
4. 通用EEG深度学习模型（CNN/LSTM/Transformer）：无面向假肢的轻量化与硬件适配流程。
5. 混合EEG-sEMG设备：成本中等，但仍受肌肉萎缩病症限制，无法全覆盖残障群体。

## 本文解决方案
### 1 完整EEG数据采集标注流水线
基于OpenBCI 16通道头套+BrainFlow采集125Hz脑电，采用巴特沃斯、50Hz陷波滤波去除噪声；设计左右手/静息三类想象任务，滑动窗口分割构建平衡标注数据集，留一被试交叉验证。
### 2 进化搜索帕累托模型寻优
以精度最大化、参数量最小为双目标进化算法，遍历CNN/LSTM/Transformer/随机森林架构、窗口、学习率等超参，筛选硬件适配最优单模型与集成模型。
### 3 模型轻量化部署方案
采用全局剪枝、8bit量化两类压缩手段；70%剪枝平衡精度与时延，量化虽提速但精度大幅下降，不用于安全控制场景。
### 4 语音多模式协同控制
集成Whisper-small轻量ASR，独立线程并行运行，语音指令切换肘、手指3自由度，实现抓取、握手等复杂日常动作。
### 5 端到端嵌入式硬件原型
Jetson Orin Nano做边缘推理，串口连接Arduino驱动3D打印三自由度假肢伺服，整套硬件成本低于500美元，离线本地运算无云端依赖。

## 实验分析
1. 测试平台：RTX A6000训练，Jetson Orin Nano边缘部署；5名受试者，三类运动想象任务。
2. 模型性能：CNN+Transformer集成最优，原始精度91%；70%剪枝后精度90.1%、推理0.071s；8bit量化时延0.036s但精度暴跌。
3. 进化寻优效果：自动筛选最优窗口、网络层数与神经元，相比人工调参精度提升12%、参数量降低62%。
4. 系统整机：离线本地推理，无需联网；20组实测会话中19次可稳定完成指定动作，成本远低于商用肌电假肢。
5. ASR对比：Whisper-small在时延与显存占用间达到帕累托最优，适配边缘并行运算。

## 研究启发
1. 运动想象EEG脑控无需云端，轻量化深度学习+边缘AI芯片可实现低延迟离线实时控制。
2. 进化多目标搜索是面向嵌入式的模型调优高效手段，人工穷举难以找到精度-时延平衡点。
3. 剪枝比量化更适合假肢这类安全关键BCI设备，量化精度损失会带来操控失效风险。
4. EEG纯脑控可覆盖肌电设备无法适配的神经损伤患者，低成本3D打印硬件具备普及潜力。
5. 脑电+语音多模态融合可大幅提升假肢操作自由度，单一运动想象指令难以完成复杂日常任务。