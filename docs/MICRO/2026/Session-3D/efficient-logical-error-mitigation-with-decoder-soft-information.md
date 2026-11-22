---
title: "Efficient Logical Error Mitigation with Decoder Soft Information"
description: "MICRO 2026 · Session 3D · 利用解码器软信息实现高效逻辑错误缓解"
tags:
  - "MICRO2026"
---

# Efficient Logical Error Mitigation with Decoder Soft Information

**中文标题：** 利用解码器软信息实现高效逻辑错误缓解

**所属 Session：** [Session 3D](index.md) · [MICRO 2026](../index.md)

**作者：** Zeyuan Zhou, Shaun Pexton, Aleksander Kubica, Yongshan Ding

**来源：** MICRO 2026，pp. 1269–1283；[DOI](https://doi.org/10.1109/MICRO67795.2026.00096)

## 英文摘要

Quantum error mitigation (QEM) is typically viewed as a suite of practical techniques for today's noisy intermediate-scale quantum devices, with limited relevance once quantum error correction (QEC) becomes available. Recent work has shown that QEM can still reduce errors further once QEC is available. One bottleneck to implementing it is that logical-level QEM requires knowledge of the logical noise channel, and standalone characterization requires high additional quantum resources. In this work, we show that QEC decoders already compute this information, enabling logical-level QEM that is even more efficient than on physical devices. We introduce a framework for logical-level QEM that leverages soft information naturally produced by QEC decoders, requiring no additional data, hardware modifications, or quantum experiments beyond what QEC syndrome measurements already provide. Within this framework, we develop and analyze three logical-level QEM techniques: post-selection and runtime abort policy, probabilistic error cancellation, and zero-noise extrapolation. Our techniques can reduce logical error rates by more than 100 times while discarding only 0.1 percent of shots; they also provide in situ characterization of logical channels for QEM protocols. As a proof of principle, we benchmark our approach using a surface-code architecture and two state-of-the-art decoders based on tensor-network contraction and minimum-weight perfect matching, validating under both code-capacity and circuit-level noise models. We evaluate the performance of logical-level QEM on random Clifford circuits and molecular simulation algorithms and find that, compared with previous approaches relying on QEC only or QEC combined with QEM, we achieve 43-64 percent spacetime overhead savings across expectation-value estimation benchmarks, without additional characterization shot overhead. Our results demonstrate that logical-level QEM with QEC decoder soft information can reliably improve logical performance, underscoring the efficiency and usefulness of QEM techniques for fault-tolerant quantum computers.

## 中文摘要

量子纠错（QEM）通常被视为适用于当今嘈杂的中型量子设备的一套实用技术，一旦量子纠错（QEC）可用，其相关性就有限。最近的研究表明，一旦 QEC 可用，QEM 仍然可以进一步减少错误。实现它的一个瓶颈是逻辑级 QEM 需要了解逻辑噪声通道，而独立表征需要大量额外的量子资源。在这项工作中，我们表明 QEC 解码器已经计算了这些信息，从而实现了比物理设备更高效的逻辑级 QEM。我们引入了一个逻辑级 QEM 框架，该框架利用 QEC 解码器自然产生的软信息，除了 QEC 综合症测量已经提供的功能之外，不需要额外的数据、硬件修改或量子实验。在此框架内，我们开发和分析了三种逻辑级 QEM 技术：选择后和运行时中止策略、概率错误消除和零噪声外推。我们的技术可以将逻辑错误率降低 100 倍以上，同时仅丢弃 0.1% 的镜头；它们还为 QEM 协议提供逻辑通道的原位表征。作为原理证明，我们使用表面码架构和两个基于张量网络收缩和最小权重完美匹配的最先进解码器对我们的方法进行基准测试，在代码容量和电路级噪声模型下进行验证。我们评估了逻辑级 QEM 在随机 Clifford 电路和分子模拟算法上的性能，发现与之前仅依赖 QEC 或 QEC 与 QEM 相结合的方法相比，我们在期望值估计基准上实现了 43-64% 的时空开销节省，而无需额外的表征镜头开销。我们的结果表明，具有 QEC 解码器软信息的逻辑级 QEM 可以可靠地提高逻辑性能，强调了 QEM 技术在容错量子计算机中的效率和实用性。

## 中文关键词

量子纠错；量子误差缓解；译码器软信息；表面码；容错量子计算

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3D](index.md) · [MICRO 2026 主页](../index.md)
