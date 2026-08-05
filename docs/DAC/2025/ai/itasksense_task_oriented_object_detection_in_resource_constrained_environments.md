---
title: "iTaskSense: Task-Oriented Object Detection in Resource-Constrained Environments"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# iTaskSense: Task-Oriented Object Detection in Resource-Constrained Environments

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133060">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133060</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 任务导向目标检测，大语言模型，知识蒸馏与量化，硬件加速器 </p>
</div>


---

## 研究概要
本文提出iTaskSense面向资源受限边缘的任务导向目标检测框架，借助LLM生成任务属性知识图实现少样本泛化，提供蒸馏高精度、量化轻量化双模型方案；设计统一ASIC脉动阵列硬件，兼容CNN分割与ViT推理。实验相较GPU提速3.5倍、能耗降低40%，蒸馏模型专项任务精度较量化版提升15%。

## 背景和动机
1. 传统通用目标检测依赖海量标注数据集，难以根据任务语义筛选功能性物体，泛化能力差，无法适配少样本工业/车载场景。
2. 现有视觉语言模型参数量大，边缘设备内存、算力、功耗约束下推理延迟过高，缺少轻量化适配方案。
3. 主流AI加速器仅单独支持CNN或ViT，无法统一加速分割+视觉Transformer联合推理管线。
4. 量化压缩模型会造成任务相关检测精度大幅下滑，蒸馏与量化两种轻量化路线缺少协同设计。
5. 现有方案缺少任务语义推理能力，无法理解“用于开瓶”“搅拌”等抽象功能需求，只能做类别识别。

## 相关工作
1. 任务导向检测TOOD/TOIST：仅优化分类定位对齐，无LLM语义知识推理，泛化依赖大量标注。
2. 轻量VLMs（MiniVLM/TinyCLIP）仅做模型裁剪，未结合任务属性知识图，专项任务精度损失严重。
3. 专用AI加速器：大多单一适配CNN或稀疏Transformer，无法同时支持卷积分割与注意力计算。
4. 智能传感近端处理：仅做帧过滤，未结合任务驱动检测实现精准ROI提取，带宽节省有限。
5. 知识蒸馏CLIP优化：只对齐全局图文特征，未针对任务功能性affinity做针对性蒸馏损失。

## 本文解决方案
### 1 LLM驱动任务知识图推理管线
输入自然语言任务指令，LLM提取物体功能属性构建知识图；视觉模型提取物体特征，通过亲和矩阵匹配属性，排序筛选符合任务的目标，实现少样本跨物体泛化。
### 2 双轻量化模型分支
- 知识蒸馏分支：设计亲和模仿+权重继承蒸馏损失，以大CLIP为教师训练EfficientViT学生，专项任务精度最优；
- 量化分支：INT8量化压缩，牺牲少量精度换取多任务通用低开销推理。
### 3 统一脉动阵列ASIC硬件
128×128 8bit PE阵列，支持权重/输入/输出三种数据流；采用乒乓移位寄存器替代片上SRAM，降低面积与关键路径延迟，同时加速CNN分割与ViT注意力计算。
### 4 配套三层编译栈
前端解析网络层，周期仿真优选每层最优数据流，汇编生成专用硬件指令，自动完成数据重排，降低主机预处理开销。
### 5 端侧智能感知优化
基于任务筛选ROI区域，过滤无关像素，减少传输与计算量，适配低功耗传感器实时推理场景。

## 实验分析
1. 实验环境：RTX4090软件评测，28nm工艺ASIC综合，对比GGNN、TOIST等SOTA检测与各类ViT/CNN加速器。
2. 模型精度：蒸馏iTask*平均AP@0.5达45.01，较TOIST提升超10%；量化轻量版精度下降8%~12%，满足低负载场景。
3. 硬件指标：芯片面积6.14mm²，峰值30.31TOPS，计算密度4.93TOPS/mm²；相比GPU推理提速3.5倍，能耗下降40%。
4. 消融实验：LLM知识图是少样本泛化核心，蒸馏相比原生TinyCLIP任务精度最高提升37.7%。
5. 多模型适配：硬件兼容TinyCLIP、EfficientViT搭配ResNet/YOLO多种组合，CNN与ViT延迟可分层拆解评估。

## 研究启发
1. 任务导向检测不能只依赖视觉特征，引入LLM抽象功能知识图可大幅降低标注数据依赖，实现跨类别泛化。
2. 轻量化分两条路线：专项高精度用知识蒸馏，多任务通用采用量化，可按需平衡精度与算力开销。
3. 边缘VLM推理同时包含CNN分割与ViT注意力，统一多数据流脉动阵列硬件比单一类型加速器更实用。
4. 乒乓移位寄存器替代SRAM可显著缩短关键路径、提升工作频率，是低功耗ASIC优化关键手段。
5. 图文亲和度可作为蒸馏监督信号，相比普通嵌入损失更贴合任务功能性检测需求。
