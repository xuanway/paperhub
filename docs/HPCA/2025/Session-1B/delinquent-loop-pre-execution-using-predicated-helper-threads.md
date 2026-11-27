---
title: "Delinquent Loop Pre-execution Using Predicated Helper Threads"
description: "HPCA 2025 · Speculating in Vegas"
tags:
  - "HPCA2025"
  - "Speculating in Vegas"
---

# Delinquent Loop Pre-execution Using Predicated Helper Threads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Speculating in Vegas。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Speculating in Vegas</p>
</div>

**论文链接**：
**作者**：Anirudh Seshadri (North Carolina State University), Eric Rotenberg (North Carolina State University)
**会议**：HPCA 2025

---

## 中文标题

利用谓词化辅助线程进行难预测循环预执行

## 英文摘要

Branch pre-execution targets delinquent branches that are not predictable by conventional branch predictors. Helper threads attempt to resolve branches ahead of the main thread. Pre-executed branch outcomes are communicated to the main thread’s fetch unit via a global branch queue or local branch queues (one per branch PC). Two key challenges are discussed in this paper. 1) Handling a delinquent branch b2 that is control-dependent on another delinquent branch b1. Prior works that include both branches resort to branch prediction of b1 in the helper thread to determine whether or not to pre-execute b2. But b1 is hard-to-predict and the misprediction bottleneck merely shifts from the main thread to the helper thread. 2) Handling a store instruction that both influences a delinquent branch and is control-dependent on it. We propose predicated helper threads (Phelps) to address these challenges. Phelps constructs a helper thread for each inner loop containing delinquent branches. All delinquent branches, even control-dependent ones (b2), are unconditionally pre-executed in each loop iteration. Per-branch queues are managed in lockstep based on loop iterations, allowing the helper thread to deposit outcomes for both b1 and b2 each iteration and the main thread to consume or ignore b2 outcomes in the correct sequence dictated by b1. The helper thread also retains influential stores for dynamic disambiguation and store-load forwarding. Any such store that is control-dependent on a delinquent branch is predicated on the branch’s outcome, which is necessary because the helper thread no longer has control-flow (except for the loop branch). Phelps also features dual decoupled helper threads for outer-inner loop pairs, for effective branch pre-execution when the inner loop has a short and unpredictable trip count.

## 中文摘要

分支预执行针对传统分支预测器无法预测的难预测分支，由辅助线程提前尝试解析分支，并通过全局分支队列或局部分支队列（每个分支 PC 一个）把预执行结果传送给主线程的取指单元。本文讨论两个关键挑战。1）处理控制依赖于另一个难预测分支 b1 的难预测分支 b2；包含这两个分支的先前工作借助辅助线程对 b1 的预测来决定是否预执行 b2，但 b1 难以预测，预测错误瓶颈只是从主线程转移到辅助线程。2）处理既影响某难预测分支、又控制依赖于它的存储指令。为此我们提出谓词化辅助线程（Phelps）：为每个含难预测分支的内层循环构造辅助线程，所有难预测分支（甚至控制依赖的 b2）在每次迭代中被无条件预执行；逐分支队列按迭代锁步管理，使辅助线程每轮为 b1 和 b2 提交结果，主线程按 b1 决定的顺序消费或忽略 b2 结果。辅助线程还保留有影响的存储用于动态消歧与存储-加载转发，其中控制依赖于难预测分支的存储以该分支结果为谓词，因为辅助线程除循环分支外已无控制流。Phelps 还针对外层-内层循环对采用双解耦辅助线程，以应对内层循环次数短且不可预测的情形。
