---
title: "PET: Proactive Demotion for Efficient Tiered Memory Management"
description: "EuroSys 2025 · Memory Tiering and Disaggregation · Wanju Doh (Seoul National University), Yaebin Moon (Samsung Electronics), Seoyou"
tags:
  - "EuroSys2025"
  - "Memory Tiering and Disaggregation"
---

# PET: Proactive Demotion for Efficient Tiered Memory Management

**中文标题：** 通过主动降级实现高效分层内存管理

**所属 Session：** [Session 6.2: Memory Tiering and Disaggregation](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Memory Tiering and Disaggregation。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Memory Tiering and Disaggregation</p>
</div>

**作者**：Wanju Doh (Seoul National University), Yaebin Moon (Samsung Electronics), Seoyoung Ko (Seoul National University), Seunghwan Chung (Seoul National University), Kwanhee Kyung (Seoul National University), Eojin Lee (Inha University), Jung Ho Ahn (Seoul National University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717471)

## 英文摘要

Tiered memory is a promising approach for increasing main-memory capacity at a lower cost by using DRAM as the upper tier (fast memory) and slower-but-cheap byte-addressable memory as the lower tier (slow memory). A proactive demotion, one of the ways to use tiered memory efficiently, demotes cold data to slow memory even when fast memory has sufficient free space. Prior works have utilized proactive demotion to reduce the high cost of main memory by reducing applications’ resident set size in fast memory. Further, proactive demotion helps mitigate severe performance degradation caused by fast memory shortages when there is a spike in demand for hot data. Still, we observe that leveraging memory access locality within the allocation units of applications enables larger fast-memory savings with lower system overhead.

We propose a new proactive demotion scheme, PET, which performs proactive demotion for efficient tiered memory management. PET proposes extending the unit of demotion and promotion from the OS page, adopted by prior works, to PET-block (P-block), which reflects the unit in which applications allocate memory. We also provide the mechanisms that carefully select the demotion target P-block and swiftly promote the demoted P-block when the access pattern changes. The prototype of PET on Linux kernel v6.1.44 reduces 39.8% (up to 80.4%) of fast-memory usage with only a 1.7% performance drop on average of the evaluated workloads. Also, it mitigates 31% performance slowdown compared to the default Linux kernel when the system’s memory usage is larger than fast-memory capacity, which outperforms state-of-the-art schemes for tiered memory management.

## 中文摘要

分层内存是一种有前景的方法，通过使用 DRAM 作为上层（快速内存）、使用较慢但廉价的字节可寻址内存作为下层（慢速内存），以更低的成本增加主存容量。主动降级是高效使用分层内存的方式之一，即使在快速内存有充足空闲空间时也将冷数据降级到慢速内存。先前工作利用主动降级，通过减少应用在快速内存中的常驻集大小来降低主存的高成本。此外，当热数据需求激增时，主动降级有助于缓解快速内存短缺造成的严重性能下降。尽管如此，我们观察到，利用应用分配单元内的内存访问局部性，能够以更低的系统开销实现更大的快速内存节省。

我们提出一种新的主动降级方案 PET，它执行主动降级以实现高效的分层内存管理。PET 提出将降级与提升的单元从先前工作采用的 OS 页扩展为 PET 块（P-block），该单元反映了应用分配内存的粒度。我们还提供了谨慎选择降级目标 P-block、并在访问模式变化时迅速提升已降级 P-block 的机制。PET 在 Linux 内核 v6.1.44 上的原型在评估工作负载上平均仅降低 1.7% 性能的情况下，减少了 39.8%（最高 80.4%）的快速内存使用量。此外，当系统内存使用超过快速内存容量时，相比默认 Linux 内核，它缓解了 31% 的性能下降，优于最先进的分层内存管理方案。

**英文关键词：** Memory Tiering, Operating Systems, Memory Management

**中文关键词：** 内存分层、操作系统、内存管理

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
