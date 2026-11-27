---
title: "Palermo: Improving the Performance of Oblivious Memory using Protocol-Hardware Co-Design"
description: "HPCA 2025 · Securing your Chips"
tags:
  - "HPCA2025"
  - "Securing your Chips"
---

# Palermo: Improving the Performance of Oblivious Memory using Protocol-Hardware Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Securing your Chips。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Securing your Chips</p>
</div>

**论文链接**：
**作者**：Haojie Ye (University of Michigan), Yuchen Xia (University of Michigan), Yuhan Chen (University of Michigan), Kuan-Yu Chen (University of Michigan), Yichao Yuan (University of Michigan), Shuwen Deng (Tsinghua University), Baris Kasikci (University of Washington and Google), Trevor Mudge (University of Michigan), Nishil Talati (University of Michigan)
**会议**：HPCA 2025

---

## 中文标题

Palermo：通过协议-硬件协同设计提升不经意内存性能

## 英文摘要

Oblivious RAM (ORAM) hides the memory access patterns, enhancing data privacy by preventing attackers from discovering sensitive information based on the sequence of memory accesses. The performance of ORAM is often limited by its inherent trade-off between security and efficiency, as concealing memory access patterns imposes significant computational and memory overhead. While prior works focus on improving the ORAM performance by prefetching and eliminating ORAM requests, we find that their performance is very sensitive to workload locality behavior and incurs additional management overhead caused by the ORAM stash pressure. This paper presents Palermo: a protocol-hardware co-design to improve ORAM performance. The key observation in Palermo is that classical ORAM protocols enforce restrictive dependencies between memory operations that result in low memory bandwidth utilization. Palermo introduces a new protocol that overlaps large portions of memory operations, within a single and between multiple ORAM requests, without breaking correctness and security guarantees. Subsequently, we propose an ORAM controller architecture that executes the proposed protocol to service ORAM requests. The hardware is responsible for concurrently issuing memory requests as well as imposing the necessary dependencies to ensure a consistent view of the ORAM tree across requests. Using a rich workload mix, we demonstrate that Palermo outperforms the RingORAM baseline by 2.9×, on average, incurring a negligible area overhead of 5.78 mm² (less than 2% in 12th generation Intel CPU after technology scaling) and 2.14W without sacrificing security. We further show that Palermo also outperforms the state-of-the-art works PageORAM, PrORAM, and IR-ORAM.

## 中文摘要

不经意内存（ORAM）隐藏内存访问模式，通过阻止攻击者依据内存访问序列发现敏感信息来增强数据隐私。ORAM 的性能常常受制于其固有的安全性与效率权衡，因为隐藏内存访问模式会带来显著的计算与内存开销。以往工作侧重于通过预取与消除 ORAM 请求来提升 ORAM 性能，但我们发现其性能对负载局部性行为非常敏感，并且会因 ORAM 暂存区（stash）压力而引入额外的管理开销。本文提出 Palermo：一种用于提升 ORAM 性能的协议-硬件协同设计。Palermo 的关键观察是，经典 ORAM 协议在内存操作之间强制施加限制性依赖，导致内存带宽利用率低下。Palermo 引入一种新协议，在单个 ORAM 请求内部以及多个 ORAM 请求之间重叠大量内存操作，同时不破坏正确性与安全性保证。随后，我们提出一种执行该协议的 ORAM 控制器架构来服务 ORAM 请求。该硬件负责并发地发出内存请求，并施加必要的依赖以确保跨请求的 ORAM 树视图一致。我们使用丰富的混合负载证明，Palermo 平均比 RingORAM 基线快 2.9 倍，仅带来 5.78 mm² 的微小面积开销（经工艺缩放后在第十二代 Intel CPU 中占比不到 2%）与 2.14W 功耗，且不牺牲安全性。我们进一步表明 Palermo 也优于最先进工作 PageORAM、PrORAM 与 IR-ORAM。
