---
title: "XShift: FPGA-efficient Binarized LLM with Joint Quantization and Sparsification"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# XShift: FPGA-efficient Binarized LLM with Joint Quantization and Sparsification

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133363">https://dl.acm.org/doi/abs/10.1109/DAC63849.2025.11133363</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 二值化大语言模型，XNOR-Shift编码，联合量化与稀疏化，FPGA加速器 </p>
</div>


---

## 研究概要
本文提出XShift软硬件协同框架面向FPGA二值LLM推理。设计XNOR-Shift编码将乘法转为异或移位；HAOS联合量化稀疏算法精准保留通道离群值；配套三模式XSSA脉动阵列与BSMC高效SoftMax单元。Alveo FPGA实测DSP用量降低10~15倍，推理提速4.17~4.76倍，能效提升6.95~14.29倍，困惑度优于同类低精度方案。

## 背景和动机
1. 现有LLM二值化仅权重二值，激活高精度带来KV缓存存储压力；全二值方案精度暴跌，缺少适配FPGA的统一编码格式。
2. 传统低比特量化对通道级离群值处理粗糙，单独存储离群矩阵硬件带宽开销巨大，无法适配脉动阵列数据流。
3. FPGA加速器大量消耗DSP实现乘法，资源紧张；预填充/解码两阶段算力需求差异大，现有架构无法动态调度硬件资源。
4. SoftMax指数运算硬件开销极高，分段近似误差大，缺少适配低比特二值网络的硬件加速单元。
5. 边缘单批量离散请求场景，预填充与解码无法并行，硬件利用率低、TTFT/TBT时延难以兼顾。

## 相关工作
1. 二值神经网络BiLLM/BitNet：仅简单二值化，无离群值保护，大模型困惑度大幅上升，无专用FPGA硬件。
2. 低比特量化AWQ/OmniQuant：依赖DSP乘法单元，未结合移位运算削减硬件开销，未联合结构化稀疏。
3. FPGA LLM加速器FlightLLM/DFX：使用大量DSP完成乘算，不支持纯异或移位二值计算，无法动态适配两阶段算力需求。
4. 离群感知量化Oltron/OPAL：单独开辟离群矩阵，访存带宽成本高，难以和脉动阵列流水线兼容。
5. 通用二值FPGA加速器：仅面向CNN/BERT，不兼容LLM自注意力与KV缓存迭代解码流程。

## 本文解决方案
### 1 XNOR-Shift(XSE)统一编码格式
基础格式用符号位异或、移位位替代乘法；扩展XSE采用类浮点分段尾数，无损表征通道离群值，全程无需DSP乘法器，移位单元资源消耗仅为乘法1/8。
### 2 HAOS硬件自适应联合量化稀疏
基于海森近似计算权重/激活通道敏感度，分层保留高重要离群通道；次要通道量化+结构化剪枝，兼容脉动阵列逐通道计算，仅少量可学习校准参数。
### 3 三模式XSSA异或移位脉动阵列
Mode1预填充满阵列并行降低TTFT；Mode2解码单层运行省电；Mode3预填充与解码权重复用并行处理离散请求，解决边缘请求等待瓶颈。
### 4 BSMC基2 SoftMax硬件转换器
将指数运算转换2的幂次分解，查表分段近似小数部分，无需高精度指数单元，适配XSE量化输出，减少归一化计算误差。
### 5 完整FPGA编译映射流水线
模型经HAOS压缩后生成高低层IR，ISA生成器适配XSSA调度指令，自动分配片上缓存与外部存储KV缓存。

## 实验分析
1. 实验环境：Xilinx Alveo U50/U280，LLaMA系列7/8/13B，WikiText2/C4，对比BiLLM、FlightLLM、V10/A100 GPU。
2. 精度表现：3/4bit XSE量化困惑度显著优于BiLLM、I-LLM，零样本分类平均精度高出6~7个百分点。
3. FPGA资源：DSP仅224~356个，相比同类加速器降低10~15倍，LUT/BRAM开销可控。
4. 性能能效：相比V100推理提速4.17~4.76倍，能效最高提升14.29倍；U5边缘板卡性价比优于U280。
5. 调度消融：三模式协同可并行处理新预填充与旧解码，消除请求排队，硬件利用率提升30%以上。

## 研究启发
1. 二值LLM不能简单截断数值，设计移位替代乘法的专用编码可同时兼顾精度与FPGA DSP资源节省。
2. 离群值不能单独开辟矩阵存储，基于通道敏感度的联合量化稀疏可无缝适配脉动阵列数据流。
3. LLM预填充、解码算力需求差异巨大，多模式可重构脉动阵列是提升边缘离散请求吞吐的关键。
4. SoftMax指数运算可通过2次幂数学变换大幅简化硬件实现，适配低比特量化网络。
5. 面向边缘FPGA的LLM协同优化，必须同时兼顾编码算法、稀疏压缩、硬件数据流与阶段调度四者联动。
