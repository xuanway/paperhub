---
title: "Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding"
description: "SC 2025 · Machine Learning: Methods · Siqi Wang; Hailong Yang; Xuezhu Wang; Tongxuan Liu; Pengbo Wang; Yufan Xu; Xunin"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Siqi Wang; Hailong Yang; Xuezhu Wang; Tongxuan Liu; Pengbo Wang; Yufan Xu; Xuning Liang; Kejie Ma; Tianyu Feng; Xin You; Ruihao Gong; Rui Wang; Zhongzhi Luan; Yi Liu; Depei Qian

**会议**：SC 2025 · St. Louis, MO

## 摘要

Efficient LLM inference remains challenging due to the autoregressive decoding process, which generates only one token at a time. Speculative decoding has been introduced to address the limitation by using small speculative models (SSMs) to speed up LLM inference. However, the low acceptance rate of SSMs and the high verification cost of LLMs prohibit further performance improvement. In this paper, we present Smurfs, an LLM inference system designed to accelerate LLM inference through collective and adaptive speculative decoding. Smurfs adopts a majority-voted mechanism that harnesses multiple SSMs to collaboratively predict LLM outputs in multi-task scenarios. It also decouples SSM speculation from LLM verification and uses a pipelined execution to reduce the latency of SSM speculation. Additionally, Smurfs proposes a mechanism to dynamically determine the optimal speculation length of SSM at runtime. The experimental results demonstrate the superiority of Smurfs in terms of inference

---

## 一句话总结

> 该工作属于 Machine Learning: Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Methods 领域贡献新的设计范式或评估框架。
