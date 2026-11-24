---
title: "Fast, Transparent Filesystem Microkernel Recovery with Ananke"
description: "FAST 2025 · File Systems · 利用微内核进程崩溃时宿主 OS 仍存活的时机，以内存 p-log 实现无损、透明的文件系统恢复"
tags:
  - "FAST2025"
  - "File Systems"
  - "最佳论文"
  - "微内核"
  - "崩溃恢复"
---

# Fast, Transparent Filesystem Microkernel Recovery with Ananke

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Ananke 面向微内核文件系统的进程级崩溃（p-crash），在宿主 OS 协调下用内存中的 p-log 记录未落盘的系统调用状态，使应用在服务进程重启后仍能看到崩溃前的文件系统状态。3 万余次故障注入实验实现无损恢复，恢复时间通常在数百毫秒以内，常见路径开销低于 2%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · File Systems · 最佳论文</p>
</div>

**中文标题**：Ananke：快速、透明的文件系统微内核恢复

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/liu-jing](https://www.usenix.org/conference/fast25/presentation/liu-jing)

**论文 PDF**：[fast25-liu-jing.pdf](https://www.usenix.org/system/files/fast25-liu-jing.pdf)

**作者**：Jing Liu（Microsoft Research）；Yifan Dai、Andrea C. Arpaci-Dusseau、Remzi H. Arpaci-Dusseau（University of Wisconsin–Madison）

**会议**：FAST 2025 · Santa Clara, CA · 第 1–18 页 · **最佳论文**

**Session**：File Systems · 2025-02-25 10:45–12:25 · Chair：Yu Hua（Huazhong University of Science and Technology）

**所属 Session**：[File Systems](index.md) · [FAST 2025](../index.md)

**关键词**：microkernel, filesystem recovery, process crash, state gap, fault injection

---

## 英文摘要

We introduce Ananke, a high-performance filesystem microkernel service that provides transparent recovery from unexpected filesystem failures. Ananke does so by leveraging the unique opportunity of the microkernels, running a small amount of recovery code coordinated by the host OS at the moment of a process crash. Ananke can record key pieces of information not usually available during full-system crash recovery, enabling fast and transparent recovery for applications. Through over 30,000 fault-injection experiments, we demonstrate that Ananke achieves lossless recovery; we also show that Ananke recovers quickly, usually in a few hundred milliseconds. Through real application workloads, we show that Ananke delivers high performance in the common case; the extra work needed to detect faults and prepare for recovery incurs minimal overheads.

## 中文摘要

Ananke 是一个高性能的文件系统微内核服务，能够在文件系统发生意外故障时提供透明恢复。它利用了微内核特有的机会：在进程崩溃的瞬间，由宿主操作系统协调运行少量恢复代码。借助这一机制，Ananke 可以记录整机崩溃恢复时通常无法获得的关键信息，从而为应用提供快速、透明的恢复能力。通过 30,000 余次故障注入实验，本文证明 Ananke 能够实现无损恢复，且恢复速度很快，通常仅需数百毫秒；在真实应用负载下，Ananke 在常见路径上保持高性能，为检测故障和准备恢复而增加的额外工作仅带来极小开销。

## 一句话总结

> Ananke 把微内核文件系统的进程崩溃当作一次可利用的恢复机会：在宿主 OS 协调下保留内存中的崩溃日志 p-log，让重启后的文件系统服务精确复原应用所见的全部状态，而不是只把磁盘恢复到一致状态。

## 研究背景与问题

- **崩溃模型不同**：单体内核文件系统出错会引发整机崩溃（s-crash），而微内核文件系统服务运行在用户态进程中，崩溃只发生在该进程（p-crash），操作系统与客户端应用仍可存活。
- **存在状态缺口（state gap）**：应用以为已完成的写入、已打开的文件描述符等临时状态保存在崩溃进程的内存里，传统的 s-crash 恢复只保证磁盘数据一致，无法还原这部分状态，应用会"看到"文件凭空变空或更新丢失。
- **已有方案不适配**：微内核恢复与文件系统恢复各自有研究，但都没有充分利用"整机仍然活着"这一 p-crash 特有优势来同时做到快速与透明。

## 核心贡献

- **提出 p-crash 恢复的原则性方法**：将 p-crash 恢复与 s-crash 恢复解耦，在现实的故障模型下给出透明恢复保证。
- **设计内存崩溃日志 p-log 与 AIM 算法**：持续记录进行中的系统调用，即便系统调用以乱序方式持久化，p-log 仍能准确刻画状态缺口的来源，且不影响常见路径性能。
- **内核协调的投机重启（speculative restart）**：由 OS 协调启动新进程并转移 p-log 与客户端连接，避开设备连接重建开销，大幅缩短恢复时间。
- **轻量校验和**：对关键内存数据结构做校验，及时检测内存损坏，把恢复能力扩展到非 fail-stop 的故障场景。

## 方法与技术要点

- **基础架构**：基于 uFS 微内核文件系统实现，在不改变常见路径性能的前提下叠加透明恢复机制。
- **p-log 记录**：正常运行时把系统调用相关信息写入内存中的 p-crash log；工作负载持续推进时，p-log 始终跟踪尚未持久化的状态差异。
- **AIM（Act-Ignore-Modify）恢复算法**：根据日志中记录的操作类型决定重放、忽略还是修正，从而在不拖慢常见路径的情况下补齐状态缺口。
- **进程切换与恢复流程**：崩溃后由 OS 协调新进程接管 p-log 与客户端连接，结合磁盘上的 s-log（如 journal）共同恢复文件系统状态，应用仅经历短暂性能抖动。
- **内存损坏检测**：用轻量 CRC 校验关键内存结构，配合 3 万余次受控与随机故障注入（含 fail-stop 与内存损坏）验证恢复正确性。

## 评估与主要结果

- **无损恢复**：在 30,000 次以上受控与随机故障注入实验中，Ananke 对 `sort`、`cp`、`zip` 等工具以及 SQLite、LevelDB 等持久化库均实现透明、无损恢复。
- **恢复时间**：通常只需数百毫秒，最坏不超过 400 ms。
- **常见路径开销**：多数场景低于 2%；复制 p-log 的内存开销为每核 8 MB，CRC 占用不到工作负载内存的 0.01%。

[返回 File Systems](index.md) · [返回 FAST 2025](../index.md)
