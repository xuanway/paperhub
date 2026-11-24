---
title: "3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches"
description: "FAST 2025 · More Machine Learning · 过滤冗余训练请求并双向采样，把学习型淘汰策略的 CPU 开销较 HALP 降低 60.9%"
tags:
  - "FAST2025"
  - "More Machine Learning"
  - "cache eviction"
  - "learning-based policy"
---

# 3L-Cache: Low Overhead and Precise Learning-based Eviction Policy for Caches

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">学习型缓存淘汰能压低 miss ratio，但平均 CPU 开销可达 LRU 的 172.5 倍。3L-Cache 过滤冗余训练请求、动态调整训练频率，并用双向采样降低预测开销，在 4855 条 trace 上较 HALP 降 60.9%、较 LRB 降 94.9% CPU 开销，仅为 LRU 的 6.4 倍与 3.4 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · More Machine Learning</p>
</div>

**中文标题**：3L-Cache：低开销且精确的缓存学习型淘汰策略

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/zhou-wenbin](https://www.usenix.org/conference/fast25/presentation/zhou-wenbin)

**论文 PDF**：[fast25-zhou-wenbin.pdf](https://www.usenix.org/system/files/fast25-zhou-wenbin.pdf)

**作者**：Wenbin Zhou（Beijing University of Technology）；Zhixiong Niu、Yongqiang Xiong（Microsoft Research）；Juan Fang、Qian Wang（Beijing University of Technology）

**会议**：FAST 2025 · Santa Clara, CA · 第 237–254 页

**Session**：More Machine Learning · 2025-02-26 09:00–10:20 · Chair：Ali R. Butt（Virginia Tech）

**所属 Session**：[More Machine Learning](index.md) · [FAST 2025](../index.md)

**关键词**：cache eviction, learning-based policy, object miss ratio, byte miss ratio, CPU overhead

---

## 英文摘要

Caches can effectively reduce request latency and network traffic, with the eviction policy serving as a core component. The effectiveness of an eviction policy is measured by both the byte miss ratio and the object miss ratio. To reduce these miss ratios, various learning-based policies have been proposed. However, the substantial computation overhead introduced by learning limits their deployment in production systems.

This work presents 3L -Cache, an object-level learning policy with L ow computation overhead, while achieving the L owest object miss ratio and the L owest byte miss ratio among learning-based policies. To reduce overhead, we introduce two key advancements. First, we propose an efficient training data collection scheme that filters out unnecessary historical cache requests and dynamically adjusts the training frequency without compromising accuracy. Second, we design a low-overhead eviction method that integrates a bidirectional sampling policy to prioritize unpopular objects and an efficient eviction strategy to effectively select evicted objects. Furthermore, we incorporate a parameter auto-tuning method to enhance adaptability across traces.

We evaluate 3L-Cache in a testbed using 4855 traces. The results show that 3L-Cache reduces the average CPU overhead by 60.9% compared to HALP and by 94.9% compared to LRB. Additionally, 3L-Cache incurs only 6.4× the average overhead of LRU for small cache sizes and 3.4× for large cache sizes, while achieving the best byte miss ratio or object miss ratio among twelve state-of-the-art policies.

## 中文摘要

缓存能有效降低请求延迟与网络流量，其中淘汰策略是核心组件；淘汰策略的效果由 byte miss ratio 与 object miss ratio 共同衡量。为降低这两个指标，已有多种学习型策略被提出，但学习带来的可观计算开销限制了它们在生产系统中的部署。3L-Cache 是一种对象级学习型淘汰策略，具有低计算开销，同时在所有学习型策略中取得最低的 object miss ratio 与最低的 byte miss ratio。为降低开销，本文引入两项关键改进：第一，提出高效的训练数据收集方案，过滤掉不必要的历史缓存请求，并在不损害精度的前提下动态调整训练频率；第二，设计低开销的淘汰方法，结合双向采样策略优先处理不受欢迎的对象，并用高效的淘汰策略有效选出被淘汰对象。此外，本文加入参数自动调优方法，以增强跨 trace 的适应性。本文在测试床上用 4855 条 trace 评估 3L-Cache。结果表明，3L-Cache 的平均 CPU 开销较 HALP 降低 60.9%、较 LRB 降低 94.9%；小缓存下其平均开销仅为 LRU 的 6.4 倍、大缓存下为 3.4 倍，同时在十二种最先进策略中取得最优的 byte miss ratio 或 object miss ratio。

## 一句话总结

> 三个 L 的关键不在模型更聪明，而在砍掉训练浪费与预测浪费：训练频率降一个量级，采样只挑冷对象。

## 研究背景与问题

- **开销是落地门槛**：淘汰策略决定哪些数据留在缓存里，学习型策略能同时压低 byte miss ratio 与 object miss ratio，但平均计算开销可达 LRU 的 172.5 倍；CDN 这类动辄成百上千台服务器的部署场景，把 LRU 换成学习型策略的成本难以承受。
- **三类学习策略各有短板**：policy-level 学习（LeCaR、CACHEUS）受强化学习对负载变化的滞后适应拖累；group-level 学习（GL-Cache）依赖分组方式与组效用定义，只在少数 trace 上有效，byte miss ratio 甚至高于 LRU；object-level 学习（LRB、HALP、Raven、Parrot）miss ratio 最好，但细粒度训练与预测让它开销最高。
- **开销集中在两处**：对 LRB 与 HALP 的剖析显示，训练与预测合计占总开销的 70%，且两者占比随缓存大小翻转——小缓存 miss 多、预测频繁，预测成为主要开销；缓存变大后预测次数下降，训练成为主要开销。
- **已有削减手段缺精度保证**：降低训练频率能显著省开销，但合适频率随 trace 与对象特征漂移；随机采样无法保证候选集中有足够冷对象，淘汰比提不上去；固定参数难以跨 trace 泛化。

## 核心贡献

- **三维度统一评测**：首次把代表性淘汰策略（启发式与学习型）放在 byte miss ratio、object miss ratio 与计算开销三个维度上比较，指出没有策略能同时占优。
- **训练数据收集方案**：过滤不必要的历史缓存请求并动态调整训练频率，在不损失模型精度的前提下削掉训练侧的算力浪费。
- **低开销淘汰方法**：用双向采样（bidirectional sampling）提高候选集中冷对象的比例，配合高效淘汰策略确定淘汰比并快速选出被淘汰对象。
- **参数自动调优**：为每条 trace 以低开销选取参数，提升跨 trace 适应性；并验证该设计可移植到其他对象级策略（如 LRB）。

## 方法与技术要点

- **训练频率按需伸缩**：不再固定每百万请求训练多少次，而是由训练数据收集模块筛掉冗余历史请求、按需调整训练频率。剖析显示 LRB 原本每百万请求训练 23 次，降到 2–3 次时 miss ratio 几乎不变，开销则明显下降。
- **双向采样抬高淘汰比**：把淘汰比（eviction ratio）定义为预测候选中真正可被淘汰的对象占比，比例越高则预测开销越低；双向采样让候选集更多落在冷对象区域，从而在 miss ratio 不退化的情况下提高该比例。
- **高效对象淘汰**：候选数量很大时仍需定下淘汰比并快速定位被淘汰对象，避免对大候选集逐个比较带来的额外开销。
- **参数自动调优**：针对 trace 差异自动搜索参数取值，避免人工调参在部分 trace 上失效。
- **实现与可移植性**：在测试床上实现完整策略并与十一种策略对比，代码开源；设计可叠加到其他对象级策略，论文将其应用于 LRB。

## 评估与主要结果

- **评测设置**：单机测试床，4855 条 trace 来自八个公开数据集，覆盖 footprint 的 0.1% 与 10% 两种缓存大小，对比六种启发式与五种学习型策略。
- **CPU 开销**：平均开销较 HALP 降低 60.9%、较 LRB 降低 94.9%；小缓存下为 LRU 的 6.4 倍、大缓存下为 3.4 倍，而 LRB 为 172 倍与 58 倍、HALP 为 23 倍与 10 倍。
- **miss ratio**：在十二种先进策略中取得最优的 byte miss ratio 或 object miss ratio；对比之下 GL-Cache 的 byte miss ratio 反而高于 LRU，LeCaR 的 object miss ratio 在学习型策略中最高。
- **可移植与原型**：把同一套设计加到 LRB 上，CPU 开销降低 80%、byte miss ratio 再降 0.6%；原型在 219GB 工作集的 Tencent CBS trace 上完成验证。

## 代码与研究制品

- [代码仓库](https://github.com/optiq-lab/3L-Cache)

[返回 More Machine Learning](index.md) · [返回 FAST 2025](../index.md)
