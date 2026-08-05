---
title: "MEEK: Re-thinking Heterogeneous Parallel Error Detection Architecture for Real-World OoO Superscalar Processors"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# MEEK: Re-thinking Heterogeneous Parallel Error Detection Architecture for Real-World OoO Superscalar Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS2: Design of Cyber-Physical Systems and IoT</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://www.cl.cam.ac.uk/~tmj32/papers/docs/jiang25-dac-meek.pdf">https://www.cl.cam.ac.uk/~tmj32/papers/docs/jiang25-dac-meek.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/SEU-ACAL/reproduce-MEEK-DAC-25">https://github.com/SEU-ACAL/reproduce-MEEK-DAC-25</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 异构并行错误检测，寄存器检查点，转发结构，全栈软硬件协同设计，真实乱序超标量处理器实现</p>
</div>

---

## 研究概要
本文提出MEEK异构并行故障检测全栈架构，基于高性能乱序大核+轻量有序小核协同校验。软硬件协同设计低侵入微架构、专用ISA与Linux轻量修改，解决前人仿真未发现的死锁、转发拥塞等瓶颈。28nm综合面积开销25.8%，故障平均检测时延小于1μ，性能远优于锁步、软件校验方案。

## 背景和动机
1. 先进工艺电压降低，处理器瞬态/永久故障频发，车载、航电ISO/DO安全标准要求毫秒级故障检测隔离。
2. 双核/三核锁步架构面积、功耗开销巨大，无法适配乱序超标量大核。
3. 现有异构并行检测仅高层仿真，无完整RTL实现，忽略片上转发拥塞、内核死锁等工程瓶颈，难以落地商用处理器。
4. 异构大小核异步交互复杂，数据采集、跨片路由易产生背压阻塞大核执行，缺少专用转发硬件。
5. 缺少配套ISA、OS调度与编程模型，无法完成线程级分段并行校验，存在页故障引发死锁缺陷。

## 相关工作
1. 锁步容错处理器：同步双核逐周期比对，覆盖完整，但面积功耗翻倍，不适用于乱序超标量核心。
2. 软件容错(Nzdc等)：编译插桩校验，性能衰减超60%，故障覆盖范围有限。
3. 早期异构并行检测(DSN18 Paramedic)：仅抽象仿真，无RTL实现，高估小核并发能力，未解决转发、死锁问题。
4. 传统片上AXI互联：带宽低、单周期仅单包传输，数据转发产生大量性能开销。
5. 通用RISC-V内核：无模式切换、加载存储日志硬件，不支持分段程序回放校验。

## 本文解决方案
### 1 软硬件协同低侵入整体架构
对成熟BOOM乱序大核仅小幅修改，搭配升级Rocket有序小核；划分硬件数据采集转发、OS调度、专用ISA三层，最小化内核改造量。
### 2 大核微架构：DEU无侵入数据提取单元
在提交阶段旁路采集寄存器、LSQ访存数据，无需新增独立缓存；按RCP寄存器检查点分割程序段，避免改写原有寄存器通路。
### 3 专用F²半双工组播转发网络
双通道DC缓冲+曼哈顿HM-NoC，单周期双包有序传输，解决传统AXI互联拥塞背压，仅向对应小核分发分段日志。
### 4 增强型轻量小核微架构
新增MSU模式切换单元与LSL加载存储日志；校验阶段LSL替代L1缓存回放访存操作，支持应用/校验双运行模式。
### 5 定制MEEK ISA+轻量Linux内核修改
区分大/小核特权指令，实现核绑定、模式切换、检查点读写；仅修改调度上下文切换代码，解决页故障死锁；提供简易校验线程编程模型。

## 实验分析
1. 实验环境：Rocket Chip SoC，BOOM乱序大核+4颗Rocket小核，28nm工艺，SPECint06、Parsec基准，FireSim FPGA仿真。
2. 性能开销：4小核配置下SPEC平均减速1.4%、Parsec4.4%，远低于等效面积锁步(48.7%)与软件Nzdc(94.2%)。
3. 检测时延：随机故障注入平均检测时延<1μs，99.9%故障在3μ内捕获，满足FTTI毫秒级安全规范。
4. 可扩展性：2/4/6小核随算力提升性能损耗超线性下降，优化除法/FPU后小核面积效率提升15.2%。
5. 硬件开销：整套MEEK附加逻辑总面积0.726mm²，整体开销25.8%；F²转发硬件是主要性能瓶颈，替换专用互联后转发开销降至5%内。

## 研究启发
1. 异构并行故障检测不能仅依赖高层仿真，完整RTL实现才能暴露死锁、互联拥塞等工程瓶颈。
2. 低侵入旁路式数据采集可避免大幅重构乱序内核，复用原有LSQ、寄存器缓存减少硬件冗余。
3. 专用片上组播转发网络是消除数据背压、保障大核吞吐的关键，通用AXI总线不适合海量日志传输。
4. 软硬件分层解耦：硬件负责高速数据通路，OS承担线程调度、死锁规避，大幅降低微架构复杂度。
5. 小核流水线瓶颈模块(除法、FPU)定向优化，比单纯增加小核数量更具面积性能收益。
