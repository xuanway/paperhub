---
title: "REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing"
description: "ASPLOS 2026 · Session 3A · REPA：面向 KV 缓存卸载与处理联合加速的可重构 PIM"
tags:
  - "ASPLOS2026"
  - "Session 3A"
  - "LLM Attention & KV Cache"
---

# REPA: Reconfigurable PIM for the Joint Acceleration of KV Cache Offloading and Processing

**中文标题：** REPA：面向 KV 缓存卸载与处理联合加速的可重构 PIM

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yang Hong (Shanghai Jiao Tong University), Junlong Yang (Shanghai Jiao Tong University), Bo Peng (Shanghai Jiao Tong University), Jianguo Yao (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790212) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The use of KV cache in LLM inference leads to large memory footprint and sub-optimal decoding performance. Prior studies typically address one of these two limitations by either offloading or stage-split inference. In this paper, we explore and reveal the possibility of a joint solution, and propose REPA, a GPU-PIM hybrid system to prototype this idea. We leverage reconfigurable ReRAM PIM to achieve fast KV cache persistence, and balance the requirement of processing speed and memory capacity. To fully unleash the parallelization potential of REPA, we propose optimizations in (1) architecture, (2) data mapping and (3) pipelining: (1) We propose bulk-wise memory instructions and multi-level controllers to enable finer-grained parallelism in the PIM device. (2) We propose locality-aware data mapping to make the best of the aforementioned architectural optimization, and reduce long-range data transfer on chip. (3) We adopt subbatch pipelining to reduce idleness in batches, and propose transfer overlapping to shadow the KV cache transfer by computation. Experimental results show that REPA exhibits high inference speed, energy efficiency and integratability. It is 1.5–6.5× faster, and 8–10× more efficient than NVIDIA A100. It also outperforms state-of-the-art DRAM PIM systems by up to 1.4× for long context inference. When integrated into existing offloading systems, REPA achieves 1.4–2.0× offloading speed, and 1.2–1.4× end-to-end speedup, showcasing its high potential for fast KV cache offloading and processing.

## 中文摘要

在 LLM 推理中使用 KV 缓存会导致巨大的内存占用和次优的解码性能。已有研究通常通过卸载或阶段拆分推理来解决这两项局限之一。本文探索并揭示了联合解决方案的可能性，并提出 REPA——一个 GPU-PIM 混合系统，以对该思路进行原型验证。我们利用可重构的 ReRAM PIM 实现快速的 KV 缓存持久化，并平衡处理速度与存储容量的需求。为充分释放 REPA 的并行化潜力，我们在（1）架构、（2）数据映射和（3）流水线三个方面提出优化：（1）我们提出按块（bulk-wise）的存储指令与多级控制器，以在 PIM 器件中实现更细粒度的并行。（2）我们提出局部性感知的数据映射，以充分利用上述架构优化，并减少片上的长距离数据传输。（3）我们采用子批次（subbatch）流水线以减少批次内的空闲，并提出传输重叠，用计算遮蔽 KV 缓存的传输。实验结果表明，REPA 展现出高推理速度、高能效和高可集成性。相比 NVIDIA A100，它的速度提升 1.5–6.5×，能效提升 8–10×。在长上下文推理中，它还以最高 1.4× 的优势超越最先进的 DRAM PIM 系统。当集成到现有的卸载系统时，REPA 可实现 1.4–2.0× 的卸载速度和 1.2–1.4× 的端到端加速，显示出其在快速 KV 缓存卸载与处理方面的巨大潜力。

## 英文关键词

Processing-in-Memory; Large Language Models; KV Cache; ReRAM

## 中文关键词

存内计算；大语言模型；KV 缓存；ReRAM

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790212)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2026](../index.md)
