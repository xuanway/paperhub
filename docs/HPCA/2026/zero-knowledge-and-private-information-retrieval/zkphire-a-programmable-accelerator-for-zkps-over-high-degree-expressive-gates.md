---
title: "zkPHIRE: A Programmable Accelerator for ZKPs over HIgh-degRee, Expressive Gates"
description: "HPCA 2026 · Zero-Knowledge and Private Information Retrieval"
tags:
  - "HPCA2026"
  - "Zero-Knowledge and Private Information Retrieval"
---

# zkPHIRE: A Programmable Accelerator for ZKPs over HIgh-degRee, Expressive Gates

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Zero-Knowledge and Private Information Retrieval。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Zero-Knowledge and Private Information Retrieval</p>
</div>

**论文链接**：
**作者**：Alhad Daftardar New York University , Jianqiao Cambridge Mo New York University , Joey Ah-kiow New York University , Benedikt Bünz New York University , Siddharth Garg New York University , Brandon Reagen New York University
**会议**：HPCA 2026

---

## 中文标题

zkPHIRE：面向高阶表达性门电路的可编程 ZKP 加速器

## 英文摘要

Zero-Knowledge Proofs (ZKPs) have emerged as a powerful tool for secure and privacy-preserving computation. ZKPs enable one party to convince another of a statement’s validity without revealing anything else. This capability has profound implications in many domains, including: machine learning, blockchain, image authentication, and electronic voting. Despite their potential, ZKPs have seen limited deployment because of their exceptionally high computational overhead, which manifests primarily during proof generation. To mitigate these overheads, a (growing) body of researchers have proposed hardware accelerators and GPU implementations of kernels and complete protocols. Prior art spans a wide variety of ZKP schemes that vary significantly in computational overhead, proof size, verifier cost, protocol setup, and trust. The latest, and widely used ZKP protocols are intentionally designed to balance these trade-offs. A particular challenge in modern ZKP systems is supporting complex, high-degree gates using the SumCheck protocol. We address this challenge with a novel programmable accelerator to efficiently handle arbitrary custom gates via SumCheck. Our accelerator achieves upwards of 1000× geomean speedup over CPU-based SumChecks across a range of gate types. We include this unit in zkPHIRE, a programmable, full-system accelerator that accelerates the HyperPlonk protocol. zkPHIRE achieves 1486× geomean speedup over CPU and 11.87× geomean speedup over the state-of-the-art at iso-area. Together, these results demonstrate compelling performance while scaling to large problem sizes (upwards of 230 constraints) and maintaining small proof sizes (4 − 5 KB).

## 中文摘要

零知识证明（ZKP）已成为安全与隐私保护计算的强大工具，使一方能在不泄露其他信息的情况下让另一方相信某陈述有效。这一能力在机器学习、区块链、图像认证与电子投票等领域影响深远。尽管潜力巨大，ZKP 因其极高的计算开销而部署有限，这些开销主要体现在证明生成阶段。为缓解开销，越来越多的研究者提出了内核与完整协议的硬件加速器及 GPU 实现，涵盖多种 ZKP 方案，它们在计算开销、证明大小、验证者成本、协议设置与信任假设上差异显著。最新且广泛使用的 ZKP 协议有意在这些折中之间取得平衡。现代 ZKP 系统的一项特殊挑战是利用 SumCheck 协议支持复杂的高阶门。我们通过一种新颖的可编程加速器应对该挑战，借助 SumCheck 高效处理任意自定义门；在一系列门类型上，该加速器相比基于 CPU 的 SumCheck 取得超过 1000 倍几何平均加速比。我们将该单元集成到 zkPHIRE 中，这是一个可编程的全系统加速器，用于加速 HyperPlonk 协议。zkPHIRE 相比 CPU 取得 1486 倍几何平均加速比，在等面积下相比最先进方案取得 11.87 倍几何平均加速比。这些结果共同展示了扩展到大规模问题（超过 230 个约束）时的出色性能与较小的证明大小（4 − 5 KB）。
