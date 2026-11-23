---
title: "SpecASan: Mitigating Transient Execution Attacks Using Speculative Address Sanitization"
description: "ISCA 2025 · Session 10C · SpecASan: 利用推测地址消毒缓解瞬态执行攻击"
tags:
  - "ISCA2025"
  - "Session 10C"
  - "Security"
---

# SpecASan: Mitigating Transient Execution Attacks Using Speculative Address Sanitization

**中文标题：** SpecASan: 利用推测地址消毒缓解瞬态执行攻击

**所属 Session：** [Session 10C](index.md) · [ISCA 2025](../index.md)

**作者：** Saber Ganjisaffar, Esmaeil Mohmmadian Koruyeh, Jason Zellmer, Hodjat Asghari Esfeden, Chengyu Song, Nael Abu-Ghazaleh, Esmaeil Mohmmadian Koruyeh

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731119) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Transient execution attacks (TEAs), such as Spectre and Meltdown, exploit speculative execution to leak sensitive data through resid- ual microarchitectural state. Traditional defenses often incur high performance and hardware costs by delaying speculative execu- tion or requiring additional shadow structures and dynamic in- formation flow tracking. In contrast, our approach models these attacks as violations of software-defined security contracts and enforces these contracts in hardware using existing features. We introduce Speculative Address Sanitization (SpecASan), which lever- ages ARM’s Memory Tagging Extension (MTE) to extend memory safety protection from the committed path to the speculative path. When a speculative access does not pass the MTE tag comparison, this access is delayed until speculation resolves. This ensures that only validated accesses affect the microarchitectural state while preserving the performance benefits of speculation. When combined with Control-Flow Integrity (CFI) enforcement mechanisms, already supported by some hardware implementations, our eval- uation shows that SpecASan effectively mitigates a broad class of transient execution attacks, including Spectre and Microarchitectural Data Sampling (MDS). Furthermore, SpecASan achieves this with low performance overhead and minimal hardware complexity, highlighting its practicality and efficiency.

## 中文摘要

瞬态执行攻击（TEA，例如Spectre、Meltdown）利用推测执行，通过微架构残留状态窃取敏感数据。传统防御方案通常会暂停推测执行，或者额外引入影子结构、动态信息流追踪，带来很高的性能与硬件开销。与之不同，本文将这类攻击建模为对软件定义安全契约的违规行为，并复用已有硬件能力来强制执行该契约。

本文提出**推测地址消毒（SpecASan）**，依托ARM内存标签扩展（MTE），把内存安全保护从提交执行路径延伸到推测执行路径。当一次推测访问无法通过MTE标签比对时，该访问会被延迟，直到推测分支确定。该机制保证只有校验通过的访问才会修改微架构状态，同时保留推测执行带来的性能收益。如果搭配部分硬件已支持的控制流完整性（CFI）机制，评测表明SpecASan可以有效防御一大类瞬态执行攻击，包括Spectre与微架构数据采样（MDS）。SpecASan性能开销低、硬件改动少，具备良好实用性与高效性。

## 英文关键词

Speculative Execution Attacks, Memory Safety, Address Sanitizer.

## 中文关键词

推测执行攻击, 内存安全, 地址消毒器

## 代码与研究制品

- [代码仓库](https://github.com/Archimantix/gem5-mte)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731119)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10C](index.md) · [返回 ISCA 2025](../index.md)
