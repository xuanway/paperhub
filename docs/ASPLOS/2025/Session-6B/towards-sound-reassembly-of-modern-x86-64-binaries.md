---
title: "Towards Sound Reassembly of Modern x86-64 Binaries"
description: "ASPLOS 2025 · Session 6B · 面向现代 x86-64 二进制的健全重组"
tags:
  - "ASPLOS2025"
  - "Session 6B"
  - "Compilers & Languages"
---

# Towards Sound Reassembly of Modern x86-64 Binaries

**中文标题：** 面向现代 x86-64 二进制的健全重组

**所属 Session：** [Session 6B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Hyungseok Kim (The Affiliated Institute of ETRI), Soomin Kim (KAIST), Sang Kil Cha (KAIST)

**单位：** The Affiliated Institute of ETRI；KAIST

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716026) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Reassembly is a promising approach to transparently rewrite binaries without source code. However, sound symbolization remains an open problem as it requires precise identification of all memory references in the binary. In this paper, we systematically study the requirements for sound reassembly of modern x86-64 binaries, and present a novel approach to reassembly that symbolizes all memory references without affecting the original semantics. The key insights are twofold: (1) we find that Control-flow Enhancement Technology (CET), which has increasingly become the default setting for major Linux distributions, adds a unique property to binaries that can be leveraged to precisely symbolize dynamically computed pointers, and (2) we consider a superset of all possible memory references for symbolization by overapproximating indirect branch targets. With these insights, we design and implement a novel reassembler, named SURI, and show its effectiveness on 9,600 real-world binaries.

## 中文摘要

重组（reassembly）是一种无需源代码即可透明地重写二进制文件的有效方法。然而，健全的符号化（sound symbolization）仍是一个悬而未决的问题，因为它要求精确识别二进制文件中的所有内存引用。本文系统研究了现代 x86-64 二进制文件健全重组所需的条件，并提出了一种新型重组方法，可在不影响原有语义的前提下对所有内存引用进行符号化。其关键洞见有两方面：(1) 我们发现控制流增强技术（Control-flow Enhancement Technology, CET）——它正日益成为主流 Linux 发行版的默认设置——为二进制文件赋予了一种独特性质，可用来精确地符号化动态计算出的指针；(2) 我们通过对间接分支目标进行过近似（overapproximation），将用于符号化的所有可能内存引用的超集纳入考虑。基于这些洞见，我们设计并实现了名为 SURI 的新型重组器，并在 9,600 个真实二进制文件上展示了其有效性。

## 英文关键词

reassembly; binary rewriting; reverse engineering; binary hardening; binary analysis; superset CFG

## 中文关键词

重组；二进制重写；逆向工程；二进制加固；二进制分析；超集 CFG

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716026)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6B](index.md) · [返回 ASPLOS 2025](../index.md)
