---
title: "PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips"
description: "ISCA 2025 · Session 5A · PuDHammer: 真实DRAM芯片中PuD读干扰效应实验分析"
tags:
  - "ISCA2025"
  - "Session 5A"
  - "RowHammer"
---

# PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips

**中文标题：** PuDHammer: 真实DRAM芯片中PuD读干扰效应实验分析

**所属 Session：** [Session 5A](index.md) · [ISCA 2025](../index.md)

**作者：** Ismail Emir Yuksel, Akash Sood, Ataberk Olgun, O?uzhan Canpolat, Haocong Luo, Nisa Bostanci, Mohammad Sadrosadati, Giray Yaglikci, Onur Mutlu

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731030) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Processing-using-DRAM (PuD) is a promising paradigm for allevi- ating the data movement bottleneck using a DRAM array’s mas- sive internal parallelism and bandwidth to execute very wide data- parallel operations. Performing a PuD operation involves activating multiple DRAM rows in quick succession or simultaneously, i.e., multiple-row activation. Multiple-row activation is fundamentally different from conventional memory access patterns that activate one DRAM row at a time. However, repeatedly activating even one DRAM row (e.g., RowHammer) can induce bitflips in unaccessed DRAM rows because modern DRAM is subject to read disturbance, a worsening safety, security, and reliability issue. Unfortunately, no prior work investigates the effects of multiple-row activation, as commonly used by PuD operations, on DRAM read disturbance. 
 
 In this paper, we present the first characterization study of read disturbance effects of multiple-row activation-based PuD (which we call PuDHammer) using 316 real DDR4 DRAM chips from four major DRAM manufacturers. Our detailed characterization results covering various operational conditions and parameters (i.e., tem- perature, data patterns, access patterns, timing parameters, and spatial variation) show that 1) PuDHammer significantly exacer- bates the read disturbance vulnerability, causing up to 158.58× reduction in the minimum hammer count required to induce the first bitflip (𝐻𝐶𝑓𝑖𝑟𝑠𝑡), compared to RowHammer, 2) PuDHammer is affected by various operational conditions and parameters, 3) com- bining RowHammer with PuDHammer is more effective than using RowHammer alone to induce read disturbance errors (e.g., com- pared to RowHammer, doing so reduces 𝐻𝐶𝑓𝑖𝑟𝑠𝑡 by 1.66×on av- erage across all tested rows), and 4) PuDHammer bypasses an in- DRAM RowHammer mitigation mechanism called Target Row Re- fresh and induces more bitflips than RowHammer. 
 
 To develop future robust PuD-enabled systems in the presence of PuDHammer, we 1) develop three countermeasures and 2) adapt and evaluate the effectiveness of state-of-the-art RowHammer mitiga- tion standardized by industry, called Per Row Activation Counting (PRAC). We show that the adapted PRAC incurs large performance overheads to mitigate PuDHammer (e.g., an average performance overhead of 48.26% across 60 five-core multiprogrammed work- loads). We hope and expect that our findings motivate and guide system-level and architectural solutions to enable read-disturbance- resilient future PuD systems.

## 中文摘要

利用 DRAM 进行计算 (PuD) 是一种很有前途的范例，可以使用 DRAM 阵列的大规模内部并行性和带宽来执行非常广泛的数据并行操作，从而缓解数据移动瓶颈。执行 PuD 操作涉及快速连续或同时激活多个 DRAM 行，即多行激活。多行激活与一次激活一个 DRAM 行的传统内存访问模式有着根本的不同。然而，重复激活即使是一个 DRAM 行（例如 RowHammer）也可能会导致未访问的 DRAM 行发生位翻转，因为现代 DRAM 容易受到读扰动，这是一个日益恶化的安全性和可靠性问题。不幸的是，之前没有研究研究 PuD 操作常用的多行激活对 DRAM 读扰动的影响。

在本文中，我们使用来自四大 DRAM 制造商的 316 个真实 DDR4 DRAM 芯片，首次对基于多行激活的 PuD（我们称为 PuDHammer）的读扰动效应进行了表征研究。我们涵盖各种操作条件和参数（即温度、数据模式、访问模式、时序参数和空间变化）的详细表征结果表明：1) PuDHammer 显著加剧了读扰动漏洞，与 RowHammer 相比，导致引发第一次位翻转 (HCfirst ) 所需的最小锤击次数减少高达 158.58 倍，2) PuDHammer 受到各种操作条件和参数的影响，3) 将 RowHammer 与PuDHammer 比单独使用 RowHammer 更有效地引发读扰动错误（例如，与 RowHammer 相比，这样做在所有测试行中平均将 HCfirst 减少 1.66 倍），并且 4）PuDHammer 绕过了称为“目标行刷新”的 inDRAM RowHammer 缓解机制，并比 RowHammer 引发更多的位翻转。

为了在 PuDHammer 存在的情况下开发未来强大的支持 PuD 的系统，我们 1) 开发三种对策，2) 采用并评估行业标准化的最先进的 RowHammer 缓解措施的有效性，称为每行激活计数 (PRAC)。我们发现，为了缓解 PuDHammer 的影响，经过调整的 PRAC 会产生大量性能开销（例如，在 60 个五核多道程序工作负载中，平均性能开销为 48.26%）。我们希望并期望我们的研究结果能够激励和指导系统级和架构解决方案，以实现未来具有抗读扰动能力的 PuD 系统。

## 英文关键词

Processing-using-DRAM, RowHammer, read disturbance, DRAM reliability

## 中文关键词

DRAM 内计算, 多行激活, 读扰动, RowHammer

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731030)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2025](../index.md)
