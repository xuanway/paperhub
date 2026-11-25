---
title: "NDFT: Accelerating Density Functional Theory Calculations via Hardware/Software Co-Design on Near-Data Computing System"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# NDFT: Accelerating Density Functional Theory Calculations via Hardware/Software Co-Design on Near-Data Computing System

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.03451">https://arxiv.org/abs/2504.03451</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 近数据处理，密度泛函理论，工作负载调度，硬件/软件协同设计</p>
</div>


---

## 研究概要
本文提出面向LR-TDDFT第一性原理计算的近数据协同框架NDFT，适配CPU-NDP异构架构。设计代价感知任务调度，优化赝势共享存储软硬件协同方案。硅原子多体系仿真表明，大规模体系下相对CPU提速5.2倍、相对GPU提速2.5倍，大幅缓解访存与内存溢出瓶颈。

## 背景和动机
1. LR-TDDFT用于材料激发态仿真，多数内核属于访存密集型，传统CPU/GPU存在大量主机-加速设备数据搬移开销，抵消并行收益。
2. GPU、神威等异构方案仅优化计算密集内核，忽略FFT等访存瓶颈，大规模体系内存占用爆炸易触发OOM。
3. CPU-NDP近数据架构算力分层，但缺少适配DFT的任务划分策略，粗/细粒度卸载均会引入高额调度开销。
4. 传统赝势并行方案每个进程完整拷贝数据，NDP多进程场景内存冗余极高，大体系直接内存溢出。

## 相关工作
1. GPU/超算加速LR-TDDFT：仅优化GEMM等计算内核，未解决跨设备数据传输瓶颈，访存内核提升有限。
2. 通用NDP调度工具：面向通用负载，无DFT专用内核特征识别，无法区分访存/计算密集任务。
3. 量子化学专用PIM方案：仅针对FFT单内核定制硬件，缺乏完整端到端DFT调度框架。
4. 并行赝势优化：仅软件层面裁剪数据，未配套NDP片上共享存储硬件，跨栈通信开销大。

## 本文解决方案
### 1 代价感知函数级任务调度
静态代码分析器判定内核算术强度，建立包含数据传输、上下文切换的调度代价模型；访存密集FFT/点积卸载至NDP，计算密集GEMM/对角化留在CPU。
### 2 赝势数据结构轻量化重构
取消每进程完整拷贝，采用索引共享机制，同一原子赝势仅存一份，各进程通过索引寻址，削减冗余内存占用。
### 3 SPM片上共享存储硬件
每层存储栈内置高速暂存共享内存，提供读写/远程广播API，同栈进程零DRAM访问开销。
### 4 分层跨栈通信机制
每栈设置通信仲裁单元，栈内本地访问优先，跨栈仅转发必要赝势数据，大幅削减全局通信量。

## 实验分析
1. 仿真环境：zsim+Ramulator搭建HBM2 CPU-NDP平台，对比Xeon CPU、V10 GPU，测试Si16~Si2048多硅原子体系。
2. 整体性能：小体系相对CPU提速1.9倍、GPU1.6倍；Si1024大体系相对CPU5.2倍、GPU2.5倍；调度开销仅占总耗时4%左右。
3. 内核增益：FFT访存内核大体系下提速11.2倍，GEMM计算内核GPU仍小幅领先。
4. 内存优化：大体系赝势内存占用降低57.8%，解决NDP架构OOM问题。
5. 扩展性：体系原子数量越大，NDFT加速比越高，Si2048最高达5.33倍。

## 研究启发
1. LR-TDDFT性能核心瓶颈是访存而非计算，近数据架构天然适配这类内存绑定科学计算负载。
2. 异构调度不能一刀切，需基于内核算术强度分层分配CPU/NDP，同时量化传输代价避免卸载得不偿失。
3. 并行科学库冗余全局参数是内存杀手，软硬件协同共享存储可低成本解决多进程内存溢出。
4. 近数据系统通信分层设计至关重要，栈内高速SPM+跨栈仲裁能平衡共享收益与通信开销。
5. 面向专用HPC负载不能复用通用NDP调度，必须结合应用算法特征定制划分策略。