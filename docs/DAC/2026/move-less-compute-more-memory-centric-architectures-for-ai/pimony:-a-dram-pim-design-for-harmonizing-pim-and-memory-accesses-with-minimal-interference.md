Pimony: A DRAM-PIM Design for Harmonizing PIM and Memory Accesses with Minimal Interference
Authors：
[Gyeonghwan Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=5642924046374767657)，[Inseong Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=30940719519694530271)，[Byungkuk Yoon](https://63dac.conference-program.com/?post_type=page&p=15&uid=3768752245312726296)，[Sanghyeok Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=338787521454050904)，[Jae-Joon Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=04856047519916349211)

## 中文标题

PIMony：一种以最小干扰协调 PIM 与访存操作的 DRAM-PIM 设计

## 英文摘要

Edge-side LLM inference is gaining importance, yet its single-query nature shifts the performance bottleneck from computation to memory traffic. Processing-in-Memory (PIM) can exploit high internal bandwidth, but on resource-constrained edge devices, the same DRAM must also serve host memory requests, causing frequent bank conflicts and global stalls. We present PIMony, a DRAM-PIM architecture that enables seamless co-execution of PIM and conventional memory operations. PIMony introduces (i) interrupt-based asynchronous PIM, which allows preemptible MAC execution to remove channel-wide stalls, and (ii) Dual-Path Subarray Access (DPSA), which permits concurrent PIM and memory access within a single bank through dual-row activation. These mechanisms jointly enable higher co-execution efficiency and stable LLM decoding latency under concurrent PIM and memory accesses.

## 中文摘要

边缘侧 LLM 推理日益重要，然而其单查询特性使性能瓶颈由计算转移到访存流量。存内计算（PIM）能够利用高内部带宽，但在资源受限的边缘设备上，同一 DRAM 还须同时服务主机的访存请求，从而导致频繁的 bank 冲突和全局停顿。我们提出 PIMony，一种 DRAM-PIM 架构，可实现 PIM 与传统访存操作的无缝协同执行。PIMony 引入了：（i）基于中断的异步 PIM，允许可抢占的 MAC 执行，从而消除通道级停顿；（ii）双路径子阵列访问（DPSA），通过双行激活在单个 bank 内实现 PIM 与访存的并发。这些机制共同提升了协同执行效率，并在 PIM 与访存并发时保持稳定的 LLM 解码延迟。

## 英文关键词

DRAM, Processing-in-Memory (PIM), Bank conflict, LLM

## 中文关键词

DRAM、存内计算（PIM）、bank 冲突、LLM
