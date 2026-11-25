---
title: "TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone"
description: "EuroSys 2026 · Security, Privacy & Vulnerabilities · Xunjie Wang (Shanghai Jiao Tong University), Jiacheng Shi (Shanghai Jiao Tong Un"
tags:
  - "EuroSys2026"
  - "Security, Privacy & Vulnerabilities"
---

# TZ-LLM: Protecting On-Device Large Language Models with Arm TrustZone

**中文标题：** TZ-LLM：利用 Arm TrustZone 保护端侧大语言模型

**所属 Session：** [Session 8.2: Security, Privacy & Vulnerabilities](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Security, Privacy & Vulnerabilities。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Security, Privacy & Vulnerabilities</p>
</div>

**作者**：Xunjie Wang (Shanghai Jiao Tong University), Jiacheng Shi (Shanghai Jiao Tong University), Zihan Zhao (Shanghai Jiao Tong University), Yang Yu (Shanghai Jiao Tong University), Zhichao Hua (Shanghai Jiao Tong University), Jinyu Gu (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769334)

## 英文摘要

Large Language Models (LLMs) deployed on mobile devices offer benefits like user privacy and reduced network latency, but introduce a significant security risk: the leakage of proprietary models to end users.

To mitigate this risk, we propose a system design for protecting on-device LLMs using Arm Trusted Execution Environment (TEE), TrustZone. Our system addresses two primary challenges: (1) The dilemma between memory efficiency and fast inference (caching model parameters within TEE memory). (2) The lack of efficient and secure Neural Processing Unit (NPU) time-sharing between Rich Execution Environment (REE) and TEE.

Our approach incorporates two key innovations. First, we employ pipelined restoration, leveraging the deterministic memory access patterns of LLM inference to prefetch parameters on demand, hiding memory allocation, I/O and decryption latency under computation time. Second, we introduce a co-driver design, creating a minimal data plane NPU driver in the TEE that collaborates with the full-fledged REE driver. This reduces the TEE TCB size and eliminates control plane reinitialization overhead during NPU world switches.

We implemented our system on the emerging OpenHarmony OS and the llama.cpp inference framework, and evaluated it with various LLMs on an Arm Rockchip device. Compared to a strawman TEE baseline lacking our optimizations, our system reduces TTFT by up to 90.9% and increases decoding speed by up to 23.2%.

## 中文摘要

部署在移动设备上的大语言模型（LLM）带来用户隐私保护与网络延迟降低等优势，但也引入了重大安全风险：专有模型泄露给最终用户。

为缓解这一风险，我们提出一种利用 Arm 可信执行环境（TEE）TrustZone 保护端侧 LLM 的系统设计。我们的系统应对两个主要挑战：（1）内存效率与快速推理之间的两难（在 TEE 内存中缓存模型参数）。（2）缺乏在富执行环境（REE）与 TEE 之间高效且安全的神经网络处理器（NPU）分时共享机制。

我们的方法包含两项关键创新。第一，我们采用流水化恢复，利用 LLM 推理确定性的内存访问模式按需预取参数，将内存分配、I/O 与解密延迟隐藏在计算时间之下。第二，我们引入协同驱动设计，在 TEE 中构建一个最小化的数据面 NPU 驱动，与功能完备的 REE 驱动协作。这减小了 TEE 的可信计算基（TCB）规模，并消除了 NPU 世界切换期间的控制面重初始化开销。

我们在新兴的 OpenHarmony 操作系统与 llama.cpp 推理框架上实现了该系统，并在 Arm Rockchip 设备上使用多种 LLM 进行了评估。与缺少这些优化的最简 TEE 基线相比，我们的系统将首 token 时延（TTFT）最多降低 90.9%，解码速度最多提升 23.2%。

**英文关键词：** Large Language Model, Mobile computing, Arm TrustZone

**中文关键词：** 大语言模型、移动计算、Arm TrustZone

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
