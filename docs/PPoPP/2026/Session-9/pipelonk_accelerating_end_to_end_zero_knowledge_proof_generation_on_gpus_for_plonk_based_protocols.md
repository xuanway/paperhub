---
title: "Pipelonk: Accelerating End-to-End Zero-Knowledge Proof Generation on GPUs for PLONK-Based Protocols"
description: "PPoPP 2026 Session 9（Parallel Algorithms）：8–80GB 显存均可运行，平均加速 10.7×、最高 19.4×"
tags:
  - "PPoPP2026"
  - "Session-9"
  - "Parallel Algorithms"
  - "Zero-Knowledge Proof"
  - "GPU Acceleration"
  - "Pipelining"
authors:
  - "Zhiyuan Zhang"
  - "Yanxin Cai"
  - "Wenhao Yin"
  - "Xueyu Wu"
  - "Yi Wang"
  - "Lei Ju"
  - "Zhuoran Ji"
session: "Session 9: Parallel Algorithms"
session_number: 9
session_chair: "Kenjiro Taura"
date: "2026-02-03"
time: "14:10–14:30"
room: "Pyrmont"
doi: "10.1145/3774934.3786448"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Pipelonk: Accelerating End-to-End Zero-Knowledge Proof Generation on GPUs for PLONK-Based Protocols

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Pipelonk，GPU 上 PLONK 协议的端到端证明生成框架：分段算子库把全部算子卸载到 GPU，流水线执行器重叠计算与传输，平均加速 10.7×、最高 19.4×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 9: Parallel Algorithms</p>
</div>

**作者**：Zhiyuan Zhang, Yanxin Cai, Wenhao Yin, Xueyu Wu, Yi Wang, Lei Ju, and Zhuoran Ji — Shandong University, China; Quan Cheng Laboratory, China; University of Hong Kong, China; Shenzhen University, China; State Key Laboratory of Cryptography and Digital Economy Security, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:10–14:30 · Session 9: Parallel Algorithms（主席：Kenjiro Taura）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786448) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Zero-knowledge proofs (ZKPs) are cryptographic protocols that allow verification of statements without disclosing the underlying information. Among them, PLONK-based ZKPs are particularly notable for offering succinct, non-interactive proofs of knowledge with a universal trusted setup, leading to widespread adoption in blockchain and cryptocurrency applications. Nonetheless, their broader deployment is hindered by long proof-generation times and substantial memory demands. While GPUs can accelerate these computations, their limited memory capacity introduces significant challenges for efficient end-to-end proof generation. This paper presents Pipelonk, a GPU-accelerated framework for end-to-end PLONK proof generation with two key contributions. First, Pipelonk introduces a segmentable operator library that offloads all operations, including those not trivially parallelized, to GPUs through new designs. Each operator supports segmented execution, allowing inputs to be divided into smaller segments processed independently, thus enabling large-scale computations on memory-constrained devices. Second, Pipelonk provides a pipeline executor that overlaps computation and data transfer. It globally schedules compute- and memory-intensive tasks while preserving data and security dependencies, balances transfer-latency hiding against peak memory, and adaptively selects per-operator segment sizes by modeling memory capacity and computational characteristics to maximize compute-transfer overlap. Evaluation shows that Pipelonk runs efficiently on devices with 8 GB to 80 GB memory, achieving an average speedup of 10.7× and up to 19.4× over the state-of-the-art baseline.

## 中文摘要

零知识证明（ZKP）是一类密码学协议，允许在不披露底层信息的情况下验证陈述。其中，基于 PLONK 的 ZKP 因能提供简洁、非交互的知识证明并具备通用可信设置而尤为突出，在区块链与加密货币应用中得到广泛采用。然而，其证明生成时间长、内存需求大，阻碍了更广泛的部署。尽管 GPU 可以加速这些计算，但其有限的内存容量为高效的端到端证明生成带来了重大挑战。本文提出 Pipelonk，一个用于端到端 PLONK 证明生成的 GPU 加速框架，包含两项关键贡献。第一，Pipelonk 引入可分段算子库，通过新的设计将所有算子（包括那些难以自然并行化的算子）卸载到 GPU 上。每个算子支持分段执行，可将输入划分为更小的段独立处理，从而在内存受限的设备上完成大规模计算。第二，Pipelonk 提供流水线执行器，重叠计算与数据传输。它在保持数据依赖与安全依赖的前提下全局调度计算密集型与内存密集型任务，在隐藏传输延迟与峰值内存之间取得平衡，并通过建模内存容量与计算特征来自适应地选择每个算子的分段大小，以最大化计算与传输的重叠。评估表明，Pipelonk 在 8 GB 至 80 GB 内存的设备上均可高效运行，相比最先进的基线平均加速 10.7 倍，最高可达 19.4 倍。

## 英文关键词

Zero knowledge proofs; GPU acceleration

## 中文关键词

零知识证明；GPU 加速

---

## 一句话总结

> 提出 Pipelonk，GPU 上 PLONK 协议的端到端证明生成框架：分段算子库把全部算子卸载到 GPU，流水线执行器重叠计算与传输，平均加速 10.7×、最高 19.4×。

## 研究问题

PLONK 类零知识证明的证明生成时间长、内存需求大；GPU 虽可加速，但显存容量有限，难以高效完成端到端证明生成。

## 方法简述

- 设计可分段算子库，通过新设计将包括难以平凡并行的操作在内的全部算子卸载到 GPU 执行。
- 让每个算子支持分段执行，把输入切分为可独立处理的较小段，使大规模计算能在内存受限设备上完成。
- 提供流水线执行器重叠计算与数据传输，全局调度计算密集型与访存密集型任务并保持数据与安全依赖。
- 在隐藏传输延迟与峰值内存之间权衡，并通过建模内存容量与计算特性自适应选择各算子的分段大小，最大化计算—传输重叠。

## 主要结果

- 在 8 GB 至 80 GB 显存的设备上都能高效运行。
- 相比最好基线平均加速 10.7×，最高加速 19.4×。

---

> 所属 Session：[Session 9: Parallel Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
