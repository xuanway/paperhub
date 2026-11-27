---
title: "Fully Parallelized BP Decoding for Quantum LDPC Codes Can Outperform BP-OSD"
description: "HPCA 2026 · Quantum Compilation and Simulation"
tags:
  - "HPCA2026"
  - "Quantum Compilation and Simulation"
---

# Fully Parallelized BP Decoding for Quantum LDPC Codes Can Outperform BP-OSD

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Quantum Compilation and Simulation。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Quantum Compilation and Simulation</p>
</div>

**论文链接**：
**作者**：Ming Wang North Carolina State University , Ang Li Pacific Northwest National Laboratory , Frank Mueller North Carolina State University, USA
**会议**：HPCA 2026

---

## 中文标题

量子 LDPC 码的全并行 BP 译码可超越 BP-OSD

## 英文摘要

This work presents a hardware-efficient and fully parallelizable decoder for quantum LDPC codes that leverages belief propagation (BP) with a speculative post-processing strategy inspired by classical Chase decoding algorithm. By monitoring bit-level oscillation patterns during BP, our method identifies unreliable bits and generates multiple candidate vectors to selectively flip syndromes. Each modified syndrome is then decoded independently using short-depth BP, a process we refer to as BP-SF (syndrome flip). This design eliminates the need for costly Gaussian elimination used in the current BP-OSD approaches. Our implementation achieves logical error rates comparable to or better than BP-OSD while offering significantly lower latency due to its high degree of parallelism for a variety of bivariate bicycle codes. Evaluation on the J144, 12, 12K bivariate bicycle code shows that the proposed decoder reduces average latency to approximately 70% of BP-OSD. When post-processing is parallelized the average latency is reduced by 55% compared to the single process implementation, with the maximum latency reaching as low as 18%. These advantages make it particularly well-suited for real-time and resource-constrained quantum error correction systems.

## 中文摘要

本文提出一种硬件高效且可完全并行化的量子 LDPC 码译码器，它利用置信传播（BP），并采用受经典 Chase 译码算法启发的推测式后处理策略。通过监测 BP 过程中的比特级振荡模式，我们的方法识别出不可靠比特，并生成多个候选向量以选择性地翻转校验子。随后每个被修改的校验子都用短深度 BP 独立译码，我们将该过程称为 BP-SF（校验子翻转）。该设计无需当前 BP-OSD 方法中代价高昂的高斯消元。在多种双变量自行车码上，我们的实现取得与 BP-OSD 相当或更优的逻辑错误率，同时由于并行度高而时延显著更低。在 J144, 12, 12K 双变量自行车码上的评估显示，所提译码器将平均时延降至 BP-OSD 的约 70%；当后处理并行化后，平均时延相比单进程实现降低 55%，最大时延低至 18%。这些优势使其特别适合实时与资源受限的量子纠错系统。
