---
title: "OutlierCIM: Outlier-Aware Digital CIM-Based LLM Accelerator with Hybrid-Strategy Quantization and Unified FP-INT Computation"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# OutlierCIM: Outlier-Aware Digital CIM-Based LLM Accelerator with Hybrid-Strategy Quantization and Unified FP-INT Computation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132578">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132578</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>大语言模型，存内计算，神经网络加速器，激活值离群点，量化 </p>
</div>

---

## 研究概要
本文提出OutlierCIM，面向LLM激活异常值实现算法-数字存内计算软硬件协同框架。设计异常值分块、混合量化、统一FP-INT运算三大优化，配套可重构双比特CIM宏。28nm流片验证，相较OliVe、Oltron最高提速3.91倍、能效提升4.54倍，支持4bit低精度推理。

## 背景和动机
1. LLM激活存在少量大幅异常值，直接低精度量化会严重恶化困惑度，现有异常感知加速方案与硬件适配差。
2. 传统分块方式含异常值的块位宽参差不齐，造成CIM利用率暴跌、内存访问不规则、等待周期冗余。
3. 非对称量化零偏移对齐引入大量循环开销，存储密度减半，通用CIM无法兼容混合位宽负载。
4. 非线性层输出需浮点，FP-INT混合运算要频繁格式转换，现有CIM架构转换能耗与延迟极高。

## 相关工作
1. 纯量化算法（SmoothQuant/OmniQuant）：仅做数值变换，无硬件协同，难以在CIM上落地，推理开销大。
2. OliVe/Olten数字加速器：异常处理依赖稀疏编码或通道置换，PE利用率低，不支持存内计算。
3. ReDCIM通用数字CIM：仅统一常规FP/INT，未针对LLM异常值优化，低精度推理能效差。
4. 传统双比特CIM：输入符号位带来空转周期，硬件利用率损失25%，无混合量化适配策略。

## 本文解决方案
### 1 异常聚类分块策略(OCTS)
通过3σ规则识别异常通道，置换至最后独立分块；同块统一精度，消除不规则访存，无需等待不同位宽数据串行计算。
### 2 混合量化+可重构双比特CIM(Re-DBCIM)
权重对称4bit量化提升存储密度；激活非对称量化，异常/非线性层保留BF1；设计双比特存储单元，搭配冗余位融合IRBF消除空转周期。
### 3 量化因子后处理QFP²+专用量化器
利用线性映射将FP×INT运算后置缩放因子，省去全局浮点转换；硬件集成前导零检测、移位拼接模块，统一INT/浮点两类MAC流水线。
### 4 完整协同架构
全局缓冲+8组CIM阵列+专用量化器，支持INT4/8、BF16混合矩阵运算，适配LLM注意力、MLP全层推理。

## 实验分析
1. 仿真与硬件：28nm CMOS，面积2.25mm²，测试LLaMA/OPT 6.7B~65B，数据集WikiText2、C4。
2. 算法精度：分组混合量化后困惑度接近FP16，远优于OliVe等低精度基线。
3. 硬件性能：对比OliVe平均提速3.91倍，能效提升4.54倍；对比Oltron提速2.06倍、能效提升2.83倍。
4. 消融实验：OCTS降低25.3%延迟；Re-DBCIM将CIM利用率提升25%；QFP²大幅削减FP-INT转换能耗。
5. 硬件指标：INT4推理能效82.11 TOPS/W，大模型LLaMA-65B达61.77 TOPS/W。

## 研究启发
1. LLM低精度推理瓶颈根源是激活异常值带来访存与计算割裂，必须算法与CIM硬件联合优化。
2. 分块规整化是释放CIM算力基础，集中异常至独立块可消除位宽不均带来的流水线等待。
3. 权重/激活差异化混合量化可平衡存储密度与模型精度，搭配双比特存内单元适配低比特负载。
4. FP-INT混合运算无需全程浮点计算，线性缩放后置处理能大幅削减格式转换开销。
5. 数字CIM不能仅适配常规固定位宽，可重构存储与专用量化单元是LLM推理适配关键。
