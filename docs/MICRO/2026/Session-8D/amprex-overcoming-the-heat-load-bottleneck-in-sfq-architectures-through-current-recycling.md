---
title: "AmpReX: Overcoming the Heat Load Bottleneck in SFQ Architectures through Current Recycling"
description: "MICRO 2026 · Session 8D · AmpReX：通过电流回收克服单磁通量子架构的热负载瓶颈"
tags:
  - "MICRO2026"
  - "Thermal Management"
---

# AmpReX: Overcoming the Heat Load Bottleneck in SFQ Architectures through Current Recycling

**中文标题：** AmpReX：通过电流回收克服单磁通量子架构的热负载瓶颈

**所属 Session：** [Session 8D](index.md) · [MICRO 2026](../index.md)

**作者：** Tara Renduchintala, Tejumadejesu Oluwadamilare, Daniel Wong, Sasan Razmkhah, Beyza Zeynep Ucpinar, Eby Friedman, Murali Annavaram

**来源：** MICRO 2026，pp. 3147–3161；[DOI](https://doi.org/10.1109/MICRO67795.2026.00212)

## 英文摘要

Single Flux Quantum (SFQ) superconducting technology offers compelling advantages over CMOS, including ultra-high operating frequencies and extremely low switching energy. Prior works have proposed superconducting SIMD/vector execution designs, such as machine learning accelerators, to exploit this low switching energy. However, SFQ architectures are fundamentally limited by the heat load imposed by DC bias current delivery into the cryogenic environment: since both active power dissipation and passive thermal conduction scale with bias current, the total deliverable current constrains the number of vector execution units supported, posing a critical barrier to scalable SFQ-based SIMD architectures. We propose AmpReX, a SIMD-oriented SFQ architecture that leverages current recycling to enable multiple SIMD execution units performing identical operations to share a common bias current, enhanced with dynamic bias current provisioning: since each vector operation activates a different number of SFQ gates, this supplies only the required current per operation rather than statically provisioning for the worst case. To mitigate the performance overhead of dynamic current adjustment, we introduce a bias-current-aware instruction scheduler that minimizes switching frequency and overlaps current ramp-up with useful computation, together providing a coordinated hardware–software framework for managing bias current. Evaluation shows AmpReX reduces average bias current, and therefore active cryogenic heat load, by up to 2.6x compared to a strong static current recycling baseline, with a geometric mean slowdown under 20%. These results demonstrate bias-current-aware design is essential for scalable, heat-efficient SFQ-based parallel computing.

## 中文摘要

单通量量子 (SFQ) 超导技术与 CMOS 相比具有引人注目的优势，包括超高工作频率和极低的开关能量。先前的工作已经提出了超导 SIMD/矢量执行设计，例如机器学习加速器，以利用这种低开关能量。然而，SFQ 架构从根本上受到向低温环境传输 DC 偏置电流所施加的热负载的限制：由于有源功耗和无源热传导均随偏置电流变化，因此总的可传输电流限制了支持的矢量执行单元的数量，这对基于 SFQ 的 SIMD 架构的可扩展构成了关键障碍。我们提出了 AmpReX，一种面向 SIMD 的 SFQ 架构，它利用电流复用来使多个 SIMD 执行单元执行相同的操作以共享公共偏置电流，并通过动态偏置电流配置进行增强：由于每个向量操作激活不同数量的 SFQ 门，因此这仅提供每个操作所需的电流，而不是在最坏的情况下静态配置。为了减轻动态电流调整的性能开销，我们引入了一种偏置电流感知指令调度程序，该调度程序可以最大限度地减少开关频率，并将电流上升与有用的计算重叠，同时提供一个协调的硬件软件框架来管理偏置电流。评估显示，与强静态电流复用基线相比，AmpReX 可降低平均偏置电流，从而降低主动低温热负荷高达 2.6 倍，几何平均减速率低于 20%。这些结果表明，偏置电流感知设计对于可扩展、热效率高的基于 SFQ 的并行计算至关重要。

## 中文关键词

超导计算；单磁通量子处理器；电流复用；热负载

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8D](index.md) · [MICRO 2026 主页](../index.md)
