---
title: "Peregrine: Accelerating TFHE Bootstrapping on GPUs via Multi-Level External Product Co-Design"
description: "HPCA 2026 · Homomorphic Encryption Acceleration"
tags:
  - "HPCA2026"
  - "Homomorphic Encryption Acceleration"
---

# Peregrine: Accelerating TFHE Bootstrapping on GPUs via Multi-Level External Product Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Homomorphic Encryption Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Homomorphic Encryption Acceleration</p>
</div>

**论文链接**：
**作者**：Haoqi He State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, Chinese Academy of Sciences and School of Cyber Security, University of Chinese Academy of Sciences , Zhiwei Wang State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS , Lutan Zhao State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS , Dian Jiao State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS , Dan Meng Institute of Information Engineering at Chinese Academy of Sciences; University of Chinese Academy of Sciences , Rui Hou Institute of Information Engineering, CAS
**会议**：HPCA 2026

---

## 中文标题

Peregrine：通过多层级外部乘积协同设计加速 GPU 上的 TFHE 自举

## 英文摘要

Fully Homomorphic Encryption (FHE) is a groundbreaking cryptographic technology that enables computation directly on encrypted data, but its practical adoption continues to be hindered by high computational costs. GPUs have emerged as an increasingly attractive acceleration platform, offering massive parallelism and architectural flexibility to accommodate rapidly evolving FHE algorithms. Despite notable advances, most efforts remain confined to isolated, single-level optimizations, limiting their ability to push performance boundaries. In this paper, we present Peregrine, an efficient GPU-based TFHE acceleration built upon multi-level co-design of external product (EP) operations across parallelism, implementation, and scheduling. First, we propose a synchronization-free key unrolling technique that restructures the execution pipeline via operator decoupling, thereby unlocking greater EP-level parallelism. Second, we consolidate fragmented operators into a matrix-centric execution pattern, yielding a high-arithmetic-intensity kernel that substantially enhances external product efficiency. Third, we propose a hierarchical tiling strategy that reformats ring ciphertexts into the Module structure and schedules polynomial-level tiles for fine-grained GPU mapping of EP operations. Experimental results show that Peregrine outperforms up to 176.9× and 2.2× over state-of-the-art CPU and GPU baselines, respectively, demonstrating its strong applicability to security-critical workloads.

## 中文摘要

全同态加密（FHE）是一种突破性的密码技术，可直接在加密数据上计算，但其实际应用仍受高计算成本制约。GPU 凭借大规模并行与架构灵活性，成为日益有吸引力的加速平台，以适应快速演进的 FHE 算法。尽管已有显著进展，多数工作仍局限于孤立的单层优化，难以突破性能边界。本文提出 Peregrine，一个基于外部乘积（EP）运算在并行性、实现与调度三个层级协同设计的高效 GPU TFHE 加速方案。首先，我们提出无同步密钥展开技术，通过算子解耦重构执行流水线，释放更大的 EP 级并行性。其次，我们将碎片化算子整合为以矩阵为中心的执行模式，形成高算术强度内核，显著提升外部乘积效率。第三，我们提出分层分块策略，将环上密文重排为 Module 结构，并按多项式级分块调度，实现 EP 运算在 GPU 上的细粒度映射。实验结果表明，Peregrine 相比最先进的 CPU 与 GPU 基线分别实现最高 176.9 倍和 2.2 倍的加速比，显示出其对安全攸关负载的强适用性。
