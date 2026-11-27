---
title: "Criticality-Aware Instruction-Centric Bandwidth Partitioning for Data Center Applications"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Criticality-Aware Instruction-Centric Bandwidth Partitioning for Data Center Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Liren Zhu (Peking University), Liujia Li (Peking University), Jianyu Wu (Peking University), Yiming Yao (Peking University), Zhan Shi (Huawei), Jie Zhang (Peking University), Zhenlin Wang (Michigan Tech), Xiaolin Wang (Peking University), Yingwei Luo (Peking University), Diyu Zhou (Peking University)
**会议**：HPCA 2025

---

## 中文标题

面向数据中心应用的关键性感知与指令中心带宽划分

## 英文摘要

To reduce operational costs, modern data centers colocate high-priority latency-critical (LC) tasks and low-priority best-effort (BE) tasks on the same physical node to increase resource utilization. However, such co-location leads to contention for memory bandwidth, resulting in priority inversion, where BE tasks severely slow down LC tasks. This priority inversion often leads to violations of the quality of service (QoS) requirements for LC tasks, defeating the purpose of co-location. Prior approaches to this issue either fail to enforce the QoS requirements for LC tasks or underutilize memory bandwidth. We present PIVOT, a novel bandwidth partitioning system that overcomes the limitations of prior approaches based on two key insights. First, memory accesses from LC tasks must be prioritized across all the components on the memory path rather than a single component, as done in prior work. Second, only the scheduling of a selective portion of performance-critical loads (i.e., those causing a long stall on the re-order buffer), instead of all memory accesses from LC tasks, should be prioritized. To leverage these insights, PIVOT overcomes the key challenge of accurately identifying performance-critical loads while incurring minimal runtime overhead by proposing a two-phase profiling technique. Our extensive evaluation shows that PIVOT improves effective machine utilization by up to 34.5% while increasing the throughput of the BE applications by up to 2.76× compared to state-of-the-art approaches.

## 中文摘要

为降低运营成本，现代数据中心将高优先级的时延敏感（LC）任务与低优先级的尽力而为（BE）任务共置在同一物理节点上，以提高资源利用率。然而这种共置导致了内存带宽竞争，引发优先级反转，即 BE 任务严重拖慢 LC 任务。这种优先级反转常常导致 LC 任务的服务质量（QoS）要求被违反，使共置失去意义。此前的方法要么无法强制满足 LC 任务的 QoS 要求，要么使内存带宽利用不足。我们提出 PIVOT，一种新颖的带宽划分系统，基于两个关键洞见克服了此前方法的局限。第一，LC 任务的内存访问必须在内存路径上的所有组件中被优先处理，而不是像此前工作那样只在单个组件中处理。第二，应当只优先调度一部分性能关键的加载，即那些在重排序缓冲区上造成长时间停顿的加载，而不是优先 LC 任务的所有内存访问。为利用这些洞见，PIVOT 提出两阶段剖析技术，克服了在引入极低运行时开销的同时准确识别性能关键加载这一关键挑战。我们的大量评估表明，与最先进的方法相比，PIVOT 将有效机器利用率最高提升 34.5%，同时将 BE 应用的吞吐最高提升 2.76 倍。
