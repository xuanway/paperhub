---
title: "SSpMV: A Sparsity-aware SpMV Framework Empowered by Multimodal Machine Learning"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# SSpMV: A Sparsity-aware SpMV Framework Empowered by Multimodal Machine Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132896">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132896</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/lsl036/SSpMV">https://github.com/lsl036/SSpMV</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 稀疏矩阵，稀疏矩阵向量乘法，机器学习</p>
</div>


---

## 研究概要
本文提出面向多核平台的稀疏感知SpMV自适应框架SSpMV，设计多模态神经网络MM-Adapter。提取人工细粒度特征与局部/分布/向量化三类稀疏模态融合预测最优存储格式与超参，覆盖21种SpMV实现。6000+真实矩阵测试，预测精度81.05%，相较MKL平均加速3.08倍，适配x86/鲲鹏多架构。

## 背景和动机
1. SpMV是科学计算、EDA、AI核心内核，但稀疏矩阵非规则访存导致CPU向量、缓存利用率低下，不同稀疏模式适配最优存储格式差异巨大，无统一通用方案。
2. COO/CSR/BCSR/CSR5等十余种存储格式搭配调度、分块超参，人工调参成本极高，单一格式无法适配全部矩阵。
3. 现有机器学习调优仅依靠均值、标准差少量人工特征，无法捕捉局部访存、负载均衡、SIMD向量化底层硬件关联特征，预测精度低。
4. 现有数据集以合成矩阵为主，电路、流体仿真等工业真实稀疏样本覆盖不足，模型泛化能力差。
5. 主流MKL、ArmPL等稀疏库采用固定默认实现，不随稀疏结构自适应切换，大量场景性能存在巨大损耗。

## 相关工作
1. 专用稀疏存储格式：CSR5、SELL-c-σ、BCSR等，仅针对特定稀疏形态优化，无自适应选型能力。
2. 传统SpMV自动调优SMAT、Wise：基于决策树、MLP，仅少量全局统计特征，无法刻画细粒度稀疏分布。
3. CNN类预测模型SpNet、MatNet：仅单模态矩阵灰度图输入，缺少访存、向量化硬件关联表征，泛化弱。
4. AlphaSparse：GPU端自动生成稀疏内核，未适配多核CPU多调度、分块超参组合场景。
5. 商用稀疏库Intel MKL、ArmPL、Ginkgo：固定执行策略，不做稀疏模式感知自适应切换。

## 本文解决方案
### 1 全栈SSpMV自适应框架
集成21种完整SpMV实现（多格式+OpenMP调度+分块超参），离线训练MM-Adapter，线上提取特征后推理最优内核，包含推理开销仍保持高性能。
### 2 多层级人工稀疏特征体系
按瓦片/行块/列块多粒度划分矩阵，计算零元占比、均值、方差、基尼系数、P均衡系数等40维细粒度特征，刻画负载均衡与缓存复用特性。
### 3 三类稀疏多模态表征
- 局部模态M1：刻画输入向量访存局部性；
- 分布模态M2：表征矩阵负载分布均衡性；
- 向量化模态M3：适配SIMD并行计算特征；
每种模态附加4通道统计信息避免压缩信息丢失。
### 4 MM-Adapter多模态融合网络
一维CNN提取局部/向量化模态特征，二维CNN提取分布模态，人工特征经FFNN编码，全部嵌入拼接后通过MLP完成多分类，输出各SpMV实现性能概率。
### 5 工业级大规模数据集构建
融合SuiteSparse真实矩阵，搭配FreeFEM、OpenFoam生成电路、流体仿真稀疏样本，总计6052份用于模型训练验证。

## 实验分析
1. 测试平台：Intel Xeon x86、鲲鹏AArch64多核CPU，A100训练MM-Adapter；基线SMAT/DIESEL/SpNet/MatNet、MKL/ArmPL/Ginkgo/CSR5。
2. 模型精度：MM-Adapter预测准确率81.05%，远超所有对比模型；消融实验证明分布模态、人工特征是核心贡献模块。
3. 性能加速：对比Intel MKL平均3.08倍，最高71.7倍，理论最优仅3.19倍，性能损失极小；鲲鹏平台相对ArmPL平均提速2.68倍。
4. 跨格式对比：在极度稀疏、对角、电路不规则矩阵上均稳定优于CSR5、SELL等专用格式。
5. 推理开销：单矩阵特征提取+模型推理平均仅3.19ms，迭代求解场景可忽略开销。

## 研究启发
1. SpMV性能瓶颈不只是存储格式，OpenMP调度、SIMD分块等超参同等关键，自适应系统需覆盖完整参数组合空间。
2. 仅全局稀疏统计特征不足以表征硬件行为，多粒度分块细特征+多模态图像表征可完整捕捉缓存、向量并行约束。
3. 多模态不能照搬视觉多模态思路，需针对性设计访存/负载/向量化三类硬件感知表征。
4. 工业电路、流体仿真矩阵稀疏模式极端不规则，是现有调优框架短板，扩充真实样本显著提升泛化性。
5. 自适应SpMV框架需兼顾离线训练成本与线上推理轻量性，轻量CNN+MLP结构可平衡预测精度与运行开销。