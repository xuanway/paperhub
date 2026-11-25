Keeping PIM Busy: Eliminating Execution Overheads for Full Throughput
Authors：
[Mun Seong Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=7046277128122436041)，[Jisung Pack](https://63dac.conference-program.com/?post_type=page&p=15&uid=5026388360282929641)，[Junil Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=8441885127845898309)，[Jun Sik Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=9827607469727029245)，[Seok Young Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=1660840409574008115)，[Seon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=7482602187392785365)

## 中文标题

让 PIM 持续忙碌：消除执行开销以实现满吞吐

## 英文摘要

Large language models (LLMs), such as GPT-3 and Llama-2, impose extreme memory-bandwidth demands, creating severe data movement bottlenecks. Processing-in-Memory (PIM) mitigates this by performing computations near memory; however, current PCIe-based PIM systems deliver only a small fraction of their theoretical throughput. On our multi-channel PIM emulation platform, PIM cores are active for only 6.55% of execution time, primarily due to (1) serialized host–device communication that limits channel-level parallelism, (2) insufficient request-generation capability in conventional DMA engines, and (3) per-bank microarchitectures that serialize batch execution. We address these bottlenecks with a co-designed memory system and microarchitectural solution: Channel-Level Burst (CL) for autonomous per-channel operand generation, PDMA for high-throughput PIM-oriented request scheduling, and an integrated PIM core for enabling true multi-batch parallelism. Across GEMM microbenchmarks and four LLMs, CL provides 9.10x speedup, PDMA adds 29.6x, and multi-batch execution contributes 102.4x. Together, they deliver a 145.8x improvement over a baseline multi-channel PIM system, enabling PIM to surpass CPU throughput in memory-bound LLM decode kernels and approach the efficiency of GPUs.

## 中文摘要

大语言模型（LLM），如 GPT-3 与 Llama-2，带来极高的存储带宽需求，造成严重的数据搬运瓶颈。存内处理（PIM）通过在存储附近执行计算来缓解该问题；然而，现有基于 PCIe 的 PIM 系统仅能达到其理论吞吐的一小部分。在我们搭建的多通道 PIM 仿真平台上，PIM 核心仅在 6.55% 的执行时间内处于活动状态，其主要原因包括：（1）主机与设备间通信串行化，限制了通道级并行；（2）传统 DMA 引擎的请求生成能力不足；（3）按 bank 划分的微架构使批次执行串行化。我们通过存储器系统与微架构的协同设计来应对上述瓶颈：通道级突发（CL）实现各通道操作数的自主生成，PDMA 实现面向 PIM 的高吞吐请求调度，集成式 PIM 核心则使真正的多批次并行成为可能。在 GEMM 微基准与四个 LLM 上的实验表明，CL 带来 9.10 倍加速，PDMA 额外贡献 29.6 倍，多批次执行再贡献 102.4 倍。三者合计，相较基线多通道 PIM 系统实现 145.8 倍的性能提升，使 PIM 在受带宽约束的 LLM 解码内核中超越 CPU 吞吐，并逼近 GPU 的效率。

## 英文关键词

PIM, Utilization, Channel-Level Parallelism, Direct Memory Access, Batch-Level Parallelism

## 中文关键词

PIM、利用率、通道级并行、直接存储器访问、批次级并行
