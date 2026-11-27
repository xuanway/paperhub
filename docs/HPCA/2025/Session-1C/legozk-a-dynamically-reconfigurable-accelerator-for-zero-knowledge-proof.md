---
title: "LegoZK: A Dynamically Reconfigurable Accelerator for Zero-Knowledge Proof"
description: "HPCA 2025 · Next Big Bets"
tags:
  - "HPCA2025"
  - "Next Big Bets"
---

# LegoZK: A Dynamically Reconfigurable Accelerator for Zero-Knowledge Proof

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Next Big Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Next Big Bets</p>
</div>

**论文链接**：
**作者**：Zhengbang Yang (Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS and School of Cyber Security, University of Chinese Academy of Sciences), Lutan Zhao (Institute of Information Engineering, CAS), Peinan Li (Institute of Information Engineering, CAS), Han Liu (Institute of Information Engineering, CAS), Kai Li (Key Laboratory of Cyberspace Security Defense, Institute of Information Engineering, CAS and School of Cyber Security, University of Chinese Academy of Sciences), Boyan Zhao (Institute of Information Engineering, CAS), Dan Meng (Institute of Information Engineering, CAS), Rui Hou (Institute of Information Engineering, CAS)
**会议**：HPCA 2025

---

## 中文标题

LegoZK：面向零知识证明的动态可重构加速器

## 英文摘要

Zero-knowledge proof (ZKP) allows a prover to convince a verifier of the truth of a statement without revealing any secret information. This property is utilized in numerous privacy-preserving applications. However, the huge overhead of proof generation impedes the widespread adoption of ZKP. As a result, many ZKP accelerators have been developed to speed up proof generation. However, existing accelerators are designed at the granularity of core operators and exhibit low hardware resource utilization and limited adaptability. In this paper, we identify the commonality of all computation stages in proof generation at the level of basic finite field arithmetic operations. Based on this insight, we propose LegoZK, a dynamically reconfigurable hardware accelerator for ZKP. LegoZK employs finite field arithmetic units (FAUs) as its fundamental components and integrates these FAUs with a hierarchical on-chip network (NoC). By dynamically configuring the FAUs and the NoC, LegoZK can effectively accelerate the entire proof generation process, achieving higher overall performance. Additionally, for the most time-consuming MSM, this paper proposes a fast, fully pipelined bucket reduction algorithm based on lookup tables, which significantly reduces the latency of MSM. Experimental results demonstrate that LegoZK achieves on average speedup of 31.96× and 11.30× in proof generation compared to the state-of-the-art ZKP ASIC accelerator PipeZK and the GPU accelerator GZKP, respectively. And compared to PipeZK, LegoZK achieves 50.1% area reduction and 37.7% power consumption reduction.

## 中文摘要

零知识证明（ZKP）使证明者能在不泄露任何秘密信息的前提下让验证者相信命题为真，该特性被广泛用于隐私保护应用。然而，证明生成的巨大开销阻碍了 ZKP 的普及。现有 ZKP 加速器多以核心算子为粒度设计，硬件资源利用率低、适应性有限。本文发现，证明生成中所有计算阶段在基本有限域算术运算层面具有共性，据此提出动态可重构的 ZKP 硬件加速器 LegoZK。它以有限域算术单元（FAU）为基本构件，并用分层片上网络（NoC）将其集成；通过动态配置 FAU 与 NoC，可有效加速整个证明生成过程，获得更高的整体性能。此外，针对最耗时的 MSM，本文提出基于查找表的快速全流水线桶归约算法，显著降低 MSM 时延。实验表明，相比最先进的 ZKP ASIC 加速器 PipeZK 和 GPU 加速器 GZKP，LegoZK 的证明生成平均加速 31.96 倍和 11.30 倍；相比 PipeZK，面积减少 50.1%，功耗降低 37.7%。
