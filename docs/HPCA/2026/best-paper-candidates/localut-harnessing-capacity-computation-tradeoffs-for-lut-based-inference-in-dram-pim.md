---
title: "LoCaLUT: Harnessing Capacity–Computation Tradeoffs for LUT-Based Inference in DRAM-PIM"
description: "HPCA 2026 · Best Paper Candidates"
tags:
  - "HPCA2026"
  - "Best Paper Candidates"
---

# LoCaLUT: Harnessing Capacity–Computation Tradeoffs for LUT-Based Inference in DRAM-PIM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Best Paper Candidates。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Best Paper Candidates</p>
</div>

**论文链接**：
**作者**：Junguk Hong Seoul National University , Changmin Shin Seoul National University , Sukjin Kim Seoul National University , Si Ung Noh Seoul National University , Taehee Kwon Seoul National University , Seongyeon Park Seoul National University , Hanjun Kim Yonsei University , Youngsok Kim Yonsei University , Jinho Lee Seoul National University
**会议**：HPCA 2026

---

## 中文标题

LoCaLUT：在 DRAM-PIM 中利用容量与计算权衡实现基于 LUT 的推理

## 英文摘要

Lookup tables (LUTs) have recently gained attention as an alternative compute mechanism that maps input operands to precomputed results, eliminating the need for arithmetic logic. LUTs not only reduce logic complexity, but also naturally support diverse numerical precisions without requiring separate circuits for each bitwidth—an increasingly important feature in quantized DNNs. This creates a favorable tradeoff in PIM: memory capacity can be used in place of logic to increase computational throughput, aligning well with DRAM-PIM architectures that offer high bandwidth and easily available memory but limited logic density. In this work, we explore this capacity-computation tradeoff in LUT-based PIM designs, where memory capacity is traded for performance by packing multiple MAC operations into a single LUT lookup. Building on this insight, we propose LOCALUT, a PIM-based design for efficient low-bit quantized DNN inference using operation-packed LUTs. First, we observe that these LUTs contain extensive redundancy and introduce LUT canonicalization, which eliminates duplicate entries to reduce LUT size. Second, we propose reordering LUT, a lightweight auxiliary LUT that remaps weight vectors to their canonical form required by LUT canonicalization with a simple LUT lookup. Third, we propose LUT slice streaming, a novel execution strategy that exploits the DRAM-buffer hierarchy by streaming only relevant LUT columns into the buffer and reusing them across multiple weight vectors. Evaluated on a real system based on UPMEM devices, we demonstrate a geometric mean speedup of 1.82× across various numeric precisions and DNN models. We believe LOCALUT opens a path toward scalable, low-logic PIM designs tailored for LUT-based DNN inference. Our implementation of LOCALUT is available at https://github.com/AIS-SNU/LoCaLUT.

## 中文摘要

查找表（LUT）近来作为一种替代计算机制受到关注：它把输入操作数映射为预计算结果，无需算术逻辑。LUT 不仅降低逻辑复杂度，还天然支持多种数值精度，无需为每种位宽配备独立电路——这一特性在量化 DNN 中日益重要。这在 PIM 中形成有利权衡：可用内存容量替代逻辑来提升计算吞吐，与提供高带宽、内存易得但逻辑密度受限的 DRAM-PIM 架构高度契合。本工作探索基于 LUT 的 PIM 设计中的容量与计算权衡，通过把多次 MAC 操作打包进单次 LUT 查找，以内存容量换取性能。基于此洞见，我们提出 LOCALUT，一种使用操作打包 LUT 的高效低位量化 DNN 推理 PIM 设计。第一，我们观察到这些 LUT 存在大量冗余，提出 LUT 规范化以消除重复条目、减小 LUT 规模。第二，我们提出重排序 LUT，一个轻量辅助 LUT，通过简单查找把权重向量重映射为规范化所需的规范形式。第三，我们提出 LUT 切片流式，一种利用 DRAM 与缓冲区层次结构的新执行策略，仅把相关 LUT 列流入缓冲区并在多个权重向量间复用。在基于 UPMEM 设备的真实系统上评估，我们在多种数值精度与 DNN 模型上取得 1.82 倍的几何平均加速比。我们相信 LOCALUT 为面向 LUT 式 DNN 推理的可扩展、低逻辑 PIM 设计开辟了道路。实现见 https://github.com/AIS-SNU/LoCaLUT。
