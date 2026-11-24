---
title: "Evaluating Compiler Optimization Impacts on zkVM Performance"
description: "ASPLOS 2026 · Session 7B · 评估编译器优化对 zkVM 性能的影响"
tags:
  - "ASPLOS2026"
  - "Session 7B"
  - "Compilers & Code Generation"
---

# Evaluating Compiler Optimization Impacts on zkVM Performance

**中文标题：** 评估编译器优化对 zkVM 性能的影响

**所属 Session：** [Session 7B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Thomas Gassmann (ETH Zurich), Stefanos Chaliasos (Imperial College London & zkSecurity), Thodoris Sotiropoulos (ETH Zurich), Zhendong Su (ETH Zurich)

**单位：** ETH Zurich；Imperial College London & zkSecurity

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790159) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Zero-knowledge proofs (ZKPs) are the cornerstone of programmable cryptography. They enable (1) privacy-preserving and verifiable computation across blockchains, and (2) an expanding range of off-chain applications such as credential schemes. Zero-knowledge virtual machines (zkVMs) lower the barrier by turning ZKPs into a drop-in backend for standard compilation pipelines. This lets developers write proof-generating programs in conventional languages (e.g., Rust or C++) instead of hand-crafting arithmetic circuits. However, these VMs inherit compiler infrastructures tuned for traditional architectures rather than for proof systems. In particular, standard compiler optimizations assume features that are absent in zkVMs, including cache locality, branch prediction, or instruction-level parallelism. Therefore, their impact on proof generation is questionable. We present the first systematic study of the impact of compiler optimizations on zkVMs. We evaluate 64 LLVM passes, six standard optimization levels, and an unoptimized baseline across 58 benchmarks on two RISC-V–based zkVMs (RISC Zero and SP1). While standard LLVM optimization levels do improve zkVM performance (over 40%), their impact is far smaller than on traditional CPUs, since their decisions rely on hardware features rather than proof constraints. Guided by a performance impact analysis, we slightly refine a small set of LLVM passes to be zkVM-aware, improving zkVM execution time by up to 45% (average +4.6% on RISC Zero, +1% on SP1) and achieving consistent proving-time gains. Our work highlights the potential of compiler-level optimizations for zkVM performance and opens new directions for zkVM-specific passes, backends, and superoptimizers.

## 中文摘要

零知识证明（ZKP）是可编程密码学的基石。它们使能：(1) 跨区块链的隐私保护且可验证的计算；(2) 范围不断扩大的链下应用，例如凭证方案。零知识虚拟机（zkVM）通过将 ZKP 转变为标准编译流水线中可直接接入的后端，降低了使用门槛。这使开发者能用常规语言（如 Rust 或 C++）编写生成证明的程序，而无需手工构造算术电路。然而，这些虚拟机继承的是面向传统架构而非面向证明系统调优的编译器基础设施。特别是，标准编译器优化所假设的特性在 zkVM 中并不存在，包括缓存局部性、分支预测或指令级并行。因此，它们对证明生成的影响值得质疑。我们给出首个关于编译器优化对 zkVM 影响的系统性研究。我们在两个基于 RISC-V 的 zkVM（RISC Zero 和 SP1）上，针对 58 个基准，评估了 64 个 LLVM pass、六个标准优化级别以及一个未优化基线。尽管标准 LLVM 优化级别确实提升了 zkVM 性能（超过 40%），但其影响远小于在传统 CPU 上的影响，因为其决策依赖硬件特性而非证明约束。在一项性能影响分析的指导下，我们对少量 LLVM pass 做了细微改进使其具备 zkVM 感知能力，将 zkVM 执行时间最多改善 45%（RISC Zero 上平均 +4.6%，SP1 上 +1%），并在证明时间上取得一致的收益。我们的工作凸显了编译器级优化提升 zkVM 性能的潜力，并为 zkVM 专用的 pass、后端和超优化器开辟了新方向。

## 英文关键词

compiler optimization,LLVM,zero-knowledge proof,zkVM,circuit,SP1,RISC Zero,performance,proving

## 中文关键词

编译器优化；LLVM；零知识证明；zkVM；电路；SP1；RISC Zero；性能；证明生成

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790159)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7B](index.md) · [返回 ASPLOS 2026](../index.md)
