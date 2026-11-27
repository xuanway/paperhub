Freebit: Unleashing the Performance Potential of Low-Bit LLMs Through PIM
Authors：
[Jiaxian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37582528852818661511)，[Haoran Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=7530074022921450141)，[Zhenxuan Ou](https://63dac.conference-program.com/?post_type=page&p=15&uid=96972711151599132861)，[Qin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=2073625141548463817)，[Shangyu Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=16415719287401436421)，[Kecheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9023677625232671802)，[Rui Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=430343)，[Yi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=030343)

## 中文标题

FreeBit：借助 PIM 释放低位 LLM 的性能潜力

## 英文摘要

Low-bit large language models (LLMs) use quantization to compress weights to 1/2/4 bits, significantly shrinking model size while preserving accuracy. Existing work leverages the reduced precision to cut computation. However, roofline analysis on the NVIDIA A100 shows limited inference speedup even with a 6.7× reduction in computation. This limitation is caused by insufficient memory bandwidth. Processing-in-memory (PIM) provides a promising solution for the memory bottleneck by integrating compute near data. To support efficient low-bit LLM inference, PIM should be carefully designed with joint software and hardware optimizations. This paper presents FreeBit, a PIM-based architecture that unleashes the performance potential of low-bit LLMs. The goal is to better exploit PIM for low-bit LLMs through hardware-software co-design. At the hardware level, a lookup-table (LUT)-centric architecture is designed to support quantized computation and minimize redundant computation. A sparsity-aware memory optimization is introduced to optimize memory access and leverage PIM bandwidth. At the software level, a static-dynamic decoupled scheduling strategy is presented to exploit PIM parallelism. We evaluate the proposed FreeBit using a set of extensive experiments. Experimental results show that FreeBit effectively reduces redundant computation and memory access, and delivers notable performance improvements over representative baselines.

## 中文摘要

低位大语言模型（LLM）利用量化将权重压缩至 1/2/4 位，在保持精度的同时显著缩小模型规模。已有工作借助这种降低的精度来削减计算量。然而，在 NVIDIA A100 上的 roofline 分析表明，即使计算量减少 6.7×，推理加速仍然有限。这一限制源于内存带宽不足。存内计算（PIM）通过在数据附近集成计算单元，为内存瓶颈提供了有前景的解决方案。为支持高效的低位 LLM 推理，PIM 需要结合软硬件联合优化进行精心设计。本文提出 FreeBit，一种基于 PIM 的架构，旨在释放低位 LLM 的性能潜力；其目标是通过软硬件协同设计更好地利用 PIM 服务于低位 LLM。在硬件层面，设计了以查找表（LUT）为中心的架构，以支持量化计算并最小化冗余计算；引入稀疏感知的内存优化，以优化内存访问并充分利用 PIM 带宽。在软件层面，提出静态-动态解耦的调度策略，以发挥 PIM 的并行性。我们通过大量实验对 FreeBit 进行评估，结果表明 FreeBit 有效减少了冗余计算与内存访问，并相较代表性基线取得了显著的性能提升。

## 英文关键词

Processing-in-Memory, Acceleration, Low-Bit LLMs, Hardware-Software Co-Design

## 中文关键词

存内计算、加速、低位 LLM、软硬件协同设计
