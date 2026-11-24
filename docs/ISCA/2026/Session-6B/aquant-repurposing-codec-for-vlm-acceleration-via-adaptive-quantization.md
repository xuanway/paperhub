---
title: "AQuant: Repurposing CODEC for VLM Acceleration via Adaptive Quantization"
description: "ISCA 2026 · Session 6B · AQuant: Repurposing CODEC for VLM Acceleration via Adaptive Quantization"
tags:
  - "ISCA2026"
  - "Session 6B"
  - "Deep Learning / Memory Acceleration"
---

# AQuant: Repurposing CODEC for VLM Acceleration via Adaptive Quantization

**中文标题：** AQuant: 通过自适应量化复用 CODEC 加速 VLM

**所属 Session：** [Session 6B](index.md) · [ISCA 2026](../index.md)

**作者：** Zhuoran Song, Chunyu Qi, Jian Weng, Xiaoyao Liang, Haibing Guan

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Vision-Language Models (VLMs) have reached the forefront of accuracy in various vision understanding tasks. Despite their remarkable success, the computing costs of VLMs scale significantly with the high image resolutions or the increasing number of video frames that need to be processed, posing substantial challenges for deployment to real-time applications. Although specialized quantization accelerators have been developed, they may not be the optimal solutions due to their neglect of the inherent data similarity within VLMs. Additionally, the use of floating-point units for floating-point to integer conversion introduces non-negligible hardware overhead. This paper introduces Adaptive Quantization (AQuant), an algorithm-hardware co-design framework that repurposes the CODEC to accelerate VLM inference in an end-to-end and unified manner. AQuant leverages the inherent similarities in visual tokens, exploiting them for differential value (delta) generation, which is well-suited for dynamic quantization due to its narrower distribution. To eliminate the expensive floating-point similarity detection, AQuant integrates an exponent-based similarity detection operation. On the hardware side, we enhance the video CODEC’s capabilities to efficiently implement exponent-similarity detection and adaptive quantization. The framework also incorporates a Neural Processing Unit (NPU) with mixed-precision support, which collaborates closely with the CODEC to translate algorithmic savings into real speedup. Experimental results show that AQuant achieves speedups of 4.5×, 2.8×, and 6.9× over state-of-the-art accelerators, such as LLM.265, CMC, and Xavier AGX GPU, with negligible accuracy loss.

## 中文摘要

视觉-语言模型（VLM）已在各类视觉理解任务的精度上达到前沿水平。尽管取得了显著成功，VLM 的计算成本会随图像分辨率提高或待处理视频帧数增加而显著增长，给部署到实时应用带来巨大挑战。虽然已开发出专用量化加速器，但由于它们忽视了 VLM 中固有的数据相似性，可能并非最优方案。此外，使用浮点单元进行浮点到整数的转换会引入不可忽视的硬件开销。本文提出自适应量化（AQuant），一个算法-硬件协同设计框架，以端到端、统一的方式复用 CODEC 来加速 VLM 推理。AQuant 利用视觉令牌中固有的相似性进行差分值（delta）生成，由于其分布更窄，非常适合动态量化。为消除昂贵的浮点相似性检测，AQuant 集成了基于指数的相似性检测操作。在硬件方面，我们增强了视频 CODEC 的能力，以高效实现指数相似性检测和自适应量化。该框架还集成了一个支持混合精度的神经网络处理器（NPU），与 CODEC 紧密协作，将算法上的节省转化为实际的加速。实验结果表明，AQuant 相比 LLM.265、CMC 和 Xavier AGX GPU 等最先进加速器分别实现 4.5 倍、2.8 倍和 6.9 倍加速，且精度损失可忽略不计。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2026](../index.md)
