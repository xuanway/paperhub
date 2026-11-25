---
title: "Segmented Angular Pre-Processing for Accurate and Efficient In-Memory Vector Similarity Search"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Segmented Angular Pre-Processing for Accurate and Efficient In-Memory Vector Similarity Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133320">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133320</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 分段角度预处理，向量相似度搜索，三态内容寻址存储器，余弦相似度，存内搜索</p>
</div>


---

## 研究概要
本文提出Seg-Cos TCAM内存向量相似度检索框架，面向余弦相似度度量。设计分段余弦度量、角度量化、幅值感知区间生成与莫比乌斯循环编码，无需改动TCAM硬件。小样本/近似检索任务测试，精度提升2.2%，召回提升10%~52%，能效最高提升2倍。

## 背景和动机
1. 冯诺依曼架构向量检索存在海量数据搬运开销，TCAM存内检索可并行比对，但现有方案仅支持L₁/L∞空间距离，与AI主流余弦相似度偏差大。
2. 汉明距离是TC原生度量，无法表征向量夹角；传统区间编码仅支持线性范围，不兼容角度循环计算逻辑。
3. 余弦相似度对高幅值维度更敏感，现有TCAM编码同等对待所有维度，检索精度损失严重。
4. 过往方案需微调预训练模型适配L范数，带来巨大训练成本，缺少原生适配余弦的TCAM编码预处理流程。

## 相关工作
1. EX-TCAM系列（RENÉ、BORE）：区间迭代搜索，适配L∞距离，循环角度计算不支持，高维任务精度差。
2. Best-TCAM（SAPIENS）：温度计编码实现L₁单趟检索，编码码长过长，能效偏低。
3. 通用汉明TCAM：仅按符号比对，完全忽略向量幅值信息，与余弦相似度差距显著。
4. 软件ANN检索：余弦计算精度高，但访存瓶颈严重，边缘端功耗延迟无法达标。

## 本文解决方案
### 1 分段余弦相似度度量
将高维向量切分为2维重叠分段，通过数学变换把余弦相似度转化为可由汉明距离近似的聚合指标，分MAX/AVG两种聚合适配EX/Best两类TCAM。
### 2 角度量化与幅值感知区间生成
二维平面均分角度做量化；依据向量/分段幅值对数差动态生成检索区间，高幅值分段区间更窄，匹配余弦权重特性。
### 3 莫比乌斯循环TCAM编码
专门适配环形角度区间，限定最大区间长度为半圆周，控制码长不爆炸，相比传统循环编码大幅削减存储开销。
### 4 双TCAM兼容完整流水线
预处理+编码流程同时适配迭代式EX-TCAM与单趟Best-TCAM，无需修改存储硬件，直接复用现有存内检索电路。

## 实验分析
1. 测试负载：小样本Omniglot/mini-ImageNet、ANNS GloVe/NYTimes词嵌入，22nm 2FeFET TCAM仿真。
2. 少样本学习（EX-TCAM）：相较BORE精度提升2.2%，单位查询能效提升1.41倍，高维图像增益更明显。
3. 近似检索（Best-TCAM）：对比L₁温度计编码召回提升10%~52倍，搜索能效提升2倍。
4. 编码开销：莫比乌编码控制码长线性增长，规避传统循环编码码长爆炸问题。
5. 消融：2维分段是精度核心，幅值区间、循环编码分别解决权重偏差、角度匹配两大缺陷。

## 研究启发
1. TCAM原生汉明度量可通过分段数学变换近似余弦相似度，无需重新设计存储单元。
2. 向量幅值不能均等处理，区间生成引入对数权重可贴合余弦计算的贡献差异。
3. 角度检索属于环形区间，专用循环编码是平衡TCAM码长与匹配精度的关键。
4. 一套预处理编码流水线兼容两类TCAM架构，可降低硬件改造成本，提升方案通用性。
5. 面向AI存内检索不能直接复用L₁/L∞方案，必须针对余弦度量定制预处理与编码协同设计。
