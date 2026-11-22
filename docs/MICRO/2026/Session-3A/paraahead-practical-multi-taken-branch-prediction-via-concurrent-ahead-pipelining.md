---
title: "ParaAhead: Practical Multi-Taken Branch Prediction via Concurrent Ahead Pipelining"
description: "MICRO 2026 · Session 3A · ParaAhead：通过并发前瞻流水线实现实用的多跳转分支预测"
tags:
  - "MICRO2026"
---

# ParaAhead: Practical Multi-Taken Branch Prediction via Concurrent Ahead Pipelining

**中文标题：** ParaAhead：通过并发前瞻流水线实现实用的多跳转分支预测

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Hongyu Guo, Hongze Tan, Tingting Zhang, Tianyi Liu, Fuxin Zhang

**来源：** MICRO 2026，pp. 960–974；[DOI](https://doi.org/10.1109/MICRO67795.2026.00077)

## 英文摘要

As out-of-order core pipelines continue to widen, branch prediction bandwidth becomes increasingly critical. Scaling the bandwidth is challenging because taken branches serialize successive predictor lookups. A straightforward approach is to predict multiple taken branches per cycle. However, prior multi-taken schemes fall into two categories, each with different limitations. Entry-encoded designs pack local control-flow graph information into BTB entries, incurring redundant storage and restricting branch-type coverage. Parallel-lookup designs issue multiple lookups per cycle in parallel but rely on a single-cycle Next Fetch Predictor (NFP), whose tight timing budget and inter-lookup dependence constrain NFP accuracy and further limit effective prediction bandwidth. We present ParaAhead, a practical multi-taken branch prediction mechanism that performs two independent predictor lookups per cycle, each producing one instruction-stream prediction and thereby enabling prediction of up to two taken branches of any type per cycle. The key component of ParaAhead is a two-cycle ahead-pipelined NFP that concurrently generates predictions at two different lookahead distances. A farther lookahead (4-ahead prediction) eliminates the serial dependence between consecutive same-cycle lookups, sustaining two predictor lookups per cycle. The nearer lookahead (2-ahead prediction), which incorporates the most recent branch context, continuously validates the farther speculation and corrects it when necessary, converting nominal dual-lookup throughput into stable effective prediction bandwidth. To realize these dual lookups with single-ported SRAMs, we adopt a bank-interleaved predictor organization that maps consecutive accesses to distinct banks. On SPEC CPU 2017, ParaAhead improves geometric mean IPC by 8.5% over a storage-matched baseline. ParaAhead captures 81.7% of an idealized upper bound and outperforms a recent multi-taken design (MB-BTB) by 5.03% with less storage overhead. Additional results on SPEC CPU 2026 and GAP confirm ParaAhead's generality across diverse workloads.

## 中文摘要

随着无序核心管道不断加宽，分支预测带宽变得越来越重要。扩展带宽具有挑战性，因为所采取的分支会序列化连续的预测器查找。一种简单的方法是预测每个周期的多个采取的分支。然而，现有的多采取方案分为两类，每一类都有不同的限制。条目编码设计将本地控制流图信息打包到 BTB 条目中，从而产生冗余存储并限制分支类型覆盖。并行查找设计在每个周期并行发出多个查找，但依赖于单周期下一个提取预测器 (NFP)，其严格的时序预算和查找间依赖性限制了 NFP 的准确性，并进一步限制了有效的预测带宽。我们提出了 ParaAhead，一种实用的多采用分支预测机制，它在每个周期执行两次独立的预测器查找，每个查找产生一个指令流预测，从而能够在每个周期预测最多两个任何类型的采用分支。 ParaAhead 的关键组件是两个周期的超前流水线 NFP，它同时生成两个不同超前距离的预测。进一步的超前预测（4 超前预测）消除了连续同周期查找之间的串行依赖性，每个周期维持两次预测器查找。较近的前瞻（2-ahead 预测）结合了最新的分支上下文，不断验证较远的推测并在必要时进行纠正，将标称双查找吞吐量转换为稳定的有效预测带宽。为了使用单端口 SRAM 实现这些双重查找，我们采用了存储体交错预测器组织，将连续访问映射到不同的存储体。在 SPEC CPU 2017 上，ParaAhead 将几何平均 IPC 比存储匹配的基准提高了 8.5%。 ParaAhead 捕获了理想化上限的 81.7%，并且比最近的多采取设计 (MB-BTB) 性能高出 5.03%，并且存储开销更少。 SPEC CPU 2026 和 GAP 的其他结果证实了 ParaAhead 在不同工作负载中的通用性。

## 中文关键词

分支预测；多跳转分支预测；超前流水线；并发预测

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
