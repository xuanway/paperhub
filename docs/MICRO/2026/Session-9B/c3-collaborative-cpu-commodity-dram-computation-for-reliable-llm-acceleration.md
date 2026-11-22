---
title: "C3: Collaborative CPU-Commodity DRAM Computation for Reliable LLM Acceleration"
description: "MICRO 2026 · Session 9B · C3：面向可靠 LLM 加速的 CPU 与商用 DRAM 协同计算"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "DRAM"
---

# C3: Collaborative CPU-Commodity DRAM Computation for Reliable LLM Acceleration

**中文标题：** C3：面向可靠 LLM 加速的 CPU 与商用 DRAM 协同计算

**所属 Session：** [Session 9B](index.md) · [MICRO 2026](../index.md)

**作者：** Houxiang Ji, E. Ezgi Yücel, Yaochen Li, Prajwal Ramakrishna, Derrick Quinn, Jungmin Choi, Hoshik Kim, Mohammad Alian, José F. Martínez

**来源：** MICRO 2026，pp. 3315–3329；[DOI](https://doi.org/10.1109/MICRO67795.2026.00222)

## 英文摘要

We demonstrate, for the first time, that Processing-using-DRAM (PuD) on commodity off-the-shelf (COTS) DRAM is a viable paradigm for reliable end-to-end execution of inherently probabilistic applications. We develop a reliable implementation of PuD-NOT, an operation essential for functionally complete arithmetic, on COTS DRAM by leveraging the subarray-crossing inversion observed in prior work. Using a real prototype capable of leveraging plain DRAM for PuD, we systematically scan the DRAM array and identify rows that are capable of performing key operations at very low error rates. We then designate a subset of these rows as compute rows while using the remainder of the device for storage. By reliably implementing multi-bit addition in our prototype, we show that it is feasible to execute assembly-level instructions entirely within DRAM. We further construct detailed latency models for the multi-bit arithmetic and logic instructions needed to offload computation to DRAM. Using a measurement- calibrated analytical model parameterized by our prototype's characteristics and these latency models, we demonstrate that PuD, operating synergistically with a CPU, and assuming support for subarray-level parallelism, can achieve up to 2.4× higher throughput for dense retrieval compared to a CPU-only baseline at Recall@10>0.95 and 3.2× higher throughput for quantized large-language-model inference compared to a two-thread CPU-only baseline while application accuracy remains close to the baseline.

## 中文摘要

我们首次证明，在商品现货 (COTS) DRAM 上使用 DRAM 进行处理 (PuD) 是可靠地端到端执行固有概率应用程序的可行范例。我们通过利用之前工作中观察到的子阵列交叉反转，在 COTS DRAM 上开发了 PuD-NOT 的可靠实现，这是功能完整算术所必需的操作。使用能够利用普通 DRAM 进行 PuD 的真实原型，我们系统地扫描 DRAM 阵列并识别能够以极低错误率执行关键操作的行。然后，我们将这些行的子集指定为计算行，同时使用设备的其余部分进行存储。通过在我们的原型中可靠地实现多位加法，我们证明了完全在 DRAM 中执行汇编级指令是可行的。我们进一步为将计算卸载到 DRAM 所需的多位算术和逻辑指令构建详细的时延模型。使用由我们的原型特征和这些时延模型参数化的测量校准分析模型，我们证明了 PuD 与 CPU 协同运行，并假设支持子阵列级并行性，与 Recall@10>0.95 的仅 CPU 基线相比，密集检索的吞吐量可实现高达 2.4 倍的高吞吐量，与仅两线程 CPU 的基线相比，量化大语言模型推理的吞吐量可实现高达 3.2 倍的吞吐量，同时应用程序精度保持接近到基线。

## 中文关键词

基于 DRAM 的计算；异构计算；DRAM；大语言模型加速；可靠性

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 9B](index.md) · [MICRO 2026 主页](../index.md)
