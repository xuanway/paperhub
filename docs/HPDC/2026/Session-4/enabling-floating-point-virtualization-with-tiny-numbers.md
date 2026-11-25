---
title: "Enabling Floating Point Virtualization With Tiny Numbers"
description: "HPDC 2026 · Session 4 — Programming Models, Frameworks & Compilers"
tags:
  - "HPDC2026"
  - "Session 4"
  - "Programming Models, Frameworks & Compilers"
---

# Enabling Floating Point Virtualization With Tiny Numbers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 4</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807578)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#HayesD26](https://dblp.org/db/conf/hpdc/hpdc2026.html#HayesD26)

**作者**：Kevin Hayes, Peter Dinda

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）

---

## 英文摘要

Floating point virtualization allows existing, unmodified application binaries to be run using an alternative arithmetic system. Such virtualization is geared to alternative numbers that are “larger” (require more bits) than the IEEE 754 numbers (e.g., 64 bit doubles) they replace. In this work, we approach the challenge of virtualizing with “smaller” numbers (requiring fewer bits), which is of increasing interest given the explosion of low-precision hardware targeting AI. We focus specifically on the ubiquitous x64 architecture through a hardware/software co-design that leverages x64 functionality that currently lays fallow. The design combines (a) instruction traps via lazy FPU abduction, and (b) simplified memory management by tiny value boxing. We also develop an example tiny alternative arithmetic system that allows smaller IEEE 754 numbers, down to 3 bits, with the exact precision able to be specified on a per-value or per-instruction basis at runtime. Our prototype system is evaluated using validation and performance tests based on running NAS and other benchmarks with a range of lower precision numbers.

## 中文摘要

浮点虚拟化允许使用替代算术系统运行现有未经修改的应用二进制。此类虚拟化面向比其所替代的 IEEE 754 数（如 64 位双精度）更“大”（需要更多位）的替代数。在本工作中，我们应对使用更“小”的数（需要更少位）进行虚拟化的挑战；鉴于面向 AI 的低精度硬件爆发式增长，这一方向日益受到关注。我们聚焦无处不在的 x64 架构，通过软硬件协同设计利用 x64 目前闲置的功能。该设计结合了：(a) 通过惰性 FPU 抢占实现指令陷阱，(b) 通过微小值装箱简化内存管理。我们还开发了一个示例性的微小替代算术系统，支持小至 3 位的更小 IEEE 754 数，并可在运行时按值或按指令精确指定精度。我们的原型系统通过在多种低精度数下运行 NAS 及其他基准的验证与性能测试进行评估。

## 英文关键词

virtualization, floating point arithmetic, software development, IEEE 754

## 中文关键词

虚拟化，浮点算术，软件开发，IEEE 754

---

[← 返回 Session 4 — Programming Models, Frameworks & Compilers](index.md)
