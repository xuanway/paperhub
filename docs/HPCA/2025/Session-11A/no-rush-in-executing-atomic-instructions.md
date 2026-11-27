---
title: "No Rush in Executing Atomic Instructions"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# No Rush in Executing Atomic Instructions

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Ashkan Asgharzadeh (University of Murcia), Josué Feliu (Universitat Politècnica de València), Manuel E. Acacio (University of Murcia), Stefanos Kaxiras (Uppsala University), Alberto Ros (University of Murcia)
**会议**：HPCA 2025

---

## 中文标题

原子指令执行无须操之过急

## 英文摘要

Hardware atomic instructions are the building blocks of the synchronization algorithms. Historically, to guarantee atomicity and consistency, they were implemented using memory fences, committing older memory instructions, and draining the store buffer before initiating the execution of atomics. Unfortunately, the use of such memory fences entails huge performance penalties as it implies execution serialization, thus impeding instruction- and memory-level parallelism. The situation, however, seems to have changed recently. Through experiments on x86 machines, we discovered that current x86 processors manage to comply with the x86-TSO requirements while avoiding the performance overhead introduced by fences (fence-free or unfenced implementation). This paves the way to new potential optimizations to atomic instruction execution. In particular, our simulation experiments modeling unfenced atomics reveal that executing atomic instructions as soon as their operands are ready does not always lead to optimal performance. In fact, this increases the time that other threads should wait to obtain the cacheline. In contended scenarios, delaying the execution of the atomic instruction to minimize the time the cacheline is locked provides superior performance. Based on this observation, we present Rush or Wait (RoW), a hardware mechanism to decide when to execute an atomic instruction. The mechanism is based on a contention predictor that estimates if an atomic will access a contended cacheline. Non-contended atomics execute once their operands are ready. Contended atomics, on the contrary, wait to become the oldest memory instruction and to drain the store buffer to execute, minimizing the contention on the accessed cacheline. Our experimental evaluation shows that RoW reduces execution time on average by 9.2% (and up to 43%) compared to a baseline that executes atomics as soon as the operands are ready, and yet it requires a small area overhead (64 bytes).

## 中文摘要

硬件原子指令是同步算法的基本构件。历史上，为保证原子性与一致性，其实现依赖内存栅栏、提交更早的内存指令以及在启动原子指令执行前排空存储缓冲。但此类栅栏会带来巨大性能损失，因为它意味着执行串行化，从而阻碍指令级与内存级并行。不过这一状况近来似乎已有改变。通过在 x86 机器上的实验，我们发现当前 x86 处理器能在满足 x86-TSO 要求的同时避免栅栏引入的性能开销（无栅栏实现）。这为原子指令执行的新优化开辟了空间。特别地，我们对无栅栏原子指令的模拟实验表明，操作数就绪后立即执行原子指令并不总能带来最优性能，反而会增加其他线程获取该缓存行所需的等待时间。在存在竞争的场合，延迟原子指令的执行以最小化缓存行被锁定的时间可获得更优性能。基于此观察，我们提出 Rush or Wait（RoW），一种决定何时执行原子指令的硬件机制。该机制基于竞争预测器，估计原子指令是否会访问存在竞争的缓存行：无竞争的原子指令在操作数就绪后即执行，有竞争的原子指令则等待成为最老的内存指令并排空存储缓冲后再执行，从而最小化对所访问缓存行的竞争。实验评估表明，与操作数就绪即执行的基线相比，RoW 平均减少 9.2% 的执行时间（最高 43%），且仅需 64 字节的小面积开销。
