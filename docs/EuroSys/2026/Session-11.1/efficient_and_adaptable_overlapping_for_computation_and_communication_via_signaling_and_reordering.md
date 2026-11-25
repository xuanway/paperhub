---
title: "Efficient and Adaptable Overlapping for Computation and Communication via Signaling and Reordering"
description: "EuroSys 2026 · Distributed Training & Collective Communication · Ke Hong (Tsinghua University), Xiuhong Li (Peking University), Minxu Liu (Infini"
tags:
  - "EuroSys2026"
  - "Distributed Training & Collective Communication"
---

# Efficient and Adaptable Overlapping for Computation and Communication via Signaling and Reordering

**中文标题：** 通过信号与重排序实现高效且可适配的计算通信重叠

**所属 Session：** [Session 11.1: Distributed Training & Collective Communication](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Training & Collective Communication。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Training & Collective Communication</p>
</div>

**作者**：Ke Hong (Tsinghua University), Xiuhong Li (Peking University), Minxu Liu (Infinigence-AI), Qiuli Mao (Infinigence-AI), Tianqi Wu (Tsinghua University), Zixiao Huang (Tsinghua University), Lufang Chen (Infinigence-AI), Zhong Wang (Tsinghua University), Yichong Zhang (Tsinghua University), Zhenhua Zhu (Tsinghua University), Guohao Dai (Shanghai Jiao Tong University), Yu Wang (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769370)

## 英文摘要

Generative models have achieved remarkable success across various applications, driving the demand for multi-GPU computing. Inter-GPU communication becomes a bottleneck in multi-GPU computing systems, particularly on consumer-grade GPUs. By exploiting concurrent hardware execution, overlapping computation and communication latency becomes an effective technique for mitigating the communication overhead. We identify that an efficient and adaptable overlapping design should satisfy (1) tile-wise overlapping to maximize the overlapping opportunity, (2) interference-free computation to maintain the original computational performance, and (3) communication agnosticism to reduce the development burden against varying communication primitives. Nevertheless, current designs fail to simultaneously optimize for all of those features.

To address the issue, we propose an overlapping design, named FlashOverlap, characterized by tile-wise overlapping, interference-free computation, and communication agnosticism. FlashOverlap utilizes a novel signaling mechanism: when part of the output finishes, the computation kernel sends a signal to trigger the communication of that part, while continuing the computation of the remaining part (interference-free computation). Consequently, the communication of the finished part and the computation of the remaining part can be overlapped. On top of the signaling mechanism, FlashOverlap comprises two key components: (1) the determination of the signaling timing to boost the overlap efficiency (tile-wise overlapping), and (2) a pre-communication reordering to create the contiguous address for finished data, enabling communication by simply calling NCCL [32] APIs (communication agnosticism), and a post-communication reordering to correct the data order. Experiments show that FlashOverlap achieves up to 1.65× speedup through overlap, outperforming existing works in most cases. Code is available at https://github.com/ infinigence/FlashOverlap.

## 中文摘要

生成模型已在各类应用中取得显著成功，推动了对多 GPU 计算的需求。在多 GPU 计算系统中，GPU 间通信成为瓶颈，在消费级 GPU 上尤为明显。通过利用硬件的并发执行能力，重叠计算与通信延迟成为缓解通信开销的有效技术。我们指出，高效且可适配的重叠设计应满足：(1) 分块重叠，以最大化重叠机会；(2) 无干扰计算，以保持原有计算性能；(3) 通信无关性，以减轻适配不同通信原语带来的开发负担。然而，现有设计无法同时优化上述所有特性。

为解决该问题，我们提出一种名为 FlashOverlap 的重叠设计，其特点是分块重叠、无干扰计算与通信无关性。FlashOverlap 采用一种新颖的信号机制：当部分输出完成时，计算内核发送信号以触发该部分的通信，同时继续计算剩余部分（无干扰计算）。因此，已完成部分的通信与剩余部分的计算可以重叠进行。在信号机制之上，FlashOverlap 包含两个关键组件：(1) 确定发信号的时机以提升重叠效率（分块重叠）；(2) 通信前重排序，为已完成的数据构造连续地址，从而只需调用 NCCL [32] API 即可完成通信（通信无关性），以及通信后重排序以纠正数据顺序。实验表明，FlashOverlap 通过重叠最高获得 1.65 倍加速，在多数情况下优于现有工作。代码见 https://github.com/infinigence/FlashOverlap。

**英文关键词：** Multi-GPU system, communication, overlap

**中文关键词：** 多 GPU 系统、通信、重叠

## 代码与研究制品

- [代码](https://github.com/infinigence/FlashOverlap)（论文摘要提供）

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
