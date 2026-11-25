DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training
Authors：
[Maoyang Xiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=59411148737464959301)，[Bo Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=246843)

## 中文标题

DAPA：面向端侧 Transformer 推理与训练的分布感知分段激活函数

## 英文摘要

Non-linear activation functions play a pivotal role in on-device inference and training, as they not only consume substantial hardware resources but also impose a significant impact on system performance and energy efficiency. In this work, we propose Distribution-Aware Piecewise Activation (DAPA), a differentiable and hardware-friendly activation function for Transformer architectures by exploiting the distribution of pre-activation data. DAPA employs a non-uniform piecewise approximation that allocates finer segments to high-probability regions of the distribution, improving generalizability over prior piecewise linear methods. The resulting approximation is further quantized using Distribution-Weighted Mean Square Error to reduce latency and resource utilization for hardware deployment. Our HLS implementation demonstrates that DAPA speeds up GELU computation by 16× and decreases DSP utilization by 16× while maintaining comparable or better performance across vision Transformers and GPT-2 models.

## 中文摘要

非线性激活函数在端侧推理与训练中起着关键作用，它们不仅消耗大量硬件资源，还会显著影响系统性能与能效。本文利用预激活数据的分布特性，提出分布感知分段激活（DAPA），一种面向 Transformer 架构的可微且硬件友好的激活函数。DAPA 采用非均匀分段近似，将更细的分段分配给分布的高概率区域，相比已有的分段线性方法具有更好的泛化能力。所得近似进一步采用分布加权均方误差进行量化，以降低硬件部署时的延迟与资源占用。我们的 HLS 实现表明，DAPA 将 GELU 计算加速 16×，并将 DSP 占用降低 16×，同时在多种视觉 Transformer 与 GPT-2 模型上保持相当或更优的性能。

## 英文关键词

Activation Function, Distribution, Piecewise Linear Approximation

## 中文关键词

激活函数、分布、分段线性近似
