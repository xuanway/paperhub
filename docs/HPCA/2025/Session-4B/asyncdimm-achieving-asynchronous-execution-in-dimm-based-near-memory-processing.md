---
title: "AsyncDIMM: Achieving Asynchronous Execution in DIMM-Based Near-Memory Processing"
description: "HPCA 2025 · Doubling Down with PIM"
tags:
  - "HPCA2025"
  - "Doubling Down with PIM"
---

# AsyncDIMM: Achieving Asynchronous Execution in DIMM-Based Near-Memory Processing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Doubling Down with PIM。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Doubling Down with PIM</p>
</div>

**论文链接**：
**作者**：Liyan Chen (Shanghai Jiao Tong University), Dongxu Lyu (Shanghai Jiao Tong University), Jianfei Jiang (Shanghai Jiao Tong University), Qin Wang (Shanghai Jiao Tong University), Zhigang Mao (Shanghai Jiao Tong University), Naifeng Jing (Shanghai Jiao Tong University)
**会议**：HPCA 2025

---

## 中文标题

AsyncDIMM：在基于 DIMM 的近存处理中实现异步执行

## 英文摘要

DIMM-based near-memory processing (NMP) architectures address the “memory wall” problem by incorporating near-memory accelerators (NMAs) into main memory devices for high memory bandwidth and low energy consumption. However, critical challenges prevent efficient asynchronous execution between host and NMAs in DIMM-NMP architectures. Memory controllers (MCs) distributed at the host side and the NMA side issue memory accesses independently without synchronization on memory states, which may lead to memory bus contention and DRAM errors. Therefore, most existing DIMM-NMP designs adopt synchronous execution to prevent concurrent memory accesses. However, this intervention wastes either the host or the NMA computation capability. In this work, we propose AsyncDIMM, a novel DIMM-NMP design with efficient asynchronous execution based on existing memory buses. It enables single access mode (host or NMA), concurrent access mode, and a seamless switch between them. First, we propose the offload-schedule-return mechanism with explicit and implicit synchronization to ensure memory access correctness for all memory modes. Second, to further improve bandwidth utilization and decrease access latency, we introduce optimized timing constraints for offloading, a locality-aware switch-recovery method for scheduling, and adaptive batch with timing-division multiplexing notification for returning. Finally, we present a detailed design with limited hardware modifications to conventional host and NMA MCs, which is extensively validated on the FPGA. Comprehensive experiments demonstrate that AsyncDIMM outperforms four NMP baselines by 1.19×-1.92×, enabling efficient asynchronous execution with up to 2.25× bandwidth utilization uplift and 47% access latency reduction.

## 中文摘要

基于 DIMM 的近存处理（NMP）架构通过将近存加速器（NMA）集成到主存设备中，从而获得高内存带宽与低能耗，解决了“内存墙”问题。然而，关键挑战阻碍了 DIMM-NMP 架构中主机与 NMA 之间的高效异步执行。分布在主机侧与 NMA 侧的内存控制器（MC）各自独立发起内存访问，且不同步内存状态，这可能导致内存总线争用与 DRAM 错误。因此，现有大多数 DIMM-NMP 设计采用同步执行以避免并发的内存访问。然而，这种干预会浪费主机或 NMA 的计算能力。在本工作中，我们提出 AsyncDIMM，一种基于现有内存总线实现高效异步执行的新型 DIMM-NMP 设计。它支持单访问模式（主机或 NMA）、并发访问模式，以及两者之间的无缝切换。首先，我们提出带显式与隐式同步的卸载-调度-返回机制，以保证所有内存模式下的内存访问正确性。其次，为进一步提升带宽利用率并降低访问时延，我们引入了针对卸载的优化时序约束、用于调度的局部性感知切换-恢复方法，以及用于返回的带时分复用通知的自适应批处理。最后，我们给出了仅对传统主机与 NMA 内存控制器做有限硬件改动即可实现的详细设计，并在 FPGA 上进行了充分验证。综合实验表明，AsyncDIMM 相较四种 NMP 基线取得 1.19×-1.92× 的提升，实现了高效的异步执行，带宽利用率最高提升 2.25×，访问时延降低 47%。
