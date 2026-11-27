---
title: "AutoRFM: Scaling Low-Cost In-DRAM Trackers to Ultra-Low Rowhammer Thresholds"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# AutoRFM: Scaling Low-Cost In-DRAM Trackers to Ultra-Low Rowhammer Thresholds

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Moinuddin Qureshi (Georgia Tech)
**会议**：HPCA 2025

---

## 中文标题

AutoRFM：将低成本 DRAM 内跟踪器扩展至超低 Rowhammer 阈值

## 英文摘要

In-DRAM Rowhammer mitigation has the potential to solve the Rowhammer problem without relying on other parts of the system. In-DRAM mitigation requires space (to identify the aggressor rows) and time (to perform the victim refresh). To reduce the storage overheads of tracking, recent works have developed secure low-cost in-DRAM trackers that can probabilistically identify aggressor rows. To obtain the time required for mitigation, these trackers rely on the Refresh Management (RFM) command introduced in DDR5. As RFM stalls the bank for a latency of 200ns-400ns, frequent use of RFM can cause significant slowdowns. For example, scaling the recent MINT tracker to a threshold of 100 incurs 33% slowdown. The goal of this paper is to enable low-cost trackers to tolerate ultralow thresholds (sub-100) while incurring negligible slowdown. This paper proposes AutoRFM, a transparent RFM mechanism that can provide mitigation time to the DRAM chips without stalling the bank. The key insight in AutoRFM is to leverage the subarray structure (e.g. each bank contains 256 subarrays) and perform mitigation on only one of the subarrays. Operations to all subarrays that are not under mitigation are serviced without any interruption. If activation occurs to the subarray under mitigation, the DRAM chip sends an ALERT signal informing the Memory Controller to retry after a predefined time. As AutoRFM works best if consecutive requests to the same bank do not get mapped to the same subarray, we use Randomized Memory Mapping to break the spatial correlation between memory accesses. Furthermore, we also develop a Fractal Mitigation Algorithm that can tolerate transitive attacks (such as Half-Double) without requiring recursive mitigations to the same subarray. Our design ensures that a declined request does not have to wait more than 200 ns before retrying, thus limiting the slowdown and avoiding any potential for denial of service. Our evaluations, with SPEC, GAP, and stream workloads, show that AutoRFM enables low-cost trackers to tolerate a threshold of as low as 74 while incurring an average slowdown of only 3.1%.

## 中文摘要

DRAM 内 Rowhammer 缓解有望在不依赖系统其他部分的情况下解决该问题，但需要空间来识别攻击者行、需要时间来执行受害行刷新。为降低跟踪的存储开销，近期工作提出了安全的低成本 DRAM 内跟踪器，可概率性地识别攻击者行；为获得缓解时间，它们依赖 DDR5 引入的刷新管理（RFM）命令。由于 RFM 会使 bank 停顿 200ns-400ns，频繁使用会导致显著性能下降，例如将 MINT 跟踪器扩展到阈值 100 会带来 33% 的性能损失。本文旨在让低成本跟踪器容忍低于 100 的超低阈值而几乎无性能损失，并提出 AutoRFM——一种透明的 RFM 机制，可在不停顿 bank 的情况下为 DRAM 芯片提供缓解时间。其关键洞见是利用子阵列结构（例如每个 bank 含 256 个子阵列），仅对其中一个子阵列执行缓解，对未处于缓解状态的子阵列的访问不受中断；若激活命中正在缓解的子阵列，DRAM 芯片会发出 ALERT 信号，通知内存控制器在预定时间后重试。由于对同一 bank 的连续请求不被映射到同一子阵列时效果最佳，我们采用随机化内存映射打破访问间的空间相关性，并设计分形缓解算法，无需对同一子阵列递归缓解即可容忍 Half-Double 等传递性攻击。该设计确保被拒绝的请求重试前等待不超过 200 ns，从而限制性能损失并避免拒绝服务。基于 SPEC、GAP 与流式负载的评估显示，AutoRFM 使低成本跟踪器可容忍低至 74 的阈值，平均性能损失仅 3.1%。
