---
title: "A Data-Centric Hardware Accelerator for Efficient Adaptive Radix Tree"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# A Data-Centric Hardware Accelerator for Efficient Adaptive Radix Tree

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132959">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132959</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>自适应基数树，硬件加速器，以数据为中心的处理，FPGA</p>
</div>


---

## 研究概要
本文面向自适应基数树（ART）并发读写存在冗余遍历、锁同步开销大的痛点，提出以数据为中心的FPGA加速器DCART。设计CTT处理模型，通过前缀合并操作、捷径缓存、价值感知片上缓存削减开销。基于Alveo U280实现，相较CPU/GPU主流ART方案提速21.1–44.2倍，能效提升71.1–148.9倍。

## 背景和动机
1. ART广泛用于KV存储与数据库，但CPU/GPU并发执行时存在两大核心瓶颈：大量重复树遍历、节点锁同步耗时占比最高超70%。
2. 真实负载存在时空局部性：大量操作访问同一子树、仅少量节点被高频访问，现有按操作串行处理架构无法复用遍历结果。
3. 传统架构逐键独立遍历，缓存行有效数据占比不足20%，内存带宽利用率极低；CAS原子锁在内存访问时延迟放大15倍以上。
4. 纯软件合并操作、维护捷径表运行开销过高，需专用硬件流水线消除调度损耗。

## 相关工作
1. 软件ART优化（ART/Heart/SMART）：采用CAS、分层锁降低冲突，但仍逐键遍历，冗余访问无法消除，写负载性能暴跌。
2. GPU加速CuART：将ART遍历卸载至GPU，但未利用访问局部性，锁竞争与重复遍历问题依然存在。
3. 分布式基数树DART、持久内存ART：侧重存储介质与分布式扩展，未从硬件层解决并发遍历冗余。
4. 通用索引FPGA加速器：面向哈希/B+树，无适配ART前缀合并、捷径复用的专用流水线。

## 本文解决方案
### 1. 数据驱动CTT处理模型
摒弃单操作串行模式，按键前缀聚合访问同一节点的请求，一次树遍历批量处理多操作，天然减少锁争抢；遍历结果生成捷径缓存供后续请求复用。
### 2. 三层硬件流水线架构
- PC前缀合并单元：流水线扫描键、提取前缀，将同前缀操作归入同一桶，消除跨单元锁竞争；
- 分发器：桶任务均衡分配至多SOU处理单元；
- SOU捷径运算单元：先检索捷径表，无捷径才自上而下遍历，遍历后自动生成缓存捷径。
### 3. 片上分层价值感知缓存
划分扫描、桶、捷径、树四类BRAM缓存；树缓存采用热度淘汰策略，高频高价值节点常驻片上，避免颠簸，提升局部性。
### 4. 流水线重叠隐藏开销
PC合并流水线与SOU处理流水线并行执行，批次间重叠掩盖操作聚合的额外延时。

## 实验分析
1. 实验平台：Xilinx Alveo U280 FPGA（230MHz），对比Xeon CPU、A10 GPU上ART/SMART/CuART；测试IPGEO/DICT/EA等真实与合成负载。
2. 冲突削减：锁冲突数量仅为基线3.2%–19.7%，部分键匹配操作降低94%以上。
3. 吞吐延迟：相比CPU SMART提速35.9–44.2倍，相比GPU CuART提速21.1–31.2倍，P99延迟大幅降低。
4. 能效优势：能耗相较SMART降低92.7–148.9倍，相较CuART降低71.1–126.2倍。
5. 敏感性测试：写占比越高、并发请求越多，DCART优化收益越显著。

## 研究启发
1. 索引加速不能仅优化单步遍历算子，需利用负载时空局部性，从请求聚合层面消除重复访存与同步开销。
2. 以数据为中心的批量处理范式，相比传统单操作流水线，更适配树索引不规则访存特征。
3. 硬件流水线可掩盖请求合并、捷径维护的软件开销，是挖掘索引局部性的可行落地路线。
4. 片上缓存不能统一LRU，针对索引节点访问热度定制淘汰策略，可大幅减少片外DRAM交互。
5. 树索引并发瓶颈核心是节点锁竞争，同前缀请求硬件聚合可从根源减少锁获取次数。
