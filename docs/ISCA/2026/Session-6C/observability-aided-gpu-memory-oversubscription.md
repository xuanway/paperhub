---
title: "Observability-aided GPU Memory Oversubscription"
description: "ISCA 2026 · Session 6C · Observability-aided GPU Memory Oversubscription"
tags:
  - "ISCA2026"
  - "Session 6C"
  - "GPUs and Compilation"
---

# Observability-aided GPU Memory Oversubscription

**中文标题：** 可观测性辅助的 GPU 内存超分

**所属 Session：** [Session 6C](index.md) · [ISCA 2026](../index.md)

**作者：** Pratheek B, Khushit Shah, Arkaprava Basu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Unified Virtual Memory (UVM) enables the oversubscription of GPUs’ limited High Bandwidth Memory (HBM) capacity. Unfortunately, applications can significantly slow down when HBM is oversubscribed. We set out to make oversubscription practical without needing custom hardware modifications. The UVM driver, executing on the CPU, is responsible for eviction and prefetching but lacks observability into GPUs’ accesses to HBM-resident memory. This fundamentally limits the driver’s ability to make informed decisions. Toward this, we repurpose existing hardware access counters originally designed to track PCIe accesses to CPU’s DRAM to aid page migration. Instead, we leverage the counters to provide (sampled) observability into GPU’s accesses to HBM-resident pages. We then create ObservUVM, a novel software framework that enables easy exploration of observability-aided custom eviction and prefetching policies in the userspace, facilitating future research. We demonstrate that better-informed eviction and prefetching policies, enabled by the newfound observability, can significantly speed up GPU applications under memory oversubscription.

## 中文摘要

统一虚拟内存（UVM）使 GPU 有限的高带宽内存（HBM）容量得以超分。遗憾的是，当 HBM 被超分时，应用可能显著变慢。我们致力于在不需定制硬件修改的情况下使超分变得实用。运行在 CPU 上的 UVM 驱动负责换出与预取，但缺乏对 GPU 访问 HBM 常驻内存的可观测性。这从根本上限制了驱动做出明智决策的能力。为此，我们重用现有的硬件访问计数器——其最初设计用于跟踪对 CPU DRAM 的 PCIe 访问以辅助页迁移——转而利用这些计数器提供对 GPU 访问 HBM 常驻页面的（采样）可观测性。随后我们构建了 ObservUVM，一个新颖的软件框架，使用户空间能够轻松探索可观测性辅助的自定义换出与预取策略，为未来研究提供便利。我们证明，借助新获得的可观测性所实现的更明智的换出与预取策略，可以显著加速内存超分下的 GPU 应用。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：csl-iisc/ObservUVM](https://github.com/csl-iisc/ObservUVM)
- [实验材料归档（Zenodo 19428841）](https://zenodo.org/records/19428841)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2026](../index.md)
