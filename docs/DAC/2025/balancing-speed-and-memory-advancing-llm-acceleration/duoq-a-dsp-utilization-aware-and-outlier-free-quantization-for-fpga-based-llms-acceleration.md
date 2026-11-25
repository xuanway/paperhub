---
title: "DuoQ: A DSP Utilization-aware and Outlier-free Quantization for FPGA-based LLMs Acceleration"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DuoQ: A DSP Utilization-aware and Outlier-free Quantization for FPGA-based LLMs Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132816">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132816</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 现场可编程门阵列，W4A4量化，大语言模型，DSP利用率，算法-硬件协同设计 </p>
</div>


---

## 研究概要
本文提出面向FPGA的DuoQ软硬件协同4bit量化框架，设计跨层等价变换+低语义Token感知算法彻底消除激活离群值，配套DSP感知可重构PE、稀疏编码器与专用非线性处理单元。在LLaMA、OPT系列模型验证，4bit下困惑度大幅优于同类方案，推理最高提速8.8倍、能效提升23.45倍。

## 背景和动机
1. LLM参数量巨大，FP16推理存储与算力开销极高，4bit量化可显著压缩开销，但激活广泛存在通道/Token离群值，直接量化精度暴跌。
2. 现有离群处理方案依赖分通道、分Token混合精度编码，引入大量格式转换、索引存储开销，硬件利用率低下。
3. FPGA核心计算单元DSP原生对4bit有支持缺陷，传统INT4实现仅能无符号运算，DSP资源利用率极低。
4. 现有FPGA LLM加速器仅做网络局部加速，缺少适配W4A4KV4全张量量化的端到端硬件流水线。
5. Softmax、SiLU等非线性算子在低比特下近似误差大，缺少硬件友好的分段线性实现方案。

## 相关工作
1. 离群感知量化算法（SmoothQuant/QuaRot/SpinQuant）：采用哈达玛旋转、通道缩放平滑离群，但未结合FPGA硬件约束，部署开销高。
2. 硬件导向量化（Omniquant/HotaQ/Oltron）：分通道隔离离群，依赖混合精度动态编码，DSP利用率差。
3. FPGA低比特加速（FlightLLM/DFX）：仅支持INT8或受限INT4，无完整W4A4流水线，未解决离群带来精度损失。
4. DSP打包优化（WP486/DoubleMAC）：仅支持部分位宽，无法高效实现有符号4bit并行乘算，校正逻辑缺失。
5. 稀疏编码硬件：仅面向权重稀疏，未针对量化后离群变换矩阵做CS压缩加速。

## 本文解决方案
### 1 无离群W4A4KV4量化算法
1）跨层仿射变换CLAT、跨块缩放CBST：构造可逆正交变换融合进权重，平滑通道离群，数学等价不引入推理开销；
2）低语义Token感知LSTA：建模注意力量化误差上界，定位BOS等异常Token，约束KV缓存离群分布；
3）交替联合优化：最小量化输出F范数误差，SVD求解正交变换矩阵，仅微调少量变换参数。
### 2 DSP感知可重构PE单元
基于DSP48E2设计多模式打包计算，支持INT4/INT8有符号并行乘；设计专用进位、符号校正电路，搭配活动位扫描ABS模块提升并行度，大幅提升DSP利用率。
### 3 离群消除稀疏编码器
将CLAT变换矩阵采用CSC稀疏格式存储，多路MUX与累加树硬件并行完成激活变换，无需在线矩阵乘，消除推理时离群计算开销。
### 4 专用辅助/后处理单元
APU整数分段线性PWL近似各类激活、归一化函数，误差极低；PPU集成窗口式排序单元，高效完成Softmax归一化与KV缓存量化。
### 5 五级全流水线FPGA架构
预加载→缓存读写→MAC阵列→非线性后处理→回写HBM，HBM与片上FIFO分层缓存，分离Prefill/Decode数据流。

## 实验分析
1. 实验平台：Xilinx Alveo U280（16nm，150MHz），LLaMA2/LLaMA3、OPT 6.7B~70B模型，WikiText、PIQA等多评测集，基线含SmoothQuant、Oltron、FlightLLM等。
2. 量化精度：W4A4下LLaMA2-7B困惑度6.11，远优于Omniquant(11.26)；7B/13B零-shot平均精度仅比FP16低1.86%，大幅领先同类4bit量化。
3. DSP硬件效率：单DSP可并行4路INT4有符号乘，LUT/FF资源占用显著低于现有打包方案，DSP利用率大幅提升。
4. 端到端性能：相较主流FPGA加速器，推理延迟最高降低8.8倍，能耗效率提升最高23.45倍。
5. 消融验证：CLAT+LSTA联合是消除离群、控制精度损失核心；DSP校正电路、APU分段线性模块对吞吐与精度增益不可替代。

## 研究启发
1. 仅靠后处理隔离离群治标，跨层可逆正交变换可在推理零开销前提下从源头抹平激活极值，更适配低比特全张量量化。
2. FPGA加速LLM必须算法-硬件协同，量化方案需贴合DSP原生位宽特性，定制校正逻辑才能释放4bit并行算力。
3 BOS等低语义Token是量化误差主要来源，针对性约束KV缓存分布可显著降低注意力模块精度损耗。
4. 正交变换矩阵天然稀疏，采用CSC硬件编码器可避免在线矩阵运算，不增加推理延迟。
5. 低比特非线性不能简单查表，整数分段线性单元兼顾精度与流水线吞吐，是FPGA轻量化推理关键配套设计。
