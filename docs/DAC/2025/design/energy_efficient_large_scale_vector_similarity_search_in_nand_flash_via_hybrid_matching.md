---
title: "Energy-Efficient Large-Scale Vector Similarity Search in NAND-Flash via Hybrid Matching"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Energy-Efficient Large-Scale Vector Similarity Search in NAND-Flash via Hybrid Matching

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132636">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132636</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 向量相似性搜索，3D NAND闪存，混合匹配，多级单元范围编码，过滤感知训练</p>
</div>


---

## 研究概要
本文提出基于3D NAND的混合匹配VSS架构Hybrid-M，在同一存储串融合精确ES过滤与近似AS检索。配套MLC区间编码、搜索电压偏移、感知训练FAT三项优化。在小样本学习、ANNS任务验证，相较纯AS方案能耗降低67%~83%，精度/召回损失极小。

## 背景和动机
1. 大规模向量相似检索(VSS)算力、带宽开销巨大，3D NAND MCAM高密度适合片内检索，但仅有AS近似模式能耗极高，98%以上电流来自无关无效向量。
2. ES精确匹配低功耗但只能完全匹配，AS可度量相似度但全串导通造成大量无用功耗，现有方案两套模式分立，额外增加TCAM硬件开销。
3. ES占用存储字线会挤压AS编码空间，同时ES失配会干扰AS电流-相似度线性对应关系，降低检索精度。
4. 传统SLC区间编码过滤能力弱，缺少适配MLC多阈值的高效编码方案，且网络训练未结合存储硬件非理想特性。

## 相关工作
1. 纯AS型NAND片内检索：仅近似搜索，所有存储串均导通，无关向量能耗浪费严重，无前置过滤机制。
2. TCAM+CIM分离架构：ES过滤、AS检索分属两套存储阵列，硬件面积与访存开销翻倍。
3. SLC区间编码过滤：仅双电平存储，单字线承载区间少，过滤覆盖率低，节能效果有限。
4. 硬件无关向量训练：未建模NAND电压、电流非理想效应，部署后检索精度大幅下滑。

## 本文解决方案
### 1. 同串混合匹配Hybrid-M架构
单条3D NAND串分段实现ES过滤+AS检索，高类间方差维度分配ES做L∞预过滤，无关串直接关断消除无用电流；剩余字线执行AS相似度计算。
### 2. MLC八态区间编码
拓展MLC存储单元至8种可编程状态，约束规划生成区间码字，有限字线下提升过滤覆盖率，相比SLC多节省10%~30%能耗。
### 3. AS搜索电压偏移优化
下调AS搜索过驱动电压，削弱ES失配对电流曲线的干扰，恢复电流与相似度线性关系，精度回升10%~15%且进一步降耗。
### 4. 过滤感知FAT训练
在网络训练中建模NAND混合匹配硬件特性，引入可学习ES阈值与平滑门控，兼顾过滤能力与检索精度，额外节能3%~8%。

## 实验分析
1. 测试负载：Omniglot/CUB小样本学习、MNIST/Fashion-MNIST/GIST近似检索，基准为纯AS、TCAM+CIM、SLC编码方案。
2. 能耗收益：Hybrid-M整体能耗下降67%~83%，MLC编码相较SLC额外节能10~30%，电压偏移叠加FAT再降3%~8%。
3. 精度指标：小样本分类精度损失低于0.5%，ANNS召回率下降不足0.01，远优于TCAM分立方案。
4. 硬件对比：无需独立TCAM阵列，复用原生3D NAND存储串，无额外面积开销；单轮检索时长50us。
5. 消融实验：仅ES过滤会损失精度，仅电压偏移节能有限，四项技术协同达到最优能耗精度权衡。

## 研究启发
1. 3D NAND原生支持多电压搜索，可在同一存储串融合精确过滤与近似检索，省去独立TCAM硬件成本。
2. MLC多阈值单元相比SLC具备更强区间编码能力，是提升预过滤效率的核心硬件基础。
3. ES模式会破坏AS电流线性度，仅靠编码优化不足，必须配套搜索电压偏移补偿精度损耗。
4. 向量提取网络训练需贴合存储硬件物理特性，硬件感知训练可大幅缩小软硬件精度鸿沟。
5. 大规模检索绝大多数向量为无关样本，轻量片内预过滤是解决存储计算能耗瓶颈的低成本路线。