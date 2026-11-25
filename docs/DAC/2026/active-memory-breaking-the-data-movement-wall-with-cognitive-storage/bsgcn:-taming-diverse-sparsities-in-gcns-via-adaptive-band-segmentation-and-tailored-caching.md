BSGCN: Taming Diverse Sparsities in GCNs via Adaptive Band-Segmentation and Tailored Caching
Authors：
[Shangtong Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=56822976604310609621)，[Xueyan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=851443)，[Yuan Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=34095731557101649741)，[Yier Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=0462365807378591021)，[Weisheng Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=061443)

## 中文标题

BSGCN：通过自适应带状分割与定制缓存驾驭 GCN 中的多样稀疏性

## 英文摘要

Graph Convolutional Networks (GCNs), a foundational technology for relational data applications, are often bottlenecked by irregular memory accesses caused by sparse graph structures. Existing accelerators face two fundamental limitations: their rigid dataflows cannot adapt to varying graph sparsities, and their narrow focus on high-degree nodes (HDNs) leads to systematic neglect of memory traffic from the vast number of low-degree nodes (LDNs). To address these issues, this paper introduces BSGCN, an accelerator built on a novel band-segmentation strategy. This approach partitions the graph such that the majority of LDNs are grouped into large bands with similar data reuse characteristics, while the remaining nodes form small bands containing only a few LDNs. This segregation enables two co-designed innovations: 1) a Band-Segmented Dataflow (BSD), which applies a tailored traversal strategy to each band type to handle diverse sparsity patterns, and 2) a Band-Segmented Caching (BSC) hierarchy, combining a specialized caching policy to exploit the reuse potential of LDNs with a dedicated pinning mechanism for HDNs. Evaluation results show that BSGCN achieves an average speedup of 1.41× (up to 4.80×) over state-of-the-art accelerators, while reducing DRAM traffic by 24.24% and improving energy efficiency by 1.30×. Codes are available at https://github.com/Zst990514/BSGCN.

## 中文摘要

图卷积网络（GCN）是关系数据应用的基础技术，但稀疏图结构引起的不规则内存访问常常使其成为瓶颈。现有加速器面临两个根本性限制：其僵化的数据流无法适应变化的图稀疏性；并且它们仅关注高度数节点（HDN），导致系统性地忽视大量低度数节点（LDN）带来的内存流量。为解决这些问题，本文提出了 BSGCN，一种基于新颖带状分割策略的加速器。该方法对图进行划分，使大多数 LDN 被分组到具有相似数据复用特征的大带中，而其余节点形成仅包含少量 LDN 的小带。这种分离促成了两项协同设计的创新：1）带状分段数据流（BSD），对每种带类型应用定制的遍历策略，以处理多样的稀疏模式；2）带状分段缓存（BSC）层次结构，结合专门的缓存策略来挖掘 LDN 的复用潜力，并为 HDN 设计专用的固定机制。评估结果表明，BSGCN 相比当前最优加速器平均实现 1.41 倍（最高 4.80 倍）的加速，同时将 DRAM 流量降低 24.24%，并将能效提升 1.30 倍。代码可在 https://github.com/Zst990514/BSGCN 获取。

## 英文关键词

Graph Convolutional Networks, Accelerators, Diverse Sparsities, Dataflow, Cache Strategy

## 中文关键词

图卷积网络、加速器、多样稀疏性、数据流、缓存策略
