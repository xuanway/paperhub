---
title: "HEPIC: Private Inference over Homomorphic Encryption with Client Intervention"
description: "ASPLOS 2026 · Session 7A · HEPIC：基于同态加密并引入客户端介入的隐私推理"
tags:
  - "ASPLOS2026"
  - "Session 7A"
  - "Fully Homomorphic Encryption"
---

# HEPIC: Private Inference over Homomorphic Encryption with Client Intervention

**中文标题：** HEPIC：基于同态加密并引入客户端介入的隐私推理

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Kevin Nam (Seoul National University), Youyeon Joo (Seoul National University), Seungjin Ha (Seoul National University), Hyungon Moon (Ulsan National Institute of Science and Technology (UNIST)), Yunheung Paek (Seoul National University)

**单位：** Seoul National University；Ulsan National Institute of Science and Technology (UNIST)

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790170) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Homomorphic Encryption (HE) enables Private Inference (PI) in Machine Learning as a Service (MLaaS), protecting both client inputs and server-side neural network (NN) parameters. Existing PI techniques are predominantly implemented as either HE-based fire-and-forget methods or MPCbased interactive methods. Recent HE-based PI systems improve the accuracy–performance trade-offvia a layer-wise scheme and parameter switching, yet remain bottlenecked by fire-and-forget execution in which the server alone performs costly ciphertext management (e.g., bootstrapping and scheme/parameter conversions). We present HEPIC, an HEbased PI system that explores a different design point by leveraging client interventions for ciphertext managements. In a sense, HEPIC shares a common ground with MPC-based PI of being interactive with the client, but differs in that the client only intervenes for ciphertext managements required in HE operations. Because ciphertext management has identical semantics on the client and the server, HEPIC lets developers decide where and how often to execute it, enabling fine-grained trade-offs among computation, communication, and ciphertext configuration. HEPIC makes such execution practical by overlapping client re-encryption, server computation, and communication via dependency-aware pipelining and streaming-based transfers. We further enhance the performance with a cache-aware task allocator (CATA) and a cost-aware client intervention scheduler (CACIS) to exploit ciphertext-level parallelism and to mitigate stalls under Our evaluation shows that HEPIC achieves up to 2.20–41.93× speedup over state-of-the-art fire-and-forget HE-based PI, while maintaining zero loss in inference accuracy.

## 中文摘要

同态加密（Homomorphic Encryption, HE）使机器学习即服务（Machine Learning as a Service, MLaaS）中的隐私推理（Private Inference, PI）成为可能，同时保护客户端输入和服务器端神经网络（NN）参数。现有的PI技术主要实现为基于HE的“发射后不管”（fire-and-forget）方法，或基于MPC的交互式方法。近期基于HE的PI系统通过逐层方案和参数切换改善了精度与性能之间的权衡，但仍受制于“发射后不管”式执行：由服务器独自承担昂贵的密文管理（例如自举以及方案/参数转换）。我们提出HEPIC，一个基于HE的PI系统，它借助客户端介入密文管理来探索不同的设计点。在某种意义上，HEPIC与基于MPC的PI有共同点，即都与客户端交互，但不同之处在于客户端仅为HE操作所需的密文管理进行介入。由于密文管理在客户端和服务器上具有相同的语义，HEPIC让开发者决定在何处以及以何种频率执行它，从而在计算、通信和密文配置之间实现细粒度权衡。HEPIC通过依赖感知的流水线和基于流的传输，将客户端重加密、服务器计算和通信重叠起来，使这种执行方式变得可行。我们进一步通过缓存感知任务分配器（CATA）和代价感知的客户端介入调度器（CACIS）提升性能，以利用密文级并行性并缓解停顿。我们的评估表明，HEPIC相比最先进的“发射后不管”式基于HE的PI系统实现了最高2.20–41.93×的加速，同时保持推理精度零损失。

## 英文关键词

Homomorphic Encryption; Private Inverence

## 中文关键词

同态加密；隐私推理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790170)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2026](../index.md)
