Parallel Combinational Equivalence Checking via Sweeping-Based Task Scheduling
Authors：
[Zhihan Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=7689398188756899571)，[Congyi Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=75318354658300780171)，[Shaohuang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=4609675302852490699)，[MengYu Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=95488769959916691701)，[Shaowei Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=8937909084464565096)

## 中文标题

基于扫掠式任务调度的并行组合等价性检查

## 英文摘要

Combinational Equivalence Checking (CEC) is a cornerstone of modern IC design and verification flows, and state-of-the-art CEC solvers predominantly rely on SAT-sweeping frameworks. As circuit scale and complexity continue to increase, purely serial sweeping becomes a critical performance bottleneck, motivating the exploration of parallelism. However, existing parallel CEC approaches primarily focus on accelerating the verification of individual candidate pairs, while leaving the sweeping process itself essentially serial. This paper presents HydraCEC, a novel, general-purpose parallel CEC framework that, to the best of our knowledge, is the first to parallelize the sweeping process itself by concurrently executing its verification tasks. Its effectiveness is further enhanced by a dynamic benefit-aware scheduling policy guided by a Task Benefit Graph (TBG), and an asynchronous equivalence sharing mechanism that enables cooperation without global synchronization. Experimental results on ISCAS/ITC, Datapath, and Large-Scale benchmarks show that HydraCEC consistently outperforms existing parallel CEC solvers, particularly on large-scale instances, where it achieves a 10.5× speedup over the best competitor and exhibits excellent scalability, reaching 72.3× speedup with 128 cores.

## 中文摘要

组合等价性检查（CEC）是现代 IC 设计与验证流程的基石，最先进的 CEC 求解器主要依赖 SAT sweeping 框架。随着电路规模与复杂度持续增长，纯串行的 sweeping 已成为关键性能瓶颈，促使研究者探索并行化。然而，现有的并行 CEC 方法主要着眼于加速单个候选对的验证，sweeping 过程本身基本仍为串行。本文提出 HydraCEC，这是一个新颖的通用并行 CEC 框架；据我们所知，它首次通过并发执行 sweeping 中的各项验证任务，实现了 sweeping 过程本身的并行化。其效果还通过两项机制进一步增强：由任务收益图（TBG）引导的动态收益感知调度策略，以及无需全局同步即可实现协作的异步等价共享机制。在 ISCAS/ITC、Datapath 与大规模基准上的实验结果表明，HydraCEC 稳定优于现有并行 CEC 求解器，在大规模实例上尤为突出：相对最佳对比方法取得 10.5 倍加速，并展现出优异的可扩展性，在 128 核下达到 72.3 倍加速。

## 英文关键词

Combinational Equivalence Checking (CEC), Parallel, SAT-sweeping, Task Scheduling, Equivalence Sharing

## 中文关键词

组合等价性检查（CEC）、并行、SAT sweeping、任务调度、等价共享
