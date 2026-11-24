---
title: "Loaded Dice: Solving the Non-Selection Problem for Scalable Probabilistic RowHammer Defense"
description: "ISCA 2026 · Session 6D · Loaded Dice: Solving the Non-Selection Problem for Scalable Probabilistic RowHammer Defense"
tags:
  - "ISCA2026"
  - "Session 6D"
  - "Rowhammer and Security"
---

# Loaded Dice: Solving the Non-Selection Problem for Scalable Probabilistic RowHammer Defense

**中文标题：** Loaded Dice: 解决可扩展概率性 RowHammer 防御中的非选择问题

**所属 Session：** [Session 6D](index.md) · [ISCA 2026](../index.md)

**作者：** Jeonghyun Woo, Junsu Kim, Aamer Jaleel, Prashant J. Nair

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

DRAM scaling has exacerbated the RowHammer vulnerability. To counter this, JEDEC recently introduced Per Row Activation Counting (PRAC) with the Alert Back-Off protocol as an optional DDR5 feature. While promising, PRAC requires per-row counter cells that incur area overhead, and updating them on every activation lengthens DRAM timing parameters, degrading performance. Probabilistic mitigations such as MINT offer a lower-cost alternative by randomly selecting and mitigating rows within periodic mitigation windows. MINT is effective at higher thresholds (≥1000), but at lower thresholds, it must raise its mitigation rate to overcome the non-selection problem, where heavily hammered rows can repeatedly escape sampling. This fixed-rate scaling reduces effective memory bandwidth even when no attack is present. To overcome this limitation, we propose PrISM, an intersection-based probabilistic mitigation that correlates sampled rows across windows using a Sampled History Queue (SHQ). PrISM samples a few activation slots per window, stores sampled-but-unmitigated rows in the SHQ, and requests an additional mitigation through the existing Alert Back-Off protocol when a sampled row reappears in this history. This allows PrISM to increase mitigation only when persistent row activity is observed, without globally increasing the fixed mitigation rate. At the threshold of 500, PrISM incurs a negligible 0.2% average slow-down compared to 14% for PRAC, with no DRAM array changes or per-row counters and only 625B of SRAM per bank, one to two orders of magnitude less than prior secure counter-based in-DRAM defenses. Compared to MINT, PrISM provides better scalability at low thresholds, reducing average slowdown from 10.7% to 1.5% at a threshold of 250, a 7.1× reduction. PrISM is open-sourced at https://github.com/STAR-Laboratory/prism.

## 中文摘要

DRAM 缩放加剧了 RowHammer 漏洞。为应对这一问题，JEDEC 最近将带有 Alert Back-Off 协议的逐行激活计数（PRAC）作为可选的 DDR5 特性引入。尽管前景可观，PRAC 需要逐行计数器单元，带来面积开销，且每次激活都更新它们会延长 DRAM 时序参数，降低性能。诸如 MINT 的概率性缓解通过周期性缓解窗口随机选择并缓解行，提供了成本更低的替代方案。MINT 在较高阈值（≥1000）下有效，但在较低阈值下必须提高缓解率以克服非选择问题——被重度锤击的行可能反复逃过采样。这种固定速率缩放即使在无攻击时也会降低有效内存带宽。为克服这一局限，我们提出 PrISM，一种基于交集的概率性缓解方法，使用采样历史队列（SHQ）跨窗口关联被采样的行。PrISM 每个窗口采样少量激活槽，将已采样但未缓解的行存入 SHQ，当某采样行在该历史中再次出现时，通过现有 Alert Back-Off 协议请求额外缓解。这使 PrISM 仅在观察到持续行活动时才增加缓解，而无需全局提高固定缓解率。在阈值 500 下，PrISM 仅带来可忽略的 0.2% 平均性能下降，而 PRAC 为 14%，且无需改变 DRAM 阵列或逐行计数器，每 bank 仅需 625B SRAM，比先前基于安全计数器的 DRAM 内防御低一到两个数量级。与 MINT 相比，PrISM 在低阈值下具有更好的可扩展性，在阈值 250 下将平均性能下降从 10.7% 降至 1.5%，降低了 7.1 倍。PrISM 已在 https://github.com/STAR-Laboratory/prism 开源。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：STAR-Laboratory/prism](https://github.com/STAR-Laboratory/prism)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6D](index.md) · [返回 ISCA 2026](../index.md)
