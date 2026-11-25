---
title: "High-Throughput Non-uniformly Quantized 3-bit LLM Inference"
description: "PPoPP 2026 Session 6（Mixed Precision and Quantization）：融合反量化流水线，核级 4.82×、端到端 11.46×"
tags:
  - "PPoPP2026"
  - "Session-6"
  - "Mixed Precision and Quantization"
  - "Non-uniform Quantization"
  - "3-bit"
  - "LLM Inference"
authors:
  - "YuAng Chen"
  - "Wenqi Zeng"
  - "Jeffrey Xu Yu"
session: "Session 6: Mixed Precision and Quantization"
session_number: 6
session_chair: "Dingwen Tao"
date: "2026-02-03"
time: "11:50–12:10"
room: "Balmoral"
doi: "10.1145/3774934.3786423"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# High-Throughput Non-uniformly Quantized 3-bit LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Quantix 框架，以硬件对齐的比特重排与融合反量化-乘流水线，把聚类非均匀 3-bit 量化的内存节省转化为推理加速，端到端最高 11.46×。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 6: Mixed Precision and Quantization</p>
</div>

**作者**：YuAng Chen, Wenqi Zeng, and Jeffrey Xu Yu — Chinese University of Hong Kong, China; Hong Kong University of Science and Technology, China; Hong Kong University of Science and Technology (Guangzhou), China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 11:50–12:10 · Session 6: Mixed Precision and Quantization（主席：Dingwen Tao）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786423) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

While Large Language Models (LLMs) are widely adopted, their massive parameter size constrains practical deployment. A common solution is clustering-based non-uniform quantization, which effectively compresses models to as low as 3 bits per weight while preserving high accuracy. However, instead of accelerating memory-bound LLM inference, the memory reduction paradoxically often causes a significant slowdown due to dequantization overhead and GPU underutilization. To address the issue, we propose Quantix, a framework designed to convert memory savings into inference speedups. Quantix applies two key optimizations: (1) a hardware-aligned bit shuffling scheme for efficient data access, and (2) a fused dequantization-multiplication pipeline that effectively maps workloads on both CUDA and Tensor Cores. Quantix enables high-throughput batched inference, delivering average kernel-level speedups of 4.82× over FP16 cuBLAS and end-to-end speedups of up to 11.46× over state-of-the-art quantization methods on NVIDIA L40 GPUs.

## 中文摘要

尽管大语言模型（LLM）已被广泛采用，其庞大的参数规模制约了实际部署。一种常见方案是基于聚类的非均匀量化，它可将模型有效压缩至每权重低至 3 比特，同时保持较高精度。然而，这种内存缩减非但未能加速受内存约束的 LLM 推理，反而常常因反量化开销与 GPU 利用率不足而导致显著变慢。为解决该问题，我们提出 Quantix，一个旨在将内存节省转化为推理加速的框架。Quantix 采用两项关键优化：（1）面向高效数据访问的、与硬件对齐的比特重排方案；（2）融合的反量化–乘法流水线，可在 CUDA 核与 Tensor Core 上有效映射工作负载。Quantix 支持高吞吐的批量推理，在 NVIDIA L40 GPU 上相较 FP16 cuBLAS 取得平均 4.82 倍的内核级加速，相较最先进的量化方法取得最高 11.46 倍的端到端加速。

## 英文关键词

Large language model (LLM) inference, GPU programming

## 中文关键词

大语言模型（LLM）推理；GPU 编程

---

## 一句话总结

> 提出 Quantix 框架，以硬件对齐的比特重排与融合反量化-乘流水线，把聚类非均匀 3-bit 量化的内存节省转化为推理加速，端到端最高 11.46×。

## 研究问题

聚类非均匀量化可压至每权重 3 bit 并保持精度，但反量化开销与 GPU 利用率不足使内存受限的 LLM 推理反而显著变慢。

## 方法简述

- 采用硬件对齐的比特重排（bit shuffling）方案实现高效数据访问。
- 设计融合的反量化-乘法流水线，将工作负载同时映射到 CUDA 核与张量核。
- 支持高吞吐的批量推理。

## 主要结果

- 在 NVIDIA L40 GPU 上，核级平均相对 FP16 cuBLAS 加速 4.82×。
- 端到端相对 SOTA 量化方法最高加速 11.46×。

---

> 所属 Session：[Session 6: Mixed Precision and Quantization](index.md) · 返回 [PPoPP 2026 总览](../index.md)
