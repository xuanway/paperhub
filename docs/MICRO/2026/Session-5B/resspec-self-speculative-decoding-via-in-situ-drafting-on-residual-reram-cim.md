---
title: "ResSpec: Self-Speculative Decoding via In-Situ Drafting on Residual ReRAM CIM"
description: "MICRO 2026 · Session 5B · ResSpec：在残差 ReRAM 存内计算中通过原位草拟实现自推测解码"
tags:
  - "MICRO2026"
---

# ResSpec: Self-Speculative Decoding via In-Situ Drafting on Residual ReRAM CIM

**中文标题：** ResSpec：在残差 ReRAM 存内计算中通过原位草拟实现自推测解码

**所属 Session：** [Session 5B](index.md) · [MICRO 2026](../index.md)

**作者：** Yibo Zhao, Peng Huang, Youwei Zhuo

**来源：** MICRO 2026，pp. 1682–1698；[DOI](https://doi.org/10.1109/MICRO67795.2026.00121)

## 英文摘要

ReRAM compute-in-memory eliminates the memory wall for LLM autoregressive decoding, but shifts the bottleneck to peripheral readout: ADC conversion across multiple residual arrays dominates per-token cost, and leakage energy grows with decode latency. Speculative decoding accelerates GPU inference but does not transfer to ReRAM CIM: batch verification requires shared digital hardware unavailable in analog arrays, and hosting a separate draft model consumes scarce array capacity. We observe that residual programming already embeds this draft–verifier structure; the coarse array approximates the full output cheaply while the full residual reconstruction provides the high-precision check. This paper presents ResSpec, a self-speculating residual ReRAM CIM architecture that repurposes this hierarchy for LLM decoding through in-situ drafting, requiring no separate draft model or extra array capacity. A burst-oriented verify pipeline overlaps consecutive verification steps, recovering speculative benefit without GPU-style batch parallelism. Drafting reads only the coarse array through a low-bit ADC path with greater parallelism than the verify side, keeping draft cost well below verification savings. ResSpec further introduces delta readout, a window-switching SAR technique that quantizes inter-token residues rather than absolute outputs, improving low-precision ADC fidelity. Across three LLM families and both WikiText continuation and MT-bench instruction prompts, ResSpec reaches up to 2.11× throughput over matched non-speculative ResSpec baselines. Against X-Former, ResSpec reaches up to 2.66× throughput.

## 中文摘要

ReRAM 存内计算消除了 LLM 自回归解码的内存墙，但将瓶颈转移到了外设读出：跨多个残差阵列的 ADC 转换主导着每个词元的成本，并且泄漏能量随着解码时延而增长。推测性解码可加速 GPU 推理，但不会转移到 ReRAM CIM：批量验证需要模拟阵列中不可用的共享数字硬件，并且托管单独的草稿模型会消耗稀缺的阵列容量。我们观察到残差编程已经嵌入了这个草稿验证者结构；粗阵列可以廉价地逼近完整输出，而完整残差重建则提供高精度检查。本文提出了 ResSpec，这是一种自我推测的残差 ReRAM CIM 架构，它通过原位绘图重新利用该层次结构进行 LLM 解码，无需单独的绘图模型或额外的阵列容量。面向突发的验证管道与连续的验证步骤重叠，无需 GPU 式批量并行即可恢复推测性收益。草稿仅通过低位 ADC 路径读取粗略数组，其并行性高于验证端，从而使草稿成本远低于验证节省的成本。 ResSpec 进一步引入了 delta readout，这是一种窗口切换 SAR 技术，可量化词元间残差而不是绝对输出，从而提高低精度 ADC 保真度。在三个 LLM 系列以及 WikiText 延续和 MT 基准指令提示中，ResSpec 的吞吐量比匹配的非推测性 ResSpec 基线高出 2.11 倍。与 X-Former 相比，ResSpec 的吞吐量高达 2.66 倍。

## 中文关键词

大语言模型；推测解码；存内计算；阻变存储器；模拟计算；混合信号加速器

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21991990](https://doi.org/10.5281/zenodo.21991990)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 5B](index.md) · [MICRO 2026 主页](../index.md)
