---
title: "AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "hardware-accelerator"
  - "zero-knowledge-proof"
  - "poseidon-hash"
  - "merkle-tree"
  - "fpga"
---

# AcclMT: A Highly Resource-Efficient and Flexible Poseidon Hash-Based Merkle Tree Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132911">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132911</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 零知识证明，默克尔树，波塞冬哈希，硬件加速</p>
</div>

---

## 研究概要
本文提出资源高效、可灵活配置的AcclMT架构，面向ZKP场景加速Poseidon哈希默克尔树。软硬件协同设计混合全/半轮哈希引擎，搭配分层片上缓存与分层任务调度。28nm实测哈希吞吐相较FPGA方案提速14.3倍，构建默克尔树相对CPU最高提速1665倍，双哈希引擎平均利用率超95%。

## 背景和动机
1. ZKP协议中Poseidon哈希与默克尔树计算占总开销65%以上，现有硬件加速多聚焦MSM、NTT，哈希树成为性能瓶颈。
2. 现有Poseidon硬件方案专用性强、适配协议单一，模块化乘法器利用率低，大量运算单元闲置，芯片面积浪费严重。
3 完整展开全轮引擎硬件成本高，大有限域场景开销不可接受，未区分全/半轮运算资源需求差异。
4. 大规模默克尔树生成产生海量稀疏中间数据，片上缓存受限，频繁片外访存拖慢速度，哈希流水线气泡多。
5. 多数架构参数固化，无法适配不同arity、轮数、有限域的各类ZKP应用场景，通用性差。

## 相关工作
1. 通用ZKP硬件加速：重点优化NTT、多标量乘法MSM，忽略Poseidon哈希与默克尔树模块。
2. TRIDENT FPGA哈希加速器：面向Filecoin专用，双全轮引擎半轮计算时大量S盒闲置，资源利用率极低。
3. Irreducible硬件方案：针对Plonky2固化设计，全轮展开大域硬件开销爆炸，无分层缓存优化。
4. CPU软件Poseidon库（NEPTUNE/Dusk）：串行计算，构建大树时延极高，无法满足实时证明需求。
5. ZPrize基准方案：仅单独加速哈希单元，未配套完整默克尔树分层调度与缓存管理。

## 本文解决方案
### 1 混合全/半轮Poseidon哈希双引擎
分资源密集全轮引擎、轻量半轮引擎；半轮线程乘法资源仅为全轮一半，调度时分摊大量半轮运算，减少闲置；支持可配置S盒、状态数适配多协议。
### 2 哈希数据流协同调度策略
按批次拆分哈希运算，双引擎并行处理全/半轮，仅产生微小等待开销；相比双全轮基线面积降低14.8%，仅增加7.04%时延。
### 3 分层片上缓存架构
叶子哈希缓冲区、根哈希缓存、分层中间存储HIDM、4KB暂存区，总片上缓存仅200KB，支持最高2²³规模默克尔树。
### 4 分层树任务拆分与聚合调度
将大树拆分为4096标准子树批量流水线；设计主次聚合机制，利用暂存填充流水线气泡，缓解高层数据稀疏导致引擎闲置。
### 5 全参数灵活可配置设计
arity、S盒指数、全/半轮数量、树规模均可运行时配置，兼容Filecoin、Plonky2等主流ZKP系统。

## 实验分析
1. 实验环境：TSMC 28nm工艺，500MHz，256位位宽，对比TRIDENT、NEPTUNE、Dusk软件库。
2. 哈希性能：arity=2时吞吐14.11M哈希/秒，相较同类FPGA提速14.3倍、CPU提速145倍；高arity性能小幅衰减。
3. 硬件开销：哈希引擎占总面积93.7%，缓存仅6.3%；相比双全轮基线面积缩减14.8%，半轮占比越高时延损耗越小。
4. 默克尔树加速：最大规模下相对CPU实现最高1665倍加速，树越大加速比越高，执行时间亚线性增长。
5. 引擎利用率：叶子哈希引擎平均99.2%，根哈希引擎95.9%，远高于优化前不足85%的利用率。

## 研究启发
1. Poseidon哈希全、半轮运算资源需求差异巨大，混合异构引擎是提升乘法器利用率、缩减芯片面积核心思路。
2. 默克尔树高层数据稀疏是流水线气泡主要来源，分层拆分+主次聚合调度可大幅提升硬件吞吐。
3. 无需超大片上存储，分层分级缓存配合子树流水线，仅数百KB即可支撑超大规模证明树构建。
4. ZKP硬件不能单一优化底层算子，必须配套上层树结构调度才能消除算力浪费。
5. 固化专用硬件适配场景窄，运行时可配置架构能兼容多类零知识证明协议，工程实用性更强。