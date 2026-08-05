---
title: "HIVE: A High-Priority Victim Cache for Accelerating GPU Memory Accesses"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# HIVE: A High-Priority Victim Cache for Accelerating GPU Memory Accesses

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133338">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133338</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 高优先级牺牲缓存，GPU内存访问加速，缓存压缩，寄存器文件复用</p>
</div>


---

## 研究概要
本文提出HIVE高优先级受害者缓存架构，改变传统后置缓存逻辑，访存请求优先查询受害者缓存再访问L1D。复用空闲寄存器做缓存数据区，搭配BDI压缩与新型替换策略。仿真显示相较基线IPC提升77.1%，对比SOTA Linebacker提升21.7%，片上硬件开销仅3.1%。

## 背景和动机
1. GPU多Warp并发引发严重L1D缓存冲突，大量驱逐缓存行具备高复用率，传统CPU式后置受害者缓存利用率极低。
2. GPU L1D与共享内存统一架构导致命中延迟高，传统受害者缓存叠加L1访问时延，对延迟敏感程序性能损耗显著。
3. 现有Linebacker等方案仅复用闲置寄存器，但仍采用L1缺失后才查询的后置架构，无法削减基础访存延迟。
4. 片上寄存器资源大量闲置，但缺少机制高效转化为缓存扩充容量，片外L2/DRAM流量居高不下、功耗高。
5. 驱逐缓存行尺寸多样，标准LRU替换易有效数据被挤走，受害者缓存有效容量进一步受限。

## 相关工作
1. 传统CPU受害者缓存：L1缺失后才查询，不匹配GPU高缺失、高驱逐复用、高L1延迟场景。
2. Linebacker：复用空闲寄存器作受害者缓存，但沿用后置查询架构，存在叠加访存延迟缺陷。
3. GPU寄存器压缩方案：仅压缩寄存器数据，未结合受害者缓存扩充片上存储。
4. BDI数据压缩：片上缓存压缩算法，本文将其适配受害者缓存提升等效容量。
5. GPU缓存冲突优化（Warp调度、聚合Tag）：仅缓解L1内部竞争，无法利用驱逐数据局部性。

## 本文解决方案
### 1 高优先级前置访存流水线
新增Tag探测阶段，所有访存请求先查询受害者VTA标签阵列，命中直接从寄存器VDA读取，缺失才进入原有L1D流程，消除L1叠加访问延迟。
### 2 寄存器复用数据区VDA
复用1024个闲置128B Warp寄存器作为受害者缓存数据区，无需新增大容量存储硬件，硬件开销极低。
### 3 BDI轻量压缩扩容
驱逐缓存行经BDI并行压缩后存入VDA，低压缩/解压缩延迟不影响时延敏感负载，大幅提升缓存等效容量。
### 4 优化VTA替换策略
基于子条目空间约束优先不驱逐有效压缩块，无空闲位时才执行LRU，减少有效缓存行替换次数。
### 5 配套硬件控制器
设置索引逻辑+分队列访存控制器，缓冲并发请求避免流水线阻塞；配套压缩/解压缩缓冲维持吞吐。

## 实验分析
1. 仿真环境：AccelSim周期模拟器，Turing类GPU配置，Rodinia等10类GPU负载，对比基线BL、Linebacker、HIVE基础版、完整版。
2. 性能：完整HIVE相比基线IPC平均提升77.1%，最高240%；相对Linebacker提升21.7%。
3. 缓存与流量：受害者缓存平均命中率44.2%，L2流量减少51.7%、片外访存降低20%。
4. 功耗与开销：硬件存储总开销仅10.75KB（占SM 3.1%）；比基线省电17.4%，仅比Linebacker多9.4%功耗。
5. 扩展性：L1/共享统一内存96~256KB多规格下，HIVE性能提升始终显著优于对比方案。

## 研究启发
1. GPU缓存优化不能照搬CPU后置受害者缓存思路，前置高优先级查询是降低基础访存延迟的核心创新点。
2. 片上闲置寄存器是低成本扩充缓存的天然资源，结合轻量压缩可大幅提升有效缓存容量。
3. 替换策略需适配压缩后可变块尺寸，单纯LRU会浪费压缩带来的容量收益。
4. 访存流水线微小改动（新增Tag探测阶段）即可充分利用驱逐数据局部性，显著削减高价片外访问。
5. 面向GPU的存储架构优化需同时兼顾延迟、容量、硬件开销三者做协同设计。
