Lhgstore: An In-Memory Learned Graph Storage for Fast Updates and Analytics
Authors：
[Pengpeng Qiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=31800713081255254271)，[Zhiwei Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=91181965250353146641)，[Xinzhou Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6908134689719935342)，[Zhetao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=496841017259257819)，[Xiaochun Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8045622277399022376)，[Yang Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0246642897166238145)

## 中文标题

LHGstore：一种面向快速更新与分析的内存学习型图存储

## 英文摘要

Various real-world applications rely on in-memory dynamic graphs that must efficiently handle frequent updates while supporting low-latency analytics on evolving structures. Achieving both objectives remains challenging due to the trade-off between update efficiency and traversal locality, particularly under highly skewed degree distributions. This motivates the design of graph indexing schemes optimized for in-memory graph management on modern multi-core CPUs. We present LHGstore, a degree-aware Learned Hierarchical Graph storage that, for the first time, integrates learned indexing into graph management. LHGstore designs a two-level hierarchy that decouples vertex and edge access and further organizes each vertex’s edges using data structures adaptive to its degree. Lightweight arrays are used for low-degree vertices to maximize traversal locality, while learned indexes are applied to high-degree vertices to improve update throughput. Extensive experiments show that LHGstore achieves 5.9-28.2× higher throughput and significantly faster analytics than SOTA in-memory graph storage systems.

## 中文摘要

各类现实应用都依赖于内存中的动态图，这些图必须高效处理频繁更新，同时支持对演化结构的低延迟分析。由于更新效率与遍历局部性之间存在权衡，尤其是在高度偏斜的度分布下，同时实现这两个目标仍然充满挑战。这促使我们面向现代多核 CPU 上的内存图管理设计优化的图索引方案。我们提出 LHGstore，一种度感知的学习型分层图存储，首次将学习型索引集成到图管理之中。LHGstore 设计了两级层次结构，将顶点访问与边访问解耦，并进一步采用适应顶点度数的数据结构来组织每个顶点的边。对于低度顶点使用轻量级数组以最大化遍历局部性，而对于高度顶点则应用学习型索引以提升更新吞吐。大量实验表明，相比 SOTA 内存图存储系统，LHGstore 实现 5.9–28.2 倍的更高吞吐以及显著更快的分析速度。
