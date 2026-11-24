# AccFS: An Accelerator-Aware File System for Non-Volatile Memory

**中文标题**：AccFS：面向非易失性内存的加速器感知文件系统

**所属 Session**：[Session 6: Storage and File Systems](index.md) · [ATC 2026](../index.md)

**作者**：Sangjin Lee (Chung-Ang University), Taehwan Ahn (Chung-Ang University), Yongseok Son (Chung-Ang University)

## 英文摘要
We present AccFS, a novel non-volatile memory (NVM) file system designed to exploit hardware accelerators, such as Intel Data Streaming Accelerator (DSA), on modern CPUs. To better leverage DSA, AccFS decouples space allocation from persistence and employs core-local data management, enabling temporal and spatial coalescing of requests issued to DSA. Furthermore, AccFS coordinates data-movement and integrity-protection operations between CPU cores and DSA using insight-driven scheduling policies. We implement AccFS in the Linux kernel and evaluate it on a 64-core machine equipped with Intel DSA and Optane DC persistent memory module (DCPMM). The experimental results show that AccFS achieves up to 2.71× higher throughput and 108.71× lower latency than seven NVM file systems while reducing CPU utilization by up to 84.99%.

## 中文摘要
我们提出 AccFS，一个新颖的非易失性内存（NVM）文件系统，旨在利用现代 CPU 上的硬件加速器，例如 Intel 数据流加速器（DSA）。为了更好地发挥 DSA 的作用，AccFS 将空间分配与持久化解耦，并采用核心本地（core-local）的数据管理方式，从而实现对发往 DSA 的请求在时间与空间上的合并。此外，AccFS 使用由洞见驱动的调度策略，协调 CPU 核与 DSA 之间的数据搬移和完整性保护操作。我们在 Linux 内核中实现 AccFS，并在配备 Intel DSA 与 Optane DC 持久内存模块（DCPMM）的 64 核机器上进行评估。实验结果表明，与七种 NVM 文件系统相比，AccFS 的吞吐最多提升 2.71×，延迟最多降低 108.71×，同时将 CPU 利用率最多降低 84.99%。

## 英文关键词
File system, Non-volatile memory, Hardware accelerator, Intel Data Streaming Accelerator (DSA)

## 中文关键词
文件系统，非易失性内存，硬件加速器，Intel 数据流加速器（DSA）

[返回 Session 6](index.md) · [返回 ATC 2026](../index.md)
