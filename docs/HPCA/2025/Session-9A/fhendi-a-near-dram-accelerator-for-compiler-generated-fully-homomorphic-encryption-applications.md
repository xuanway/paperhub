---
title: "FHENDI: A Near-DRAM Accelerator for Compiler-Generated Fully Homomorphic Encryption Applications"
description: "HPCA 2025 · The Poker Face of FHE"
tags:
  - "HPCA2025"
  - "The Poker Face of FHE"
---

# FHENDI: A Near-DRAM Accelerator for Compiler-Generated Fully Homomorphic Encryption Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Poker Face of FHE。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Poker Face of FHE</p>
</div>

**论文链接**：
**作者**：Yongmo Park (IBM Research), Aporva Amarnath (IBM Research), Subhankar Pal (IBM Research), Karthik Swaminathan (IBM Research), Alper Buyuktosunoglu (IBM Research), Hayim Shaul (IBM Research), Ehud Aharoni (IBM Research), Nir Drucker (IBM Research), Wei D. Lu (University of Michigan), Omri Soceanu (IBM Research), Pradip Bose (IBM Research)
**会议**：HPCA 2025

---

## 中文标题

FHENDI：面向编译器生成的全同态加密应用的近 DRAM 加速器

## 英文摘要

Fully homomorphic encryption (FHE) is a powerful cryptographic technique that enables computation on encrypted data without needing to decrypt it. It has broad applications in scenarios where sensitive data needs to be processed in the cloud or in other untrusted environments. FHE applications are both compute- and memory-intensive, owing to expensive operations on large data. While prior works address the challenges of efficient compute using dedicated hardware, expensive memory transfers still remain a major limiting factor. In this work, we propose a hierarchical near-DRAM processing (NDP) solution for FHE applications, called FHENDI, that harnesses the massive DRAM bank bandwidth. We observe various data access patterns in FHE that reveal distinct levels of parallelism: element-wise, limb-wise, coefficient-wise, and ciphertext-wise. FHENDI exploits these levels of parallelism to map FHE operations and data onto different hierarchies of our design, while addressing three major challenges with NDP for FHE: (i) the lack of bank-to-bank communication support, (ii) limited die-to-die bandwidth, and (iii) large memory access latencies. We resolve the first problem through a novel, conflict-free mapping algorithm built atop localized permutation networks that enables efficient element-wise and butterfly operations in FHE. The second problem is addressed by pipelining the execution of parallel bootstrap operations observed in compiled FHE workloads. Finally, we hide the memory access latency behind computation latency by exploiting a dual-banking scheme and subarray-level parallelism (SLP) of the DRAM banks. We evaluate FHENDI using representative workloads in the domains of privacy-preserving machine learning inference on CNNs and Transformers, database range query, and sorting, that are obtained using a compiler framework called HElayers. We compare FHENDI with a server-class CPU and GPU running the state-of-the-art HEaaN library, and an FHE accelerator ASIC, and report mean speedups of 2145.8⇥, 118.29⇥, and 2.45⇥, respectively.

## 中文摘要

全同态加密（FHE）是一种强大的密码学技术，可以在不解密的情况下对加密数据进行计算，在需要于云端或其他不可信环境中处理敏感数据的场景中有广泛应用。由于大规模数据上的昂贵操作，FHE 应用既是计算密集型也是内存密集型。已有工作通过专用硬件解决高效计算问题，但昂贵的内存传输仍是主要限制因素。本文提出一种面向 FHE 应用的分层近 DRAM 处理（NDP）方案 FHENDI，充分利用 DRAM bank 的巨大带宽。我们观察到 FHE 中的多种数据访问模式呈现出不同层次的并行性：逐元素、逐 limb、逐系数以及逐密文。FHENDI 利用这些并行层次将 FHE 操作与数据映射到设计的不同层次，同时解决 NDP 用于 FHE 的三大挑战：（i）缺乏 bank 间通信支持，（ii）有限的 die-to-die 带宽，（iii）很大的内存访问时延。我们通过构建在局部置换网络之上的新型无冲突映射算法解决第一个问题，从而在 FHE 中实现高效的逐元素与蝶形操作。第二个问题通过将编译后 FHE 负载中观察到的并行自举操作流水化执行来解决。最后，我们利用 DRAM bank 的双 bank 方案与子阵列级并行（SLP）将内存访问时延隐藏在计算时延之后。我们使用隐私保护机器学习推理（CNN 与 Transformer）、数据库范围查询和排序等领域的代表性负载评估 FHENDI，这些负载由名为 HElayers 的编译器框架获得。我们将 FHENDI 与运行最先进 HEaaN 库的服务器级 CPU 和 GPU 以及 FHE 加速 ASIC 比较，平均加速比分别为 2145.8 倍、118.29 倍和 2.45 倍。
