---
title: "One Chiplet to Build Them All: Cost-Efficient Hardware Specialization for Stage-Disaggregated LLM Inference"
description: "MICRO 2026 · Session 8C · One Chiplet to Build Them All：面向分阶段解耦 LLM 推理的低成本硬件专门化"
tags:
  - "MICRO2026"
  - "LLM Inference"
---

# One Chiplet to Build Them All: Cost-Efficient Hardware Specialization for Stage-Disaggregated LLM Inference

**中文标题：** One Chiplet to Build Them All：面向分阶段解耦 LLM 推理的低成本硬件专门化

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Haonan Zhu, Mengdi Wang, Haoyi Jiang, Danqing Zhang, Lian Liu, Shixin Zhao, Yutian Zhou, Yudong Pan, Tianhua Han, Yinhe Han, Ying Wang

**来源：** MICRO 2026，pp. 3020–3036；[DOI](https://doi.org/10.1109/MICRO67795.2026.00204)

## 英文摘要

The growing adoption of Prefill-Decode (PD) disaggregation and Attention-Feed-Forward (AF) disaggregation has become a defining trend in large-scale LLM serving systems. These fine-grained disaggregation strategies expose the inherent heterogeneity of LLM inference-compute-bound prefill, memory- and KV-bound decode, communication-heavy attention, and GEMM-intensive feed-forward have been shown to substantially improve throughput and latency. However, fully realizing the benefits of deeper disaggregation requires stage-specialized hardware, and designing a dedicated accelerator for each disaggregated stage leads to prohibitive chip development cost and poor scalability as disaggregation granularity increases. Therefore, balancing performance and chip cost becomes an urgent problem. To address these challenges, this paper proposes a low-cost chip design methodology that employs a unified compute chiplet to build stage-specific chips for the disaggregated requirements of LLMs. A two-phase customization framework is introduced for the unified-compute-chiplet-based chip composition. The Phase-1 determines the best split level and the "perfect" split Pareto reference-chip sets over the global LLM disaggregation space. After that, Phase-2 synthesizes a unified compute chiplet and composes stage-specific chips with different memory/package configurations to approximate reference-chips. Based on two-phase framework, the unified-compute-chiplet-based stage-specific chips achieve an average (2.15×) performance boost over the LLM inference based on single type of chip design, and match the performance of fully customized reference-chip systems within ≈5%.

## 中文摘要

预填充解码 (PD) 分解和注意力前馈 (AF) 分解的日益普及已成为大规模 LLM 服务系统的决定性趋势。这些细粒度的分解策略暴露了 LLM 推理计算绑定预填充、内存和 KV 绑定解码、通信密集型注意力和 GEMM 密集型前馈的固有异构性，这些策略已被证明可以显着提高吞吐量和时延。然而，充分实现更深层次分解的好处需要阶段专用的硬件，并且为每个分解阶段设计专用加速器会导致芯片开发成本过高，并且随着分解粒度的增加，可扩展性较差。因此，平衡性能和芯片成本成为迫在眉睫的问题。为了应对这些挑战，本文提出了一种低成本芯片设计方法，该方法采用统一的计算芯粒来构建特定阶段的芯片，以满足大语言模型的解耦需求。针对基于统一计算芯粒的芯片组合引入了两阶段定制框架。第一阶段确定全局 LLM 分解空间上的最佳分割级别和“完美”分割 Pareto 参考芯片集。之后，第二阶段综合一个统一的计算芯粒，并用不同的内存/封装配置组成特定阶段的芯片，以近似参考芯片。基于两阶段框架，基于统一计算芯粒的阶段专用芯片平均性能达到采用单一类型芯片的 LLM 推理系统的 2.15 倍，并且与完全定制的参考芯片系统的性能匹配在约5%以内。

## 中文关键词

大语言模型；阶段解耦设计；芯粒；设计空间探索；成本优化

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
