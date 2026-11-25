---
title: "FineRR-ZNS: Enabling Fine-Granularity Read Refreshing for ZNS SSDs"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# FineRR-ZNS: Enabling Fine-Granularity Read Refreshing for ZNS SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://jiemingyin.github.io/docs/DAC2025.pdf">https://jiemingyin.github.io/docs/DAC2025.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>分区命名空间固态硬盘，细粒度读刷新，重映射，重构，副本 </p>
</div>


---

## 研究概要
本文提出FineRR-ZNS细粒度读刷新机制，适配ZNS SSD架构。设计区重映射、区重构两大核心模块，仅对达到读取阈值闪存块执行刷新，规避整区迁移大量有效数据。FEMU仿真基于RocksDB多负载验证，相较基准ZoneRR-ZNS，数据迁移量平均降41.8%、擦除次数减少36.4%、IO吞吐量提升28.2%。

## 背景和动机
1. ZNS SSD依靠主机管理、顺序写入消除片上DRAM与冗余OP空间，但主流ZenFS等文件系统缺少读刷新(RR)机制，无法抵御读干扰导致的数据失效。
2. 现有ZNS整区级读刷新方案，只要区内单块触发刷新，就要迁移全区所有有效块，产生巨额数据拷贝与块擦除开销，严重拖累IO性能。
3. 同一区域内闪存块读取热度差异巨大，多数块远未达到刷新阈值，整区刷新存在大量无意义数据迁移。
4. 传统SSD块级刷新依赖片上映射与OP空间，违背ZNS轻量化设计理念，无法直接移植使用。
5. 缺少细粒度、兼容ZNS顺序写入约束的读刷新方案，平衡数据可靠性与存储IO性能。

## 相关工作
1. 传统SSD读刷新优化（Read Level、强化学习调度等）：基于页级FTL与片上冗余空间，无法适配Z主机托管、仅顺序写的硬件规范。
2. ZNS垃圾回收优化（SplitZNS、WA-Zone）：仅针对空间回收GC，未解决读干扰引发的数据刷新开销。
3. ZenFS基准ZoneRR-ZNS：采用整区级读刷新，实现简单但有效数据迁移、块擦除开销极高。
4. 片内干扰抑制方案：依赖硬件单元改造，无法通过主机文件系统层轻量化实现，部署成本高。
5. 冷热数据分离存储策略：侧重均衡磨损，不能针对性削减读刷新带来的数据拷贝。

## 本文解决方案
### 1 整体主机侧细粒度RR架构
在ZenFS文件系统新增FineRR管理模块，配合SSD控制器块读取计数器；引入判定指标δ，动态选择块级/整区级刷新，仅迁移达到读取阈值闪存块。
### 2 区重映射Zone Remapping模块
块触发刷新时，将该块数据迁移至专用重映射区，维护偏移位图映射关系；读请求优先从重映射区获取副本，未达阈值数据保留原区，避免整区拷贝。
### 3 区重构Zone Reconstruction模块
原区触发GC或整区刷新时，合并原数据与重映射副本，重构连续有序ZNS数据；副本保留复用直至自身块达到刷新阈值，禁止二次重映射减少元数据开销。
### 4 轻量化元数据管理
SSD端仅40KB块读取计数器；主机侧新增少量偏移、区标识元数据，总空间开销仅68KB，计算判定δ仅简单加减，时序损耗可忽略。
### 5 读写协同调度逻辑
读请求先匹配重映射偏移；后台RRWorker仅处理达标块，GCWorker处理普通回收，两类线程解耦减少IO拥塞。

## 实验分析
1. 仿真平台：FEMU模拟器，QLC ZNS SSD配置，测试RocksDB五类典型KV负载，对比NoRR、ZoneRR、理想BlockRR三组基线。
2. 数据迁移：相比ZoneRR，有效数据迁移量平均下降41.8%，性能逼近理想无约束块级刷新。
3. 闪存寿命：块擦除次数平均减少36.4%，显著降低P/E损耗，延长SSD使用寿命。
4. IO吞吐：全负载下吞吐量平均提升28.2%，仅顺序读场景与基准差距极小。
5. 开销评估：SSD侧无额外存储负担，主机元数据开销不足70KB，读写判定逻辑计算耗时可忽略。

## 研究启发
1. ZNS的性能瓶颈并非GC，整区级读刷新带来的过量数据迁移是易被忽视的关键损耗点。
2. 利用块读取热度不均匀特性，分块刷新可大幅削减拷贝，无需修改SSD硬件，仅在主机文件系统实现即可落地。
3. 重映射副本复用机制能延迟二次刷新，进一步降低整体RR触发频次。
4. 细粒度存储管理方案需配套重构逻辑，严格遵守ZNS仅顺序写入的硬性约束。
5. 主机托管式ZNS优化无需依赖片上DRAM/OP，轻量元数据设计是兼顾成本与性能的核心思路。