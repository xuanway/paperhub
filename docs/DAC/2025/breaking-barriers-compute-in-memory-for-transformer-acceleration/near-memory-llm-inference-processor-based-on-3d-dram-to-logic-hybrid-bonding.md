---
title: "Near-Memory LLM Inference Processor based on 3D DRAM-to-logic Hybrid Bonding"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Near-Memory LLM Inference Processor based on 3D DRAM-to-logic Hybrid Bonding

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132870">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132870</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 混合键合，近存处理，大语言模型推理加速器，可重构</p>
</div>

---

## 研究概要
本文基于3D混合键合(HB)提出近内存LLM推理架构HB-NPU，采用集中控制器与双I/O通路解决分布式控制器面积开销、算力频率受限问题。支持可重构GEMM/GEMV/TS-GEMM数据流，OPT66B仿真相较NPU、DRAM-PIM、异构系统分别提速2.9/3.5/2.5倍，能耗大幅降低。

## 背景和动机
1. LLM推理分为Prefill(GEMM计算密集)与Decode(GEMV访存密集)阶段，单类加速器无法同时适配两种计算特征，批处理TS-GEMM任务资源利用率极低。
2. 传统3D HB近内存加速器采用每Bank独立分布式控制器，译码、BIST等模块带来17%单Bank面积损耗，挤占计算单元空间。
3. 分布式HB架构PE运行频率受DRAM时序约束仅500MHz，GEMM场景算力瓶颈显著，无法发挥 systolic阵列峰值性能。
4. NPU+PIM异构系统存在负载失衡，批大小受限场景TS-GEMM加速效果差，且整机内存与硬件成本翻倍。

## 相关工作
1. 独立NPU(TPUv4i)： systolic阵列算力充足，但Decode阶段带宽不足，KV缓存膨胀后吞吐量暴跌。
2. DRAM-PIM(AiM等)：Bank级并行带宽极高，但单Bank仅少量PE，GEMM计算密度低，Prefill性能弱。
3. NPU+PIM异构架构：分别承载GEMM/GEMV，但两类硬件负载难以均衡，TS-GEMM适配性差，硬件成本翻倍。
4. 早期3D HB近内存芯片：全分布式控制器架构，无分层双I/O设计，无法动态切换高低频数据流。

## 本文解决方案
### 1 集中式全局存储控制器
移除每Bank独立控制器，全局统一广播地址与指令，节省大量外设面积，可扩容更多MAC处理单元，提升整体计算密度。
### 2 双HB I/O分层通路
Local I/O：Bank直连PE，低频率、超大并行带宽，适配GEMV/TS-GEMM；Global I/O：跨Bank交错访问，1GHz高频，适配GEMM权重驻留数据流。
### 3 可重构双数据流机制
GEMM采用权重驻留、全局I/O交错访存；GEMV/TS-GEMM采用输入驻留、本地I/O批量读取权重，解决PE利用率低下问题。
### 4 HB-NPU完整芯片架构
DRAM Die搭配8通道16Bank，Logic Die集成镜像128×128 systolic阵列与VPU向量单元，VPU完成激活、Softmax后经全局I/O回写DRAM。

## 实验分析
1. 仿真环境：基于DRAMSim3搭建周期级模拟器，对比NPU、纯DRAM-PIM、NPU+PIM异构系统，测试OPT2.7B/6.7B/13B/66B多模型。
2. 吞吐性能：OPT66B下相较NPU、PIM、异构系统分别提速2.9×、3.5×、2.5×；小批量TS-GEMM场景优势最突出。
3. 面积收益：集中控制器释放的面积可扩充20%以上PE阵列，交错访存将PE频率从500MHz提升至1GHz。
4. 能耗表现：OPT2.7B测试中，能耗分别为DRAM-PIM的1/19、NPU的1/9、异构系统的1/3。
5. 批处理特性：批大小受限的长上下文推理场景，HB-NPU吞吐量衰减远低于三类基线架构。

## 研究启发
1. 3D混合键合近内存芯片无需分布式控制，全局集中广播指令可大幅释放芯片计算面积。
2. LLM两类核心计算(GEMM/GEMV)带宽与频率需求完全相反，分层双I/O是兼顾两者关键设计。
3. TS-GEMM是现有加速器普遍短板，输入驻留数据流搭配本地高带宽通路可显著提升PE利用率。
4. 相比NPU+PIM异构方案，单颗HB一体化芯片硬件成本更低、负载均衡性更好。
5. DRAM时序约束可通过多Bank交错访问规避，有效提升 systolic阵列运行主频与峰值算力。
