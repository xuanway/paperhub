---
title: "FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference"
description: "HPCA 2025 · Viva Las Learning Models (with PIM)"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models (with PIM)"
---

# FACIL: Flexible DRAM Address Mapping for SoC-PIM Cooperative On-device LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models (with PIM)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models (with PIM)</p>
</div>

**论文链接**：
**作者**：Seong Hoon Seo (Seoul National University), Junghoon Kim (Seoul National University / Samsung Electronics), Donghyun Lee (Seoul National University), Seonah Yoo (POSTECH), Seokwon Moon (Hanyang University), Yeonhong Park (Seoul National University), Jae W. Lee (Seoul National University)
**会议**：HPCA 2025

---

## 中文标题

FACIL：面向 SoC-PIM 协同端侧 LLM 推理的灵活 DRAM 地址映射

## 英文摘要

The rise of on-device inference of large language models (LLMs) is rapidly escalating the demand for memory-intensive operations on edge devices. While DRAM-based processing-in-memory (PIM) is a promising solution for overcoming the memory wall, edge devices require PIM to function both as a compute unit and a memory device due to their limited memory capacity. Such PIM-enabled memory complicates the partition and placement of a tensor into DRAM banks in a PIM-operable manner. Notably, we highlight that LLM weights need to be accessible by both PIM and system-on-chip (SoC) processors, as the same weights are used for both SoC-favorable GEMM and PIM-favorable GEMV operations. This necessitates different memory mappings for PIM and SoC processors, leading to potential re-layout costs when switching between the two. To address this challenge, we propose FACIL, a flexible DRAM address mapping solution that efficiently places tensors in DRAM for PIM operations while allowing SoC processors to access the same data using contiguous virtual addresses. FACIL consists of (i) a memory controller that assigns different DRAM address mapping to the page offset bits of each huge page and (ii) a user-level library that determines the appropriate DRAM address mapping. We demonstrate that enabling re-layout-free access of both PIM and SoC processor benefits LLM inference on various on-device LLM tasks, including short conversation and code autocompletion, reducing the time-to-first-token by 2.37× and 2.63×, respectively, over the SoC-PIM baseline.

## 中文摘要

大语言模型（LLM）端侧推理的兴起迅速加剧了边缘设备对访存密集型运算的需求。尽管基于 DRAM 的存内处理（PIM）是克服内存墙的一种有前景的方案，但边缘设备内存容量有限，要求 PIM 同时充当计算单元和存储设备。这种支持 PIM 的内存使张量以可执行 PIM 操作的方式划分并放置到 DRAM 存储体变得复杂。值得注意的是，我们强调 LLM 权重需要同时能被 PIM 和片上系统（SoC）处理器访问，因为相同的权重既用于适合 SoC 的 GEMM 运算，也用于适合 PIM 的 GEMV 运算。这要求 PIM 与 SoC 处理器采用不同的内存映射，从而在两者之间切换时可能产生重新布局开销。为应对这一挑战，我们提出 FACIL，一种灵活的 DRAM 地址映射方案，它能在 DRAM 中高效地放置张量以执行 PIM 操作，同时允许 SoC 处理器使用连续的虚拟地址访问相同的数据。FACIL 由两部分组成：（i）一个内存控制器，为每个大页的页内偏移位分配不同的 DRAM 地址映射；（ii）一个用户级库，用于确定合适的 DRAM 地址映射。我们证明，使 PIM 与 SoC 处理器都能无重新布局地访问数据，可惠及各种端侧 LLM 任务上的 LLM 推理，包括简短对话和代码自动补全，相比 SoC-PIM 基线分别把首词元时延降低 2.37 倍和 2.63 倍。
