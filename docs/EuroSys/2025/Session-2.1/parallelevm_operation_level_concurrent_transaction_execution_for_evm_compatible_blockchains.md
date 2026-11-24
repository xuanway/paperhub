---
title: "ParallelEVM: Operation-Level Concurrent Transaction Execution for EVM-Compatible Blockchains"
description: "EuroSys 2025 · Fault Tolerance and Consensus · Haoran Lin (Zhejiang University), Hang Feng (Zhejiang University), Yajin Zhou (Z"
tags:
  - "EuroSys2025"
  - "Fault Tolerance and Consensus"
---

# ParallelEVM: Operation-Level Concurrent Transaction Execution for EVM-Compatible Blockchains

**中文标题：** 面向 EVM 兼容区块链的操作级并发交易执行

**所属 Session：** [Session 2.1: Fault Tolerance and Consensus](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Fault Tolerance and Consensus。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Fault Tolerance and Consensus</p>
</div>

**作者**：Haoran Lin (Zhejiang University), Hang Feng (Zhejiang University), Yajin Zhou (Zhejiang University), Lei Wu (Zhejiang University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696063)

## 英文摘要

Blockchain systems, especially EVM-compatible ones that serially execute transactions, face a significant limitation in throughput. One promising solution is concurrent transaction execution, which accelerates transaction processing and increases the overall throughput. However, existing concurrency control algorithms fail to obtain adequate speedups in high-contention blockchain workloads, primarily due to their transaction-level conflict resolution strategies.

This paper introduces a novel operation-level concurrency control algorithm tailored for blockchains. The crux of our approach is to ensure that only operations depending on conflicts are executed serially, while permitting concurrent execution of the remaining conflict-free operations. In contrast to conventional approaches that either block or abort an entire transaction upon detecting conflicts, our algorithm integrates a redo phase that identifies and re-executes conflicting operations. To facilitate this, we propose the SSA (static single-assignment) operation log, a mechanism to trace operation dependencies, thereby enabling precise conflict identification and efficient re-execution. Our prototype, ParallelEVM, is evaluated using real-world Ethereum blocks. Experimental results show that ParallelEVM achieves an average speedup of 4.28×, a marked improvement over the 2.49× speedup achieved by optimistic concurrency control.

## 中文摘要

区块链系统，尤其是串行执行交易的 EVM 兼容系统，在吞吐量上面临显著局限。一种有前景的解决方案是并发交易执行，它可加速交易处理并提升整体吞吐量。然而，现有并发控制算法在高竞争的区块链负载中无法获得足够的加速，主要原因在于其交易级的冲突消解策略。

本文提出一种为区块链量身定制的、新颖的操作级并发控制算法。我们方法的关键在于：确保只有存在冲突依赖的操作串行执行，而其余无冲突操作可以并发执行。与在检测到冲突时阻塞或中止整笔交易的传统方法不同，我们的算法引入了重做阶段，用于识别并重新执行冲突操作。为此，我们提出 SSA（静态单赋值）操作日志，这是一种追踪操作依赖关系的机制，从而实现精确的冲突识别和高效的重执行。我们使用真实以太坊区块评估了原型系统 ParallelEVM。实验结果表明，ParallelEVM 平均获得 4.28 倍加速，明显优于乐观并发控制所取得的 2.49 倍加速。

**英文关键词：** Concurrency, Operation-Level, EVM, Transaction Execution, SSA Operation Log

**中文关键词：** 并发、操作级、EVM、交易执行、SSA 操作日志

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
