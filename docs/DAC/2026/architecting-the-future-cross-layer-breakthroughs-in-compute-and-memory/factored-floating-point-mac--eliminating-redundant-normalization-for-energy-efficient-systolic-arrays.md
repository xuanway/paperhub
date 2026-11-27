Factored Floating-Point MAC: Eliminating Redundant Normalization for Energy-Efficient Systolic Arrays
Authors：
[Hao Xiong](https://63dac.conference-program.com/?post_type=page&p=15&uid=15758280858839018411)，[Zhichao Rui](https://63dac.conference-program.com/?post_type=page&p=15&uid=9592378996804833351)，[Zhijie Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=57609327200251751861)，[Rui Gong](https://63dac.conference-program.com/?post_type=page&p=15&uid=2552656039119181316)，[Lei Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=30555009972474906541)

## 中文标题

因式分解浮点 MAC：为高能效脉动阵列消除冗余规格化

## 英文摘要

Floating-point multiply-accumulate (FPMAC) is essential in scientific computing and AI but remains a major performance and energy bottleneck. Conventional IEEE-754 FP-FMA schemes optimize single multiply-add fusion but overlook long-chain MAC patterns in GEMM, leading to redundant rounding and normalization, accumulated numerical error, and high delay and power overhead from wide carry-propagate adders (CPAs). We propose Factored-FPMAC, using 4:2 carry-save adders (CSAs) and CSA-based redundant representation inside systolic arrays (SAs) to eliminate CPAs from processing elements and defer normalization to a unified post-processing stage. To prevent accumulated intermediate value overflow (AIVO) under deferred normalization, we introduce a lightweight hierarchical risk-aware boundary protection mechanism. To further reduce register overhead from redundant representation, an array-shared buffer pool replaces per-PE dual buffers. Experiments show F-FPMAC reduces critical-path delay by 61.9%, lowers power by 22.6%, improves energy efficiency by 3×, reduces error by two orders of magnitude and achieves 44.5% fewer overflows.

## 中文摘要

浮点乘累加（FPMAC）在科学计算与人工智能中至关重要，但仍是主要的性能与能耗瓶颈。传统的 IEEE-754 浮点 FMA 方案优化了单次乘加融合，却忽视了 GEMM 中的长链 MAC 模式，导致冗余的舍入与规格化、累积的数值误差，以及宽进位传播加法器（CPA）带来的高延迟与高功耗开销。我们提出 Factored-FPMAC，在脉动阵列（SA）内部使用 4:2 进位保留加法器（CSA）与基于 CSA 的冗余表示，从而将 CPA 从处理单元中移除，并把规格化推迟到统一的后处理阶段。为防止延迟规格化下的中间值累积溢出（AIVO），我们引入一种轻量级的分层风险感知边界保护机制。为进一步降低冗余表示带来的寄存器开销，用阵列共享缓冲池替代每个 PE 的双缓冲。实验表明，F-FPMAC 将关键路径延迟降低 61.9%，功耗降低 22.6%，能效提升 3 倍，误差降低两个数量级，且溢出减少 44.5%。

## 英文关键词

multiply-accumulate, floating-point, normalize, systolic array

## 中文关键词

乘累加、浮点、规格化、脉动阵列
