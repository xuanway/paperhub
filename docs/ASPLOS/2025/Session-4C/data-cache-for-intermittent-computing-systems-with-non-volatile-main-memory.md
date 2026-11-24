---
title: "Data Cache for Intermittent Computing Systems with Non-Volatile Main Memory"
description: "ASPLOS 2025 · Session 4C · 面向非易失主存间歇计算系统的数据缓存"
tags:
  - "ASPLOS2025"
  - "Session 4C"
  - "Potpourri 1"
---

# Data Cache for Intermittent Computing Systems with Non-Volatile Main Memory

**中文标题：** 面向非易失主存间歇计算系统的数据缓存

**所属 Session：** [Session 4C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Sourav Mohapatra (Department of Computer Science, TU Delft,ARM Limited), Vito Kortbeek (Department of Computer Science, TU Delft,Synopsys), Marco Antonio van Eerden (Department of Computer Science, TU Delft), Jochem Broekhoff (Department of Computer Science, TU Delft,DSP Innovation B.V.), Saad Ahmed (School of Interactive Computing, Georgia Institute of Technology), Przemysław Pawełczak (Department of Computer Science, TU Delft)

**单位：** Department of Computer Science, TU Delft,ARM Limited；Department of Computer Science, TU Delft,Synopsys；Department of Computer Science, TU Delft；Department of Computer Science, TU Delft,DSP Innovation B.V.；School of Interactive Computing, Georgia Institute of Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715989) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Intermittently-operating embedded computing platforms powered by energy harvesting must frequently checkpoint their computation state. Using non-volatile memory reduces checkpoint size by eliminating the need to checkpoint volatile memory but increases checkpoint frequency to cover Write After Read (WAR) dependencies. Additionally, non-volatile memory is significantly slower to access—while consuming more energy than its volatile counterpart—suggesting the use of a data cache. Unfortunately, existing data cache solutions do not fit the challenges of intermittent computing and often require additional hardware or software to detect WARs. In this paper, we extend the data cache by integrating it with WAR detection—dropping the need for an additional memory tracker. This idea forms the basis of NACHO: a data cache tailored to intermittent computing. NACHO, on average, reduces intermittent computing runtime overhead by 54% compared to state of the art cache-based systems. It also reduces the number of non-volatile memory writes by 82% compared to a data cache-less system, and 18% on average compared to multiple state of the art cache-based systems.

## 中文摘要

由能量收集供能的间歇运行嵌入式计算平台必须频繁地对其计算状态进行检查点保存。使用非易失存储器无需对易失存储器做检查点，从而减小检查点大小，但会增加检查点频率以覆盖写后读（Write After Read, WAR）依赖。此外，非易失存储器的访问速度显著更慢，并且比容量相当的易失存储器消耗更多能量，这提示应使用数据缓存。遗憾的是，现有的数据缓存方案无法应对间歇计算的挑战，且往往需要额外的硬件或软件来检测 WAR。在本文中，我们通过将数据缓存与 WAR 检测相集成来扩展数据缓存，从而不再需要额外的内存追踪器。这一思路构成了 NACHO 的基础：一种为间歇计算量身定制的数据缓存。与最先进的基于缓存的系统相比，NACHO 平均将间歇计算的运行时开销降低 54%。与无数据缓存的系统相比，它还将非易失存储器的写次数减少 82%，与多个最先进的基于缓存的系统相比平均减少 18%。

## 英文关键词

intermittent computing, battery-free, cache, embedded system

## 中文关键词

间歇计算；无电池；缓存；嵌入式系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715989)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4C](index.md) · [返回 ASPLOS 2025](../index.md)
