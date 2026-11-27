---
title: "HERO-Sign: Hierarchical Tuning and Efficient Compiler-Time GPU Optimizations for SPHINCS$^+$ Signature Generation"
description: "HPCA 2026 · Hardware Security and Side-Channel Defenses"
tags:
  - "HPCA2026"
  - "Hardware Security and Side-Channel Defenses"
---

# HERO-Sign: Hierarchical Tuning and Efficient Compiler-Time GPU Optimizations for SPHINCS$^+$ Signature Generation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Hardware Security and Side-Channel Defenses。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Hardware Security and Side-Channel Defenses</p>
</div>

**论文链接**：
**作者**：Yaoyun Zhou University of California, Merced , Qian Wang University of California, Merced (UC Merced)
**会议**：HPCA 2026

---

## 中文标题

HERO-Sign：面向 SPHINCS+ 签名生成的分层调优与高效编译期 GPU 优化

## 英文摘要

SPHINCS+ is a stateless hash-based signature scheme known for its strong post-quantum security, but it suffers from slow signature speed due to the heavy use of hash operations. The parallel architecture of GPUs offers a potential advantage for accelerating the computation of SPHINCS+ signatures. However, existing GPU-based optimization efforts for SPHINCS+ either do not fully exploit the inherent parallelism of its Merkle Tree-based structure, or lack fine-grained, compiler-level customization tailored to its diverse computational kernels. This paper proposes HERO-Sign, which adopts hierarchical tuning methodologies and efficient compiler-time GPU optimizations for SPHINCS+. HERO-Sign rethinks the parallelization potential arising from data independence in SPHINCS+ ’ components, including FORS (Forest of Random Subsets), MSS (Merkle Signature Scheme, and WOTS+ (Winternitz One-Time Signature Plus). First, it introduces a Tree Fusion strategy for FORS, whose structure contains a large number of branches. Our FORS Fusion strategy is supported by an automated Tree Tuning search algorithm, allowing it to adapt and optimize fusion schemes across various GPU platforms. To further enhance performance, HERO-Sign adopts an adaptive compilation strategy that accounts for the varying effectiveness of compiler optimizations across different SPHINCS+ component kernels (FORS_Sign, TREE_Sign, WOTS+_Sign). This strategy automatically selects between PTX and native branches during the compilation phase to maximize efficiency. For multiple batches of message signatures, HERO-Sign focuses on optimizing kernel-level overlapping and employs a Task Graph-based construction strategy to minimize multi-stream idle time and reduce kernel launch overhead. Compared to state-of-the-art GPU implementations, under the SPHINCS+-128f, SPHINCS+-192f and SPHINCS+-256f parameter sets, HERO-Sign demonstrates an enhanced throughput of 1.28×–3.13×, 1.28×–2.92×, and 1.24×–2.60× on RTX 4090. Similar performance improvements have also been achieved on other architectures, including the A100, H100, and GTX 2080. HERO-Sign also achieves a two-order-of-magnitude reduction in kernel launch latency.

## 中文摘要

SPHINCS+ 是一种无状态、基于哈希的签名方案，以强抗量子安全性著称，但因大量哈希运算导致签名速度较慢。GPU 的并行架构有潜力加速 SPHINCS+ 签名计算，然而现有 GPU 优化要么未充分利用其 Merkle 树结构固有的并行性，要么缺乏针对其多样计算内核的细粒度编译器级定制。本文提出 HERO-Sign，采用分层调优方法学与高效的编译期 GPU 优化。HERO-Sign 重新审视 SPHINCS+ 各组件（FORS（随机子集森林）、MSS（Merkle 签名方案）、WOTS+（Winternitz 一次性签名增强版））中数据独立性带来的并行化潜力：针对分支众多的 FORS 引入树融合策略，并由自动化树调优搜索算法支撑，以适配不同 GPU 平台；采用自适应编译策略，考虑编译器优化在各组件内核（FORS_Sign、TREE_Sign、WOTS+_Sign）上效果的差异，在编译阶段自动在 PTX 与原生分支之间选择；对多批消息签名则采用基于任务图的构造策略优化内核级重叠，以最小化多流空闲时间并降低内核启动开销。与最先进的 GPU 实现相比，在 SPHINCS+-128f、SPHINCS+-192f 和 SPHINCS+-256f 参数集下，HERO-Sign 在 RTX 4090 上分别取得 1.28 倍至 3.13 倍、1.28 倍至 2.92 倍和 1.24 倍至 2.60 倍的吞吐提升，在 A100、H100 和 GTX 2080 上也有类似提升，并将内核启动时延降低两个数量级。
