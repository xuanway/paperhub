---
title: "UniFHE: Faster Accelerator for FHE with Diverse Algebraic Structure and Balanced Memory System"
description: "HPCA 2026 · Homomorphic Encryption Acceleration"
tags:
  - "HPCA2026"
  - "Homomorphic Encryption Acceleration"
---

# UniFHE: Faster Accelerator for FHE with Diverse Algebraic Structure and Balanced Memory System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Homomorphic Encryption Acceleration。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Homomorphic Encryption Acceleration</p>
</div>

**论文链接**：
**作者**：Qingyun Niu Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS and School of Cyber Security, University of Chinese Academy of Sciences , Lutan Zhao State Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS , Ming Cai Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS and School of Cyber Security, University of Chinese Academy of Sciences , kai li Institute of Information Engineering,CAS , Dan Meng Institute of Information Engineering at Chinese Academy of Sciences; University of Chinese Academy of Sciences , Rui Hou Institute of Information Engineering, CAS
**会议**：HPCA 2026

---

## 中文标题

UniFHE：面向多样代数结构与均衡存储系统的更快速 FHE 加速器

## 英文摘要

Fully homomorphic encryption (FHE) enables computations on encrypted data. Existing FHE schemes are primarily categorized into RLWE-based word-wise schemes and LWE-based bit-wise schemes. Efficient combination of different FHE schemes adapted to real-world applications has emerged as a research focus. This paper proposes UniFHE, the first FHE accelerator that supports diverse algebraic structures using general arithmetic units to achieve higher performance. UniFHE is compatible with both RLWE-based and LWE-based FHE schemes without modifications to their original algorithmic designs. To support both finite ring and complex field operations, UniFHE introduces a general arithmetic unit and further constructs core computation structures. To balance on-chip memory demands across different schemes, UniFHE adopts a multi-pipeline architecture for LWE-based schemes. The core functional units for RLWE-based schemes are spliced based on the LWE-based pipelines. Furthermore, an on-chip plaintext encoding mechanism significantly reduces off-chip memory bandwidth demands. Experimental results show that, beyond superior area and energy efficiency, UniFHE delivers up to 13.6× higher performance compared to scheme-specific accelerator combinations. Moreover, in hybrid schemes, UniFHE achieves a 3.2× speedup over the state-of-the-art unified FHE accelerator Trinity.

## 中文摘要

全同态加密（FHE）支持在加密数据上进行计算。现有 FHE 方案主要分为基于 RLWE 的字级方案与基于 LWE 的位级方案，将不同 FHE 方案高效组合以适应实际应用已成为研究热点。本文提出 UniFHE，首个使用通用算术单元支持多样代数结构以实现更高性能的 FHE 加速器。UniFHE 兼容基于 RLWE 与基于 LWE 的 FHE 方案，且无需修改其原有算法设计。为同时支持有限环与复数域运算，UniFHE 引入通用算术单元并进一步构建核心计算结构。为平衡不同方案间的片上存储需求，UniFHE 对基于 LWE 的方案采用多流水线架构，并在其基础上拼接面向 RLWE 方案的核心功能单元。此外，一种片上明文编码机制显著降低了片外存储带宽需求。实验结果表明，除更优的面积与能效外，UniFHE 相比方案专用加速器的组合最高提升 13.6 倍性能；在混合方案中，UniFHE 相比最先进的统一 FHE 加速器 Trinity 获得 3.2 倍加速比。
