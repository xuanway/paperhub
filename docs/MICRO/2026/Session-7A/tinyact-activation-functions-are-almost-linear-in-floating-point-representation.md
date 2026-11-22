---
title: "TinyAct: Activation Functions are (Almost) Linear in Floating Point Representation"
description: "MICRO 2026 · Session 7A · TinyAct：激活函数在浮点表示中几乎是线性的"
tags:
  - "MICRO2026"
---

# TinyAct: Activation Functions are (Almost) Linear in Floating Point Representation

**中文标题：** TinyAct：激活函数在浮点表示中几乎是线性的

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Chris Kjellqvist, Mansi Choudhary, Ning Liang, Lisa Wu Wills

**来源：** MICRO 2026，pp. 2278–2292；[DOI](https://doi.org/10.1109/MICRO67795.2026.00157)

## 英文摘要

Activation functions and other nonlinear functions such as exponential, SiLU, GeLU, and tanh are fundamental to modern neural networks inference and training. While these operations constitute less than 1% of total FLOPs in transformer inference, their hardware implementations are disproportionately expensive: each evaluation requires either large lookup tables or multi-cycle floating-point pipelines, and they lie on the critical path of every layer. Due to their computational complexity, they have become a pipeline bottleneck in recent GPU architectures, motivating improvements to methods for area-efficient and low-latency evaluation of transcendental functions. Activation functions and other nonlinear functions such as exponential, SiLU, GeLU, and tanh are fundamental to modern neural networks inference and training. While these operations constitute less than 1% of total FLOPs in transformer inference, their hardware implementations are disproportionately expensive: each evaluation requires either large lookup tables or multi-cycle floating-point pipelines, and they lie on the critical path of every layer. Due to their computational complexity, they have become a pipeline bottleneck in recent GPU architectures, motivating improvements to methods for area-efficient and low-latency evaluation of transcendental functions. We introduce TinyAct, a hardware-efficient activation unit that reinterprets floating-point inputs in log space to approximate exponentiation using a single integer multiply-accumulate operation. Sigmoid-family activations (SiLU, GeLU, tanh) require only one additional floating-point multiply-accumulate. The implementation relies on very small lookup tables, achieves 5.19x lower area than traditional methods, and synthesizes cleanly at high clock rates, making it suitable for both high-throughput datacenter accelerators and resource-constrained edge devices. We show that our approximation framework unifies several classical floating-point tricks, including Schraudolph's method and the fast inverse square root, under a common theoretical foundation. Evaluations on BF16 and FP32 formats show 1.04% average error, and inference on Qwen3, Gemma-3, ViT, and Yolo v8 demonstrates that our approximations preserve model accuracy with no significant degradation (<0.1%). We evaluate training stability by fine-tuning and pre-training on Gemma-3 and demonstrate no tranining loss degradation during training.

## 中文摘要

激活函数和其他非线性函数（例如指数函数、SiLU、GeLU 和 tanh）是现代神经网络推理和训练的基础。虽然这些操作仅占 Transformer 推理中总 FLOP 的不到 1%，但它们的硬件实现非常昂贵：每次评估都需要大型查找表或多周期浮点管道，并且它们位于每一层的关键路径上。由于其计算复杂性，它们已成为近期 GPU 架构中的管道瓶颈，推动了超越函数的区域高效和低时延评估方法的改进。激活函数和其他非线性函数（例如指数函数、SiLU、GeLU 和 tanh）是现代神经网络推理和训练的基础。虽然这些操作仅占 Transformer 推理中总 FLOP 的不到 1%，但它们的硬件实现非常昂贵：每次评估都需要大型查找表或多周期浮点管道，并且它们位于每一层的关键路径上。由于其计算复杂性，它们已成为近期 GPU 架构中的管道瓶颈，推动了超越函数的区域高效和低时延评估方法的改进。我们引入了 TinyAct，一种硬件高效的激活单元，它重新解释对数空间中的浮点输入，以使用单个整数乘法累加运算来近似求幂。 Sigmoid 系列激活（SiLU、GeLU、tanh）仅需要一个额外的浮点乘法累加。该实现依赖于非常小的查找表，面积比传统方法小 5.19 倍，并以高时钟速率干净地综合，使其适用于高吞吐量数据中心加速器和资源受限的边缘设备。我们表明，我们的近似框架在共同的理论基础下统一了几种经典的浮点技巧，包括施劳道夫方法和快速逆平方根。对 BF16 和 FP32 格式的评估显示平均误差为 1.04%，对 Qwen3、Gemma-3、ViT 和 Yolo v8 的推断表明，我们的近似保留了模型精度，且没有明显下降 (<0.1%)。我们通过在 Gemma-3 上进行微调和预训练来评估训练稳定性，并证明训练期间没有训练损失退化。

## 中文关键词

人工智能加速器；近似计算；浮点算术；激活函数；注意力机制；边缘人工智能

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21995486](https://doi.org/10.5281/zenodo.21995486)

以上入口来自论文正文或 Artifact 附录。

## 来源核对说明

附录列出了归档 DOI，但具体仓库入口仍保留 TODO 字样；此处仅收录其归档地址。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
