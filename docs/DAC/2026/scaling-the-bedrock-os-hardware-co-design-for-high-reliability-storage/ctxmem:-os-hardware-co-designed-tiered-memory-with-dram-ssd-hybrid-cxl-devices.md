Ctxmem: OS-Hardware Co-Designed Tiered Memory with DRAM-SSD Hybrid CXL Devices
Authors：
[Longyi Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=74934680768318693281)，[Kan Zhong](https://63dac.conference-program.com/?post_type=page&p=15&uid=1683549744506293238)，[Haorui He](https://63dac.conference-program.com/?post_type=page&p=15&uid=39876431888293062071)，[Zhenhua Tan](https://63dac.conference-program.com/?post_type=page&p=15&uid=4152838259081271645)，[Duo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=764143)

## 中文标题

CtxMem：基于 DRAM-SSD 混合 CXL 器件的操作系统-硬件协同设计分层内存

## 英文摘要

The “memory wall” problem continues to constrain modern applications, making scalable memory expansion via Compute Express Link (CXL) increasingly critical. While DRAM-Flash hybrid CXL systems offer a capacity solution, their performance remains hampered by inefficient access models. This paper presents CtxMem, an OS-hardware co-designed memory expansion system built on byte-addressable CXL interconnect and inexpensive flash storage. Unlike existing approaches, CtxMem introduces an asynchronous page fault-based mechanism that offloads the entire data plane of page fault handling to the CXL device. This is achieved through three key innovations: a dynamic direct-mapped cache that maximizes DRAM utilization, a lightweight hardware profiling unit enabling accurate and rapid hot/cold page identification with minimal overhead, and a OS-hardware co-designed page fault handling procedure that efficiently offloads data migration. Our GEM5-based evaluation shows CtxMem outperforms conventional CXL-SSD by 1.4× in execution time and doubles system throughput, demonstrating efficient large-scale memory expansion.

## 中文摘要

“内存墙”问题持续制约现代应用，使得通过 Compute Express Link（CXL）实现可扩展的内存扩展愈发关键。DRAM-Flash 混合 CXL 系统虽提供了容量层面的解决方案，但其性能仍受低效访问模型拖累。本文提出 CtxMem，一个构建于字节可寻址 CXL 互连与低成本闪存之上的、操作系统与硬件协同设计的内存扩展系统。与现有方案不同，CtxMem 引入基于异步缺页的机制，将缺页处理的数据平面整体卸载至 CXL 器件。这一目标由三项关键创新实现：动态直接映射缓存以最大化 DRAM 利用率；轻量级硬件剖析单元，以极小开销实现准确而快速的热/冷页识别；以及操作系统与硬件协同设计的缺页处理流程，高效地卸载数据迁移。基于 GEM5 的评估显示，CtxMem 的执行时间比传统 CXL-SSD 快 1.4 倍，系统吞吐量提升一倍，展现出高效的大规模内存扩展能力。

## 英文关键词

CXL, Memory expansion, OS-hardware co-design

## 中文关键词

CXL、内存扩展、操作系统-硬件协同设计
