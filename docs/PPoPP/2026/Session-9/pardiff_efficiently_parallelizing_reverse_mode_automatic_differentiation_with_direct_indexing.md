---
title: "ParDiff: Efficiently Parallelizing Reverse-Mode Automatic Differentiation with Direct Indexing"
description: "PPoPP 2026 Session 9（Parallel Algorithms）：直接索引磁带 + 求和感知循环变换，较 Enzyme 最高 483.21×"
tags:
  - "PPoPP2026"
  - "Session-9"
  - "Parallel Algorithms"
  - "Automatic Differentiation"
  - "Parallelization"
  - "Tape Design"
authors:
  - "Shuhong Huang"
  - "Shizhi Tang"
  - "Yuan Wen"
  - "Huanqi Cao"
  - "Ruibai Tang"
  - "Yidong Chen"
  - "Jiping Yu"
  - "Yang Li"
  - "Chao Jiang"
  - "Limin Xiao"
  - "Jidong Zhai"
session: "Session 9: Parallel Algorithms"
session_number: 9
session_chair: "Kenjiro Taura"
date: "2026-02-03"
time: "14:30–14:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786418"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# ParDiff: Efficiently Parallelizing Reverse-Mode Automatic Differentiation with Direct Indexing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 ParDiff，采用直接索引磁带设计的自动微分系统，配合求和感知循环变换与多种并行方案，相比 Enzyme 最高加速 483.21×（几何平均 30.88×）。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 9: Parallel Algorithms</p>
</div>

**作者**：Shuhong Huang, Shizhi Tang, Yuan Wen, Huanqi Cao, Ruibai Tang, Yidong Chen, Jiping Yu, Yang Li, Chao Jiang, Limin Xiao, and Jidong Zhai — Tsinghua University, China; Qingcheng.AI, China; University of Aberdeen, UK; Lenovo Research, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:30–14:50 · Session 9: Parallel Algorithms（主席：Kenjiro Taura）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786418) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Automatic Differentiation (AD) is a technique that computes the derivatives of numerical programs by systematically applying the chain rule, playing a critical role in domains such as machine learning, simulation, and control systems. However, parallelizing differentiated programs remains a significant challenge due to the conflict between tapes (a data structure for intermediate variable storage) and summations: the differentiation process inherently introduces inter-thread summation patterns, which require prohibitively expensive atomic operations; and traditional tape designs tightly couple data retrieval with the program’s control flow, preventing code restructuring needed to eliminate these costly dependencies. To address these challenges, we present ParDiff, a novel AD system with a direct-indexed tape design, which enables summation-aware loop transformations and various parallel schemes for differentiated programs. This results in a higher degree of parallelization, less synchronization, and reduced overhead. We conduct comprehensive experiments on both multi-core CPUs and GPUs. Results show that ParDiff delivers up to 483.21× (geometric mean: 30.88×) speedup over the state-of-the-art fully-AD system, Enzyme. It also achieves a speedup of 2.05× and 2.06× over PyTorch on CPU and GPU, respectively. The source code is publicly available at https://github.com/roastduck/FreeTensor.

## 中文摘要

自动微分（AD）是一种通过系统应用链式法则来计算数值程序导数的技术，在机器学习、仿真和控制系统等领域发挥着关键作用。然而，并行化微分后的程序仍是重大挑战，根源在于磁带（tape，一种用于存储中间变量的数据结构）与求和之间的矛盾：微分过程本身会引入线程间求和模式，这需要代价高昂的原子操作；而传统磁带设计将数据获取与程序控制流紧密耦合，阻碍了为消除这些昂贵依赖所需的代码重构。为应对这些挑战，我们提出 ParDiff，一个具有直接索引磁带设计的新型 AD 系统，它支持求和感知的循环变换以及针对微分后程序的各种并行方案。这带来了更高的并行度、更少的同步以及更低的额外开销。我们在多核 CPU 与 GPU 上开展了全面实验。结果表明，ParDiff 相比最先进的完全 AD 系统 Enzyme 最高取得 483.21 倍（几何平均 30.88 倍）的加速，并在 CPU 与 GPU 上分别相比 PyTorch 取得 2.05 倍和 2.06 倍的加速。源码公开于 https://github.com/roastduck/FreeTensor。

## 英文关键词

AD, Tape, Parallel Computing, Direct Indexing

## 中文关键词

自动微分（AD）；磁带；并行计算；直接索引

---

## 一句话总结

> 提出 ParDiff，采用直接索引磁带设计的自动微分系统，配合求和感知循环变换与多种并行方案，相比 Enzyme 最高加速 483.21×（几何平均 30.88×）。

## 研究问题

并行化微分程序很困难：微分过程会引入线程间求和模式，需要代价高昂的原子操作；而传统磁带设计把数据检索与控制流紧耦合，使代码无法重构以消除这些依赖。

## 方法简述

- 提出直接索引（direct-indexed）磁带设计，将数据检索与程序控制流解耦。
- 将微分引入的求和模式建模为可变换对象，实现求和感知的循环变换。
- 为微分后的程序提供多种并行方案，以提升并行度并减少同步。
- 在多核 CPU 与 GPU 上实现该系统并做全面评测，源代码已公开。

## 主要结果

- 相比全自动微分的最先进系统 Enzyme 最高加速 483.21×，几何平均 30.88×。
- 在 CPU 与 GPU 上分别比 PyTorch 加速 2.05× 与 2.06×。

---

> 所属 Session：[Session 9: Parallel Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
