---
title: "VersaSlot: Efficient Fine-grained FPGA Sharing with Big.Little Slots and Live Migration in FPGA Cluster"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# VersaSlot: Efficient Fine-grained FPGA Sharing with Big.Little Slots and Live Migration in FPGA Cluster

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS2: Design of Cyber-Physical Systems and IoT</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2503.05930">https://arxiv.org/abs/2503.05930</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 细粒度FPGA共享，槽位架构，动态重配置，争用缓解，跨板实时迁移</p>
</div>


---

## 研究概要
本文提出VersaSlot时空复用FPGA集群共享系统，创新Big.Little异构槽架构解决DPR串行端口引发的重配阻塞问题。设计双核心调度、自适应槽分配算法，配套跨板低开销热迁移机制。基于ZCU216集群实测，相较SOTA平均响应提速2.19倍，LUT、FF资源利用率分别提升35%、29%。

## 背景和动机
1. 数据中心FPGA依靠DPR实现细粒度时分复用，但PCAP端口仅串行加载比特流，多任务并发产生严重重配竞争、任务阻塞，拉长应用时延。
2. 现有方案采用统一尺寸槽位，HLS生成任务资源呈阶梯式占用，极易出现资源空置或超配，动态改槽需重生成比特流，开销巨大。
3. 单CPU核心同时处理调度与重配请求，重配流程阻塞正常任务执行流水线，进一步恶化尾延迟。
4. 单一全小槽(Only.Little)或固定大槽布局无法适配多变负载，切换槽配置需整机重启，中断全部任务。
5. 现有FPGA共享调度缺少集群跨设备动态负载均衡能力，单卡拥塞无法分流至空闲FPGA。

## 相关工作
1. 传统FPGA时分复用：独占整芯片、全局重配，上下文切换开销极高，硬件资源浪费严重。
2. 均匀槽DPR方案(Nimblock/DML)：采用统一尺寸分区，单核心调度无法隔离重配阻塞，无异构槽缓解竞争机制。
3. 动态调槽方案：运行时重生成部分比特流，引入极高编译与加载延时，不适在线集群场景。
4. FC/RR基础调度：仅简单任务排队，未针对DPR串行瓶颈做专项优化，负载均衡效果差。
5. 单FPGA虚拟化框架：仅单卡本地调度，不支持集群跨板任务迁移，缺乏全局负载调控能力。

## 本文解决方案
### 1 Big.Little异构槽硬件架构
FPGA划分为大容量Big槽与标准Little槽，Big槽可捆绑3个子任务并行/串行执行，大幅减少重配请求，消除槽间PR竞争；提供Only.Little纯小槽备选布局适配少任务大批次负载。
### 2 双核心解耦调度架构
PS侧ARM双核分离调度器与PR服务，重配请求异步下发，重配流程不再阻塞任务流水线，从根源解决执行阻塞问题。
### 3 自适应槽分配调度算法
分初次分配、再分配、重绑定三阶段，优先分配Big槽给可捆绑任务；闲置大槽可回收小槽应用，平衡两类槽负载，提升硬件利用率。
### 4 3-in-1任务动态捆绑机制
根据单任务最长执行时间自动选择并行/串行捆绑流水线，预先生成适配两类槽的比特流，运行时无编译开销。
### 5 集群跨板热迁移切换机制
设计Dswitch拥塞评估指标与施密特触发阈值，负载拥塞时通过Aurora高速链路将就绪任务DMA迁移至其他FPGA，切换平均开销仅1.13ms，无需中断运行任务。

## 实验分析
1. 实验平台：Xilinx ZCU216 UltraScale+ FPGA集群，基准含传统时分、FCFS、RR、Nimblock四类，负载覆盖宽松/标准/压力/实时四类流量，测试3D渲染、CNN等5类应用。
2. 响应时延：标准负载下较传统方案提速13.66倍，比Nimblock提升2.19倍；P95/P99尾延迟大幅下降。
3. 资源收益：Big槽3-in-1捆绑使LUT利用率平均+35%、FF利用率平均+29%，缓解单小槽资源碎片化。
4. 跨板迁移：拥塞触发切换后平均响应降低近3倍，切换开销仅1.13ms，运行任务不中断。
5. 消融对比：Big.Little架构相比纯小槽平均时延降低63%，双核心解耦是消除任务阻塞核心模块。

## 研究启发
1. DPR串行PCAP端口是FPGA共享核心瓶颈，异构聚合槽减少重配次数，比单纯调度优化收益更高。
2 调度与重配硬件操作必须CPU核心隔离，同步执行会持续阻塞流水线，带来长尾延迟。
3. 统一尺寸槽无法匹配HLS阶梯式任务资源需求，大小异构组合能显著减少硬件闲置。
4. 集群FPGA不能单卡独立调度，基于拥塞指标的跨板热迁移可实现全局负载均衡。
5. 提前离线生成多规格比特流，避免运行时动态布局编译，是低开销细粒度共享的关键工程手段。
