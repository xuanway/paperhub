---
title: "Holistic Design towards Resource-Stringent Binary Vector Symbolic Architecture"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Holistic Design towards Resource-Stringent Binary Vector Symbolic Architecture


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES3: Emerging Models of Computation</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132468">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132468</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>二元向量符号架构，算法-硬件协同设计，资源受限设备，二元特征提取，软投票 </p>
</div>

---

## 研究概要
本文面向资源受限植入式BCI等边缘设备，提出UniVSA软硬件协同二值向量符号计算框架。设计差异化投影、二值卷积特征交互、软集成投票三大算法模块；配套流水线FPGA硬件架构。多类脑电/传感数据集验证，平均分类精度优于LDC等现有VSA，模型内存仅8.31KB，功耗低于0.5W。

## 背景和动机
1. 植入式脑机接口等微型设备功耗、存储极度受限，SVM、BNN等传统模型内存与功耗超标，难以部署。
2. 低维二值VSA(LDC)内存极小，但忽略特征间交互，部分脑电任务精度比SVM低5%，且低维下易欠拟合。
3. 现有VSA算法与硬件分离设计，仅单一优化算法或加速器，未做软硬件联合权衡，硬件开销难以控制。
4. 传统VSA对所有特征采用同维度向量编码，未区分特征重要性，造成维度资源浪费、精度上限低。

## 相关工作
1. 高维VSA(LeHDC)：向量维度上万，模型占用MB级存储，不适合微型边缘设备。
2. LDC低维VSA：仅实现特征独立编码，无特征交互建模，低维度分类精度不足。
3. LookHD VSA硬件：高维向量加速器，硬件资源、功耗开销巨大，无法用于BCI。
4. SVM/BNN/QNN轻量模型：分类精度尚可，但模型内存达MB、瓦级功耗，不符合植入设备约束。

## 本文解决方案
### 1 三层联合优化VSA算法
1）差异化值投影DVP：按特征重要性分高低维度VB编码，节省向量存储；
2）二值卷积BiConv：建模特征交互，弥补传统VSA独立编码缺陷；
3）软投票集成SV：多并行相似度层集成，缓解低维模型欠拟合。
### 2 分层流水线硬件架构
包含DVP、BiConv、编码、相似度四大模块，BiConv做并行加速，其余模块串行控资源；双缓冲卷积、部分并行向量运算，全局FSM调度流式输入。
### 3 软硬件联合寻优
建立硬件开销量化模型，以精度减硬件损耗为目标，进化搜索自动匹配各任务最优超参。

## 实验分析
1. 测试平台：Ultra96-V2 ZU3EG FPGA；数据集含EEG、癫痫脑电、语音、人体传感6类TinyML任务。
2. 算法指标：UniVSA平均精度94.45%，高于LDC(92.25%)、SVM(91.24%)，全局模型平均内存仅8.31KB。
3. 硬件性能：单样本推理延迟0.007~0.206ms，全部任务功耗<0.5W，无DSP资源占用。
4. 对比基线：相较SVM硬件资源仅0.1~0.5倍；相比LDC精度提升但硬件小幅增加，属于精度-资源可控折中。
5. 消融实验：BiConv对精度提升最显著，DVP优化存储，软投票缓解低维欠拟合，三者叠加收益最大。

## 研究启发
1. 低维VSA精度瓶颈源于无特征交互，引入轻量化二值卷积可极小内存代价显著提升分类效果。
2. 按特征重要性差异化编码是压缩向量维度、降低存储开销高效手段。
3. 软硬件必须协同寻优，不能单独优化算法或硬件，通过量化硬件损失可自动平衡精度与资源。
4. 硬件调度策略：计算瓶颈模块做并行，次要模块串行，整体流水线可在低功耗下保持高吞吐。
5. 二值向量符号计算天然适配超低功耗植入式边缘设备，是TinyML轻量化优选路线。
