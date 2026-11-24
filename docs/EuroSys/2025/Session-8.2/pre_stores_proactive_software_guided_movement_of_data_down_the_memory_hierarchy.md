---
title: "Pre-Stores: Proactive Software-guided Movement of Data Down the Memory Hierarchy"
description: "EuroSys 2025 · Storage · Xiaoxiang Wu (The University of Sydney), Baptiste Lepers (Inria and The Universi"
tags:
  - "EuroSys2025"
  - "Storage"
---

# Pre-Stores: Proactive Software-guided Movement of Data Down the Memory Hierarchy

**中文标题：** 软件引导的主动数据下移以优化内存层次结构

**所属 Session：** [Session 8.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Xiaoxiang Wu (The University of Sydney), Baptiste Lepers (Inria and The University of Neuchâtel), Willy Zwaenepoel (University of Sydney)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696097)

## 英文摘要

We introduce the notion of software pre-storing – the converse of software pre-fetching. With software pre-fetching, instructions are inserted in the code to asynchronously move data up in the memory hierarchy. With software pre-storing, instructions are inserted to direct the CPU to asynchronously move data down in the memory hierarchy. Pre-storing can be implemented by using existing processor instructions.

Software pre-storing provides performance benefits for write-heavy applications, especially with emerging architectures that incorporate memories with diverse characteristics such as, for instance, remote DRAM accessed via a CXL switch or nonvolatile PMEM memory. We identify application scenarios in which software pre-storing is beneficial, and we have developed a tool, DirtBuster, that identifies applications and code regions that can benefit from pre-storing.

We evaluate the concept of software pre-storing and the DirtBuster tool on two CPU architectures (ARM and x86) and two types of cacheable memories (PMEM and cache-coherent DRAM accessed through an FPGA). We demonstrate performance improvements for key-value stores, HPC applications, message passing, and Tensorflow, by up to 2.3×.

## 中文摘要

我们引入软件预存储的概念——它是软件预取的逆向操作。在软件预取中，指令被插入代码中，以异步地将数据在内存层次中上移。在软件预存储中，指令被插入以指示 CPU 异步地将数据在内存层次中下移。预存储可以通过使用现有的处理器指令来实现。

软件预存储为写密集型应用带来性能收益，尤其是对于集成了具有多样特性内存的新兴架构，例如通过 CXL 交换机访问的远程 DRAM，或非易失性 PMEM 内存。我们识别了软件预存储有益的应用场景，并开发了一个工具 DirtBuster，它能够识别可从预存储中获益的应用和代码区域。

我们在两种 CPU 架构（ARM 和 x86）和两种可缓存内存（PMEM 和通过 FPGA 访问的缓存一致性 DRAM）上评估了软件预存储概念和 DirtBuster 工具。我们展示了键值存储、HPC 应用、消息传递和 TensorFlow 的性能提升最高可达 2.3 倍。

**英文关键词：** CPU caches, pre-fetch, pre-store, hybrid memory

**中文关键词：** CPU 缓存、预取、预存储、混合内存

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
