---
title: "Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems"
description: "HPCA 2026 · Near-Data Processing and Storage"
tags:
  - "HPCA2026"
  - "Near-Data Processing and Storage"
---

# Adaptive Draft Sequence Length: Enhancing Speculative Decoding Throughput on PIM-Enabled Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Near-Data Processing and Storage。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Near-Data Processing and Storage</p>
</div>

**论文链接**：
**作者**：Runze Wang Huazhong University of Science and Technology , Qinggang Wang Huazhong University of Science and Technology , Haifeng Liu Huazhong University of Science and Technology , Long Zheng Huazhong University of Science and Technology , XIAOFEI LIAO Huazhong University of Science and Technology , Hai Jin Huazhong University of Science and Technology , Jingling Xue UNSW Sydney
**会议**：HPCA 2026

---

## 中文标题

自适应草稿序列长度：提升 PIM 系统上的推测解码吞吐

## 英文摘要

Transformer-based large language models (LLMs) exhibit remarkable generative capabilities, but their inference throughput is limited by the autoregressive decoding process, which generates only one token per iteration. Speculative decoding mitigates this bottleneck by using a lightweight draft language model (DLM) to generate multiple draft tokens, which are then verified in parallel by a more accurate target language model (TLM). To accommodate the differing computational patterns of the DLM and TLM, prior work has leveraged heterogeneous systems combining xPUs and processing-in-memory (PIM) units to offload compute- and memory-intensive operators, respectively. However, existing systems often adopt a fixed draft sequence length, leading to excessive rejection of draft tokens during verification—especially under large-batch scenarios—resulting in redundant computation and reduced efficiency. This paper proposes a runtime adaptive draft length adjustment technique that dynamically tailors the draft length for each request by monitoring cumulative acceptance probabilities, thereby minimizing the generation and verification of invalid tokens. Yet, integrating adaptive draft lengths into existing PIM-enabled heterogeneous systems introduces two new challenges: (1) sequential execution of the DLM and TLM becomes inefficient due to synchronization bubbles caused by request-wise variability in draft lengths, and (2) static operator mappings become suboptimal as draft length variability alters operator arithmetic intensities dynamically. To address these issues, we introduce SADDLE, a PIM-enabled heterogeneous system designed to exploit adaptive draft lengths effectively. SADDLE incorporates two key mechanisms: (1) an asynchronous speculative decoding pipeline that decouples DLM prediction and TLM verification to reduce idle time, and (2) an arithmetic intensity-aware operator scheduler that dynamically assigns operators to the most suitable hardware units. Experimental results show that SADDLE achieves average speedups of 2.88× over a state-of-the-art GPU-only solution and 1.71× over the best-performing GPU+PIM baseline.

## 中文摘要

基于 Transformer 的大语言模型（LLM）生成能力出色，但其推理吞吐受限于自回归解码过程，每次迭代仅生成一个 token。推测解码用轻量级草稿语言模型（DLM）生成多个草稿 token，再由更精确的目标语言模型（TLM）并行验证，从而缓解该瓶颈。为适应 DLM 与 TLM 不同的计算模式，已有工作采用 xPU 与存内处理（PIM）单元相结合的异构系统，分别卸载计算密集型与访存密集型算子。但现有系统多采用固定草稿长度，导致验证阶段大量草稿 token 被拒绝，尤其在大批量场景下，造成冗余计算与效率下降。本文提出运行时自适应草稿长度调整技术，通过监测累积接受概率为每个请求动态裁剪草稿长度，最大限度减少无效 token 的生成与验证。将自适应长度引入 PIM 异构系统带来两个新挑战：（1）各请求草稿长度不同造成同步气泡，使 DLM 与 TLM 的顺序执行效率低下；（2）草稿长度的变化会动态改变算子算术强度，使静态算子映射不再最优。为此我们提出 SADDLE，包含两项机制：（1）异步推测解码流水线，解耦 DLM 预测与 TLM 验证以减少空闲；（2）算术强度感知的算子调度器，把算子动态分配到最合适的硬件单元。实验表明，SADDLE 相比最先进的纯 GPU 方案平均加速 2.88 倍，相比最佳 GPU+PIM 基线加速 1.71 倍。
