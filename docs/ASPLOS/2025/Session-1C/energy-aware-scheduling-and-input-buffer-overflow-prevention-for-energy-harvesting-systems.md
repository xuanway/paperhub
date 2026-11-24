---
title: "Energy-aware Scheduling and Input Buffer Overflow Prevention for Energy-harvesting Systems"
description: "ASPLOS 2025 · Session 1C · 面向能量采集系统的能量感知调度与输入缓冲区溢出防止"
tags:
  - "ASPLOS2025"
  - "Session 1C"
  - "Edge Computing"
---

# Energy-aware Scheduling and Input Buffer Overflow Prevention for Energy-harvesting Systems

**中文标题：** 面向能量采集系统的能量感知调度与输入缓冲区溢出防止

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Harsh Desai (Carnegie Mellon University), Xinye Wang (Carnegie Mellon University), Brandon Lucia (Carnegie Mellon University)

**单位：** Carnegie Mellon University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715995) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern energy-harvesting devices [23] use on-device compute to discard data uninteresting to the application, improving energy availability. These devices capture data at fixed rate, and process captured data at a rate that varies with environmental factors like input power and event activity. If capture rate exceeds processing rate, new inputs are stored in a small on-device input buffer (hundreds of kBs). When the input buffer fills up, the device discards newer inputs, missing potentially interesting events. Energy-harvesting devices must avoid such input buffer overflows (IBO) to avoid missing interesting events. A static solution to IBOs is impossible given dynamic variations in processing rate, and prior research fails to provide a suitable dynamic solution. We propose Quetzal, a new hardware-software solution targeted at avoiding IBOs. Quetzal's software has two parts: a new energy-aware scheduler that selects jobs with the lowest endto-end latency (including energy recharging), and a runtime which uses queueing-theory to predict if the selected job will cause IBOs. Quetzal reacts to imminent IBOs by degrading the scheduled job. Quetzal's scheduler and runtime use a simple, system-agnostic hardware circuit to measure power at runtime. Quetzal reduces events missed due to IBOs by up to 4.2× compared to several baselines.

## 中文摘要

现代能量采集设备[23]利用设备端计算丢弃应用不感兴趣的数据，从而提升能量可用性。这类设备以固定速率采集数据，并以随输入功率、事件活动等环境因素而变化的速率处理已采集的数据。若采集速率超过处理速率，新输入便被存入设备端一个小容量输入缓冲区（数百 KB）。当输入缓冲区写满时，设备会丢弃较新的输入，从而错过可能感兴趣的事件。能量采集设备必须避免此类输入缓冲区溢出（IBO），以免漏掉感兴趣的事件。考虑到处理速率是动态变化的，对 IBO 采用静态解决方案并不可行，而先前研究也未能给出合适的动态解决方案。我们提出 Quetzal，一种旨在避免 IBO 的新型软硬件协同方案。Quetzal 的软件部分包含两个组件：一个新的能量感知调度器，它选择端到端时延（含能量补充时间）最低的任务；以及一个运行时，它利用排队论预测所选任务是否会导致 IBO。面对即将发生的 IBO，Quetzal 通过降级被调度的任务来应对。Quetzal 的调度器与运行时使用一个简单且与具体系统无关的硬件电路在运行期测量功率。与若干基线相比，Quetzal 最多可将因 IBO 而丢失的事件数减少 4.2 倍。

## 英文关键词

energy-harvesting devices; input-buffer overflows; intermittent computing; energy-aware scheduling

## 中文关键词

能量采集设备；输入缓冲区溢出；间歇计算；能量感知调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715995)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2025](../index.md)
