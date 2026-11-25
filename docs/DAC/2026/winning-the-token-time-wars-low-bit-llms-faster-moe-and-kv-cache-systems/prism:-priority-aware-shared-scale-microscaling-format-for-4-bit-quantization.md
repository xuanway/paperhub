PRISM: Priority Aware Shared Scale Microscaling Format for 4-Bit Quantization
Authors：
[Dongyoung Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=96532902272167684651)，[Seokjin Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=279778477217232982)，[Yiran Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=712143)，[Ik Joon Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=628143)

## 中文标题

PRISM：一种面向 4 比特量化的优先级感知共享缩放微缩放格式

## 英文摘要

Microscaling formats have emerged as prominent candidates for 4-bit quantization of modern AI models due to its fine-grained group-wise quantization granularity. However, such format still exhibit fundamental accuracy degradations. In particular, MXFP4 and NVFP4 are limited by fixed shared-scale precision, and NVFP4 further cannot cover the full value range without an added FP32 scale. This paper presents PRISM, a Microscaling format with a single 8-bit encoded group level shared scale that adaptively allocates shared scale’s representation based on the relative importance of values. Through our evaluation, PRISM surpasses conventional Microscaling format accuracy with only 0.62% area and 0.86% energy overhead.

## 中文摘要

得益于细粒度的分组量化粒度，微缩放（Microscaling）格式已成为现代 AI 模型 4 比特量化的重要候选方案。然而，此类格式仍存在根本性的精度退化问题。具体而言，MXFP4 与 NVFP4 受限于固定的共享缩放精度，且 NVFP4 在不额外引入 FP32 缩放的情况下无法覆盖完整的数值范围。本文提出 PRISM，一种采用单一 8 比特编码的组级共享缩放的微缩放格式，可依据数值的相对重要性自适应地分配共享缩放的表示。经评估，PRISM 仅以 0.62% 的面积与 0.86% 的能耗开销即超越了传统微缩放格式的精度。
