---
title: "When Mitigations Backfire: Timing Channel Attacks and Defense for PRAC-Based RowHammer Mitigations"
description: "ISCA 2025 · Session 5A · When Mitigations Backfire: PRAC时序侧信道攻击与防御"
tags:
  - "ISCA2025"
  - "Session 5A"
  - "RowHammer"
---

# When Mitigations Backfire: Timing Channel Attacks and Defense for PRAC-Based RowHammer Mitigations

**中文标题：** When Mitigations Backfire: PRAC时序侧信道攻击与防御

**所属 Session：** [Session 5A](index.md) · [ISCA 2025](../index.md)

**作者：** Jeonghyun Woo, Joyce Qu, Gururaj Saileshwar, Prashant Nair

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731007) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Per Row Activation Counting (PRAC) has emerged as a robust framework for mitigating RowHammer (RH) vulnerabilities in mod- ern DRAM systems. However, we uncover a critical vulnerability: a timing channel introduced by the Alert Back-Off (ABO) protocol and Refresh Management (RFM) commands. We present PRACLeak, a novel attack that exploits these timing differences to leak sensitive information, such as secret keys from vulnerable AES implementa- tions, by monitoring memory access latencies. To counter this, we propose Timing-Safe PRAC (TPRAC), a de- fense that eliminates PRAC-induced timing channels without com- promising RH mitigation efficacy. TPRAC uses Timing-Based RFMs, issued periodically and independent of memory activity. It requires only a single-entry in-DRAM mitigation queue per DRAM bank and is compatible with existing DRAM standards. Our evaluations demonstrate that TPRAC closes timing channels while incurring only 3.4% performance overhead at the RH threshold of 1024.

## 中文摘要

逐行激活计数（PRAC）是现代DRAM系统中缓解行锤（RowHammer，RH）漏洞的可靠方案。但本文发现一个严重漏洞：告警退避（ABO）协议与刷新管理（RFM）命令会引入时序通道。本文提出PRACLeak，一种新型攻击，通过监测访存延迟，利用该时序差异窃取敏感信息，例如从存在漏洞的AES实现中提取密钥。针对该攻击，本文提出时序安全PRAC（TPRAC）防护方案，在不削弱行锤防护能力的前提下消除PRAC带来的时序通道。TPRAC采用基于固定时序的RFM，周期性下发，和内存访问行为解耦；每个DRAM Bank仅需要一条表项的片内防护队列，兼容现有DRAM标准。实验表明，在行锤阈值为1024时，TPRAC可以封堵该时序通道，性能开销仅3.4%。

## 英文关键词

DRAM, RowHammer, Timing Channel, Security, PRAC, RFM

## 中文关键词

DRAM, RowHammer, 时序侧信道, 安全, PRAC, RFM

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15104038)
- [代码仓库](https://github.com/STAR-Laboratory/PRAC_TC_ISCA25)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731007)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2025](../index.md)
