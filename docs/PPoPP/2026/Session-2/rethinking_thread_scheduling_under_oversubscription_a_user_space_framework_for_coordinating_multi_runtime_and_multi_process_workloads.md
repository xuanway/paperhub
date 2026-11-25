---
title: "Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads"
description: "PPoPP 2026 Session 2（Scheduling and Load Balancing）：用户态调度框架 + 协作策略，超订场景最高加速 2.4×"
tags:
  - "PPoPP2026"
  - "Session-2"
  - "Scheduling and Load Balancing"
  - "Thread Scheduling"
  - "Oversubscription"
  - "User-space Runtime"
authors:
  - "Aleix Roca"
  - "Vicenç Beltran"
session: "Session 2: Scheduling and Load Balancing"
session_number: 2
session_chair: "V Krishna Nandivada"
date: "2026-02-02"
time: "11:30–11:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786451"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
award: "Best Paper Nominee"
---

# Rethinking Thread Scheduling under Oversubscription: A User-Space Framework for Coordinating Multi-runtime and Multi-process Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出完全在用户态实现的进程调度框架 USF 及其默认协作策略 SCHED_COOP，在超订的多运行时、多进程负载下减少调度干扰。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 2: Scheduling and Load Balancing</p>
</div>

**作者**：Aleix Roca and Vicenç Beltran — Barcelona Supercomputing Center, Spain

**会议**：PPoPP 2026 · 2026 年 2 月 2 日 11:30–11:50 · Session 2: Scheduling and Load Balancing（主席：V Krishna Nandivada）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786451) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

> 🏆 **Best Paper Nominee**

---

## 英文摘要

The convergence of high-performance computing (HPC) and artificial intelligence (AI) is driving the emergence of increasingly complex parallel applications and workloads. These workloads often combine multiple parallel runtimes within the same application or across co-located jobs, creating scheduling demands that place significant stress on traditional OS schedulers. When oversubscribed (there are more ready threads than cores), OS schedulers rely on periodic preemptions to multiplex cores, often introducing interference that may degrade performance. In this paper, we present: (1) The User-space Scheduling Framework (USF), a novel seamless process scheduling framework completely implemented in user-space. USF enables users to implement their own process scheduling algorithms without requiring special permissions. We evaluate USF with its default cooperative policy, (2) SCHED_COOP, designed to reduce interference by switching threads only upon blocking. This approach mitigates well-known issues such as Lock-Holder Preemption (LHP), Lock-Waiter Preemption (LWP), and scalability collapse. We implement USF and SCHED_COOP by extending the GNU C library with the nOS-V runtime, enabling seamless coordination across multiple runtimes (e.g., OpenMP) without requiring invasive application changes. Evaluations show gains up to 2.4x in oversubscribed multi-process scenarios, including nested BLAS workloads, multi-process PyTorch inference with LLaMA-3, and Molecular Dynamics (MD) simulations.

## 中文摘要

高性能计算（HPC）与人工智能（AI）的融合正推动着日益复杂的并行应用与工作负载的出现。这些工作负载常常在同一应用内部或跨共置作业组合使用多个并行运行时，由此产生的调度需求给传统操作系统调度器带来了巨大压力。当出现过订阅（就绪线程数多于核数）时，操作系统调度器依赖周期性抢占来复用核，这往往会引入干扰，并可能降低性能。在本文中，我们提出：(1) 用户空间调度框架（User-space Scheduling Framework，USF），一个完全在用户空间实现的新颖无缝进程调度框架。USF 使用户无需特殊权限即可实现自己的进程调度算法。我们以其默认的协作式策略 (2) SCHED_COOP 对 USF 进行评估，该策略旨在通过仅在阻塞时才切换线程来减少干扰。这一方法缓解了诸如锁持有者抢占（Lock-Holder Preemption，LHP）、锁等待者抢占（Lock-Waiter Preemption，LWP）以及可扩展性崩溃等众所周知的问题。我们通过用 nOS-V 运行时扩展 GNU C 库来实现 USF 与 SCHED_COOP，从而在无需对应用做侵入式修改的情况下实现多个运行时（例如 OpenMP）之间的无缝协调。评估显示，在过订阅的多进程场景中可获得最高 2.4 倍的收益，这些场景包括嵌套 BLAS 工作负载、使用 LLaMA-3 的多进程 PyTorch 推理以及分子动力学（MD）模拟。

## 英文关键词

High Performance Computing, Thread Oversubscription, Runtime Systems, User-Space Scheduling

## 中文关键词

高性能计算（HPC）；线程过订阅（Thread Oversubscription）；运行时系统；用户空间调度（User-Space Scheduling）

---

## 一句话总结

> 提出完全在用户态实现的进程调度框架 USF 及其默认协作策略 SCHED_COOP，在超订的多运行时、多进程负载下减少调度干扰。

## 研究问题

HPC 与 AI 融合使应用在同一进程或共置作业中组合多个并行运行时；当就绪线程多于核心时，OS 依赖周期性抢占复用核心，带来锁持有者抢占、锁等待者抢占与可扩展性坍塌等干扰。

## 方法简述

- 用用户态实现进程调度框架，用户无需特权即可自定义调度算法。
- SCHED_COOP 仅在阻塞时切换线程，以缓解锁持有者抢占、锁等待者抢占与可扩展性坍塌。
- 通过扩展 GNU C 库并集成 nOS-V 运行时，在不侵入应用的前提下协调 OpenMP 等多个运行时。

## 主要结果

- 超订多进程场景最高加速 2.4×。
- 在嵌套 BLAS、多进程 PyTorch LLaMA-3 推理与分子动力学模拟等负载上验证有效。

---

> 所属 Session：[Session 2: Scheduling and Load Balancing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
