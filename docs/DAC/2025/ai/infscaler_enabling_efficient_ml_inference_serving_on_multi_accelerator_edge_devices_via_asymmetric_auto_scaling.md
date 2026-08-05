---
title: "InfScaler: Enabling Efficient ML Inference Serving on Multi-Accelerator Edge Devices via Asymmetric Auto-Scaling"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# InfScaler: Enabling Efficient ML Inference Serving on Multi-Accelerator Edge Devices via Asymmetric Auto-Scaling

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://www.liborui.cn/publication/23-dac25-infscaler/23-DAC25-InfScaler.pdf">https://www.liborui.cn/publication/23-dac25-infscaler/23-DAC25-InfScaler.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 边缘推理服务，非对称自动缩放，瓶颈感知，张量共享 </p>
</div>

---

## 研究概要
本文提出InfScaler异构多加速器边缘推理服务框架，针对传统全实例对称扩容内存受限问题。设计瓶颈感知非对称自动扩容算法，结合边缘硬件统一内存实现跨加速器无拷贝张量共享。在Jetson Xavier测试，相较主流方案吞吐量最高提升126.59%，内存占用降低27.32%，且满足延迟约束。

## 背景和动机
1. 现代边缘SoC集成CPU/GPU/NPU多异构加速器，但云端对称全实例扩容方案需完整复制模型，边缘内存不足以支撑突发请求。
2. 神经网络算子计算量差异大，存在固有计算瓶颈层，统一扩容会造成大量硬件资源闲置浪费。
3. 现有推理框架将各加速器视作独立外设，未利用边缘硬件统一共享内存的特性，张量传输拷贝开销高。
4. 模型剪枝、量化优化需修改/重训模型，存在精度损失与额外训练成本。
5. 现有零拷贝共享方案无法适配多生产者多消费者、跨异构加速器的数据流转场景。

## 相关工作
1. 云端推理框架（Knative、KServe）：采用完整实例横向扩容，不适配边缘内存约束，无算子级细粒度调度。
2. INFless、SPRIGHT：依靠批处理、基础零拷贝优化，仅支持全局对称扩容，无法针对性扩容瓶颈算子。
3. 模型压缩类工作（量化/剪枝）：需改动模型结构，存在精度衰减、训练开销大的缺陷。
4. 模型拆分推理：仅固定分层部署，无法随请求负载动态调整各分片并行度。
5. 通用零拷贝内存方案：不支持多生产者多消费者、跨异构加速器的事件驱动数据同步。

## 本文解决方案
### 1 瓶颈感知离线模型划分
离线剖算子FLOPs与时延，以分片计算量方差最小为优化目标，约束分片通信开销与整体SLO，将网络切分为若干独立算子分片；仅计算量高于均值的算子参与分片优化。
### 2 非对称在线自动扩容策略
负载触发时延不达标时，优先对瓶颈指标最高分片扩容；依据算子硬件亲和性选择CPU/GPU/NPU部署，各分片拥有独立并行份数，实现细粒度资源分配。
### 3 跨加速器无拷贝张量共享
依托边缘统一内存，设计eBPF事件驱动令牌机制，解决多生产者多消费者数据竞争；采用惰性内存分配，仅在内存不足时申请新缓冲区，降低内存占用。
### 4 完整离线+在线双阶段系统
离线完成剖分、亲和性采集、扩容参数预计算；在线接收请求，动态调整分片并行度，调度跨加速器张量流转，对用户透明、无需修改原始模型。

## 实验分析
1. 实验环境：NVIDIA Xavier AGX边缘开发板；基线Knative、INFless、SPRIGHT；测试5类工业AI流水线，复现Azure真实请求负载。
2. 吞吐量收益：对比Knative最高提升126.59%，对比SPRIGHT平均提升34.78%，高负载SLO场景增益更显著。
3. 内存优化：内存占用下降10.49%~27.32%，同类基线无法完成高负载视频理解任务，InfScaler可满足延迟要求。
4. 共享开销：eBPF事件驱动控制流，张量拷贝延迟低于1ms，相比轮询式零拷贝大幅减少内存访问次数。
5. 消融结论：非对称扩容是核心增益，张量共享机制消除分片通信带来的性能损耗，二者协同效果最优。

## 研究启发
1. 边缘设备内存稀缺，放弃全实例对称扩容、针对瓶颈算子细粒度分片扩容，是提升资源利用率核心思路。
2. 边缘异构SoC统一硬件内存是独特优化抓手，可构建跨加速器零拷贝共享，大幅消除张量传输开销。
3. 神经网络各层算力不均衡，仅扩容瓶颈分片即可大幅提升吞吐，均衡分片计算量可减少扩容冗余。
4. 传统轮询共享不适合边缘低负载场景，eBPF事件驱动令牌机制能有效解决多生产者数据竞争。
5. 推理优化可分为离线剖分与在线动态调度两阶段，离线预计算降低在线调度开销，兼顾性能与实时性。
