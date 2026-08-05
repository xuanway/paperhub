---
title: "BBAL: A Bidirectional Block Floating Point-Based Quantization Accelerator for Large Language Models"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# BBAL: A Bidirectional Block Floating Point-Based Quantization Accelerator for Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI3: AI/ML Architecture Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.15721">https://arxiv.org/abs/2504.15721</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 双向块浮点，大语言模型加速器，低精度量化，非线性计算单元 </p>
</div>

---

## 研究概要
本文提出双向块浮点BBFP格式与LLM软硬件协同加速器BBAL。BBFP引入标志位与重叠比特缓解传统BFP对齐最大指数带来的量化误差；配套稀疏MAC单元、分段查表非线性模块。TSMC28nm流片验证，同等硬件开销精度比离群感知加速器提升22%，同精度吞吐量较标准BFP提升40%。

## 背景和动机
1. LLM权重/激活存在大量极端离群值，INT低比特量化困惑度暴涨，BF16/FP8硬件开销过高。
2. 传统BFP块统一对齐最大指数，中小数值截断误差大，低比特下模型精度严重下滑，且难以适配Softmax/SiLU非线性运算。
3. Transformer推理中非线性算子随序列变长成为性能瓶颈，现有BFP硬件仅优化线性矩阵乘，无配套低成本非线性单元。
4. 主流离群感知量化硬件面积功耗开销巨大，缺少兼顾量化精度、计算效率、硬件成本的全栈LLM加速方案。
5. 现有BFP乘法单元无比特稀疏优化，累加器位宽冗余，阵列资源利用率偏低。

## 相关工作
1. 整数量化（GPTQ/SmoothQuant/OmniQuant）：依靠定点压缩，但离群敏感，低比特精度衰减明显。
2. 基础块浮点BFP：单共享最大指数，量化误差大，仅适配CNN线性层，无专用非线性硬件。
3 FP8/BF16浮点格式：动态范围充足，但乘加单元硬件面积远高于块定点方案。
4. 离群感知加速器（Oltron/Olive）：单独存储极端值，控制逻辑复杂，硬件开销显著增加。
5. Transformer非线性专用硬件：多基于高精度浮点查表，无法与低比特块浮点体系兼容。

## 本文解决方案
### 1 BBFP双向块浮点数据格式
增加1bit标志位区分高低尾数，搭配重叠比特减少移位截断；共享指数选用Max-(m-o)而非全局最大值，降低量化方差，同等尾数位宽表示范围远超传统BFP。
### 2 自适应重叠位宽选择算法
权衡模型困惑度与硬件面积，遍历不同重叠比特配置，归一化精度、开销打分自动选出最优o参数，适配各类LLM分布特征。
### 3 比特稀疏BBFP MAC单元
利用标志位带来的尾数稀疏特性，拆分乘后移位逻辑；采用进位链简化宽加法器，相比完整12bit加法器减少15%组合门电路。
### 4 分段查表非线性计算单元
按BB共享指数拆分查表子块，流水线分段加载LUT，统一支持Softmax、SiLU、GELU，全程维持BBFP格式无格式转换开销。
### 5 BBAL全栈LLM加速器
权重驻留脉动阵列架构，区分两类BBFP处理单元；集成编码/缓存/非线性流水线，线性与非线性算子分时复用控制通路。

## 实验分析
1. 实验平台：TSMC 28nm工艺，Chisel实现、DC综合，Llama/OPT系列模型，WikiText2评测困惑度PPL。
2. 量化精度：BBFP(6,3)精度接近FP16；同等硬件开销下相比Oltron平均精度提升22%；非线性层PP涨幅仅0.44，而BFP10涨幅超3倍。
3. 硬件效率：同等精度吞吐量相比标准BFP提升40%；BBFP(3,1)PE面积仅为BFP6的0.31倍，静态能耗降低13%。
4. 非线性单元：相比高精度浮点非线性单元能效提升30倍，采用片外分段LUT大幅缩减片上存储开销。
5. 消融对比：重叠比特是误差抑制核心；共享指数选用Max-(m-o)相比全局Max误差方差显著下降。

## 研究启发
1. 块浮点无需强制对齐块内最大指数，双向标志+重叠比特可低成本大幅降低量化误差，适配含大量离群LLM数据分布。
2. 低比特量化不能仅优化线性矩阵乘，必须配套同格式非线性运算单元才能端到端保障推理精度。
3. 尾数比特稀疏特性可用于简化乘加电路，进位链替代宽加法器能显著削减加速器硬件面积。
4. 分段指数查表策略平衡片上存储与非线性时延，是块浮点适配Softmax等超越函数关键思路。
5. 面向LLM的量化硬件需分层设计线性/非线性模块，统一数据格式避免频繁格式转换带来额外能耗。
