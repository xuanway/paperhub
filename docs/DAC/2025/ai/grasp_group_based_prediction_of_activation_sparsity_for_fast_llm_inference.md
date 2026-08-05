---
title: "Grasp: Group-based Prediction of Activation Sparsity for Fast LLM Inference"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# Grasp: Group-based Prediction of Activation Sparsity for Fast LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI1: AI/ML Algorithms</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132899</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 大语言模型，快速推理，激活稀疏性，稀疏性预测 </p>
</div>

---

## 研究概要
本文提出Grasp无训练式激活稀疏预测方法，面向ReLU改造型LLM，在符号比特基础上引入幅值分组与离群点校正。通过正态分布分块加权近似内积，平衡预测精确率与召回率。在Jetson Orin部署ProSparse-Llama7B/13B，相比SparseInfer跳过效率提升11倍，稠密推理加速至1.85倍，精度损失小于1%。

## 背景和动机
1. LLM推理中MLP占60%-70%算力，ReLU改造模型可生成大量零激活，提前预测稀疏能跳过无效计算与访存。
2. 训练类稀疏预测（PowerInfer/DejaVu）额外网络开销大，且需重新微调模型，部署成本高。
3. SparseInfer仅依靠符号异或统计正负数量，完全忽略幅值，存在大量假正/假负预测，只能通过保守系数折中精度与速度。
4. 深层隐藏向量存在大幅值离群点，对内积结果影响极大，现有方法未单独建模，预测误差持续放大。
5. 符号统计无法区分大小乘积贡献，无法同步提升精确率与召回率，难以挖掘稀疏加速上限。

## 相关工作
1. 训练式稀疏预测（DejaVu、PowerInfer）：增加专用预测网络，推理延迟高，模型修改后需重训。
2. SparseInfer无训练符号预测：仅比对符号比特，计算极简，但幅值信息丢失，精确召回存在固有权衡。
3. ProSparse系列模型：将SiLU/GELU替换为ReLU制造激活稀疏，为稀疏加速提供模型基础，但缺少配套预测算法。
4. LLM权重稀疏优化：仅压缩权重，无法利用推理时动态激活稀疏，加速上限更低。
5. 硬件稀疏加速器：依赖软件给出稀疏掩码，缺少轻量级前端预测配套算法。

## 本文解决方案
### 1 正态分布幅值三分组机制
利用均值、标准差快速计算四分位数，将输入与权重元素划分为大/小两类，乘积分为G1(双大)、G2(一大一小)、G3(双小)三组，每组赋予代表幅值权重。
### 2 离群点单独建模G0组
Z-score>6元素划为独立离群组，单独分配高权重，抵消大幅值样本带来的预测偏差，降低深层模型假负样本数量。
### 3 两种分组权重标定方案
方案一：组内平均绝对值比值缩放；方案二：基于少量校准集逻辑回归求解分组权重，通过约登指数选定最优稀疏阈值，灵活调优精度速度权衡。
### 4 离线权重打包+在线轻量计算
离线预存权重符号/幅值1bit压缩编码；在线仅计算输入均值方差，通过位运算快速完成分组，预测总开销仅占MLP 2.4%。
### 5 分层动态阈值调优
逻辑回归阈值可分层缩放，激进阈值提升推理速度，保守阈值保证下游任务准确率，适配不同场景需求。

## 实验分析
1. 实验环境：Jetson Orin 64GB，llama.cpp推理框架，测试ProSparse-Llama2 7B/13B，GSM8K、BBH评测集。
2. 预测效果：Grasp(MC+OC)大幅减少四象限假负样本，相比SparseInfer同时提升精确率、召回率。
3. 任务精度：Grasp平均精度损失控制在1%以内，优于α=1.0版本SparseInfer，接近保守α=1.03基线。
4. 推理加速：对比稠密推理最高1.85倍提速，比最优SparseInfer跳过效率提升11%；预测开销仅5.5ms。
5. 消融验证：幅值分组、离群校正两个模块缺一不可，逻辑回归标定相较均值比值拥有更灵活精度速度调节能力。

## 研究启发
1. 仅依靠符号比特的无训练稀疏预测存在本质缺陷，引入幅值分组可打破精确率与召回率的强权衡。
2. LLM隐藏层大幅离群点是预测误差主要来源，单独分组建模能显著改善深层网络稀疏识别效果。
3. 基于正态分布统计量无需排序即可快速划分幅值区间，极低开销实现幅值加权近似内积。
4. 少量无标注推理样本即可完成分组权重校准，无需模型微调，工程落地门槛极低。
5. 稀疏预测阈值分层可调，可根据终端算力、任务精度需求动态切换激进/保守稀疏策略。
