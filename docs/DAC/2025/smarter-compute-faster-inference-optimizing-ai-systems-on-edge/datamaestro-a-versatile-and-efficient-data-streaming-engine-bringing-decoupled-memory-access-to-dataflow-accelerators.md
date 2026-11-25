---
title: "DataMaestro: A Versatile and Efficient Data Streaming Engine Bringing Decoupled Memory Access To Dataflow Accelerators"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# DataMaestro: A Versatile and Efficient Data Streaming Engine Bringing Decoupled Memory Access To Dataflow Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.14091">https://arxiv.org/abs/2504.14091</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 数据流加速器，解耦访问执行，数据流引擎，存储优化 </p>
</div>

---

## 研究概要
本文提出DataMaestro通用解耦数据流引擎，面向DNN加速器分离访存与计算流程。支持N维可编程仿射地址、细粒度预取、运行时切换存储寻址模式，内置可扩展通路实时数据变换。集成矩阵/量化加速器在22nm、FPGA验证，PE利用率接近100%，吞吐量较SOTA提升1.05~21.39倍，仅占系统6.43%面积、15.06%功耗。

## 背景和动机
1. 现代DNN加速器算力充足，但片外/片上存储数据搬运成为核心性能与能耗瓶颈，大量周期因访存阻塞闲置PE阵列。
2. 现有数据搬运单元与特定加速器强耦合，仅支持固定访存模式，无法适配CNN、Transformer多样数据流，复用性极差。
3. 多Bank片上缓存极易发生存储冲突，传统方案依赖私有缓冲区或限制分块尺寸，带宽利用率低。
4. 转置、im2col、广播等数据预处理需额外缓存与重复访存，大幅提升内存能耗。
5. 现有解耦访问架构仅支持低维地址生成，无法覆盖卷积高维张量复杂访问需求。

## 相关工作
1. Gemmini：专用数据流单元，仅二维地址，多Bank冲突严重，PE利用率最低仅10%。
2. BitWave：面向稀疏卷积定制，通用性差，不支持Transformer通用矩阵运算。
3. FEATHER：仅基础数据重排，无预取、寻址模式动态切换能力。
4. Buffet/Softbrain：实现解耦访存，但仅支持二维地址生成，高维卷积适配性弱。
5. SSR：面向通用处理器解耦流，并非针对DNN张量多维访存优化。

## 本文解决方案
### 1 通用解耦访存整体架构
多组读/写DataMaestro独立配置，通过交叉互联连接多Bank片上缓存与PE阵列，访存、计算两条流水线完全解耦，FIFO掩盖存储延迟。
### 2 N维可编程仿射地址生成单元
分层时空双计数器架构，支持任意时空维度循环，低硬件开销生成多维张量访存地址，原生支持im2col隐式变换。
### 3 细粒度异步预取机制
拆分宽访存请求为多通道细粒度请求，请求管理器预留FIFO空间、动态节流，充分利用多Bank并行带宽。
### 4 运行时可切换地址重映射器
硬件实现地址比特置换，运行时切换全交错/分组交错/非交错三种寻址模式，缓解Bank冲突。
### 5 可插拔实时数据变换通路
流水线式扩展模块，支持矩阵转置、通道广播等操作，无需中间缓存，直接流式送入PE，减少内存访问次数。

## 实验分析
1. 实验平台：22FDX VLSI综合、AMD VPK180 FPGA原型，搭配8×8三维GeMM与量化加速器，测试ResNet/VGG/ViT/BERT。
2. PE利用率：四类真实网络阵列利用率均超95%，VGG、ViT接近100%；消融实验证明预取、寻址切换是核心增益来源。
3. 吞吐性能：同等PE规模对比主流加速器，各类矩阵/卷积任务提速区间1.05~21.39倍，数据访问量最高下降21.15%。
4. 硬件开销：整套DataMaestro面积占系统6.43%，功耗占15.06%，各扩展模块硬件占比极低。
5. 泛化验证：兼容CNN、Transformer不同数据流，设计时可配置参数适配各类张量维度，开源可复用。

## 研究启发
1. 数据搬运瓶颈优先于算力瓶颈，通用解耦访存引擎可大幅提升PE阵列实际有效算力。
2. 多维张量访存不能局限二维地址生成，分层时空计数器以低开销适配卷积、多头注意力复杂访问模式。
3. 单一存储寻址模式无法适配所有网络，运行时动态切换交错策略可显著缓解Bank冲突。
4. 预处理操作放到数据流通路实时完成，省去中间缓存是降低内存能耗关键手段。
5. 数据引擎采用参数化可配置设计，可跨矩阵、卷积、量化加速器复用，减少硬件重复开发成本。
