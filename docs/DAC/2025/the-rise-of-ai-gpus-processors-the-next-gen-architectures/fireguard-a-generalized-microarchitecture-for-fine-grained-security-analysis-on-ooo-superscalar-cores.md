---
title: "FireGuard: A Generalized Microarchitecture for Fine-Grained Security Analysis on OoO Superscalar Cores"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# FireGuard: A Generalized Microarchitecture for Fine-Grained Security Analysis on OoO Superscalar Cores


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES1: SoC, Heterogeneous, and Reconfigurable Architectures</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://www.cl.cam.ac.uk/~tmj32/papers/docs/jiang25-dac-fireguard.pdf">https://www.cl.cam.ac.uk/~tmj32/papers/docs/jiang25-dac-fireguard.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>源码链接:</strong> <a href="https://github.com/SEU-ACAL/reproduce-FireGuard-DAC-25">https://github.com/SEU-ACAL/reproduce-FireGuard-DAC-25</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 细粒度指令分析，乱序超标量核心，微架构安全支持，可编程安全引擎，硬件辅助安全监控</p>
</div>

---

## 研究概要
本文提出FireGuard细粒度指令安全分析微架构，适配乱序超标量RISC-V BOOM内核。设计无缓冲数据转发、超标量事件过滤器、无广播分布式映射器，搭配优化ISA编程模型。FPGA与商用SoC验证，多安全检测负载性能开销远低于软件方案，集成至M1-Pro、麒麟960等芯片面积开销不足1%。

## 背景和动机
1. 车载、手机等异构共享平台并存可信与第三方程序，传统硬件安全机制（MTE/CET）功能固化，易被攻击绕过，漏洞修复周期长。
2. 现有细粒度指令分析仅基于模拟器/顺序核实现，无法落地真实乱序超标量处理器，流水线数据采集、分发存在严重拥塞与关键路径问题。
3. 全局指令监控需海量事件传输，全广播分发硬件开销巨大，多并行安全内核调度缺乏可扩展路由机制。
4. 传统协处理器ISA交互存在大量数据冒险，安全检测内核频繁队列操作带来显著性能损耗。

## 相关工作
1. 商用硬件安全扩展（Arm MTE、Intel CET）：功能固定可编程性差，仅支持单一内存防护，无法拓展新型检测规则。
2. 软件安全工具（AddressSanitizer、影子栈）：依托编译器插桩，主线程阻塞，程序减速最高超160%。
3. 硬件监控架构Guardian Council：仅仿真验证，未适配乱序超标量流水线，存在缓存、寄存器数据采集瓶颈。
4. 专用监控加速器Fade/Flex：仅支持单类指令过滤，无分布式多安全内核路由，并行扩展性差。

## 本文解决方案
### 1. 无缓冲流水线数据转发通道
在ROB、物理寄存器、LSQ等位置插入只读旁路电路，提交阶段原位提取指令与操作数，不新增中间缓存，最小化主线核侵入与时序竞争。
### 2. 超标量并行事件过滤器
每组提交通路搭配SRAM微型过滤器，基于操作码查表筛选事件，并行匹配多发射指令，FIFO有序缓存过滤报文保证程序时序。
### 3. 无广播分布式映射网络
两级位图分配器+曼哈顿片上网络，调度引擎SE绑定安全检测内核，按需点对点传输报文，消除全局广播硬件开销。
### 4. 流水线适配ISA扩展与编程模型
将消息队列定制指令嵌入访存阶段，规避数据冒险；新增count/recent指令，结合循环展开、Duff设备降低队列操作开销。
### 5. 双时钟域划分
主核高频域、安全微内核低频域隔离，跨时钟握手传输，避免分析逻辑成为主线关键路径。

## 实验分析
1. 实验平台：RISC-V SonicBOOM乱序核+Rocket顺序安全微内核，FireSim FPGA仿真，14nm版图评估；测试影子栈、UaF、AddressSanitizer、PMC四类安全负载。
2. 性能开销：4微核配置下PMC仅2.5%减速、影子栈2.1%；12核可将AS开销由39%降至6，专用硬件加速器可完全消除延迟。
3. 检测时延：PMC检测普遍低于50ns，影子栈中位数<200ns，极端负载尾延迟可控。
4. 可扩展性：微核数量提升可持续压低开销，6核下绝大多数负载减速<5%；4宽过滤器无队列瓶颈，窄过滤器拥塞显著上升。
5. 芯片开销：原型BOOM核集成面积占25.9%；映射至M1-Pro、麒麟960、i7等商用SoC整体面积增加不足1%。

## 研究启发
1. 乱序核安全采集不能新增流水线缓冲，原位旁路转发是控制主线性能损失的核心手段。
2. 全广播分发架构不可扩展，两级位图调度+专用片上网络可实现多安全内核低开销并行。
3. 安全协处理器自定义指令需嵌入无冒险流水线阶段，传统提交后接口会带来大量气泡周期。
4. 软硬件协同优化编程模型（循环展开、队列专用指令）可大幅削减微内核处理延迟。
5. 原型小核硬件占比偏高，但在商用大尺寸高性能SoC中集成开销极低，具备工业落地可行性。
