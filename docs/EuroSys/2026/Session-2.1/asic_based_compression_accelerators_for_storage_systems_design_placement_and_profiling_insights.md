---
title: "ASIC-based Compression Accelerators for Storage Systems: Design, Placement, and Profiling Insights"
description: "EuroSys 2026 · File Systems & Storage · Tao Lu (DapuStor Corporation), Jiapin Wang (DapuStor Corporation), Yelin Shan (D"
tags:
  - "EuroSys2026"
  - "File Systems & Storage"
---

# ASIC-based Compression Accelerators for Storage Systems: Design, Placement, and Profiling Insights

**中文标题：** 面向存储系统的基于 ASIC 的压缩加速器：设计、部署位置与剖析洞见

**所属 Session：** [Session 2.1: File Systems & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：File Systems & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · File Systems & Storage</p>
</div>

**作者**：Tao Lu (DapuStor Corporation), Jiapin Wang (DapuStor Corporation), Yelin Shan (DapuStor Corporation), Xiangping Zhang (DapuStor Corporation), Xiang Chen (DapuStor Corporation)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769384)

## 英文摘要

Lossless compression imposes significant computational overhead on datacenters when performed on CPUs. Hardware compression and decompression processing units (CDPUs) can alleviate this overhead, but optimal algorithm selection, microarchitectural design, and system-level placement of CDPUs are still not well understood. We present the design of an ASIC-based in-storage CDPU and provide a comprehensive end-to-end evaluation against two leading ASIC accelerators, Intel QAT 8970 and QAT 4xxx. The evaluation spans three dominant CDPU placement regimes: peripheral, on-chip, and in-storage. Our results reveal: (i) acute sensitivity of throughput and latency to CDPU placement and interconnection, (ii) strong correlation between compression efficiency and data patterns/layouts, (iii) placement-driven divergences between microbenchmark gains and real-application speedups, (iv) discrepancies between module and system-level power efficiency, and (v) scalability and multi-tenant interference issues of various CDPUs. These findings motivate a placement-aware, cross-layer rethinking of hardware (de)compression for hyperscale storage infrastructures.

## 中文摘要

无损压缩在 CPU 上执行时会给数据中心带来显著的计算开销。硬件压缩与解压缩处理单元（CDPU）可以缓解这一开销，但最优算法选择、微架构设计以及 CDPU 的系统级部署位置仍未被充分理解。我们给出了一种基于 ASIC 的存内 CDPU 的设计，并与两款领先的 ASIC 加速器 Intel QAT 8970 与 QAT 4xxx 进行了全面的端到端评估。评估涵盖三种主流的 CDPU 部署模式：外设侧、片上以及存内。结果揭示了：(i) 吞吐量与延迟对 CDPU 部署位置与互连的极度敏感性；(ii) 压缩效率与数据模式/布局之间的强相关性；(iii) 部署位置导致的微基准测试收益与真实应用加速之间的背离；(iv) 模块级与系统级能效之间的差异；(v) 各类 CDPU 的可扩展性与多租户干扰问题。这些发现促使我们以位置感知、跨层的视角，重新思考面向超大规模存储基础设施的硬件（解）压缩。

**英文关键词：** ASIC Compression Accelerator, Storage System

**中文关键词：** ASIC 压缩加速器、存储系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
