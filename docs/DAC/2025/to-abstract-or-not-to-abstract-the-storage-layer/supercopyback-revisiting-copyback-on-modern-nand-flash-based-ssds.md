---
title: "SuperCopyback: Revisiting Copyback on Modern NAND Flash-based SSDs"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# SuperCopyback: Revisiting Copyback on Modern NAND Flash-based SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133348">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133348</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> NAND闪存，固态硬盘，回拷</p>
</div>


---

## 研究概要
本文提出SuperCopyback，解决现代子页、超页、RAIN架构下传统Copyback失效问题。设计轻量硬件MROW实现子页级拷贝回收，配套协同GC调度与重布局RAIN机制。MQSim仿真显示，相较标准GC平均吞吐量提升26.3%，99分位尾延迟降低28.4%，性能接近1ns理想数据迁移场景。

## 背景和动机
1. NAND块仅顺序写入，GC需迁移大量有效页，片外数据传输带来严重时延、写放大与QoS抖动。
2. 原生Copyback仅支持整页迁移，现代SSD采用4KB子页/16KB物理页架构，单页内混合有效/无效子页时无法复用拷贝。
3. 企业SSD跨片RAIN校验需读取条带全部数据做异或，Copyback仅片内传输、无法读出页面，导致可靠性机制失效。
4. 现有FastGC等拷贝方案仅适配传统整页SSD，不兼容超页并行、子页映射架构，无法解决两大核心冲突。
5. 传统RAIN奇偶与数据同超页存储，拷贝执行会阻塞奇偶写入，进一步放大GC阻塞时延。

## 相关工作
1. 传统Copyback优化（FastGC、rcFTL）：阈值限制拷贝次数规避ECC失效，但仅支持整页，无子页合并能力。
2. 互连通道SSD（DecoupledSSD、Venice）：新增片间互联减少通道争抢，硬件改动大，无法消除GC片外传输开销。
3. SOML子页读：支持平面跨页读取，但块解码器限制，不能用于GC数据迁移场景。
4. 超页/子页管理方案：仅优化分配与读写并行，未改造GC数据迁移链路。
5. RAIN容错机制：默认奇偶与数据同超页布局，未适配Copyback无片外读取的运行约束。

## 本文解决方案
### 1 轻量硬件MROW子页拷贝
改造平面双锁存器电路，增加少量晶体管实现子页级寄存器互传；两次分阶段读取不同页面有效子页，合并为完整页面再编程，支持混合有效页GC迁移。
### 2 协同贪心GC调度机制
按4bit有效性位图分组页面，优先互补子页组合减少页面读出；设置拷贝次数阈值防止ECC累积失效，限制单芯片连续拷贝上限平衡各块负载。
### 3 适配拷贝的RAIN存储架构
奇偶页统一后置至块末尾，DRAM临时缓存奇偶数据延迟写入；页面读出操作掩藏在页编程长延迟内，不阻塞拷贝流水线。
### 4 低系统开销设计
硬件仅新增少量开关晶体管；DRAM位图、奇偶缓冲区总开销可控制在百MB内，断电可重新生成无需持久存储。
### 5 完整SSD固件流水线
前端FTL地址映射、GC单元、后端NAND芯片三层协同，兼容NVMe标准，无需修改主机接口。

## 实验分析
1. 仿真平台：扩展MQSim搭建TLC企业SSD，基线为标准超页GC、带片上缓存GC；负载含合成随机写、阿里云真实云盘轨迹。
2. 吞吐性能：SuperCopyback平均IOPS提升26.3%，最高达34.6%，性能达到理想1ns迁移方案的96.9%。
3. 时延指标：平均响应时间下降20.9%，99%尾延迟平均降低28.4%，大幅改善业务QoS。
4. 写放大：与基线基本持平，不会缩短闪存使用寿命。
5. 阈值消融：拷贝阈值≥6即可收获绝大部分收益，过低会频繁切回普通GC削弱加速效果。

## 研究启发
1. Copyback的性能潜力在子页、RAIN现代架构下被完全封锁，需硬件微改造才能适配新一代SSD存储管理模式。
2. 利用闪存固有双锁存器增加少量逻辑，即可低成本实现子页合并，无需大幅改动NAND底层电路。
3. 可靠性RAIN与GC拷贝并非互斥，只需调整奇偶存储布局并利用编程长延迟掩藏数据读出开销。
4. GC调度不能盲目执行拷贝，基于子页有效性贪心匹配可最小化跨片数据读出次数。
5. 企业SSD性能优化需软硬件协同，单纯FTL算法或单纯硬件改造均无法同时兼顾吞吐、尾延迟与容错可靠性。
