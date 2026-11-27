---
title: "μShare: Non-Intrusive Kernel Co-Locating on NVIDIA GPUs"
description: "HPCA 2026 · GPU Kernel Optimization and Resource Sharing"
tags:
  - "HPCA2026"
  - "GPU Kernel Optimization and Resource Sharing"
---

# μShare: Non-Intrusive Kernel Co-Locating on NVIDIA GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Kernel Optimization and Resource Sharing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Kernel Optimization and Resource Sharing</p>
</div>

**论文链接**：
**作者**：Wenhao Huang Tianjin University , Zhaolin Duan Tianjin University , Laiping Zhao Tianjin University , Yuhao Zhang Tianjin University , Yanjie Wang Tianjin University , Yiming Li Tianjin University , Yihan Wang Tianjin University , Yichi Chen Tianjin University , Zhihang Tang Tianjin University , Kang Chen Tsinghua University , Deze Zeng China University of Geosciences , Wenxin Li Tianjin University , Keqiu Li Tianjin University
**会议**：HPCA 2026

---

## 中文标题

μShare：NVIDIA GPU 上的非侵入式内核共置

## 英文摘要

The hardware scheduler on NVIDIA GPUs is highly inefficient in utilizing micro-architectural hardware resources. It places blocks from the same kernel within the same GPU Streaming Multiprocessor (SM) core, resulting in a stacking colocating problem, where identical blocks are placed within the same SM core, saturating only a subset of intra-SM hardware resources while leaving others underutilized. The primary challenge in addressing this issue is that the NVIDIA hardware is closed-source, preventing us from directly modifying the hardware scheduler. To bridge the semantic gap between the resource demands of kernels and the scheduler, we introduce μShare, which enables intra-SM scattered colocating of kernels through a non-intrusive half-plus blocksize shaping method. It shapes the blocksize of kernels to a half-plus blocksize (i.e., slightly more than half of the SM’s thread capacity), scattering identical blocks of the same kernel across different SMs. It further adopts a time-shifted launching method to reduce intra-SM resource contention. Compared to state-of-the-art systems, μShare does not require intrusive modifications to hardware or kernel code, yet it can still improve inference throughput by 26.90%-54.09% and increases low-level hardware utilization by 38.53%–61.15%.

## 中文摘要

NVIDIA GPU 上的硬件调度器在利用微架构硬件资源方面效率很低。它把同一内核的线程块放在同一个 GPU 流式多处理器（SM）核内，造成“堆叠共置”问题：相同的线程块被放入同一 SM 核，只让部分 SM 内部硬件资源饱和，而其他资源闲置。解决这一问题的主要挑战在于 NVIDIA 硬件是闭源的，我们无法直接修改硬件调度器。为弥合内核资源需求与调度器之间的语义差距，我们提出 μShare，它通过非侵入式的“半加”块大小整形方法实现内核在 SM 内的分散共置。μShare 将内核的块大小整形为半加块大小（即略多于 SM 线程容量的一半），使同一内核的相同线程块分散到不同 SM 上。它还采用时间偏移的启动方法以减少 SM 内资源争用。与最先进的系统相比，μShare 无需对硬件或内核代码做侵入式修改，却仍能将推理吞吐提升 26.90%-54.09%，并将底层硬件利用率提高 38.53%-61.15%。
