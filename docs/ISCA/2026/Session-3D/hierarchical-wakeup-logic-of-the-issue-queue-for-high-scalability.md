---
title: "Hierarchical Wakeup Logic of the Issue Queue for High Scalability"
description: "ISCA 2026 · Session 3D · Hierarchical Wakeup Logic of the Issue Queue for High Scalability"
tags:
  - "ISCA2026"
  - "Session 3D"
  - "Microarchitexture"
---

# Hierarchical Wakeup Logic of the Issue Queue for High Scalability

**中文标题：** 面向高可扩展性的发射队列分层唤醒逻辑

**所属 Session：** [Session 3D](index.md) · [ISCA 2026](../index.md)

**作者：** Hideki Ando, Hajime Shimada

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The reduction of the critical-path delay of processor circuits is essential not only for sustaining high clock frequency but also for enabling microarchitectural scaling toward higher IPC. A general approach to reducing cycle time is pipelining long-delay circuits. However, applying pipelining to the issue queue (IQ) is inappropriate because pipelining the wakeup–select loop, one of the processor’s critical paths, prevents dependent instructions from being issued back-to-back, thereby degrading IPC. As modern processors pursue higher IPC through wider issue and larger instruction windows, the IQ size must scale accordingly. However, enlarging the IQ significantly increases the delay of the wakeup logic, making such scaling difficult under practical timing constraints. In this paper, we propose a hierarchical wakeup logic (HWL), where the IQ is logically segmented, each segment has a small non-pipelined level-1 (L1) wakeup logic, and full-size pipelined level-2 (L2) wakeup logic is placed behind the L1s. Wakeup is performed using L1, if possible, and L2 otherwise. The cycle time is reduced because the L1 size is small and L2 is pipelined. A fundamental attempt is made to dispatch an instruction (written to the IQ) to its producer’s segment to complete wakeup–select in a single cycle, but it is not always possible because of the L1 size limit. This causes IPC degradation. To mitigate IPC degradation, we propose a dispatch scheme, which we call the HWL-structure-aware dispatch (HSD) scheme, that uses the L1s efficiently. We enhance the HSD scheme using a scheme to adaptively choose dispatch behavior, depending on the degree of L1 contentions. Through evaluation using SPEC2017 benchmark programs, we found that the HWL shortens the IQ cycle time by 53%, while incurring only 0.9% degradation in IPC. These results indicate that reducing IQ wakeup delay can alleviate a key timing bottleneck and enable more scalable microarchitectural configurations.

## 中文摘要

降低处理器电路的关键路径延迟，不仅对维持高时钟频率至关重要，也是实现微架构向更高 IPC 扩展的必要条件。降低周期时间的一种通用方法是对长延迟电路进行流水化。然而，将流水化应用于发射队列（issue queue, IQ）并不合适，因为对唤醒—选择（wakeup–select）环路（处理器的关键路径之一）进行流水化会使相关指令无法背靠背发射，从而降低 IPC。随着现代处理器通过更宽的发射和更大的指令窗口追求更高的 IPC，IQ 的规模也必须相应扩展。然而，增大 IQ 会显著增加唤醒逻辑的延迟，使得在实际时序约束下难以实现这样的扩展。在本文中，我们提出一种分层唤醒逻辑（hierarchical wakeup logic, HWL）：将 IQ 在逻辑上分段，每个分段拥有一个小型非流水化的第一级（L1）唤醒逻辑，而在各 L1 之后放置全尺寸的流水化第二级（L2）唤醒逻辑。唤醒尽可能通过 L1 完成，否则通过 L2 完成。由于 L1 规模小且 L2 已流水化，周期时间得以缩短。我们做了一项基础性尝试：将一条指令（写入 IQ 的指令）派发到其生产者的分段，以便在单个周期内完成唤醒—选择，但由于 L1 的规模限制，这并非总能做到。这会导致 IPC 下降。为缓解 IPC 下降，我们提出一种派发方案，称为 HWL 结构感知派发（HWL-structure-aware dispatch, HSD）方案，它高效地利用各 L1。我们进一步用一种根据 L1 争用程度自适应选择派发行为的方案来增强 HSD。通过使用 SPEC2017 基准程序进行评估，我们发现 HWL 将 IQ 周期时间缩短了 53%，而仅带来 0.9% 的 IPC 下降。这些结果表明，降低 IQ 唤醒延迟可以缓解一个关键的时序瓶颈，并支持更具可扩展性的微架构配置。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3D](index.md) · [返回 ISCA 2026](../index.md)
