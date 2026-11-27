---
title: "FlashFuser: Expanding the Scale of Kernel Fusion for Compute-Intensive operators via Inter-Core Connection"
description: "HPCA 2026 · GPU Kernel Optimization and Resource Sharing"
tags:
  - "HPCA2026"
  - "GPU Kernel Optimization and Resource Sharing"
---

# FlashFuser: Expanding the Scale of Kernel Fusion for Compute-Intensive operators via Inter-Core Connection

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: GPU Kernel Optimization and Resource Sharing。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · GPU Kernel Optimization and Resource Sharing</p>
</div>

**论文链接**：
**作者**：huang ziyu Shanghai Jiao Tong University , Yangjie Zhou National University of Singapore , Zihan Liu Shanghai Jiao Tong University , Xinhao Luo Shanghai Jiao Tong University , Yijia Diao Shanghai Jiao Tong University , Minyi Guo Shanghai Jiao Tong University , Jidong Zhai Tsinghua University , Yu Feng Shanghai Jiao Tong University , Chen Zhang Shanghai Jiao Tong University , Anbang Wu Shanghai Jiao Tong University , Jingwen Leng Shanghai Jiao Tong University
**会议**：HPCA 2026

---

## 中文标题

FlashFuser：通过核间连接扩展计算密集型算子的内核融合规模

## 英文摘要

The scaling of computation throughput continues to outpace improvements in memory bandwidth, making many deep learning workloads memory-bound. Kernel fusion is a key technique to alleviate this problem, but the fusion strategies of existing compilers and frameworks are limited to using local scratchpad memory. When the intermediate results exceed the limited capacity (such as FFN), the fusion fails. Although modern GPUs (like the NVIDIA H100) now incorporate an inter-core connection mechanism known as Distributed Shared Memory (DSM)—providing a larger, high-bandwidth, and low-latency on-chip memory pool—this hardware potential has yet to be exploited by software frameworks. To bridge this gap, we present FlashFuser, the first compiler framework to utilize inter-core connection for kernel fusion on modern GPUs. FlashFuser extends established fusion techniques to the DSM domain through three core contributions. First, we propose a powerful DSM-based communication abstraction that formalizes complex cluster-based data exchange patterns, such as reduce, shuffle and multiply. Second, we introduce a dataflow analyzer that generalizes loop scheduling, resource mapping, and tile selection to the distributed memory hierarchy; it determines the optimal execution order and tile sizes by quantifying data movement across memory levels. Finally, FlashFuser integrates these components into a unified search engine that employs analytical cost modeling and DSM-aware pruning strategies to efficiently discover the optimal execution plan. Our evaluation on an NVIDIA H100 GPU shows that FlashFuser reduces memory access by 58% and delivers kernel speedups of 3.3x against highly-tuned libraries and 4.1x against state-of-the-art compilers, resulting in a 1.24× end-to-end speedup.

## 中文摘要

计算吞吐的扩张持续快于存储带宽的改善，使许多深度学习负载受限于访存。内核融合是缓解该问题的关键技术，但现有编译器与框架的融合策略仅限于使用本地便笺存储器；当中间结果超出有限容量（如 FFN）时，融合便失败。尽管现代 GPU（如 NVIDIA H100）已引入称为分布式共享存储（DSM）的核间连接机制，提供更大、高带宽、低时延的片上存储池，但该硬件潜力尚未被软件框架利用。为填补这一空白，我们提出 FlashFuser，首个在现代 GPU 上利用核间连接进行内核融合的编译器框架。FlashFuser 通过三项核心贡献将既有融合技术扩展到 DSM 领域。首先，提出强大的基于 DSM 的通信抽象，将 reduce、shuffle 和 multiply 等复杂集群内数据交换模式形式化。其次，引入数据流分析器，将循环调度、资源映射与瓦片选择推广到分布式存储层次；它通过量化各存储层级间的数据移动来确定最优执行顺序与瓦片尺寸。最后，FlashFuser 将这些组件集成到统一搜索引擎中，采用解析代价建模与 DSM 感知剪枝策略高效发现最优执行计划。在 NVIDIA H100 GPU 上的评估表明，FlashFuser 将访存减少 58%，内核相比高度调优的库加速 3.3 倍、相比最先进编译器加速 4.1 倍，端到端加速 1.24 倍。
