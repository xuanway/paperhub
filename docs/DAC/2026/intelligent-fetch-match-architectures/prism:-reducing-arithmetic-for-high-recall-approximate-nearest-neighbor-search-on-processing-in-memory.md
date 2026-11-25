Prism: Reducing Arithmetic for High-Recall Approximate Nearest Neighbor Search on Processing-in-Memory
Authors：
[Weihan Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=57665325702380027031)，[Shengan Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=93998885764835769641)，[Yingxue Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=05260487337182133061)，[Yifan Hua](https://63dac.conference-program.com/?post_type=page&p=15&uid=80172732887188604481)，[Yuheng Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=47313913863148983021)，[Cong Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=48039618468757618421)，[Guifeng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9358608897372060712)，[Linpeng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=657243)

## 中文标题

Prism：面向存内计算高召回近似最近邻搜索的算术量削减

## 英文摘要

Approximate Nearest Neighbor Search (ANNS) at scale is constrained by the memory wall. By moving compute to memory, Processing-in-Memory (PIM) offers ample internal bandwidth but limited on-die compute, making arithmetic reduction crucial. We propose Prism, a PIM-based ANNS system co-optimizing vector pruning, distance evaluation, and host-PIM orchestration. It employs a proximity-aware vector pruner to leverage high intra-PIM bandwidth and dual-cluster affiliations to filter out distant vectors. Prism then performs sensitivity-ordered distance computation, prioritizing high-impact dimension segments and early terminating candidates once exclusion criteria are met. A stall-free host-PIM pipeline overlaps query preparation, PIM execution, and global ranking to sustain high throughput. Experiments show that Prism achieves 2.7-19.8× higher throughput over state-of-the-art systems.

## 中文摘要

大规模近似最近邻搜索（ANNS）受制于存储墙。通过将计算迁移至内存，存内计算（PIM）提供了充裕的内部带宽但片上算力有限，因此削减算术量至关重要。我们提出 Prism，一种基于 PIM 的 ANNS 系统，协同优化向量剪枝、距离评估以及主机与 PIM 之间的编排。它采用邻近感知的向量剪枝器，利用 PIM 内高带宽与双簇隶属关系过滤掉距离较远的向量。随后 Prism 执行按敏感度排序的距离计算，优先处理高影响的维度分段，并在满足排除条件后提前终止候选。一条无停顿的主机–PIM 流水线将查询准备、PIM 执行与全局排序相互重叠，以维持高吞吐。实验表明，Prism 相较最先进系统实现 2.7–19.8 倍的吞吐提升。

## 英文关键词

Approximate Nearest Neighbor Search, Early Termination, Processing-in-Memory, Vector Database

## 中文关键词

近似最近邻搜索、提前终止、存内计算、向量数据库
