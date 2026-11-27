---
title: "TENET-v2: Applying Relation-centric Notation to Model and Optimize Data Swizzle in the Cache of Modern NPU"
description: "HPCA 2026 · Caching and Prefetching"
tags:
  - "HPCA2026"
  - "Caching and Prefetching"
---

# TENET-v2: Applying Relation-centric Notation to Model and Optimize Data Swizzle in the Cache of Modern NPU

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Caching and Prefetching。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Caching and Prefetching</p>
</div>

**论文链接**：
**作者**：Hanyu Zhang Zhejiang University , Fangxu Guo Zhejiang University , Liqiang Lu Zhejiang University , Long Wang Huawei Technologies , Yunfei Du Huawei Technologies , Zhe Wang Huawei Technologies , Jinghan Zhang Huawei Technologies , Jie Zhang Peking University , Chenli Xue Zhejiang University , Chengpeng Wu Zhejiang University , Ziyi Zhang Zhejiang University , Yun Liang Peking University , Size Zheng Tsinghua University , Jianwei Yin Zhejiang University
**会议**：HPCA 2026

---

## 中文标题

TENET-v2：用关系中心记号建模与优化现代 NPU 缓存中的数据 swizzle

## 英文摘要

Swizzle is a data access pattern optimization technique by reorganizing the execution order of computational tasks to improve the cache locality in modern NPUs. Existing analysis and optimization techniques lack support for swizzle-aware modeling on NPUs and fail to effectively capture cache behavior across diverse swizzle configurations. To this end, we propose TENET-v2, a framework for modeling and optimizing swizzle. We introduce a relation-centric notation to characterize different cache access patterns, thus exploring wider swizzle space. Then, we propose a hybrid performance model for cache analysis. The proposed performance model uses an analytical approach to quantify cache miss behavior under unsaturated cache conditions (non-saturated misses), and employs a simulation method combined with an early exiting mechanism to rapidly model cache behavior under saturated cache conditions (saturated misses). Experimental evaluations demonstrate that TENET-v2 achieves an average absolute error of 1.05% in read hit rate compared to real-world hardware. Evaluation on a variety of DNNs shows that TENET-v2 outperforms existing tensor program optimizers by up to 1.5× on A100 GPUs. We also demonstrate NPU cache size optimization based on TENET-v2.

## 中文摘要

Swizzle 是一种数据访问模式优化技术，通过重排计算任务的执行顺序来改善现代 NPU 中的缓存局部性。现有的分析与优化技术缺乏对 NPU 上 swizzle 感知建模的支持，也无法有效刻画不同 swizzle 配置下的缓存行为。为此，我们提出 TENET-v2，一个用于建模与优化 swizzle 的框架。我们引入关系中心记号来刻画不同的缓存访问模式，从而探索更广阔的 swizzle 空间。随后，我们提出用于缓存分析的混合性能模型。该模型采用解析方法量化缓存未饱和条件下的缓存缺失行为（非饱和缺失），并采用结合提前退出机制的仿真方法快速建模缓存饱和条件下的缓存行为（饱和缺失）。实验评估表明，TENET-v2 相比真实硬件在读命中率上的平均绝对误差为 1.05%。在多种 DNN 上的评估显示，TENET-v2 在 A100 GPU 上比现有张量程序优化器最高快 1.5 倍。我们还展示了基于 TENET-v2 的 NPU 缓存容量优化。
