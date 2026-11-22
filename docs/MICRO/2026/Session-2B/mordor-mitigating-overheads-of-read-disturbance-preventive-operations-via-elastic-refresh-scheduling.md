---
title: "MORDOR: Mitigating Overheads of Read Disturbance Preventive Operations via Elastic Refresh Scheduling"
description: "MICRO 2026 · Session 2B · MORDOR：通过弹性刷新调度降低读扰动预防操作的开销"
tags:
  - "MICRO2026"
---

# MORDOR: Mitigating Overheads of Read Disturbance Preventive Operations via Elastic Refresh Scheduling

**中文标题：** MORDOR：通过弹性刷新调度降低读扰动预防操作的开销

**所属 Session：** [Session 2B](index.md) · [MICRO 2026](../index.md)

**作者：** Maria Makeenkova, Ataberk Olgun, F. Nisa Bostancı, İsmail Emir Yüksel, Spiros Galanopoulos, Onur Mutlu

**来源：** MICRO 2026，pp. 572–591；[DOI](https://doi.org/10.1109/MICRO67795.2026.00053)

## 英文摘要

Modern DRAM chips are susceptible to read disturbance phenomena such as RowHammer, where repeatedly accessing (hammering) a row of DRAM cells (i.e., a DRAM row) induces bitflips in other physically nearby (victim) DRAM rows. A common practice to avoid such bitflips is to preventively refresh victim rows that might otherwise experience bitflips. Unfortunately, preventive refreshes cause long latencies and need to be performed urgently before the aggressor row is activated again to ensure data integrity. This is done by prioritizing them over demand memory requests, thereby potentially imposing significant delays on those requests and causing performance and energy overheads. Our goal in this work is to alleviate these overheads by scheduling preventive refreshes off the critical path of demand memory requests. We propose MORDOR, a new preventive refresh scheduling policy that significantly reduces system performance degradation and energy consumption caused by preventive refresh operations. MORDOR is integrated into the memory controller and operates alongside memory-controller-based read disturbance mitigation techniques to intelligently delay preventive refresh operations, while maintaining their data integrity guarantees. MORDOR leverages the key observation that a preventive refresh operation targeting an aggressor row can be delayed to serve any other demand memory request, as long as that memory request does not access the aggressor row. By doing so, MORDOR executes latency-critical memory requests before long-latency preventive refresh operations, while mitigating read disturbance bitflips. We evaluate MORDOR by integrating it into six state-of-the-art read disturbance mitigation techniques. Our comprehensive evaluation shows that MORDOR significantly improves system performance and energy efficiency at low area cost, by reducing the latencies of demand memory requests, while maintaining the data integrity guarantees of the underlying read disturbance mitigation technique. Across 55 eight-core workloads, MORDOR provides an average (maximum) 21.7% (423.0%) speedup and a 22.1% (411.5%) DRAM energy reduction when integrated with four state-of-the-art read disturbance mitigation techniques that issue a significant number of preventive refresh operations for a preventive refresh threshold of 125. MORDOR is openly and freely available at https://github.com/CMU-SAFARI/MORDOR.

## 中文摘要

现代 DRAM 芯片很容易受到诸如 RowHammer 之类的读取干扰现象的影响，其中重复访问（敲击）一行 DRAM 单元（即 DRAM 行）会导致其他物理附近（受害者）DRAM 行中的位翻转。避免此类位翻转的常见做法是预防性地刷新可能会发生位翻转的受害行。不幸的是，预防性刷新会导致较长的时延，并且需要在再次激活攻击者行之前紧急执行以确保数据完整性。这是通过将它们优先于需求内存请求来完成的，从而可能对这些请求造成显着的时延并导致性能和能源开销。我们这项工作的目标是通过在需求内存请求的关键路径上安排预防性刷新来减轻这些开销。我们提出了 MORDOR，一种新的预防性刷新调度策略，可显着减少预防性刷新操作引起的系统性能下降和能耗。 MORDOR 集成到内存控制器中，并与基于内存控制器的读取干扰缓解技术一起运行，以智能地时延预防性刷新操作，同时保持数据完整性保证。 MORDOR 利用了一个关键观察结果，即针对攻击者行的预防性刷新操作可以被时延，以服务任何其他需求内存请求，只要该内存请求不访问攻击者行。通过这样做，MORDOR 在长时延预防性刷新操作之前执行时延关键的内存请求，同时减轻读取干扰位翻转。我们通过将 MORDOR 集成到六种最先进的读取干扰缓解技术中来对其进行评估。我们的综合评估表明，MORDOR 通过减少需求内存请求的时延，以较低的面积成本显着提高了系统性能和能效，同时保持了底层读取干扰缓解技术的数据完整性保证。在 55 个八核工作负载中，当与四种最先进的读取干扰缓解技术集成时，MORDOR 提供平均（最大）21.7% (423.0%) 的加速和 22.1% (411.5%) 的 DRAM 能耗降低，这些技术针对 125 次预防性刷新阈值发出大量预防性刷新操作。 https://github.com/CMU-SAFARI/MORDOR。

## 中文关键词

DRAM 读干扰；预防性操作；弹性刷新调度；RowHammer；性能开销

## 代码与研究制品

- 代码仓库：[https://github.com/CMU-SAFARI/MORDOR](https://github.com/CMU-SAFARI/MORDOR)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21539624](https://doi.org/10.5281/zenodo.21539624)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21514599](https://doi.org/10.5281/zenodo.21514599)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2B](index.md) · [MICRO 2026 主页](../index.md)
