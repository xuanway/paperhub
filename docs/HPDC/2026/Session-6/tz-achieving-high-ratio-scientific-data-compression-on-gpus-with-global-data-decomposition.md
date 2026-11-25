---
title: "TZ: Achieving High-Ratio Scientific Data Compression on GPUs with Global Data Decomposition"
description: "HPDC 2026 · Session 6 — Scientific Data Compression"
tags:
  - "HPDC2026"
  - "Session 6"
  - "Scientific Data Compression"
---

# TZ: Achieving High-Ratio Scientific Data Compression on GPUs with Global Data Decomposition

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 6</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807811)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#YangLSRDUZLCZ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#YangLSRDUZLCZ26)

**作者**：Zhuoxun Yang, Ruoyu Li, Amit Subrahmanya, Vishwas Rao, Sheng Di, Robert Underwood, Longtao Zhang, Jinyang Liu, Franck Cappello, Kai Zhao

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 6 — Scientific Data Compression（2026年7月15日 11:30–12:30 · Session Chair：Jay Lofstead）

---

## 英文摘要

As high-performance computing shifts toward GPU-accelerated exascale systems, the exponential growth of scientific data poses severe challenges to both storage capacity and I/O bandwidth. While current GPU-based lossy compressors attempt to address this by porting CPU algorithms to the device, they rely heavily on blockwise spatial decomposition to fit GPU parallelism. This approach suffers from a fundamental locality barrier: by partitioning data into independent blocks, these methods fail to capture global correlations and fragment the unified data patterns required for effective coding, severely limiting compression ratios. In this paper, we propose TZ, a novel GPU-native error-bounded lossy compressor that breaks this ceiling by adopting global Tucker decomposition. By prioritizing global spectral energy compaction over local approximation, TZ naturally maximizes the compression potential for scientific datasets. To render this computationally intensive approach practical for high-throughput GPU workflows, we introduce a highly optimized adaptive randomized SVD engine. This design allows TZ to achieve the superior compression ratios of global spectral decomposition while maintaining competitive execution speeds. Furthermore, the global processing nature of TZ enables a unified quantization and coding scheme that eliminates block artifacts and metadata overhead. Evaluation on production-scale scientific datasets demonstrates that TZ achieves approximately 10× higher compression ratios than state-of-the-art GPU compressors under the same error bound, while maintaining competitive, high-throughput performance.

## 中文摘要

随着高性能计算向 GPU 加速的百亿亿次系统演进，科学数据的指数级增长对存储容量和 I/O 带宽都构成严峻挑战。当前基于 GPU 的有损压缩器试图通过将 CPU 算法移植到设备上来应对，但它们严重依赖块状空间分解以适配 GPU 并行性。这种做法存在根本性的局部性障碍：通过将数据划分为独立块，这些方法无法捕捉全局相关性，并割裂了有效编码所需的统一数据模式，严重限制了压缩比。本文提出 TZ，一种新颖的 GPU 原生误差有界有损压缩器，它采用全局 Tucker 分解来突破这一上限。通过优先考虑全局谱能量紧致化而非局部近似，TZ 自然地最大化科学数据集的压缩潜力。为使这种计算密集的方法适用于高吞吐 GPU 工作流，我们引入高度优化的自适应随机化 SVD 引擎。该设计使 TZ 在保持有竞争力的执行速度的同时，实现全局谱分解的优异压缩比。此外，TZ 的全局处理特性支持统一的量化与编码方案，消除了块伪影和元数据开销。在生产规模科学数据集上的评估表明，在相同误差界下，TZ 的压缩比约为最先进 GPU 压缩器的 10 倍，同时保持有竞争力的高吞吐性能。

---

[← 返回 Session 6 — Scientific Data Compression](index.md)
