---
title: "Expanding Logical Space Freely: A Memory-efficient Mapping Table Design for Compressional SSDs"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Expanding Logical Space Freely: A Memory-efficient Mapping Table Design for Compressional SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132583">https://ieeexplore.ieee.org/document/11132583</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>压缩固态硬盘，闪存转换层，缓存管理 </p>
</div>

---

## 研究概要
本文面向内置压缩SSD提出N-to-1高效L2P映射FTL架构，利用同压缩率连续逻辑页合并映射条目消除PPN冗余，设计升降级机制适配动态压缩比，配套分块分配、复用回收与压缩感知GC。MQsim仿真显示映射表内存平均缩减50%，缓存命中率提升，IO延迟相较DFL基准最高提速2.06倍。

## 背景和动机
1. 压缩SSD多逻辑页存入单物理页，传统1对1 L2映射重复存储相同物理页号，映射表体积暴增，挤占片上DRAM缓存。
2. 映射表过大导致缓存缺失频发，频繁读取闪存映射页，IO延迟显著上升，现有FT仅优化缓存策略未解决条目冗余根源。
3. 业务数据压缩比动态变化，固定N合并策略易产生逻辑地址碎片，传统整页分配浪费映射空间。
4. 数据更新改变压缩比，原有合并映射失效，缺少动态切换映射粒度的自适应机制。
5. 压缩SSD存在部分无效物理页，传统GC直接拷贝有效页，回收开销高、空间利用率低。

## 相关工作
1. DFTL系列按需映射方案：采用闪存存储映射、DRAM缓存，仅优化缓存预取，无法消除压缩场景下PPN重复条目，内存开销居高不下。
2. 传统压缩SSD固件：仅优化编解码流水线，未从FTL映射层解决地址表膨胀问题，缓存缺失瓶颈依旧存在。
3. 通用SSD垃圾回收：只判断物理页整体有效性，无法处理压缩带来的局部无效页，拷贝开销大。
4. 局部性感知FT（S-FTL/HCFTL）：基于访问热点优化缓存布局，不支持多逻辑页合并映射，不适配压缩存储架构。
5. 主机端压缩方案：压缩卸载至CPU，无法利用SSD硬件压缩，且不解决片上映射内存瓶颈。

## 本文解决方案
### 1 N-to-1分层映射表架构
全局转换目录GTD新增压缩比、偏移标记，翻译页划分为独立Translation Chunk；支持1/2/4/8多种合并粒度，单个条目承载多连续逻辑页，消除重复PPN存储。
### 2 分块分配与复用回收机制
放弃整翻译页分配，以Chunk为最小单位分配空间；维护各类粒度空闲块链表，升降级产生无效块可复用，减少闪存回写次数，缓解逻辑碎片。
### 3 映射升降级自适应策略
数据更新压缩比降低时执行降级，拆分映射粒度；全部逻辑页压缩比提升则执行升级，合并条目，动态控制映射表内存占用。
### 4 压缩感知GC算法
区分块内有效物理页与有效逻辑页；低有效物理页数量时延迟拷贝、暂存内存，等待后续写入重压缩，减少GC拷贝操作，提升回收效率。

## 实验分析
1. 仿真环境：MQSim模拟器，512GB/1TB压缩SSD，对比DFTL-base、DFTL-prefetch、最优全缓存基线，使用Filebench真实业务负载。
2. 映射内存：相比标准DFL，映射表体积平均降低50%，GTD与标记元数据开销可忽略。
3. 缓存与时延：缓存命中率提升约50%，端到端IO延迟相较DFTL-base提速2.06倍，小缓存256KB场景优势更明显。
4. GC性能：压缩感知GC减少约22%回收操作，大幅降低部分无效页的数据拷贝开销。
5. 扩展性：1TB大容量SSD、多混合负载下仍保持稳定内存缩减与加速效果，架构可横向扩展。

## 研究启发
1. 压缩SSD性能瓶颈不在编解码，而在FTL映射表内存膨胀，需从地址映射层解决PPN冗余。
2. 利用连续逻辑页压缩比局部相似性，多对一合并映射是削减映射内存的核心思路。
3. 映射粒度不能固定，升降级机制可动态适配更新带来的压缩比变化，兼顾空间与地址转换效率。
4. 传统整页GC不适配压缩存储，基于局部有效信息的延迟重压缩GC可显著降低闪存写放大。
5. 翻译页分块细粒度分配能避免逻辑地址碎片，空闲块复用进一步减少映射页闪存刷写。