---
title: "RowArmor: Efficient and Comprehensive Protection Against DRAM Disturbance Errors"
description: "ASPLOS 2026 · Session 2D · RowArmor：高效且全面的 DRAM 干扰错误防护"
tags:
  - "ASPLOS2026"
  - "Session 2D"
  - "DRAM Reliability & Security"
---

# RowArmor: Efficient and Comprehensive Protection Against DRAM Disturbance Errors

**中文标题：** RowArmor：高效且全面的 DRAM 干扰错误防护

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Minbok Wi (Seoul National University), Yoonyul Yoo (Samsung Electronics), Yoojin Kim (Sungkyunkwan University), Jaeho Shin (Sungkyunkwan University), Jumin Kim (Seoul National University), Yesin Ryu (Sungkyunkwan University, Samsung Electronics), Saeid Gorgin (Sungkyunkwan University), Jung Ho Ahn (Seoul National University), Jungrae Kim (Sungkyunkwan University)

**单位：** Seoul National University；Samsung Electronics；Sungkyunkwan University；Sungkyunkwan University, Samsung Electronics

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790213) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

**出版标题：** RowArmor: Efficient and Comprehensive Protection Against DRAM Disturbance Attacks

## 英文摘要

Shrinking process technologies have made DRAM increasingly vulnerable to disturbance attacks, such as RowHammer, which can compromise data integrity or induce a Denial-of-Service (DoS) state. Existing solutions focus on preventing errors through activation monitoring and extra refreshes, but they often incur substantial performance overhead and can unintentionally exacerbate DoS risks. This paper introduces RowArmor, a novel defense mechanism that addresses both data corruption and DoS attacks. RowArmor adopts a reactive approach, correcting disturbance errors as they occur via address scrambling and enhanced error correcting codes. This strategy avoids the high costs of preventive methods while addressing diverse attack patterns, including RowPress. Our evaluation demonstrates that RowArmor effectively defends against data corruption and DoS attacks with a negligible performance overhead of up to 0.7%.

## 中文摘要

工艺尺寸的不断缩小使 DRAM 越来越易受 RowHammer 等干扰攻击的影响，这类攻击可能破坏数据完整性或导致拒绝服务（Denial-of-Service，DoS）状态。现有方案侧重于通过激活监控和额外刷新来防止错误，但它们往往带来较大的性能开销，并可能无意中加剧 DoS 风险。本文提出 RowArmor，这是一种同时应对数据损坏和 DoS 攻击的新型防御机制。RowArmor 采用反应式方法，通过地址扰乱和增强型纠错码在干扰错误发生时对其进行纠正。该策略避免了预防式方法的高昂成本，同时能够应对包括 RowPress 在内的多种攻击模式。我们的评估表明，RowArmor 能有效防御数据损坏和 DoS 攻击，性能开销最高仅为 0.7%，可忽略不计。

## 英文关键词

DRAM; RowHammer; Memory System; Security; Reliability; ECC; Denial-of-Service

## 中文关键词

DRAM；RowHammer；存储系统；安全；可靠性；ECC；拒绝服务

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790213)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2026](../index.md)
