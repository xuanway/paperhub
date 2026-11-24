---
title: "MC-ORAM: A Mask-Assisted and Counter-Based Non-Deterministic ORAM inside VM-Based TEEs"
description: "ISCA 2026 · Session 3C · MC-ORAM: A Mask-Assisted and Counter-Based Non-Deterministic ORAM inside VM-Based TEEs"
tags:
  - "ISCA2026"
  - "Session 3C"
  - "Security"
---

# MC-ORAM: A Mask-Assisted and Counter-Based Non-Deterministic ORAM inside VM-Based TEEs

**中文标题：** MC-ORAM: 基于 VM 的 TEE 中一种掩码辅助且基于计数器的非确定性 ORAM

**所属 Session：** [Session 3C](index.md) · [ISCA 2026](../index.md)

**作者：** Yongqin Wang, Rachit Rajat, Jonghyun Lee, Mengyuan Li, Murali Annavaram

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Protecting memory access patterns is crucial for secure computation in environments where sensitive data is processed. Oblivious RAM (ORAM) offers a promising solution to safeguard against such leaks by hiding memory access patterns. However, integrating ORAM with modern Trusted Execution Environments (TEEs) introduces challenges due to the TEE’s deterministic encryption, which undermines ORAM’s oblivious guarantees. In this work, we present MC-ORAM, a novel mechanism to introduce non-determinism into ORAM systems running in VM-based TEEs. Traditional counter-based designs, such as those using 64-bit counters for every 64-bit data, introduce non-determinism but incur significant overheads due to increased memory traffic. In contrast, MC-ORAM employs a shorter, masking-assisted and counter-based design that ensures ciphertext freshness with minimal overhead. Our method minimizes memory traffic, achieving only a 1.125× increase in bandwidth, compared to the baseline, a substantial improvement over previous approaches that incur a 2× bandwidth overhead. Through experiments on PathORAM and RingORAM, we demonstrate that MC-ORAM delivers notable performance improvements, achieving end-to-end speedup of 1.82× over existing non-deterministic ORAM solutions.

## 中文摘要

保护内存访问模式对于在处理敏感数据的环境中进行安全计算至关重要。Oblivious RAM（ORAM）通过隐藏内存访问模式，为防范此类泄漏提供了一种有前景的解决方案。然而，将 ORAM 与现代可信执行环境（TEE）集成会带来挑战，因为 TEE 的确定性加密会削弱 ORAM 的不经意性保证。在本工作中，我们提出 MC-ORAM，一种在基于 VM 的 TEE 中运行的 ORAM 系统里引入非确定性的新机制。传统的基于计数器的设计（例如为每 64 位数据使用 64 位计数器）虽然引入了非确定性，但会因内存流量增加而带来显著开销。相比之下，MC-ORAM 采用一种更短的、掩码辅助且基于计数器的设计，以最小的开销保证密文新鲜性。我们的方法将内存流量降至最低，相比基线仅带来 1.125× 的带宽增长，相较此前会产生 2× 带宽开销的方法有实质性改进。通过在 PathORAM 与 RingORAM 上的实验，我们证明 MC-ORAM 带来显著的性能提升，相比现有的非确定性 ORAM 方案实现 1.82× 的端到端加速。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2026](../index.md)
