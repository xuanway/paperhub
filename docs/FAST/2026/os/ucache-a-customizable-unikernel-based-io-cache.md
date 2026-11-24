---
title: "uCache: A Customizable Unikernel-based IO Cache"
description: "FAST 2026 · OS · 第 701–720 页"
tags:
  - "FAST2026"
  - "OS"
---

# uCache: A Customizable Unikernel-based IO Cache

**中文标题**：uCache：可定制的基于 Unikernel 的 IO 缓存

**Session**：OS · 2026-02-26 15:50–17:10 · Chair：Yu Liang（ETH Zurich）

**作者**：Ilya Meignan--Masson, Masanori Misono, Viktor Leis, and Pramod Bhatotia, Technical University of Munich

**会议**：FAST 2026 · Santa Clara, CA · 第 701–720 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/meignan-masson](https://www.usenix.org/conference/fast26/presentation/meignan-masson)

**论文 PDF**：[fast26-meignan-masson.pdf](https://www.usenix.org/system/files/fast26-meignan-masson.pdf)

---

## 英文摘要

Data-intensive cloud applications require high-performance IO caching to fully leverage modern storage systems like NVMe SSDs and cloud storage. Today’s developers face a dilemma: choose a simple, but often slow, OS-level IO cache, or a fast, but complex, userspace cache. This trade-off forces developers to sacrifice either performance or simplicity. This paper introduces uCache, a novel IO cache that resolves this fundamental tension. Leveraging a unikernel-based libOS architecture, uCache seamlessly integrates application-specific knowledge directly into the OS-level cache. It combines an mmap-like memory surface with an explicit, conventional interface, offering fine-grained control over cache behavior. This design allows for the seamless integration of application-specific semantics within the OS-level cache itself—a capability previously confined to complex userspace solutions; thus, ensuring scalability, performance, and adaptability. The core of uCache’s flexibility is the uVFS abstraction, which enables direct adaptation to diverse IO backends while maintaining filesystem compatibility without the performance overheads of the traditional OS IO stack. Our evaluation demonstrates that uCache effectively merges the simplicity of OS-level caches with the performance and flexibility of userspace solutions. For out-of-memory workloads, uCache achieves performance on par with kernel-bypass IO libraries, proving it can eliminate the IO caching bottleneck for data-intensive applications.

## 中文摘要

数据密集型云应用需要高性能 IO 缓存，以充分利用 NVMe SSD 和云存储等现代存储系统。如今的开发者面临两难：选择简单但往往缓慢的操作系统级 IO 缓存，或选择快速但复杂的用户态缓存。这种权衡迫使开发者牺牲性能或简单性。本文提出 uCache，一种新颖的 IO 缓存，解决了这一根本矛盾。借助基于 Unikernel 的 libOS 架构，uCache 将应用特定知识无缝集成到操作系统级缓存中。它将类 mmap 的内存接口与显式的常规接口相结合，提供对缓存行为的细粒度控制。这种设计允许在操作系统级缓存本身中无缝集成应用特定语义——这一能力此前仅限于复杂的用户态方案；因此，它确保了可扩展性、性能和适应性。uCache 灵活性的核心是 uVFS 抽象，它能够直接适配多样的 IO 后端，同时保持文件系统兼容性，且不引入传统操作系统 IO 栈的性能开销。我们的评估表明，uCache 有效融合了操作系统级缓存的简单性与用户态方案的性能和灵活性。对于内存不足（out-of-memory）负载，uCache 的性能与内核旁路 IO 库相当，证明它能够消除数据密集型应用的 IO 缓存瓶颈。
