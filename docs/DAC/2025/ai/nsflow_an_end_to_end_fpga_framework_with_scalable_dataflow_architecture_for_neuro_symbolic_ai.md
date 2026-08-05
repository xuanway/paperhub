---
title: "NSFlow: An End-to-End FPGA Framework with Scalable Dataflow Architecture for Neuro-Symbolic AI"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# NSFlow: An End-to-End FPGA Framework with Scalable Dataflow Architecture for Neuro-Symbolic AI

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI4: AI/ML System and Platform Design</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.19323">https://arxiv.org/abs/2504.19323</a></p> 
<p class="paper-seo-summary__meta"><strong>PPT链接:</strong> <a href="https://zishenwan.github.io/publication/DAC25_NSFlow_Slide.pdf">https://zishenwan.github.io/publication/DAC25_NSFlow_Slide.pdf</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 神经符号AI，FPGA加速框架，数据流架构生成，自适应脉动阵列 </p>
</div>

---

## 研究概要
本文提出NSFlow端到端FPGA神经符号AI加速框架，前端设计生成器解析数据流并两阶段空间探索，后端自适应脉动阵列支持神经网络与VSA符号运算，搭配可重组片上存储与混合精度。在多推理任务验证，相较TX2提速31倍、GPU超2倍、TPU8倍、DPU3倍，符号负载150倍扩展时运行时仅增4倍。

## 背景和动机
1. 神经符号AI融合神经网络与向量符号(VSA)推理，兼具感知与逻辑能力，但CPU/GPU/TPU等通用硬件适配极差。
2. NSAI负载异构：CNN计算密集、VSA循环卷积访存受限，二者串行执行形成关键路径，硬件利用率极低。
3. VSA向量符号运算存储占用极高，现有固定脉动阵列无法适配向量循环卷积数据流，片上缓存频繁溢出。
4. 传统FPGA加速工具仅面向纯DNN，无神经符号混合负载自动映射流程，人工设计成本高。
5. 符号推理规模伸缩性差，负载量大幅提升时现有加速器时延暴涨，难以支持大规模抽象推理任务。

## 相关工作
1. 通用FPGA DNN加速器：仅支持卷积、GEMM，无VSA循环卷积专用数据流设计，无法处理符号推理。
2. 商用ML硬件(Xilinx DPU、TPU)：架构固化，访存模式不匹配VSA流式向量，符号任务速度衰减严重。
3. 神经符号算法研究(NVSA/MIMONet)：仅优化算法逻辑，未配套专用硬件加速方案。
4. FPGA数据流综合工具：单网络负载优化，不支持神经、符号混合异构任务协同调度。
5. 传统脉动阵列设计：仅面向权重固定卷积，缺少循环卷积所需传递寄存器，向量运算吞吐低。

## 本文解决方案
### 1 前端数据流架构生成器(DAG)
提取程序执行轨迹构建算子级数据流图，DFS识别关键路径、BFS挖掘层内/层间并行；两阶段DSE大幅压缩搜索空间，输出硬件配置与CPU调度代码。
### 2 自适应脉动阵列AdArray
阵列可动态分块，子阵列并行执行CNN或VSA循环卷积；PE增设传递寄存器适配向量循环移位，运行时折叠调度平衡两类算子算力。
### 3 可重组分层片上存储
多组双缓冲BRAM动态合并/拆分，分别缓存特征图、向量符号；URAM构建大容量片上缓存，减少片外DRAM交互。
### 4 混合精度自适应计算单元
NN采用INT8、符号向量采用INT4，乘法器适配多比特，低精度加法用LUT加速，在推理精度损失极小前提下压缩存储。
### 5 专用SIMD协处理器
封装求和、归一化、激活、稀疏向量运算，承接阵列输出逐元素处理，打通神经-符号数据流转流水线。

## 实验分析
1. 实验环境：AMD U250 FPGA，272MHz；NVSA/MIMONet/LVRF三类NSAI模型，RAVEN/PGM等推理数据集，对比TX2、RTX2080、TPU、Xilinx DPU。
2. 加速性能：端到端推理相较TX2提速31×，GPU>2×，类TPU脉动阵列8×，DPU>3×；符号负载扩150倍仅4倍时延增长。
3. 精度存储：INT8/INT4混合精度推理精度仅小幅下降，存储占用降低5.8倍。
4. 消融实验：两阶段DSE带来最高44%性能提升；AdArray分块架构在符号占比80场景提速7倍。
5. 资源开销：U25芯片DSP/LUT/BRAM利用率可控，时钟稳定272MHz，满足实时推理需求。

## 研究启发
1. 神经符号AI是异构混合负载，不能复用纯DNN固定加速器，需可分块自适应计算阵列兼顾卷积与VSA循环卷积。
2. 算法硬件协同数据流生成是关键，通过图挖掘并行可消除神经、符号串行关键路径瓶颈。
3. VSA向量运算属于访存绑定负载，分层可重组片上存储能显著降低片外带宽压力。
4. 两阶段分治设计空间探索可指数级缩减搜索量，解决混合异构架构寻优难题。
5. 差异化混合精度策略对符号向量收益显著，可在几乎无损推理的前提下大幅降低存储与传输开销。
