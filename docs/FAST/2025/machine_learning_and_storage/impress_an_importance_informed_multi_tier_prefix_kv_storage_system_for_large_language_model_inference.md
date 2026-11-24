---
title: "IMPRESS: An Importance-Informed Multi-Tier Prefix KV Storage System for Large Language Model Inference"
description: "FAST 2025 · Machine Learning and Storage · 只加载重要前缀 KV 的三层 KV 存储，TTFT 最多缩短至 1/2.8"
tags:
  - "FAST2025"
  - "Machine Learning and Storage"
  - "prefix KV cache"
  - "KV cache reuse"
---

# IMPRESS: An Importance-Informed Multi-Tier Prefix KV Storage System for Large Language Model Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">前缀 KV 落到磁盘后，SSD 到 GPU 的 I/O 可占 TTFT 的 51%-98%，复用前缀未必更快。IMPRESS 利用同层各注意力头重要 token 索引高度相似的规律，只读少量 probe head 的 key 定位重要 KV，把 TTFT 最多缩短至 1/2.8。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Machine Learning and Storage</p>
</div>

**中文标题**：IMPRESS：面向大语言模型推理的重要性感知多层前缀 KV 存储系统

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/chen-weijian-impress](https://www.usenix.org/conference/fast25/presentation/chen-weijian-impress)

**论文 PDF**：[fast25-chen-weijian-impress.pdf](https://www.usenix.org/system/files/fast25-chen-weijian-impress.pdf)

**作者**：Weijian Chen、Shuibing He、Haoyang Qu、Ruidong Zhang、Siling Yang、Ping Chen（Zhejiang University）；Yi Zheng、Baoxing Huai（Huawei Cloud）；Gang Chen（Zhejiang University）

**会议**：FAST 2025 · Santa Clara, CA · 第 187–201 页

**Session**：Machine Learning and Storage · 2025-02-25 15:50–17:30 · Chair：Kan Wu（Google）

**所属 Session**：[Machine Learning and Storage](index.md) · [FAST 2025](../index.md)

**关键词**：prefix KV cache, KV cache reuse, multi-tier storage, TTFT, attention head similarity, cache management

---

## 英文摘要

Modern advanced large language model (LLM) applications often prepend long contexts before user queries to improve model output quality. These contexts frequently repeat, either partially or fully, across multiple queries. Existing systems typically store and reuse the keys and values of these contexts (referred to as prefix KVs) to reduce redundant computation and time to first token (TTFT). When prefix KVs need to be stored on disks due to insufficient CPU memory, reusing them does not always reduce TTFT, as disk I/O latency is high. In this paper, we propose IMPRESS, an importance-informed multi-tier prefix KV storage system to reduce I/O delay for LLM inference by only loading important prefix KVs.

IMPRESS first leverages the insight that there is significant similarity in important token index sets across attention heads and introduces an I/O-efficient important KV identification algorithm. It then optimizes prefix KV storage and caching through importance-informed KV management, reducing TTFT during model inference. Our experimental results show that IMPRESS can reduce TTFT by up to 2.8× compared to state-of-the-art systems, while maintaining comparable inference accuracy.

## 中文摘要

现代 LLM 应用常在查询前拼接长上下文以提升输出质量，这些上下文在多次查询间往往部分或完全重复。已有系统存储并复用其 key 与 value（前缀 KV）以减少冗余计算、降低首 token 延迟（TTFT）。但当 CPU 内存不足、前缀 KV 落到磁盘时，磁盘 I/O 延迟很高，复用并不总能缩短 TTFT。

IMPRESS 是重要性感知的多层前缀 KV 存储系统，只加载重要的前缀 KV 以压缩 I/O 延迟。它利用不同注意力头之间重要 token 索引高度相似这一观察，设计了 I/O 高效的重要 KV 识别算法；再以重要性感知的 KV 管理优化存储与缓存。实验表明，它的 TTFT 最多降低 2.8 倍（即缩短至原来的 1/2.8），同时保持相当的推理精度。

## 一句话总结

> 同层各注意力头的重要 token 索引高度重合，因此只读少量 probe head 的 key 就能挑出该加载的前缀 KV。

## 研究背景与问题

- **长前缀换质量却拉长延迟**：应用在查询前拼接检索文档、历史对话或少样本示例等上下文，Chameleon 这类系统会追加 2,600 余个 token，相对约 750 token 的常见查询把请求长度放大 4 倍以上，使 OPT-30B 的 TTFT 拉长 9 倍。
- **缓存空间不够用**：已有系统多把前缀 KV 只放在 GPU 或 CPU 内存，长序列与大 batch 下很快耗尽；一块 2,600 token 的前缀 KV 在中等规模 OPT-30B 上就要占 3.4 GB。
- **放到磁盘又被 I/O 卡住**：AttentionStore 把前缀 KV 扩到磁盘并按调度器预测预取，但 SSD 到 GPU 的 I/O 延迟几乎无法被查询计算掩盖，实测占 TTFT 的 51%-98%，在预抢占调度下更难预测未来请求。
- **选择性加载引入新问题**：研究显示部分 token 的 KV 对输出更关键，丢弃次要 KV 仍可保持相近质量；但逐查询判定重要性要把全部 key 读进 GPU，而按 chunk 组织存储又会把重要 KV 与无关数据绑在一起。

## 核心贡献

- **三层前缀 KV 存储系统**：融合 GPU 内存、CPU 内存与磁盘三层，以重要性为指导，只加载重要的前缀 KV 以减少慢速磁盘 I/O。
- **相似性引导的重要 token 识别**：利用同一层内不同注意力头的重要 token 索引高度相似这一观察，只加载部分头（probe head）的 key 就能判定整个前缀中的重要 KV，避免全量读 key。
- **重要性感知的 KV 管理**：用 KV 重排序把前缀 KV 在磁盘上重新排序打包，提高 chunk 内重要 KV 的密度；并引入按分数的缓存管理策略替代只看 chunk 访问模式的策略。
- **实现与评估**：在 6.7B 到 30B 的三个模型、四个数据集上评估，验证降 I/O 与保精度可以同时成立。

## 方法与技术要点

- **三层与预取**：GPU 内存与 CPU 内存作为磁盘数据之上的缓存层，新请求到来时异步预取前缀 KV，以缩短 prefill 阶段的首 token 延迟；系统只针对 prefill 阶段，不改变 decoding。
- **以少量头换 I/O**：识别算法不再把全部 key 读进 GPU 算注意力分数，而是只读 probe head 的 key，据此推断覆盖全前缀的重要 token 索引集合。
- **存储重排**：KV 重排序异步按重要性排序并把 token 重新打包写回磁盘，chunk 元数据中增加重排后的 token 位置映射表，使一次读盘带上的重要 KV 更密集。
- **分数化缓存**：为每个 chunk 维护一个体现其内部 KV 重要性的分数，避免重要 KV 密集的 chunk 被放在慢速层，从而提升有效缓存命中率。
- **副作用的抑制**：probe head 的 key 单独冗余存放，读取时不必带入其他头的数据；重排序在关键路径之外执行，不干扰 TTFT。

## 评估与主要结果

- **主结果**：相比最先进的前缀 KV 存储系统（AttentionStore 结合 H2O 与 LFU 的组合），IMPRESS 的 TTFT 最多缩短至 1/2.8、I/O 时间最多缩短至 1/3.8，推理精度下降小于 0.2%。
- **模型覆盖**：在 6.7B-30B 的三个模型与四个数据集上验证；在 Llama2-7B 与 Llama2-13B 的 PIQA、COPA 任务上取得 1.7-2.7 倍加速。
- **时间开销**：相似性引导的识别只读少量 probe head 的 key，平均仅占系统开销的 6%；KV 重排序异步执行，总耗时不到 1 分钟且不在关键路径上。
- **空间开销**：64 token 的 chunk 下，位置映射表与每 chunk 分数合计不到 chunk 内存的 0.5%；probe head key 的冗余存储占全部前缀 KV 存储的 1.2%。

[返回 Machine Learning and Storage](index.md) · [返回 FAST 2025](../index.md)
