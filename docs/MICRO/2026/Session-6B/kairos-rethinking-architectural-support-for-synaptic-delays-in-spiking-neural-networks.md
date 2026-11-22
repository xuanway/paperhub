---
title: "Kairos: Rethinking Architectural Support for Synaptic Delays in Spiking Neural Networks"
description: "MICRO 2026 · Session 6B · Kairos：重新思考脉冲神经网络中突触延迟的架构支持"
tags:
  - "MICRO2026"
  - "Neural Networks"
---

# Kairos: Rethinking Architectural Support for Synaptic Delays in Spiking Neural Networks

**中文标题：** Kairos：重新思考脉冲神经网络中突触延迟的架构支持

**所属 Session：** [Session 6B](index.md) · [MICRO 2026](../index.md)

**作者：** Amirreza Movahedin, Lennart P. L. Landsmeer, Said Hamdioui, Christos Strydis

**来源：** MICRO 2026，pp. 1932–1948；[DOI](https://doi.org/10.1109/MICRO67795.2026.00136)

## 英文摘要

Recent advances in training Spiking Neural Networks (SNNs) have promoted variable-length synaptic delays to a first-class network parameter, improving temporal expressiveness and performance on temporally rich tasks. Yet, architectural support for long-range delays remains highly inefficient. Existing SNN accelerators follow two design approaches, dictated by whether spike delays are applied before or after the synapses. Presynaptic designs store delayed spikes compactly but perform costly, iterative source-to-destination, synaptic resolutions across timesteps. Postsynaptic designs resolve spike destinations immediately but rely on delay buffers whose memory cost and underutilization grow with the maximum supported delay. In effect, both design approaches struggle to scale efficiently to larger, trainable synaptic delays. Here, we present Kairos, a new design approach that rethinks delay handling at the architectural level by combining compressed presynaptic storage for long-term spikes with a bounded postsynaptic short-term delivery window. This combination allows for a novel spike-delivery method where source-to-destination spike resolution is only performed periodically. At the microarchitectural level, Kairos further improves performance by handling spike deliveries in parallel, based on the range of encountered delays per executed workload, in addition to aggressive eviction of delivered spikes. To evaluate Kairos, we build a configurable, cycle-level, architectural simulator that models Kairos and other design approaches for fair energy, latency, and area comparisons and evaluate all of them across diverse SNN benchmarks. Kairos achieves on average 78× and 2.5× improvements in the energy-latency product over parallel presynaptic and postsynaptic designs, respectively, while demonstrating sublinear scaling with an increasing supported delay range. Furthermore, Kairos supports at least 5× larger delays at the same memory and energy budgets as existing postsynaptic designs. Specifically against Intel Loihi 2, Kairos exhibits a 4.6× better energy-latency product.

## 中文摘要

训练脉冲神经网络 (SNN) 的最新进展已将可变长度突触时延提升为一流的网络参数，从而提高了时间表达能力和时间丰富任务的性能。然而，对长距离时延的架构支持仍然非常低效。现有的 SNN 加速器遵循两种设计方法，具体取决于是在突触之前还是之后应用尖峰时延。突触前设计紧凑地存储时延尖峰，但执行成本高昂、迭代源到目的地、跨时间步长的突触分辨率。突触后设计立即解决尖峰目的地，但依赖于时延缓冲区，其内存成本和未充分利用随着最大支持时延的增加而增加。实际上，这两种设计方法都难以有效地扩展到更大的、可训练的突触时延。在这里，我们提出 Kairos，一种新的设计方法，通过将长期尖峰的压缩突触前存储与有界突触后短期传递窗口相结合，重新思考架构级别的时延处理。这种组合允许一种新颖的尖峰传递方法，其中仅定期执行源到目的地尖峰解析。在微架构层面，Kairos 除了积极驱逐已交付的峰值之外，还根据每个执行工作负载遇到的时延范围并行处理峰值交付，进一步提高了性能。为了评估 Kairos，我们构建了一个可配置的周期级架构模拟器，对 Kairos 和其他设计方法进行建模，以实现公平的能量、时延和面积比较，并在不同的 SNN 基准测试中评估所有这些方法。与并行突触前和突触后设计相比，Kairos 的能量时延乘积分别平均提高了 78 倍和 2.5 倍，同时展示了亚线性缩放以及支持的时延范围的增加。此外，Kairos 在相同的内存和能量预算下支持比现有突触后设计至少大 5 倍的时延。特别针对 Intel Loihi 2，Kairos 展示了 4.6 倍更好的能量时延积。

## 中文关键词

加速器；神经形态计算；脉冲神经网络；突触延迟；节能计算

## 代码与研究制品

- 代码仓库：[https://gitlab.com/c7859/neurocomputing-lab/kairos](https://gitlab.com/c7859/neurocomputing-lab/kairos)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21474215](https://doi.org/10.5281/zenodo.21474215)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6B](index.md) · [MICRO 2026 主页](../index.md)
