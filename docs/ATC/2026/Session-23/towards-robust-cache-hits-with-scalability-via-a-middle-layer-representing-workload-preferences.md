# Towards Robust Cache Hits with Scalability via a Middle Layer Representing Workload Preferences

**中文标题**：通过表征负载偏好的中间层实现稳健缓存命中与可扩展性

**所属 Session**：[Session 23: Storage and OS Policies](index.md) · [ATC 2026](../index.md)

**作者**：Kunpeng Ding (University of Science and Technology of China), Jiangping Han (University of Science and Technology of China), Kaiping Xue (University of Science and Technology of China), Qiangqiang Wei (University of Science and Technology of China)

## 英文摘要
Cache effectiveness heavily depends on the eviction policy. Learning-based eviction policies have improved over heuristics by adapting to workload characteristics, but most existing designs still rely on static object utilities as learning targets, whose semantics remain fixed across workloads and may deviate from the optimal eviction objective, especially when their assumptions do not match the workload. Moreover, utility prediction is often placed on the critical eviction path, forcing the cache to wait for model inference before selecting a victim. This serial dependency raises scalability concerns under high-rate request arrivals. To address these limitations, we propose RSM, which achieves robust cache hits and scalable request processing via a workload-preference middle layer. Rather than learning a static object utility, our model learns how the current workload prioritizes different eviction-relevant features. We express this preference as a parameterized scoring formula over a concise set of representative features at the middle layer. The formula is simple enough to execute on every eviction, allowing the cache to select victims directly on the critical path without per-eviction model inference. The learned model is moved off the critical path and updates the middle layer intermittently to reflect the latest workload preferences, preserving eviction quality while improving scalability. Extensive simulations across 5,768 real-world traces show that RSM consistently outperforms state-of-the-art eviction policies in miss ratio without sacrificing heuristic-level throughput, and a Cachelib prototype confirms its practicality in production caches.

## 中文摘要
缓存有效性在很大程度上取决于淘汰策略。基于学习的淘汰策略通过适应负载特征而优于启发式方法，但大多数现有设计仍依赖静态的对象效用作为学习目标，其语义在不同负载之间保持不变，当假设与负载不匹配时可能偏离最优的淘汰目标。此外，效用预测常被置于关键的淘汰路径上，迫使缓存在选择牺牲对象之前等待模型推理。这种串行依赖在高请求到达率下引发可扩展性担忧。为解决这些局限，我们提出 RSM，它借助一个负载偏好中间层实现稳健的缓存命中与可扩展的请求处理。我们的模型不学习静态的对象效用，而是学习当前负载如何为不同的淘汰相关特征赋予优先级。我们把这种偏好表达为中间层上一组简洁的代表性特征之上的参数化评分公式。该公式足够简单，可在每次淘汰时执行，使缓存能够直接在关键路径上选择牺牲对象，而无需为每次淘汰进行模型推理。学习得到的模型被移出关键路径，并间歇性地更新中间层以反映最新的负载偏好，从而在提升可扩展性的同时保持淘汰质量。在 5,768 条真实世界 trace 上的大量仿真表明，RSM 在缺失率上持续优于最先进的淘汰策略，且不牺牲启发式级别的吞吐，Cachelib 原型也验证了其在生产缓存中的实用性。

## 英文关键词
Cache eviction policy, middle layer, workload preference

## 中文关键词
缓存淘汰策略，中间层，负载偏好

[返回 Session 23](index.md) · [返回 ATC 2026](../index.md)
