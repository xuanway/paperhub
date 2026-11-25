---
title: "MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production"
description: "EuroSys 2026 · LLM Training at Scale · Chao Jin (School of Computer Science, Peking University), Ziheng Jiang (ByteDanc"
tags:
  - "EuroSys2026"
  - "LLM Training at Scale"
---

# MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production

**中文标题：** MegaScale-MoE：生产环境中专家混合模型的大规模通信高效训练

**所属 Session：** [Session 3.1: LLM Training at Scale](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Training at Scale。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Training at Scale</p>
</div>

**作者**：Chao Jin (School of Computer Science, Peking University), Ziheng Jiang (ByteDance Seed), Zhihao Bai (ByteDance Seed), Zheng Zhong (ByteDance Seed), Juncai Liu (ByteDance Seed), Xiang Li (ByteDance Seed), Ningxin Zheng (ByteDance Seed), Xi Wang (ByteDance Seed), Cong Xie (ByteDance Seed), Qi Huang (ByteDance Seed), Wen Heng (ByteDance Seed), Yiyuan Ma (ByteDance Seed), Wenlei Bao (ByteDance Seed), Size Zheng (ByteDance Seed), Xuegui Zheng (ByteDance Seed), Yanghua Peng (ByteDance Seed), Haibin Lin (ByteDance Seed), Xuanzhe Liu (School of Computer Science, Peking University), Xin Jin (School of Computer Science, Peking University), Xin Liu (ByteDance Seed)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769325)

## 英文摘要

We present MegaScale-MoE, a production system tailored for the efficient training of large-scale mixture-of-experts (MoE) models. MoE emerges as a promising architecture to scale large language models (LLMs) to unprecedented sizes, thereby enhancing model performance. However, existing MoE training systems experience a degradation in training efficiency, exacerbated by the escalating scale of MoE models and the continuous evolution of hardware.

Recognizing the pivotal role of efficient communication in enhancing MoE training, MegaScale-MoE customizes communication-efficient parallelism strategies for attention and FFNs in each MoE layer and adopts a holistic approach to overlap communication with computation at both inter- and intra-operator levels. Additionally, MegaScale-MoE applies communication compression with adjusted communication patterns to lower precision, further improving training efficiency. When training a 352B MoE model on 1,440 NVIDIA Hopper GPUs, MegaScale-MoE achieves a training throughput of 1.41M tokens/s, improving the efficiency by 1.88× compared to Megatron-LM. We share our operational experience in accelerating MoE training and hope that by offering our insights in system design, this work will motivate future research in MoE systems.

## 中文摘要

我们介绍 MegaScale-MoE，一个为大规模专家混合（MoE）模型的高效训练而定制的生产系统。MoE 已成为将大语言模型（LLM）扩展到前所未有的规模从而提升模型性能的一条有前景的架构路径。然而，现有 MoE 训练系统的训练效率出现下降，而 MoE 模型规模的不断攀升与硬件的持续演进进一步加剧了这一问题。

认识到高效通信在提升 MoE 训练中的关键作用，MegaScale-MoE 为每个 MoE 层中的注意力和 FFN 定制了通信高效的并行策略，并采用整体性方法在算子间与算子内两个层面重叠通信与计算。此外，MegaScale-MoE 以调整后的通信模式将通信压缩应用到更低精度，进一步提升训练效率。在 1,440 块 NVIDIA Hopper GPU 上训练一个 352B 的 MoE 模型时，MegaScale-MoE 达到 1.41M tokens/s 的训练吞吐，相比 Megatron-LM 将效率提升 1.88 倍。我们分享了在加速 MoE 训练方面的运维经验，并希望通过对系统设计的洞见推动未来 MoE 系统的研究。

**英文关键词：** Mixture-of-experts, distributed training, computation-communication overlap

**中文关键词：** 专家混合、分布式训练、计算-通信重叠

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
