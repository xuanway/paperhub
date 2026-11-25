---
title: "JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference"
description: "PPoPP 2026 Session 6（Mixed Precision and Quantization）：2-bit KV cache 量化，省显存 5.3×、解码吞吐 4.45×"
tags:
  - "PPoPP2026"
  - "Session-6"
  - "Mixed Precision and Quantization"
  - "KV Cache Quantization"
  - "Long-context Inference"
  - "2-bit"
authors:
  - "Chengyu Sun"
  - "Yaqi Xia"
  - "Hulin Wang"
  - "Donglin Yang"
  - "Xiaobo Zhou"
  - "Dazhao Cheng"
session: "Session 6: Mixed Precision and Quantization"
session_number: 6
session_chair: "Dingwen Tao"
date: "2026-02-03"
time: "12:10–12:30"
room: "Balmoral"
doi: "10.1145/3774934.3786428"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# JanusQuant: Accurate and Efficient 2-bit KV Cache Quantization for Long-Context Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 2-bit KV cache 量化系统 JanusQuant，以 RtSmooth 算法抑制离群值并配混合精度注意力核，保留 99% FP16 精度、解码吞吐 4.45×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 6: Mixed Precision and Quantization</p>
</div>

**作者**：Chengyu Sun, Yaqi Xia, Hulin Wang, Donglin Yang, Xiaobo Zhou, and Dazhao Cheng — Wuhan University, China; Nvidia Corporation, USA; University of Macau, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 12:10–12:30 · Session 6: Mixed Precision and Quantization（主席：Dingwen Tao）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786428) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Long-context large language models (LLMs) have seen widespread adoption in recent years. However, during inference, the key-value (KV) cache—which stores intermediate activations—consumes significant memory, particularly as sequence lengths grow. Quantization offers a promising path to compress KV cache, but existing 2-bit approaches fall short of achieving optimal inference efficiency due to hardware-unfriendly algorithms and system implementations. We present JanusQuant, a 2-bit KV cache quantization system that achieves both high accuracy and end-to-end efficiency through algorithm–system co-design for long-context generation tasks. At its core is RtSmooth, a novel runtime smoothing quantization algorithm that mitigates outlier-induced accuracy loss via adaptive transformation. Building on RtSmooth, JanusQuant further enhances quantized inference with a series of optimizations: a fast absmax positioning technique for lightweight quantization, a memory-efficient data structure for managing recent tokens, and a custom mixed-precision attention kernel to accelerate computation. Across representative LLMs, JanusQuant preserves 99% of FP16 accuracy, reduces KV cache memory usage by up to 5.3×, and delivers up to 4.45× faster decoding throughput compared to state-of-the-art methods, while scaling efficiently to long-context inference.

## 中文摘要

近年来，长上下文大语言模型（LLM）得到广泛采用。然而在推理过程中，用于存储中间激活的键值（KV）缓存会消耗大量内存，随着序列长度增长尤为突出。量化是压缩 KV 缓存的一条有前景的路径，但现有 2 比特方法由于算法与系统实现对硬件不友好，未能达到最优的推理效率。我们提出 JanusQuant，一个 2 比特 KV 缓存量化系统，它通过面向长上下文生成任务的算法–系统协同设计，同时实现高精度与端到端效率。其核心是 RtSmooth，一种新颖的运行时平滑量化算法，通过自适应变换缓解离群值导致的精度损失。在 RtSmooth 的基础上，JanusQuant 通过一系列优化进一步增强量化推理：用于轻量级量化的快速 absmax 定位技术、用于管理近期 token 的内存高效数据结构，以及用于加速计算的定制混合精度注意力内核。在代表性 LLM 上，JanusQuant 保留了 FP16 精度的 99%，将 KV 缓存内存占用最高降低 5.3 倍，并相较最先进方法实现最高 4.45 倍的解码吞吐提升，同时可高效扩展至长上下文推理。

## 英文关键词

Long-context Inference, KV Cache Quantization

## 中文关键词

长上下文推理；KV 缓存量化

---

## 一句话总结

> 提出 2-bit KV cache 量化系统 JanusQuant，以 RtSmooth 算法抑制离群值并配混合精度注意力核，保留 99% FP16 精度、解码吞吐 4.45×。

## 研究问题

长上下文推理中 KV cache 显存占用随序列长度快速增长；现有 2-bit 方法因算法与系统实现对硬件不友好，难以兼顾精度与效率。

## 方法简述

- 提出 RtSmooth 运行时平滑量化算法，通过自适应变换缓解离群值引起的精度损失。
- 设计快速 absmax 定位技术，实现轻量量化。
- 采用内存高效的数据结构管理近期 token。
- 实现定制混合精度注意力核以加速计算。

## 主要结果

- 在代表性 LLM 上保留 99% 的 FP16 精度。
- KV cache 显存占用最高降低 5.3×。
- 解码吞吐相对 SOTA 方法最高提升 4.45×，并可高效扩展到长上下文推理。

---

> 所属 Session：[Session 6: Mixed Precision and Quantization](index.md) · 返回 [PPoPP 2026 总览](../index.md)
