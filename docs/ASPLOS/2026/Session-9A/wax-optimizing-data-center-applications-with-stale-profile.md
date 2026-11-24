---
title: "Wax: Optimizing Data Center Applications With Stale Profile"
description: "ASPLOS 2026 · Session 9A · Wax：利用陈旧 Profile 优化数据中心应用"
tags:
  - "ASPLOS2026"
  - "Session 9A"
  - "Systems Profiling & Optimization"
---

# Wax: Optimizing Data Center Applications With Stale Profile

**中文标题：** Wax：利用陈旧 Profile 优化数据中心应用

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tawhid Bhuiyan (Columbia University in the City of New York), Sumya Hoque (Columbia University in the City of New York), Angelica Moreira (Microsoft Research), Tanvir Ahmed Khan (Columbia University in the City of New York)

**单位：** Columbia University in the City of New York；Microsoft Research

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790248) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Data center applications' large instruction footprints cause frequent front-end stalls by overwhelming on-chip microarchitectural structures such as instruction cache (I-cache), instruction translation look-aside buffer (iTLB), and branch target buffer (BTB). To reduce pressure on these structures, data center providers leverage profile-guided optimizations by reordering binary layout along a relatively small number of hot code paths. Such reordering provides the highest benefit if profile collection and optimization happen on the same version of the binary. In practice, companies have to optimize and deploy a fresh version of the binary with a profile from a previous version, making a large fraction of the profile stale. In this paper, we propose Wax1, a novel technique to optimize data center applications with stale profiles. Wax's key insight is to leverage the debug and source code information while optimizing fresh binaries with stale profiles. We evaluate Wax for 5 data center applications to show that Wax provides significant (5.76%-26.46%) performance speedups. Wax achieves 1.20%-7.86% greater speedups than the state of the art, obtaining 65%-93% of fresh profiles' benefits.

## 中文摘要

数据中心应用的庞大指令足迹会使指令缓存（I-cache）、指令转译后备缓冲器（iTLB）和分支目标缓冲器（BTB）等片上微架构结构不堪重负，从而造成频繁的前端停顿。为减轻这些结构上的压力，数据中心提供商利用 Profile 引导的优化，沿相对少量的热代码路径重排二进制布局。如果 Profile 采集与优化发生在同一版本的二进制文件上，这种重排能带来最大收益。而在实践中，企业不得不用来自前一版本的 Profile 来优化并部署新版本的二进制文件，这使得很大一部分 Profile 变得陈旧。本文提出 Wax1，一种利用陈旧 Profile 优化数据中心应用的新技术。Wax 的关键洞见在于：在使用陈旧 Profile 优化新二进制文件时，利用调试信息与源代码信息。我们针对 5 个数据中心应用对 Wax 进行评估，结果表明 Wax 带来了显著的性能加速（5.76%-26.46%）。Wax 的加速比当前最优技术高出 1.20%-7.86%，可获得新 Profile 收益的 65%-93%。

## 英文关键词

Profile-guided optimizations; Profile staleness; Frontend stalls; Debug information; Data centers

## 中文关键词

Profile 引导的优化；Profile 陈旧性；前端停顿；调试信息；数据中心

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790248)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2026](../index.md)
