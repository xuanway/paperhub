---
title: "DBX-DIMM: Scalable and Reliable Near-Data Processing with Concurrent Host Access through Buffer-Centric Pseudo-Channels"
description: "MICRO 2026 · Session 4A · DBX-DIMM：通过以缓冲区为中心的伪通道实现支持主机并发访问的可扩展可靠近数据处理"
tags:
  - "MICRO2026"
---

# DBX-DIMM: Scalable and Reliable Near-Data Processing with Concurrent Host Access through Buffer-Centric Pseudo-Channels

**中文标题：** DBX-DIMM：通过以缓冲区为中心的伪通道实现支持主机并发访问的可扩展可靠近数据处理

**所属 Session：** [Session 4A](index.md) · [MICRO 2026](../index.md)

**作者：** Minkyu Lee, Sang-Seol Lee, Churoo Park, Kyungho Kim, Eunchong Lee, Sung-Joon Jang

**来源：** MICRO 2026，pp. 1381–1396；[DOI](https://doi.org/10.1109/MICRO67795.2026.00103)

## 英文摘要

For data-intensive workloads, memory bandwidth now bounds performance more tightly than compute, which makes DIMM-based Near-Data Processing (NDP) an attractive option. But deploying NDP on commodity buffered DIMMs forces a trade-off. Consolidating the distributed data buffers of modern DDR5 Load-Reduced DIMMs (LRDIMMs) into a unified buffer simplifies NDP integration but introduces excessive trace lengths that degrade signal integrity at DDR5 frequencies. While the distributed topology preserves signal integrity, it fragments rank-wide ECC codewords across multiple buffers. Either way, a DIMM-local controller manages NDP execution outside host memory controller visibility. We propose DBX-DIMM (Data Buffer eXtended DIMM), which reorganizes DRAM devices into Buffer-centric Pseudo-Channels (BPCs). Each BPC pairs one enhanced data buffer (DBX) with a dedicated group of data and parity devices, forming an independent pseudo-channel. Each DBX has an asymmetric datapath, wide toward DRAM and narrow toward the host. Decoupled Two-Phase Access (D2PA) exploits this asymmetry to overlap NDP execution with in-flight host transfers. The host memory controller schedules both host and NDP commands and throttles NDP under host pressure to sustain host-NDP concurrency. Because each BPC contains a full set of ECC devices, rank-level Reed-Solomon correction (RS(10,8,8)) is computed locally, with no inter-buffer coordination. Chiplet integration of wider x8 and x16 devices scales NDP bandwidth further. The DBX design extends a fabricated NDP-enabled data buffer in 28 nm CMOS. In our evaluation, DBX-DIMM achieves up to 4.0x standalone NDP speedup with 60% energy reduction over a conventional DIMM, retaining 96% of the NDP throughput of a unified-buffer design. Under concurrent host-NDP execution, it delivers 3.35x higher host performance than the unified-buffer design (NDP throughput stays within 35%). When a conventional DIMM serves the same memory-intensive load through its host interface, it retains only 51-86% host performance at 18-31 GB/s. DBX-DIMM keeps 61-87% of host performance while sustaining 90-121 GB/s NDP bandwidth per DIMM. It scales to 15.0x with x16 chiplet integration at 509 GB/s effective per-DIMM bandwidth at DDR5-4800.

## 中文摘要

对于数据密集型工作负载，内存带宽现在比计算更严格地限制性能，这使得基于 DIMM 的近数据处理 (NDP) 成为一个有吸引力的选择。但在商品缓冲 DIMM 上部署 NDP 需要进行权衡。将现代 DDR5 减载 DIMM (LRDIMM) 的分布式数据缓冲区整合到统一缓冲区中可简化 NDP 集成，但会引入过长的走线长度，从而降低 DDR5 频率下的信号完整性。虽然分布式拓扑保持了信号完整性，但它会将队列范围的 ECC 码字分段到多个缓冲区中。无论哪种方式，DIMM 本地控制器都会在主机内存控制器可见性之外管理 NDP 执行。我们提出了 DBX-DIMM（数据缓冲区扩展 DIMM），它将 DRAM 设备重新组织为以缓冲区为中心的伪通道 (BPC)。每个 BPC 将一个增强型数据缓冲区 (DBX) 与一组专用数据和奇偶校验设备配对，形成独立的伪通道。每个 DBX 都有一条不对称数据路径，宽通向 DRAM，窄通向主机。解耦两相访问 (D2PA) 利用这种不对称性将 NDP 执行与正在进行的主机传输重叠。主机内存控制器调度主机和 NDP 命令，并在主机压力下限制 NDP 以维持主机-NDP 并发性。由于每个 BPC 包含一整套 ECC 设备，因此等级级 Reed-Solomon 校正 (RS(10,8,8)) 是在本地计算的，没有缓冲区间协调。更宽的 x8 和 x16 器件的小芯片集成进一步扩展了 NDP 带宽。 DBX 设计扩展了 28 nm CMOS 中制造的支持 NDP 的数据缓冲器。在我们的评估中，与传统 DIMM 相比，DBX-DIMM 实现了高达 4.0 倍的独立 NDP 加速，能耗降低了 60%，保留了统一缓冲区设计的 96% 的 NDP 吞吐量。在并发主机 NDP 执行下，它的主机性能比统一缓冲区设计高出 3.35 倍（NDP 吞吐量保持在 35% 以内）。当传统 DIMM 通过其主机接口提供相同的内存密集型负载时，它在 18-31 GB/s 时仅保留 51-86% 的主机性能。 DBX-DIMM 保持 61-87% 的主机性能，同时维持每个 DIMM 90-121 GB/s NDP 带宽。通过 x16 小芯片集成，它可扩展至 15.0 倍，DDR5-4800 下每 DIMM 的有效带宽为 509 GB/s。

## 中文关键词

近数据处理；双列直插内存模块；DDR5；数据缓冲器；纠错码；芯粒

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 4A](index.md) · [MICRO 2026 主页](../index.md)
