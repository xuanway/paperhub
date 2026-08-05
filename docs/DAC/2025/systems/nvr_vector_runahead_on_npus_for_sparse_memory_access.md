---
title: "NVR: Vector Runahead on NPUs for Sparse Memory Access"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# NVR: Vector Runahead on NPUs for Sparse Memory Access

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2502.13873">https://arxiv.org/abs/2502.13873</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 向量前瞻预取，稀疏内存访问，NPU加速，缓存缺失优化 </p>
</div>

---

## 研究概要
本文提出NVR面向稀疏DNN NPU的向量前瞻预取硬件机制，采用非侵入解耦架构，复用NPU空闲稀疏单元做前瞻地址推演，配套NSB小缓存。硬件面积开销低于5%，相比主流预取方案缓存缺失平均降低90%，稀疏负载整体加速4倍，同等芯片面积下NS扩容收益远高于L2扩容。

## 背景和动机
1. 大模型稀疏剪枝带来理论算力收益，但非规则间接访存引发大量缓存缺失，NPU单向量缺失阻塞整条SIMD流水线，性能远达不到理论加速比。
2. NPU缺少CPU乱序、GPU多线程延迟隐藏能力，稀疏SpMM、LLM KVCache、MoE等IO密集场景 stall时间占比极高。
3. 现有优化多修改稀疏编码/片上暂存，算法绑定、硬件开销大，通用性差；通用CPU前瞻预取无法适配NPU粗粒度向量指令。
4. 传统步长/间接预取难以捕捉稀疏多层索引依赖链，预测覆盖率低，无法适配点云、图、LLM多类稀疏负载。
5. 单纯扩容L2缓存成本高、收益有限，缺少适配NPU的低成本专用预取微架构。

## 相关工作
1. 稀疏硬件定制：NVDLA位掩码、Eyeriss游程编码、蝴蝶稀疏单元，需修改数据格式，通用性弱、控制逻辑开销大。
2. 通用预取器：流预取、IMP间接预取，仅适配规则访存，稀疏多层索引预测精度不足。
3. CPU向量前瞻VR/DVR：面向CPU细粒度指令，不兼容NPU粗粒度向量运算与稀疏处理单元。
4. 片上存储优化：扩充L2/大容量scratchpad，硬件面积代价高，稀疏离散数据复用率低。
5. 稀疏编译优化：重构访存顺序，依赖编译器改造，无法做到硬件透明通用加速。

## 本文解决方案
### 1 解耦非侵入NVR整体架构
独立于NPU主流水线，通过侦听单元只读采集指令、寄存器状态，不干扰原有计算；复用空闲稀疏单元执行前瞻地址推演，无额外大规模运算单元。
### 2 四大核心检测硬件单元
- SD步长检测器：捕获权重连续访存模式；
- SCD稀疏链检测器：维护索引历史表，预测多层间接IA访存地址；
- LBD循环边界检测器：跟踪嵌套循环，防止预取越界；
- VMIG向量微指令生成器：合并多条预取请求，提升内存并行度。
### 3 向量级前瞻执行流程
检测加载指令触发前瞻，并行推演多条稀疏索引依赖链，批量生成向量预取指令提前填充L1/L2缓存。
### 4 NS非阻塞专用小缓存（可选）
高相联度16KB片上缓存，配套MSHR合并同地址请求，进一步削减片外访问，与NVR协同优化带宽。
### 5 低开销硬件实现
TSMC 28nm综合，无NSB面积开销3%，带NSB仅4.6%，适配Gemmini通用NPU架构，无需修改编译器与网络算法。

## 实验分析
1. 仿真平台：ScaleSim+LLMCompass，基线为顺序/理想乱序Gemmini，对比流预取、IMP、DVR；负载覆盖LLM、图网络、点云、MoE稀疏任务。
2. 缓存与带宽：缓存缺失平均降低90%，片外访存总量减少75%；搭配NS可再降80%片外访问。
3. 性能加速：纯NVR稀疏负载平均4倍提速；LLM解码IO密集阶段吞吐量提升50%。
4. 缓存对比：同等硬件面积下扩容NS性能增益是扩容L2缓存的5倍。
5. 消融实验：SD/SCD/LBD任一模块移除，预取覆盖率大幅下滑；INT8/FP1/INT32多精度下优化效果稳定。

## 研究启发
1. 稀疏NPU性能瓶颈不在计算单元，而不规则间接访存阻塞流水线，前瞻预取是通用硬件级解法，无需修改稀疏算法。
2. NPU自带稀疏处理单元存在大量空闲周期，复用做前瞻推演可零新增算力开销，是低面积优化关键思路。
3 专用小缓存NS相比盲目扩容L2更具性价比，离散稀疏数据更适配高相联小规模片上存储。
4. 传统CPU前瞻机制不能直接移植，必须拆解NPU粗粒度向量指令至微指令层级做批量预取。
5. 微架构优化优先复用现有硬件资源，新增独立逻辑会带来不可接受的面积、功耗成本。
