---
title: "MiniWear: Minimizing Flash Wear via Hybrid Persistent Cache for Extended EF-SMR Lifetime"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MiniWear: Minimizing Flash Wear via Hybrid Persistent Cache for Extended EF-SMR Lifetime

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132092">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132092</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 寿命，嵌入式闪存，叠瓦式磁记录，缓存管理 </p>
</div>

---

## 研究概要
本文面向嵌入式闪存+SMR混合存储(EF-SMR)闪存磨损严重、寿命短问题，提出MiniWear混合持久缓存协同方案。划分Flash-PC与SMR-PC两级缓存，配套细粒度回收与主动均衡调度。多负载测试最高降低闪存擦除66.67%，同时削减写放大、降低IO响应延迟，兼顾寿命与读写性能。

## 背景和动机
1. EF-SMR仅用嵌入式闪存作单一缓存，闪存容量仅整机1%，所有随机写全部涌入闪存，频繁GC带来大量块擦除，TLC闪存P/E循环上限极易触达，设备寿命大幅缩短。
2. SMR磁盘原生RMW操作引发写放大、长尾延迟，现有优化仅聚焦时延，未解决闪存耐久核心痛点。
3. 直接扩大闪存会显著提升硬件成本，无法兼顾高密度低成本存储需求。
4. 现有缓存策略无分层介质分流机制，闪存写压力无法向外转移，僵尸闲置闪存块加剧GC频率。
5. 缺乏软硬件协同混合缓存架构，无法在不牺牲IO性能前提下分摊闪存写入负载。

## 相关工作
1. Skylight、PORE：纯闪存缓存EF-SMR方案，仅优化GC范围与时延，无法缓解闪存整体磨损压力。
2. MCM、Duchy：冷热数据分离、写过滤策略，仅在闪存内部做数据区分，不能向外分流写入流量。
3. SMR磁盘缓存优化(ROCO/HS-BAS)：采用外置SSD缓存，非片上嵌入式EF-SMR架构，落地成本高。
4. 强化学习调度MAID-Q：仅降低长尾延迟，未针对闪存磨损、寿命做专项优化。
5. 传统SMR文件系统：聚焦RMW开销削减，未利用磁盘轨道构建二级持久缓存分担闪存压力。

## 本文解决方案
### 1 混合持久缓存硬件架构
将系统缓存拆分为Flash-PC（嵌入式闪存块）、SMR-PC（磁盘外圈专用轨道）两类介质，各占总容量1%；SMR-PC采用追加写入模式，规避普通Band的RMW开销，分流随机写。
### 2 混合页级地址映射
设计页映射表、双优先级队列、分带分叉链表，区分逻辑页归属Flash/SMR/普通Band，快速检索空闲缓存资源，降低元数据开销。
### 3 细粒度缓存分配与三级回收
分配优先使用Flash-PC，不足时启用SMR-PC；回收分为无效块快速回收、带局部回收、全带回收，最小化单次闪存擦除数量。
### 4 主动均衡调度机制
定义带热度指标T，被动GC达阈值时主动回收低热度带闲置僵尸闪存块，释放可用Flash-PC，减少GC触发频次。
### 5 软硬件协同控制器
缓存管理器统一完成映射查询、资源分配、均衡回收，算法时间复杂度O(n)，元数据内存开销可控。

## 实验分析
1. 对比基线：Skylight、PORE、MCM、Duchy，采用8类标准存储轨迹，2TB EF-SMR仿真平台。
2. 闪存磨损：相较各基线平均磨损降低20%~35%，web负载最高减少66.67%擦除次数，闪存容量越稀缺优化优势越明显。
3. IO性能：平均响应时延大幅下降，长尾高延迟请求占比显著降低；仅读密集负载因均衡机制出现轻微时延波动。
4. 写放大：实际写入总数据量远低于基线，相比Skylight减少74%写入量，大幅削减磁盘RMW操作。
5. 资源开销：映射、队列、链表总内存开销不足45MiB，调度算法计算负载极低，不影响控制器实时处理。

## 研究启发
1. EF-SMR闪存磨损根源是单一介质承载全部随机写，复用SMR外圈轨道构建二级缓存是低成本延寿核心思路。
2. 缓存回收不能一刀切全带刷新，分层细粒度回收可大幅减少闪存块擦除操作，直接延长耐久寿命。
3. 闲置僵尸闪存块会加剧GC压力，主动热度均衡调度能持续释放空闲缓存，从源头减少擦除触发。
4. SMR外圈轨道具备媲美闪存的随机写能力，追加写入模式可规避普通Band的RMW缺陷，适合作为二级持久缓存。
5. 存储优化不能只关注时延，介质分层分流、磨损均衡是高密度低成本SMR存储落地的关键设计目标。
