---
title: "Cylon: Fast and Accurate Full-System Emulation of CXL-SSDs"
description: "FAST 2026 · SSDs and CXL · 第 313–328 页"
tags:
  - "FAST2026"
  - "SSDs and CXL"
---

# Cylon: Fast and Accurate Full-System Emulation of CXL-SSDs

**中文标题**：Cylon：快速准确的全系统 CXL-SSD 仿真

**Session**：SSDs and CXL · 2026-02-25 14:00–15:40 · Chair：Ethan Miller（University of California, Santa Cruz, and Pure Storage）

**作者**：Dongha Yoon, Hansen Idden, Jinshu Liu, Berkay Inceisci, Sam H. Noh, and Huaicheng Li, Virginia Tech

**会议**：FAST 2026 · Santa Clara, CA · 第 313–328 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/yoon](https://www.usenix.org/conference/fast26/presentation/yoon)

**论文 PDF**：[fast26-yoon.pdf](https://www.usenix.org/system/files/fast26-yoon.pdf)

---

## 英文摘要

We present Cylon, a fast and extensible full-system emulator for CXL-SSDs built on FEMU. Cylon bridges the gap between closed hardware prototypes and slow software simulators by faithfully reproducing sub-μs cache hits and tens-of-μs misses that fall to NAND through a hybrid execution path that mitigates hypervisor trap overheads. Cylon supports configurable caching policies and provides an application-level interface for hardware-software co-design. Validated against a real CXL-SSD prototype, Cylon accurately models performance across a wide range of applications, from microbenchmarks to full-scale workloads. Our evaluation shows that Cylon reproduces realistic latency distributions, executes unmodified applications at near bare-metal speed, and scales to system-level studies. By combining speed, fidelity, and extensibility, Cylon fills a critical gap for evaluating today’s CXL-SSDs and exploring next-generation architectures that blend CXL-enabled memory and storage semantics.

## 中文摘要

我们提出 Cylon，一个基于 FEMU 构建的快速、可扩展的 CXL-SSD 全系统仿真器。Cylon 通过一种缓解虚拟机监控器陷入开销的混合执行路径，忠实复现低于 1 微秒的缓存命中和数十微秒、需访问 NAND 的缓存缺失，从而弥合了封闭硬件原型与缓慢软件模拟器之间的差距。Cylon 支持可配置的缓存策略，并提供应用级接口以支持软硬件协同设计。Cylon 已对照真实 CXL-SSD 原型进行验证，能够准确建模从微基准到全规模负载的广泛应用性能。我们的评估表明，Cylon 可复现真实的延迟分布，以接近裸机的速度执行未经修改的应用，并可扩展到系统级研究。通过结合速度、保真度和可扩展性，Cylon 填补了评估当今 CXL-SSD 以及探索融合 CXL 内存与存储语义的下一代架构方面的关键空白。
