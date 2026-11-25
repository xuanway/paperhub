---
title: "VISTA: Optimizing GPU Scheduling through Versatile Locality-Aware Data Sharing"
description: "DAC 2025 · AI"
tags:
  - "DAC2025"
  - "AI"
---

# VISTA: Optimizing GPU Scheduling through Versatile Locality-Aware Data Sharing

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">AI2: AI/ML Application and Infrastructure</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133076">https://ieeexplore.ieee.org/document/11133076</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>  GPU，内存访问，能效，性能，数据共享，调度 </p>
</div>


---

## 研究概要
本文提出VISTA感知GPU调度器，同时挖掘SM间、SM内非相邻CTA/Warp数据共享。设计两级定位追踪器：ISVM轻量模型预测Warp局部性、LSH匹配CTA访存特征。在内存密集型负载验证，相比基线IPC提升48.1%、内存能耗降低51.8%，硬件面积开销不足3%。

## 背景和动机
1. 内存密集GPGPU程序存在大量跨SM、SM内非相邻线程数据共享，现有调度仅利用相邻CTA/Warp局部性，大量复用机会被浪费。
2. 传统轮询/局部调度将邻近块绑定同一SM，忽略远距离线程间访存重合，L1/L2缓存频繁失效、内存带宽拥堵。
3. 跨SM静态资源分配难以匹配动态访存特征，SM负载失衡，片上缓存复用率低，访存阻塞拖慢整体吞吐。
4. 缺少统一CTA全局分配+Warp片内调度协同方案，单一层级优化收益有限。
5. 现有访存预测模型硬件开销大，难以集成到GPU调度流水线。

## 相关工作
1. 片内Warp局部调度(CCWS)：仅优先邻近Warp，不处理跨SM CTA共享，缓存提升幅度有限。
2. 跨SM协同调度(CCDS)：只优化CTA块分配，未对SM内Warp执行优先级做动态调整。
3. 编译级局部优化：依赖静态代码分析，不规则动态访存场景预测精度差。
4. 缓存旁路/片上共享优化：属于存储层改造，未从调度源头减少冗余访存。
5. ML访存预测：多采用复杂网络，硬件存储/逻辑开销过高，不适合实时GPU调度。

## 本文解决方案
### 1 双层协同调度整体架构
全局CTA调度器+各SM独立Warp调度器，分别追踪跨SM、片内访存局部性，联动匹配高共享计算单元。
### 2 基于ISVM的Warp局部追踪器
记录近16条访存PC哈希特征，训练轻量整数SVM计算局部得分；优先调度高分Warp，提取16bit SM访存特征向量用于CTA匹配。
### 3 LSH驱动CTA匹配分配器
空闲子核执行少量采样访存，生成CTA16bit特征；通过哈希相似度匹配，将CTA分配至特征最接近、负载最低的SM。
### 4 低开销硬件逻辑设计
哈希、计分存储单元容量极小，单次特征计算仅数周期，总面积开销<3%、功耗<2%，不破坏原有GPU流水线。
### 5 动态负载平衡策略
多SM特征相似度相同时，选择活跃线程更少的SM，避免局部SM过载，均衡全芯片缓存压力。

## 实验分析
1. 实验环境：Volta V100仿真平台，Accel-Sim/Accel-Wattch，Rodinia、GraphBench等多套内存密集基准。
2. 性能收益：相比基线IPC提升48.1%，L1/L2缓存命中率分别提升53.9%、48.7%，内存阻塞减少50.4%。
3. 能耗表现：整体内存能耗下降51.8%，优于CCDS、CCWS等SOTA调度方案。
4. 消融实验：CTA+Warp两级协同收益远高于单一层优化，非相邻线程占比越高的图计算类程序增益越大。
5. 硬件开销：追踪器总面积小于GPU总3%，静态功耗仅9.1W，特征计算单级延迟不超过12周期。

## 研究启发
1. GPU数据共享不只存在邻近线程，非相邻CTA/Warp存在大量可复用访存，双层调度才能充分挖掘。
2. 轻量哈希+简单机器学习模型可在极低硬件开销下精准预测访存局部性，适合实时调度。
3. CTA全局分配与SM内Warp优先级必须协同优化，单一维度无法彻底缓解缓存颠簸。
4. 图、稀疏计算等内存密集负载对感知调度增益最显著，是调度优化重点场景。
5. 访存特征可用短哈希向量高效表征，无需完整指令历史，大幅降低存储与计算开销。
