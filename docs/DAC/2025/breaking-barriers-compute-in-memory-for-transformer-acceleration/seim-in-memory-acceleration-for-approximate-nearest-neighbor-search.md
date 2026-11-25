---
title: "SeIM: In-Memory Acceleration for Approximate Nearest Neighbor Search"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# SeIM: In-Memory Acceleration for Approximate Nearest Neighbor Search

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132620">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132620</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存内处理，双列直插式内存模块，近似最近邻搜索 </p>
</div>

---

## 研究概要
本文提出分层存内加速架构SeIM，面向IVF-PQ量化近似近邻检索。区分访存密集向量/查表运算、计算密集排序任务，分别在DRAM Bank与内存控制器部署专用单元，配套统一执行模型与自适应传输过滤。十亿级向量测试，相较CPU/GPU/ASIC吞吐最高提升268倍、时延降低306倍、能效提升3081倍。

## 背景和动机
1. RAG、推荐系统广泛使用ANNS，主流IVF-PQ包含聚类过滤、距离表构建、压缩扫描三阶段，向量查表访存密集，Top-K排序计算瓶颈突出。
2. CPU/GPU存在巨大片内外向量搬运开销，传统GEMV型PIM仅支持矩阵乘，无查表计算硬件，无法完整覆盖ANNS全流程。
3 单一层次PIM难以适配混合计算特征：向量/查表高度并行访存受限，排序需全局结果聚合，不适合Bank级并行。
4. 海量无效距离数据传输至控制器参与排序，带来额外带宽与延时损耗，现有加速器缺少传输过滤机制。

## 相关工作
1. CPU/GPU ANNS方案（FAISS）：冯诺依曼架构数据搬运瓶颈严重，十亿向量场景吞吐、能效极低。
2. ANNA专用ASIC加速器：纯片上设计内存容量受限，扩展性差，性能远不及存内方案。
3. 通用DRAM PIM（Newton/Trim）：仅优化GEMV向量乘，未设计查表计算单元，无法适配PQ压缩检索。
4. 其他存内架构：未分层区分访存/计算型任务，缺少统一执行模型，硬件复用率低。

## 本文解决方案
### 1 分层异构PIM整体架构
Bank级部署ANNS处理单元APU，并行执行向量计算、查表运算；内存控制器集成硬件优先队列，统一处理全局Top-K排序，仅轻量改造标准DDR5 DIMM。
### 2 统一Bank执行模型
质心、码本、压缩向量分Tile均衡分配至各Bank，子块分块遍历复用运算通路，硬件单元高度复用，平衡各Bank负载。
### 3 APU专用计算通路
内置距离表多级缓存，同时支持L2/内积两种距离，集成向量运算、查表两套计算流水线，适配IVF-PQ全阶段。
### 4 自适应传输过滤机制
控制器定期下发当前Top-K最大距离阈值，AP直接丢弃超出阈值的无效距离，大幅削减跨Bank传输的数据量。
### 5 异构编程模型
类CUDA抽象PIM内核，数据自动映射至对应Bank Tile，降低上层检索开发成本。

## 实验分析
1. 实验平台：Ramulator周期仿真器，32nm综合APU/控制器，测试Sift/Gist/Deep/TTI百万/十亿向量数据集。
2. 吞吐对比：相较CPU/GPU/ANNA分别提速268×、22×、5×；自适应过滤单独带来近2倍吞吐增益。
3. 时延指标：相比CPU降低306倍、GPU降低59倍、ASIC降低4倍，十亿向量仍保持毫秒级查询。
4. 能效表现：相较CPU提升3081倍、GPU提升287倍、ANNA提升2倍，硬件面积功耗开销极低。
5. 硬件开销：单DIMM新增单元面积0.447mm²、功耗394mW，控制器额外开销可控，兼容商用DRAM。

## 研究启发
1. ANNS存在两类完全不同计算负载，分层存内架构是兼顾并行访存与全局聚合的最优路线。
2. 仅优化矩阵乘的通用PIM无法适配量化检索，必须新增查表专用硬件通路。
3. 海量中间距离存在大量无效值，前置过滤能显著缓解内存控制器传输瓶颈。
4. 统一Tile分块布局可均衡多Bank负载，最大化DRAM内部原生并行带宽。
5. 面向检索的PIM无需大规模硬件改动，基于标准DIMM轻量化改造具备落地可行性。
