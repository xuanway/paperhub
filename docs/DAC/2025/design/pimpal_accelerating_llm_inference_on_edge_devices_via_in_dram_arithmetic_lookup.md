---
title: "PIMPAL: Accelerating LLM Inference on Edge Devices via In-DRAM Arithmetic Lookup"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# PIMPAL: Accelerating LLM Inference on Edge Devices via In-DRAM Arithmetic Lookup

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133391">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133391</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 查找表存内处理，通用矩阵-向量乘法，大语言模型推理，局部性感知计算映射，LUT聚合</p>
</div>

---

## 研究概要
本文提出面向边缘小型LLM的LUT型存内计算架构PIMPAL，用于加速GEMV运算。设计子数组并行查找、局部感知映射LCM、LUT聚合LAG三大机制，解决传统LUT-PIM行激活多、精度受限问题。测试相较pLUTo提速17.8倍，相比PU型PIM面积开销降低40、单位面积性能提升25%。

## 背景和动机
1. 边缘小型LLM推理以GEMV为核心，占60%以上时延，单输入无批量GEMM优化，传统芯片带宽瓶颈严重。
2. PU式PIM集成大量乘法单元，DRAM工艺下逻辑面积损耗大，内存容量直接减半，不适合边缘设备。
3. 现有LUT-PIM频繁触发DRAM行激活，访存延迟与能耗极高，且仅支持低精度，无法满足INT8/BF16推理需求。
4. 高精度完整LUT体积远超行缓存，拆分后进一步加剧行激活开销，缺乏分表聚合硬件方案。

## 相关工作
1. PU类PIM(Newton)：集成专用MAC单元，GEMV速度快，但占用近一半DRAM存储，边缘设备无法适配。
2. pPIM：外置缓存存储LUT，仅支持8位运算，不兼容BF16高精度推理。
3. pLUTo：全行扫描查表，每次乘法触发大量行激活，时延能耗极差。
4. ReD-LUT：单次查表仅输出一个结果，矩阵运算时行激活次数随数据量线性暴涨。

## 本文解决方案
### 1 子数组并行计算块组织
DRAM Bank划分为多计算块，每块配对矩阵子数组与LUT子数组，子数组间并行查表，复用BLSA行缓存减少激活。
### 2 局部感知映射LCM
采用列主序GEMV计算，向量值作为LUT行地址，单次行激活完成整列所有乘运算，将行激活次数压缩至向量长度量级。
### 3 LUT聚合LAG高精度机制
将BF16乘法拆分为指数、尾数独立小LUT，单条子数组即可存储，配合部分行激活PL仅读取所需分段，LUT总容量从8GB降至128KB。
### 4 LISA低成本子数组互连
启动时快速在各计算块复制LUT，无需每块独立存储查表，降低DRAM容量占用；搭配专用加法树完成多查表结果累加。

## 实验分析
1. 仿真环境：Ramulator周期级LPDDR5模拟器，对比Jetson Xavier、Newton、pLUTo，负载为Gemma-2、OPT等小型LLM。
2. 性能：端到端推理较pLUTo提速17.8倍，和Newton性能接近，均远超边缘GPU；各类GEMV平均提速13.8倍。
3. 面积：PIMPAL总面积1.82mm²，Newton为3.04mm²，乘法器区域面积削减40%。
4. 能效：仅比Newton高约10%，远低于频繁行激活的pLUTo。
5. 消融：LCM大幅削减行激活；LAG是支持BF16高精度的核心，PL机制进一步降低查表能耗。

## 研究启发
1. 边缘LLM GEMV无需海量PU阵列，基于LUT的存内计算可大幅削减硬件面积开销，适配内存受限终端。
2. DRAM行缓存局部性是LUT-PIM性能关键，列主序映射可最大化行命中，从根源减少昂贵行激活操作。
3. 高精度浮点运算无需巨型完整查表，拆分为指数、尾数独立小LUT聚合是低成本高精度路线。
4. 子数组互连技术可实现LUT快速全局分发，避免每块独立存储带来容量浪费。
5. 单位面积算力是边缘PIM核心指标，舍弃专用乘法器、复用存储单元查表更贴合DRAM工艺特性。
