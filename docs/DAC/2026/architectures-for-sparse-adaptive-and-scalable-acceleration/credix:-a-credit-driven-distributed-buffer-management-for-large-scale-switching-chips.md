Credix: A Credit-Driven Distributed Buffer Management for Large-Scale Switching Chips
Authors：
[Xu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7861395647009418375)，[Yang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9039450446179609051)，[Danfeng Shan](https://63dac.conference-program.com/?post_type=page&p=15&uid=6711635237178537946)，[Fengyuan Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=1398029769030912563)

## 中文标题

Credix：面向大规模交换芯片的信用驱动分布式缓冲管理

## 英文摘要

With the scaling of switching chips, modular architectures are becoming mainstream. As a result, buffers become physically distributed across tiles, leading to poor utilization under imbalanced traffic. To address this, we propose CrediX, a lightweight dynamic buffer management mechanism that aggregates distributed buffers into region-based shared pools and allocates usage on demand through a Regional Credit Allocator (RCA). The design leverages existing credit-based flow control and preserves packet ordering via a simple VC-to-path mapping. Evaluations show that CrediX reduces backpressure by 65.6% under synthetic Hotspot traffic and mitigates severe hotspot occupancy in a realistic workload.

## 中文摘要

随着交换芯片规模的扩大，模块化架构逐渐成为主流。其结果是，缓冲区在物理上分散于各个 tile 之中，在流量不均衡时导致利用率低下。为解决该问题，我们提出 CrediX，一种轻量级的动态缓冲管理机制，它将分布式缓冲区聚合为基于区域的共享池，并通过区域信用分配器（RCA）按需分配使用量。该设计复用了现有的基于信用的流控机制，并通过简单的 VC 到路径映射来保持分组顺序。评估表明，CrediX 在合成 Hotspot 流量下将反压降低了 65.6%，并在真实工作负载中缓解了严重的热点占用问题。

## 英文关键词

NoC, Switching Chip, Distributed Architecture, Buffer Management

## 中文关键词

NoC、交换芯片、分布式架构、缓冲管理
