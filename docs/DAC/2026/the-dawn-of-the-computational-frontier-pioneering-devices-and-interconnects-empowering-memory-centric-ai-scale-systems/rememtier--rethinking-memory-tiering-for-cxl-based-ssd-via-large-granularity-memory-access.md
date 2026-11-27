Rememtier: Rethinking Memory Tiering for CXL-Based SSD via Large Granularity Memory Access
Authors：
[Yi-Sia Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2289361770012898741)，[Wen Sheng Lim](https://63dac.conference-program.com/?post_type=page&p=15&uid=21938300841628633941)，[Tei-Wei Kuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=325243)，[Yuan-Hao Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=014843)

## 中文标题

ReMemTier：基于大粒度内存访问的 CXL-SSD 内存分层重构

## 英文摘要

Modern data-intensive applications (e.g., AI/ML) increasingly exceed the capacity of host DRAM, motivating the adoption of CXL-based SSDs (CXL-SSDs) that provide memory-semantic device DRAM backed by large flash storage. To deliver reliable and robust services, these main applications are typically deployed alongside auxiliary tasks such as backup, logging, and monitoring. However, we observe that when these tasks run concurrently, their memory accesses generate substantial interference, causing the operating system to evict the main application’s hot pages from both DRAM and CXL DRAM to flash. This leads to severe refaults and long CPU stalls. This paper introduces ReMemTier, a reversed memory tiering approach that preserves main-application performance under such interference. ReMemTier exploits a new large-granularity memory access path over CXL, which enables a workload-aware reversed memory tiering approach that dedicates CXL DRAM as the fast tier for the main data-intensive application. To better utilize the fast tier, ReMemTier incorporates a sparse-burst resistant page replacement policy that distinguishes bursty pages from truly hot pages. Our evaluation demonstrates that ReMemTier significantly outperforms existing CXL memory tiering approaches.

## 中文摘要

现代数据密集型应用（如 AI/ML）的规模日益超出主机 DRAM 容量，促使人们采用基于 CXL 的 SSD（CXL-SSD），其以大规模闪存为后盾，提供具有内存语义的设备 DRAM。为交付可靠而稳健的服务，这类主应用通常与备份、日志、监控等辅助任务一并部署。然而我们观察到，当这些任务并发运行时，其内存访问会产生显著干扰，使操作系统将主应用的热页从 DRAM 与 CXL DRAM 逐出至闪存，从而引发严重的重复缺页与长时间 CPU 停顿。本文提出 ReMemTier，一种反向内存分层方法，可在此类干扰下保全主应用的性能。ReMemTier 利用 CXL 上新增的大粒度内存访问路径，实现负载感知的反向内存分层，将 CXL DRAM 专门用作主数据密集型应用的快速层。为更好地利用该快速层，ReMemTier 采用了抗稀疏突发的页面替换策略，可区分突发访问页与真正的热页。评估表明，ReMemTier 显著优于现有 CXL 内存分层方法。

## 英文关键词

Compute Express Link (CXL), CXL-SSD, Memory Tiering, Page Replacement Policy

## 中文关键词

Compute Express Link (CXL)、CXL-SSD、内存分层、页面替换策略
