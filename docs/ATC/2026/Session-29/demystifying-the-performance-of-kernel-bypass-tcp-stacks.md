# Demystifying the Performance of Kernel-Bypass TCP Stacks

**中文标题**：揭示内核旁路 TCP 协议栈的性能

**所属 Session**：[Session 29: Networking II](index.md) · [ATC 2026](../index.md)

**作者**：Minhu Wang (Tsinghua University), Mingwei Xu (Quan Cheng Laboratory), Jianping Wu (Tsinghua University)

## 英文摘要
Kernel-bypass TCP stacks (uTCPs) typically deliver severalfold higher throughput and an order of magnitude lower tail latency than in-kernel TCP (kTCP), yet their performance advantages still lack comprehensive and systematic explanation. Existing analyses with side-by-side benchmarking and profiling fail to identify and disentangle individual factors’ contributions, as stacks differ in many aspects simultaneously. This paper instead conducts an iterative ablation study that identifies performance factors from uTCPs and reproduces them in kTCP one by one to estimate their contributions. Focusing on small-message RPC scenarios, we identify 11 such factors that jointly close the 3.81× per-request processing time gap between kTCP and the fastest uTCP to within 5%, while also achieving comparable latency. Our study reveals that uTCPs benefit most from feature specialization (closing 49% of the gap): they shed stack functionality such as security hardening and protocol completeness, resulting in reduced instruction count. Meanwhile, uTCPs apply architectural improvements (closing 35% of the gap) by achieving better data locality and scheduling for higher execution efficiency. The remaining implementation optimizations close the final 16% of the gap. Notably, kernel-bypass itself is neither sufficient nor necessary: eliminating syscall overhead accounts for only ∼5% of the gap, and all identified factors can be reproduced within the kernel. Overall, no single factor dominates the gap. Crucially, most contributors involve a deployment tradeoff: uTCPs gain speed by sacrificing generality, security, or resource sharing.

## 中文摘要
内核旁路 TCP 协议栈（uTCP）通常比内核内 TCP（kTCP）提供数倍的吞吐和低一个数量级的尾延迟，然而其性能优势仍缺乏全面而系统的解释。现有通过并排基准测试与性能剖析进行的分析无法识别并拆分各个因素的贡献，因为协议栈在许多方面同时存在差异。本文转而开展迭代式消融研究，从 uTCP 中识别性能因素，并逐一在 kTCP 中复现这些因素以估计其贡献。聚焦小消息 RPC 场景，我们识别出 11 个此类因素，它们共同将 kTCP 与最快 uTCP 之间 3.81× 的每请求处理时间差距缩小到 5% 以内，同时达到相当的延迟。我们的研究揭示，uTCP 受益最多的是功能特化（缩小了 49% 的差距）：它们去除了协议栈功能，如安全加固与协议完整性，从而减少了指令数。同时，uTCP 通过实现更好的数据局部性与调度以获得更高的执行效率，应用了架构层面的改进（缩小 35% 的差距）。其余实现层面的优化缩小了最后 16% 的差距。值得注意的是，内核旁路本身既不充分也不必要：消除系统调用开销仅占差距的约 5%，且所有识别出的因素都能在内核内复现。总体而言，没有单一因素主导该差距。关键的是，大多数贡献因素都涉及部署权衡：uTCP 通过牺牲通用性、安全性或资源共享来换取速度。

## 英文关键词
TCP, kernel bypass, network performance, ablation study

## 中文关键词
TCP，内核旁路，网络性能，消融研究

[返回 Session 29](index.md) · [返回 ATC 2026](../index.md)
