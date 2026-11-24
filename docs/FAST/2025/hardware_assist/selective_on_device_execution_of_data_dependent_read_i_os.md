---
title: "Selective On-Device Execution of Data-Dependent Read I/Os"
description: "FAST 2025 · Hardware Assist · 在设备内选择性重提交数据依赖读，B+-树 KV 吞吐最高提升 41%"
tags:
  - "FAST2025"
  - "Hardware Assist"
  - "on-device computing"
  - "in-kernel storage function"
---

# Selective On-Device Execution of Data-Dependent Read I/Os

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">设备内计算通常靠削减数据传输取胜，但数据依赖读每次只取一小块，设备处理器主频又低。SODE 用 eBPF 在设备内执行重提交，资源不足时回落内核路径，B+-树 KV 吞吐最高提升 41%，WiredTiger 在 YCSB C 上 99 分位尾延迟降低 3.85%。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Hardware Assist</p>
</div>

**中文标题**：数据依赖读 I/O 的选择性设备内执行

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/park](https://www.usenix.org/conference/fast25/presentation/park)

**论文 PDF**：[fast25-park.pdf](https://www.usenix.org/system/files/fast25-park.pdf)

**作者**：Chanyoung Park、Minu Chung、Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

**会议**：FAST 2025 · Santa Clara, CA · 第 373–390 页

**Session**：Hardware Assist · 2025-02-26 10:50–12:30 · Chair：Kiran Kumar Muniswamy Reddy（Amazon）

**所属 Session**：[Hardware Assist](index.md) · [FAST 2025](../index.md)

**关键词**：on-device computing, in-kernel storage function, eBPF, data-dependent read, I/O resubmission, NVMe

---

## 英文摘要

Recent studies have demonstrated the benefits of employing on-device and in-kernel storage functions. On-device functions are primarily used to preprocess data within storage devices, effectively reducing the amount of I/O. In contrast, in-kernel functions are proposed to expedite sequences of data-dependent read I/O requests, particularly useful for applications traversing on-disk data structures. In this work, we investigate the unexplored potential of using on-device functions for data-dependent read I/O requests on read-only on-disk data structures. The results are promising: on-device I/O functions enable applications to issue I/O requests more rapidly and integrate seamlessly with in-kernel functions to efficiently manage high volumes of requests. We developed a prototype of this on-device function atop NVMeVirt, a state-of-the-art storage emulator. We demonstrate that on-device function enhances performance through experiments utilizing a simple B+-tree key-value store and WiredTiger, a widely used log-structured merge tree-based key-value store. Use of the on-device function improves the throughput of the B+-tree key-value store by up to 41%, and reduces WiredTiger's 99-percentile tail latency on YCSB C by up to 3.85%, compared to the host-only in-kernel storage function.

## 中文摘要

近期研究展示了采用设备内函数与内核内存储函数的好处。设备内函数主要用于在存储设备内预处理数据，有效减少 I/O 量；相比之下，内核内函数用于加速一连串数据依赖的读 I/O 请求，对遍历磁盘数据结构的应用尤其有用。本文研究一个尚未被探索的潜力：对只读磁盘数据结构上的数据依赖读 I/O 请求使用设备内函数。结果令人鼓舞：设备内 I/O 函数使应用能更快发出 I/O 请求，并与内核内函数无缝集成，从而高效管理大量请求。本文在最先进的存储模拟器 NVMeVirt 上实现了该设备内函数的原型。本文用简单的 B+-树键值存储与广泛使用的基于 LSM 树的键值存储 WiredTiger 进行实验，证明设备内函数能提升性能。相比仅使用主机内核内存储函数的方案，使用设备内函数使 B+-树键值存储的吞吐最高提升 41%，并使 WiredTiger 在 YCSB C 上的 99 分位尾延迟最高降低 3.85%。

## 一句话总结

> 设备内计算的价值不在省带宽，而在让下一次读离数据更近——前提是那一刻设备处理器正好空闲。

## 研究背景与问题

- **已有两条路线**：设备内函数（λ-IO、Insider 等）主要先在设备内预处理以减少 I/O 量；内核内函数（XRP）把计算放到设备驱动之上，用来加速指针追逐式的数据依赖读请求序列。
- **设备算力与位置都不占优**：SSD 内处理器主频低，同一个任务在设备上执行往往比在内核中更慢；商用可编程设备里的 FPGA 与存储之间也走 PCIe，从设备 FPGA 访问数据的延迟并不显著低于主机处理器。
- **因此适用条件苛刻**：任务本身时延必须足够短、能尽快产出下一次读请求，否则省下的访问延迟不足以抵消增加的计算时间；同时处理器必须真正位于设备内部，最好与存储控制器同处一颗 SoC。
- **延迟结构佐证**：512B 随机读时，NAND 设备上软件层耗时 30.6 到 44.4µs、硬件 67.5 到 194.4µs，而 NVM 设备分别是 3.0 到 3.2µs 与 6.7 到 7.5µs，设备越快，软件栈在总延迟中的占比越高，绕过它的收益才越明显。

## 核心贡献

- **首次考察设备内算力能否加速数据依赖读**：在低延迟存储时代重新提出这个问题，并给出两个可迁移的结论：设备资源能及时可用时设备内执行确实有效；PCIe 延迟与设备自身的限制又常常使主机侧执行更划算。
- **选择性设备内执行（SODE）**：同时保留设备内与内核内两条重提交路径，按设备处理器的实时可用性动态选择，必要时把任务反向卸载（R-offload）回主机内核。
- **乐观的元数据使用**：设备内直接用缓存的文件系统元数据把文件偏移翻译成 LBA，只在重提交链结束时、响应回到主机后才检查元数据是否被改动过。
- **并行化重提交任务**：把判定“是否重提交、提交到哪个地址”的磁盘块遍历拆成可并行的任务，以缩短设备内任务的执行时延。
- **设备内沙箱与开源原型**：沿用 eBPF 加进程内隔离的思路约束设备内任务，在 NVMeVirt 上实现原型并公开实现与实验配置。

## 方法与技术要点

- **任务形态**：重提交任务以 eBPF filter 的形式表达，以上一次读的结果为输入，决定是否发出下一次读以及读哪里；同一份 filter 既能跑在内核路径，也能跑在设备内。
- **调度判定**：SODE 先看设备内处理器能否立即执行该任务；若其排队或执行延迟预计超过主机与设备之间的往返时间，就把任务回落到内核路径执行。
- **地址翻译**：设备内重提交必须把文件偏移转成逻辑块地址（LBA），而每次向主机取元数据都要一次 PCIe 往返；SODE 假定重提交期间元数据基本不变，用缓存副本翻译，在整条链结束后再统一校验。
- **并行化**：重提交任务常常要通过遍历磁盘数据块来判断下一步，SODE 将这些判定并行执行，从而压低单个任务的时延，扩大可受益的负载范围。
- **隔离与原型**：设备内任务必须被隔离，否则可能篡改设备侧软件栈或绕过文件系统访问控制发出任意 I/O；SODE 用 eBPF 校验与进程内隔离实现沙箱，并在 NVMeVirt 模拟环境中以限频 1.2GHz 的孱弱处理器形态运行。

## 评估与主要结果

- **平台**：在 NVMeVirt（先进存储模拟器）上实现原型，把模拟线程限频到 1.2GHz 以模拟紧邻控制器的孱弱处理器；对比对象是仅有内核内存储函数的路径（即 XRP 的做法）。
- **两个遍历磁盘结构的基准**：简单 B+-树键值存储的吞吐最高提升 41%；WiredTiger 这一日志结构合并树（LSM）型键值存储在 YCSB C 上的 99 分位尾延迟最高降低 3.85%。
- **三项指标同向**：SODE 的设计目标是不在吞吐、平均延迟、尾延迟之间做交换，实验结果在这三项上都取得改善。
- **适用范围**：只针对含数据依赖读的负载评估；对以吞吐为中心的负载，SODE 预期与 λ-IO 表现相当，因此未作专门测量。

## 代码与研究制品

- [代码仓库](https://github.com/cssl-unist/sode)

[返回 Hardware Assist](index.md) · [返回 FAST 2025](../index.md)
