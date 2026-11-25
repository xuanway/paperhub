---
title: "Crystality: A Programming Model for Smart Contracts on Parallel EVMs"
description: "PPoPP 2025 Session 9（Concurrent Data Structures and Synchronization II）：可编程合约作用域 + 异步中继，在 64 核上优于 Ethereum/Aptos/Sui"
tags:
  - "PPoPP2025"
  - "Session-9"
  - "Concurrent Data Structures and Synchronization II"
  - "Smart Contracts"
  - "Parallel EVM"
  - "Programming Model"
authors:
  - "Hao Wang"
  - "Minghao Pan"
  - "Jiaping Wang"
session: "Session 9: Concurrent Data Structures and Synchronization II"
session_number: 9
session_chair: "Pengfei Su"
date: "2025-03-04"
time: "16:40–17:00"
room: "Acacia D"
doi: "10.1145/3710848.3710879"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Crystality: A Programming Model for Smart Contracts on Parallel EVMs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向并行 EVM 的智能合约编程模型 Crystality，用可编程合约作用域划分并行状态、用异步函数中继管理跨 EVM 执行流，并以 Solidity 扩展和转译保持兼容。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 9: Concurrent Data Structures and Synchronization II</p>
</div>

**作者**：Hao Wang, Minghao Pan (International Digital Economy Academy (IDEA), China); Jiaping Wang (International Digital Economy Academy (IDEA), China; and The Hong Kong University of Science and Technology (Guangzhou), China)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 16:40–17:00 · Session 9: Concurrent Data Structures and Synchronization II（主席：Pengfei Su）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710879) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向并行 EVM 的智能合约编程模型 Crystality，用可编程合约作用域划分并行状态、用异步函数中继管理跨 EVM 执行流，并以 Solidity 扩展和转译保持兼容。

## 研究问题

以太坊顺序、共享一切的模型限制了并行机制效率：乐观方法回滚频繁，悲观方法则因状态依赖分析和加锁而开销高昂。

## 方法简述

- Programmable Contract Scopes 把合约状态划分为互不重叠的可并行段，并把合约函数分解为更细粒度的组件。
- Asynchronous Functional Relay 管理跨 EVM 的执行流，支持可交换合约操作的异步执行。
- 扩展 Solidity 指令并转译为标准 Solidity；提供异步模式与基于乐观的回退模式以保持区块内交易顺序。

## 主要结果

- 在 64 核机器上性能优于 Ethereum、Aptos 与 Sui。
- 在保持 EVM 兼容的同时简化了合约并行性的表达。

<details>
<summary>原文摘要（英文）</summary>

Scaling blockchain performance through parallel smart contract execution has gained significant attention, as traditional methods remain constrained by the performance of a single virtual machine (VM), even in multi-chain or Layer-2 systems. Parallel VMs offer a compelling solution by enabling concurrent transaction execution within a single smart contract, using multiple CPU cores. However, Ethereum’s sequential, shared-everything model limits the efficiency of existing parallel mechanisms, resulting in frequent rollbacks with optimistic methods and high overhead with pessimistic methods due to state dependency analysis and locking. This paper introduces Crystality, a programming model for smart contracts on parallel Ethereum Virtual Machines (EVMs) that enables developers to express and leverage the parallelism inherent in smart contracts. Crystality introduces Programmable Contract Scopes to partition contract states into non-overlapping, parallelizable segments and decompose a smart contract function into finer-grained components. Crystality also features Asynchronous Functional Relay to manage execution flow across EVMs. These features simplify parallelism expression and enable asynchronous execution for commutative contract operations. Crystality extends Solidity with directives, transpiling Crystality code into standard Solidity code for EVM compatibility. The system supports two execution modes: an asynchronous mode for transactions involving commutative operations and an optimistic-based fallback to ensure block-defined transaction order. Our experiments demonstrated Crystality’s superior performance compared to Ethereum, Aptos, and Sui on a 64-core machine.

</details>

---

> 所属 Session：[Session 9: Concurrent Data Structures and Synchronization II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
