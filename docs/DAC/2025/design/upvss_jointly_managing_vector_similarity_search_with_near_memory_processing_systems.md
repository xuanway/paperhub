---
title: "UPVSS: Jointly Managing Vector Similarity Search with Near-Memory Processing Systems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# UPVSS: Jointly Managing Vector Similarity Search with Near-Memory Processing Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132577">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132577</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 向量相似性搜索，大语言模型，倒排文件，K近邻，存内处理，硬件/软件协同设计，并行性</p>
</div>

---

## 研究概要
本文提出UPVSS面向商用UPMEM近存处理系统优化IVF向量检索，设计DPU感知聚类划分与协同调度器。均衡分发向量规避DPU内存溢出，就近卸载距离计算削减主机带宽开销，配套WRAM多级缓存充分利用DPU多线程流水线。千万级高维向量测试，相较FAISS平均提速1.95倍，有效缓解冯诺依曼访存瓶颈。

## 背景和动机
1. 传统CPU运行FAISS-IVF向量检索属于访存受限负载，向量复用率极低，多线程下DRAM带宽快速打满，性能增长停滞。
2. 商用UPMEM NMP单DPU仅64MB本地内存，原生部署IVF会出现簇向量超限OOM，且DPU间无法直连，向量迁移开销巨大。
3. DPU流水线需至少11并发线程才能满负载，原生检索流程单线程执行，硬件并行资源严重浪费。
4. 现有UPMEM相关工作仅面向数据库、基因序列，缺少针对高维ANN检索的软硬件协同优化方案。

## 相关工作
1. 传统CPU向量库（FAISS）：基于AVX多线程优化，但共享内存总线存在带宽天花板，高维向量场景扩展性差。
2. 模拟存内TC/RRAM加速器：依赖大量ADC/DAC，面积能耗成本高，难以商用落地。
3. UPMEM通用处理研究：仅实现数据库连接、基因比对，未适配IVF倒排索引检索逻辑。
4. 通用NMP调度算法：未针对IVF分簇特性做均衡数据划分，易出现DPU负载不均、内存溢出。

## 本文解决方案
### 1 DPU感知均衡聚类划分
构建IVF倒排索引后，将每个簇内向量均等切分，每份子集分发至不同DPU；每个DPU存储所有簇的部分向量，查询时全部DPU同步参与计算，无闲置硬件，彻底解决单DPU向量溢出问题。
### 2 主机-DPU协同检索调度器
查询向量+待检索簇ID广播至全部DPU，将高开销向量距离计算卸载至DPU；仅小规模<ID,距离>键值对传回主机合并Top-K，大幅减少主机-DPU数据传输量。
### 3 DPU片上WRAM分层缓存机制
WRAM划分查询缓存、向量缓存、结果键值缓存；每个任务线程独立持有向量缓冲区，2KB固定分片批量写回MRAM，降低片内数据搬运。
### 4 多线程流水线适配调度
自动拆分向量至DPU内24个tasklet，保证并发线程≥11，填满14级流水线，充分释放DPU内部1GB/s带宽优势。

## 实验分析
1. 实验平台：双Xeon主机+8片UPMEM DIMM共1024个DPU，测试S/D系列2048~4096维百万向量数据集，基线为64线程FAISS。
2. 整体性能：UPVSS检索耗时降低30%~46%，平均加速1.95倍；nlist越小、单簇向量越多，加速比最高达2.62倍。
3. 并行扩展性：性能随DPU数量线性提升，单DPU内12线程达到性能饱和，匹配硬件流水线约束。
4. 带宽收益：大量向量计算在DPU本地完成，主机侧DRAM带宽占用大幅下降，消除带宽饱和瓶颈。
5. 负载均衡：均衡划分策略使所有DPU计算负载差异低于5%，无闲置计算单元。

## 研究启发
1. 商用数字近存UPMEM无需改造存储硬件，通过索引数据重分配即可适配高维ANN检索。
2. 向量检索瓶颈是主机与内存间大向量传输，将距离计算就近卸载、只回传精简距离对是核心优化思路。
3. NMP优化必须贴合硬件限制（单DPU内存、线程下限、无直连通信），单纯移植CPU算法会出现严重性能退化。
4. IVF倒排索引不能整簇绑定单一处理单元，跨DPU均匀分片可实现全硬件并行、规避内存溢出。
5. 片上高速SRAM(WRAM)分层缓存可降低慢速MRAM读写频次，充分挖掘DPU内部高带宽优势。
