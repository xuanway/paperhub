A Boolean Processor-Based Hardware Emulation System with Reconfigurable Interconnects
Authors：
[Ruiyao Pu](https://63dac.conference-program.com/?post_type=page&p=15&uid=80800939848183038841)，[Muhan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=23673647873413936281)，[Li Shang](https://63dac.conference-program.com/?post_type=page&p=15&uid=911843)，[Fan Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=332243)

## 中文标题

一种具有可重构互连的基于布尔处理器的硬件仿真系统

## 英文摘要

Existing Boolean processor-based (BP-based) hardware emulation systems typically rely on fixed interconnects, which often suffer from severe bandwidth underutilization under highly imbalanced traffic. We propose a BP-based hardware emulation system with hierarchical reconfigurable interconnects. At both the inter-chip and intra-chip levels, our system dynamically reallocates idle interconnect lanes from low-traffic pairs to high-demand pairs, alleviating communication bottlenecks and improving interconnect utilization without modifying the underlying ASIC fabric. The hardware is co-designed with the compiler, which profiles communication, generates per-lane configuration tables and scheduling strategies, and programs the interconnect via registers. Experimental results on industrial digital designs show up to 64% emulation performance improvement and an average 27% reduction in compilation time, with only 7.4% area overhead compared to a fixed-interconnect baseline system.

## 中文摘要

现有的基于布尔处理器（BP）的硬件仿真系统通常依赖固定互连，在流量高度不均衡时往往出现严重的带宽利用不足。我们提出一种具有分层可重构互连的基于 BP 的硬件仿真系统。在芯片间与芯片内两个层级上，本系统将空闲的互连通道从低流量节点对动态重新分配给高需求节点对，从而在不修改底层 ASIC 结构的前提下缓解通信瓶颈、提升互连利用率。该硬件与编译器协同设计，编译器对通信进行剖析、生成逐通道配置表与调度策略，并通过寄存器对互连进行编程。在工业数字设计上的实验结果表明，与固定互连的基线系统相比，本系统的仿真性能最高提升 64%，编译时间平均缩短 27%，而面积开销仅为 7.4%。

## 英文关键词

Processor-based Emulation, Reconfigurable Interconnect, Hardware-Software Co-Design

## 中文关键词

基于处理器的仿真、可重构互连、软硬件协同设计
