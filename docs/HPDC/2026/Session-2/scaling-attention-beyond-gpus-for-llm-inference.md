---
title: "Scaling Attention Beyond GPUs for LLM Inference"
description: "HPDC 2026 · Session 2 — Scaling Generative Inference"
tags:
  - "HPDC2026"
  - "Session 2"
  - "Scaling Generative Inference"
---

# Scaling Attention Beyond GPUs for LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 2</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807596)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#DengYDXLZACSJLR26](https://dblp.org/db/conf/hpdc/hpdc2026.html#DengYDXLZACSJLR26)

**作者**：Weishu Deng, Yujie Yang, Peiran Du, Lingfeng Xiang, Zhen Lin, Chen Zhong, Faraz Ahmed, Lianjie Cao, Puneet Sharma, Song Jiang, Hui Lu, Jia Rao

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

Scaling inference for large language models is increasingly constrained by limited GPU memory, primarily due to the expanding intermediate states (KV caches) required for long-context generation and multi-user workloads. Once the KV cache exceeds the capacity of high-bandwidth memory, it must be offloaded to host memory and reloaded on demand, a workflow severely bottlenecked by the CPU–GPU interconnect, typically PCIe. Existing approaches exploiting offload KV caches to CPU memory and selectively reload partial segments for attention computation often underutilize CPU compute resources and suffer from accuracy degradation. We present Beyond, a drop-in runtime that integrates a smart offloading scheme to selectively identify and retain salient KV entries across continuous decoding sessions, together with a hybrid CPU–GPU attention mechanism for scalable inference. Beyond executes dense attention over recent KV entries stored in GPU memory while performing parallel, per-head sparse attention on salient contextual KV entries residing in CPU memory. The outputs are fused efficiently through a log-sum-exp scheme. During the bandwidth-constrained decoding phase, oversized KV caches are processed cooperatively by the aggregated CPU and GPU memory bandwidth, with only minimal PCIe data movement. Experiments across diverse models and workloads demonstrate that Beyond improves scalability, supports longer sequences and larger batch sizes, and outperforms existing sparse attention baselines in both efficiency and accuracy—all on commodity GPU hardware.

## 中文摘要

大语言模型的推理扩展日益受限于有限的 GPU 显存，主要原因是长上下文生成与多用户负载所需的中间状态（KV cache）不断膨胀。一旦 KV cache 超出高带宽显存容量，就必须卸载到主机内存并按需重新加载，而该流程受 CPU–GPU 互连（通常为 PCIe）的严重制约。现有将 KV cache 卸载至 CPU 内存并选择性重载部分片段用于注意力计算的方法，往往未充分利用 CPU 计算资源，且存在精度下降。我们提出 Beyond，一个即插即用的运行时，集成智能卸载方案，在连续的解码会话中有选择地识别并保留显著的 KV 条目，并结合混合 CPU–GPU 注意力机制实现可扩展推理。Beyond 对存放在 GPU 显存中的近期 KV 条目执行稠密注意力，同时对驻留 CPU 内存的显著上下文 KV 条目执行逐头并行的稀疏注意力。输出通过 log-sum-exp 方案高效融合。在带宽受限的解码阶段，超大的 KV cache 由 CPU 与 GPU 聚合的内存带宽协同处理，仅有极少的 PCIe 数据搬运。跨多种模型与负载的实验表明，Beyond 提升了可扩展性，支持更长的序列与更大的批大小，并在效率与精度上均优于现有稀疏注意力基线——且全部在商用 GPU 硬件上实现。

---

[← 返回 Session 2 — Scaling Generative Inference](index.md)
