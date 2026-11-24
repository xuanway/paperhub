---
title: "Radshield: Software Radiation Protection for Commodity Hardware in Space"
description: "ASPLOS 2026 · Session 9C · Radshield：面向太空商用硬件的软件辐射防护"
tags:
  - "ASPLOS2026"
  - "Session 9C"
  - "Reliability & Fault Tolerance"
---

# Radshield: Software Radiation Protection for Commodity Hardware in Space

**中文标题：** Radshield：面向太空商用硬件的软件辐射防护

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Haoda Wang (Columbia University), Yonatan Winetraub (Aptos Orbital), Steven Myint (Jet Propulsion Laboratory, California Institute of Technology), Vandi Verma (Jet Propulsion Laboratory, California Institute of Technology), Junfeng Yang (Columbia University), Asaf Cidon (Columbia University)

**单位：** Columbia University；Aptos Orbital；Jet Propulsion Laboratory, California Institute of Technology

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762218) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Exponentially-declining launch costs have led to an explosion of inexpensive satellites launched to space, often equipped with off-the-shelf chips. These chips, however, lack hardware radiation protection, leaving them vulnerable to space radiation. We thus design Radshield, a software system protecting against the two most ubiquitous and costly radiation fault scenarios: (a) radiation-induced short-circuits that lead to permanent hardware failure; and (b) radiation-induced transient charges that result in single-bit silent data corruption (SDC). Radshield counters these failure scenarios with two components. First, it uses a short-circuit detector that can detect tiny increases in the device's current draw by estimating the normal current draw when resource utilization is low. Second, it duplicates the execution of spacecraft workloads in a CPU and memory-efficient manner, and catches SDCs even when they affect the CPU's pipeline or cache. In our experiments, we show Radshield is very effective at preventing both errors, and is 1.4−35.5× more power-efficient than the state-of-the-art protection mechanisms in detecting SDC. Radshield is deployed on missions in low-earth orbit and in deep space. “The 9000 series is the most reliable computer ever made. No 9000 computer has ever made a mistake or distorted information. We are all, by any practical definition of the words, foolproof and incapable of error.” HAL, 2001: A Space Odyssey

## 中文摘要

发射成本的指数级下降带来了被送入太空的廉价卫星数量的爆发式增长，这些卫星往往搭载现货商用芯片。然而，此类芯片缺乏硬件辐射防护，使它们易受空间辐射的影响。因此，我们设计了 Radshield，这是一个软件系统，用于防范两种最常见且代价最高的辐射故障场景：(a) 辐射引发的短路，会导致硬件永久性失效；(b) 辐射引起的瞬态电荷，会造成单比特静默数据损坏（SDC）。Radshield 通过两个组件应对这些故障场景。首先，它使用一个短路检测器，通过在资源利用率较低时估计正常电流消耗，能够检测到设备电流消耗的微小增加。其次，它以对 CPU 和内存高效的方式复制航天器工作负载的执行，并且即使 SDC 影响了 CPU 的流水线或缓存也能将其捕获。在实验中，我们表明 Radshield 在防止这两类错误方面非常有效，并且在检测 SDC 时，其能效比最先进的防护机制高 1.4−35.5×。Radshield 已部署在低地球轨道和深空的任务中。“9000 系列是有史以来最可靠的计算机。没有任何一台 9000 计算机出过错或歪曲过信息。按任何实际的定义来说，我们都是万无一失的，不可能犯错的。”HAL，《2001 太空漫游》

## 英文关键词

satellite computing, fault tolerance, radiation hardening

## 中文关键词

卫星计算；容错；辐射加固

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762218)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2026](../index.md)
