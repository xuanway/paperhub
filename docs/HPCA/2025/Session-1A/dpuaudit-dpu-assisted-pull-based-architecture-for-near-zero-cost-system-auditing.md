---
title: "DPUaudit: DPU-assisted Pull-based Architecture for Near-Zero Cost System Auditing"
description: "HPCA 2025 · Reliable Bets"
tags:
  - "HPCA2025"
  - "Reliable Bets"
---

# DPUaudit: DPU-assisted Pull-based Architecture for Near-Zero Cost System Auditing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Reliable Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Reliable Bets</p>
</div>

**论文链接**：
**作者**：Peng Jiang (Southeast University), Hanlin Jiang (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Ruizhe Huang (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Hanwen Lei (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Zhineng Zhong (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Shaokun Zhang (Huawei Technologies), Yuxin Ren (Huawei Technologies), Ning Jia (Huawei Technologies), Xinwei Hu (Huawei Technologies), Yao Guo (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Xiangqun Chen (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University), Ding Li (Key Laboratory of High-Confidence Software Technologies (MOE), School of Computer Science, Peking University)
**会议**：HPCA 2025

---

## 中文标题

DPUaudit：面向近零开销系统审计的 DPU 辅助拉取式架构

## 英文摘要

System auditing frameworks are crucial for modern data center security, as they record system events to detect intrusions. However, existing software-based auditing frameworks are limited by their high runtime overhead. To address the limitations of software-based frameworks, researchers had proposed a hardware-based auditing framework that offloads log processing to isolated hardware. However, despite using powerful specialized hardware, this approach still suffers from high runtime overhead, which contradicts their efficiency goal. We have identified that the high overhead is due to the push-based architecture, which involves operating a log sender on the monitored host. Consequently, the existing approach requires heavy software protection mechanisms to secure the log sender, resulting in high runtime overhead. In this paper, we propose a new DPU-assisted pull-based architecture called DPUaudit for hardware-based auditing, which achieves near-zero runtime overhead. Instead of using a log sender, DPUaudit utilizes DPU to actively pull system events from the monitored host. This eliminates the need for heavy mechanisms to handle and safeguard the log sender, achieving highly efficient system auditing. Experimental results show that, on average, DPUaudit only slows down applications on the monitored host by 2.1% for six mainstream data center applications under different workloads, which is at least one order of magnitude smaller than existing approaches, while still ensuring the integrity of audit logs.

## 中文摘要

系统审计框架对现代数据中心安全至关重要，因为它们记录系统事件以检测入侵。然而，现有的基于软件的审计框架受制于较高的运行时开销。为解决基于软件框架的局限，研究者曾提出一种基于硬件的审计框架，将日志处理卸载到隔离的硬件上。然而，尽管使用了强大的专用硬件，该方法仍然存在较高的运行时开销，这与其效率目标相矛盾。我们发现，高开销源于推送式架构，该架构需要在被监控主机上运行日志发送器。因此，现有方法需要繁重的软件保护机制来保护日志发送器，从而导致高运行时开销。本文提出一种新的 DPU 辅助拉取式架构 DPUaudit，用于基于硬件的审计，可实现近零运行时开销。DPUaudit 不使用日志发送器，而是利用 DPU 主动从被监控主机拉取系统事件。这消除了处理与保护日志发送器所需的繁重机制，从而实现高效的系统审计。实验结果表明，在不同负载下，对于六种主流数据中心应用，DPUaudit 平均仅使被监控主机上的应用性能下降 2.1%，比现有方法至少低一个数量级，同时仍能保证审计日志的完整性。
