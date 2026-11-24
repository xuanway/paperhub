---
title: "Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding"
description: "SC 2025 · Machine Learning: Methods · Siqi Wang; Hailong Yang; Xuezhu Wang; Tongxuan Liu; Pengbo Wang; Yufan Xu; Xunin"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Towards Efficient LLM Inference via Collective and Adaptive Speculative Decoding

**中文标题：** 通过集合式自适应推测解码实现高效大语言模型推理

**所属 Session：** [Machine Learning: Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Siqi Wang; Hailong Yang; Xuezhu Wang; Tongxuan Liu; Pengbo Wang; Yufan Xu; Xuning Liang; Kejie Ma; Tianyu Feng; Xin You; Ruihao Gong; Rui Wang; Zhongzhi Luan; Yi Liu; Depei Qian

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap496&sess=sess183)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Efficient LLM inference remains challenging due to the autoregressive decoding process, which generates only one token at a time. Speculative decoding has been introduced to address the limitation by using small speculative models (SSMs) to speed up LLM inference. However, the low acceptance rate of SSMs and the high verification cost of LLMs prohibit further performance improvement. In this paper, we present Smurfs, an LLM inference system designed to accelerate LLM inference through collective and adaptive speculative decoding. Smurfs adopts a majority-voted mechanism that harnesses multiple SSMs to collaboratively predict LLM outputs in multi-task scenarios. It also decouples SSM speculation from LLM verification and uses a pipelined execution to reduce the latency of SSM speculation. Additionally, Smurfs proposes a mechanism to dynamically determine the optimal speculation length of SSM at runtime. The experimental results demonstrate the superiority of Smurfs in terms of inference

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
