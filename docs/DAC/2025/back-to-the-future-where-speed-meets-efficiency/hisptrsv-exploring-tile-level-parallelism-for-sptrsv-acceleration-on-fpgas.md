---
title: "HiSpTRSV: Exploring Tile-Level Parallelism for SpTRSV Acceleration on FPGAs"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# HiSpTRSV: Exploring Tile-Level Parallelism for SpTRSV Acceleration on FPGAs


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133234">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133234</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>硬件加速器，计算机系统组织，可重构计算 </p>
</div>

---

## 研究概要
本文提出HiSpTRSV，面向HBM FPGA挖掘稀疏三角求解分块间+分块内双层并行。设计细粒度依赖图、流过滤单元、模双向索引均衡负载，配套THLS并行算法。基于Alveo U55C验证，对比FPGA基线平均提速34.3%，相较GPU平均提速3.58倍、能效提升9.59倍。

## 背景和动机
1. SpTRSV存在强串行数据依赖，传统LevelST仅挖掘单分块内部并行，忽略分块间可并行计算，硬件算力闲置严重。
2. 跨分块细粒度并行实现存在三大难点：稀疏矩阵依赖复杂、细粒度模块通信开销高、非零元随机分布导致PE负载失衡。
3. GPU执行SpTRSV时线程大量空闲，核心利用率极低，功耗开销巨大；现有FPGA加速器无法同时释放双层并行潜力。
4. 稀疏矩阵气泡空元素带来冗余同步传输，进一步放大片上通信延迟，限制吞吐上限。

## 相关工作
1. LevelST：主流FPGA SpTRSV加速器，仅实现分块内并行，分块间串行执行，并行度存在天花板。
2. TileSpTRSV、Split Execution GPU方案：仅面向GPU优化分块调度，未适配FPGA流架构与HBM带宽特性。
3. Serpens/Sextans：FPGA稀疏矩阵乘加速器，仅优化SpMV，无法适配SpTRSV特有的递推求解依赖。
4. 通用稀疏求解器：仅软件算法层面分块并行，无配套硬件流水线、过滤与负载均衡硬件设计。

## 本文解决方案
### 1 THLS分块高并行Level-Set算法
拆分SpTRSV、SpMV两类分块，构建双层依赖图，实现分块内、分块间同步流水线并行，重叠求解与矩阵乘计算。
### 2 细粒度自动化依赖图解析
按行粒度拆解稀疏矩阵节点/边依赖，支持任意规模矩阵自动生成计算索引，为多PE并行提供调度依据。
### 3 气泡元素流过滤单元
识别无意义气泡空元，过滤其片上同步传输，削减跨PEG通信流量，缓解URAM读写压力。
### 4 模运算双向索引负载均衡
SpTRSV/SpMV采用差异化模映射规则，匹配URAM高低存储分区，保证PE间计算量均衡，减少空闲周期。
### 5 基于HBM的流式PEG硬件架构
多处理元组PEG并行对接HBM通道，环形同步流传递中间解，SpMV/SpTRSV共用URAM缓存资源。

## 实验分析
1. 实验平台：Xilinx Alveo U55C FPGA，对比LevelST FPGA、RTX3060/V100 GPU；测试SuiteSparse 16组稀疏矩阵。
2. 性能指标：相较LevelST几何平均提速34.3%；对比V10平均提速3.58倍，最高加速16.29倍。
3. 能效表现：相比GPU平均能效提升9.59倍，大稀疏矩阵场景增益可达59.94倍。
4. 通信优化：元素聚集型矩阵过滤单元削减最高65%传输量；均匀稀疏矩阵优化收益微弱。
5. 硬件资源：246MHz工作频率，URAM占用66.67%，DSP仅消耗13.52%，资源利用率均衡可控。

## 研究启发
1. SpTRSV并行不能局限单分块，利用分块间弱依赖做流水线重叠是提升吞吐核心突破口。
2. 稀疏计算中气泡空元是通信冗余主要来源，专用硬件过滤单元可低成本降低片上传输开销。
3. 差异化索引映射结合片上分区存储，能有效解决稀疏随机分布带来的PE负载不均问题。
4. FPGA HBM流式架构适配稀疏递推计算，相比GPU可大幅降低闲置算力带来的无效功耗。
5. 算法分块并行策略必须与硬件存储、通信架构协同设计，单纯软件并行难以发挥FPGA硬件优势。