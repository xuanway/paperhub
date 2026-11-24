---
title: "Selectively Uniform Concurrency Testing"
description: "ASPLOS 2025 · Session 6D · 选择性均匀并发测试"
tags:
  - "ASPLOS2025"
  - "Session 6D"
  - "Testing"
---

# Selectively Uniform Concurrency Testing

**中文标题：** 选择性均匀并发测试

**所属 Session：** [Session 6D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Huan Zhao (National University of Singapore), Dylan Wolff (National University of Singapore), Umang Mathur (National University of Singapore), Abhik Roychoudhury (National University of Singapore)

**单位：** National University of Singapore

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707214) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Buggy behaviors in concurrent programs are notoriously elusive, as they may manifest only in few of exponentially many possible thread interleavings. Randomized concurrency testing techniques probabilistically sample from (instead of enumerating) the vast search space and have been shown to be both an effective as well as a scalable class of algorithms for automated discovery of concurrency bugs. In this work we focus on the key desirable characteristic of black-box randomized concurrency testing algorithms — uniformity of exploration. Unfortunately, prior randomized algorithms acutely fall short on uniformity and, as a result, struggle to expose bugs that only manifest in few, infrequent interleavings. Towards this, we show that, indeed, a sampling strategy for uniformly sampling over the interleaving space, is eminently achievable with minimal additional information for broad classes of programs. Moreover, when applied to a carefully selected subset of program events, this interleaving-uniformity strategy allows for an effective exploration of program behaviors. We present an online randomized concurrency testing algorithm named Selectively Uniform Random Walk (SURW) that builds on these insights. SURW is the first of its class to achieve interleaving-uniformity for a wide class of programs, or an arbitrary subset of events thereof. This property translates to effective behavioral exploration should a subset with desirable characteristics be selected. Extensive evaluation on leading concurrency benchmarks suggests SURW is able to expose more bugs and significantly faster than comparable randomized algorithms. In addition, we show that SURW is able to explore both the space of interleavings and behaviors more uniformly on real-world programs.

## 中文摘要

并发程序中的错误行为以难以捕捉著称，因为它们可能只在指数级众多的线程交错中的少数几种下才会显现。随机化并发测试技术从这一巨大的搜索空间中按概率采样（而非枚举），已被证明是一类既能有效又可扩展的并发缺陷自动发现算法。本工作关注黑盒随机化并发测试算法的一项关键理想特性——探索的均匀性。遗憾的是，已有随机化算法在均匀性上存在明显不足，因而难以暴露那些只在少数、低频交错中显现的缺陷。为此，我们表明，对于广泛类别的程序，仅需极少的额外信息，就可以切实实现一种在交错空间上均匀采样的采样策略。此外，当该策略应用于精心选取的程序事件子集时，这种交错均匀性策略能够有效地探索程序行为。基于这些洞见，我们提出了一种在线随机化并发测试算法——选择性均匀随机游走（SURW）。SURW 是该类算法中首个对广泛类别的程序（或其任意事件子集）实现交错均匀性的算法。若所选子集具有理想特性，这一性质便可转化为有效的行为探索。在主流并发基准上的大量评估表明，SURW 相比同类随机化算法能够暴露更多缺陷，且速度显著更快。此外，我们还表明 SURW 在真实程序上能够更均匀地探索交错空间与行为空间。

## 英文关键词

Concurrency Bugs Detection, Concurrency Testing, Random Testing, Probabilistic Sampling

## 中文关键词

并发缺陷检测；并发测试；随机测试；概率采样

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707214)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6D](index.md) · [返回 ASPLOS 2025](../index.md)
