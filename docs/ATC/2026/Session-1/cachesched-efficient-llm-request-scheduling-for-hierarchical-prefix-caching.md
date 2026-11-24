# CacheSched: Efficient LLM Request Scheduling for Hierarchical Prefix Caching

**中文标题**：CacheSched：面向分层前缀缓存的高效 LLM 请求调度

**所属 Session**：[Session 1: LLM Inference I](index.md) · [ATC 2026](../index.md)

**作者**：Rilin Huang (Peking University), Junyi Shu (UCLA), Yaofeng Tu (Nanjing Branch of ZTE Corporation), Xin Jin (Peking University)

## 英文摘要
Stateful Large Language Model (LLM) applications heavily rely on prefix caching to eliminate redundant prefill computations. To support massive concurrency, modern serving engines deploy hierarchical, multi-tier caches that offload less-active prefixes from limited GPU memory to spacious host DRAM. However, existing multi-worker request schedulers typically route traffic based solely on the longest prefix match, ignoring the highly heterogeneous data transfer costs between cache tiers. This oversight causes severe cluster-level load imbalance and triggers frequent GPU pipeline stalls as workers wait for slow host-to-device data transfers. To resolve these inefficiencies, we propose CacheSched, a scheduling system tailored for multi-worker LLM serving with hierarchical prefix caching. CacheSched is driven by a lightweight analytic performance model that estimates batch execution and data transfer times. Building on this model, CacheSched introduces two key mechanisms: (1) a heterogeneity-adaptive routing algorithm that dispatches requests based on predicted prefill costs, successfully balancing cache tier locality with cluster-wide worker load, and (2) a dynamic batch-matching algorithm at the worker level, which restricts host-memory prefix loads to the predicted compute window of the active batch, reducing GPU pipeline stalls. Evaluations demonstrate that CacheSched increases overall serving throughput by up to 2.58× compared to state-of-the-art systems while satisfying strict Time-to-First-Token (TTFT) Service-Level Objectives (SLOs).

## 中文摘要
有状态的大语言模型（LLM）应用高度依赖前缀缓存来消除冗余的预填充计算。为支撑海量并发，现代服务引擎部署了分层的多级缓存，将活跃度较低的前缀从有限的 GPU 显存卸载到容量充裕的主机 DRAM 中。然而，现有的多 worker 请求调度器通常仅依据最长前缀匹配来路由流量，忽略了缓存层级之间高度异构的数据传输开销。这一疏漏造成严重的集群级负载不均衡，并且当 worker 等待缓慢的主机到设备数据传输时，会引发 GPU 流水线频繁停顿。为解决这些低效问题，我们提出 CacheSched，一个为采用分层前缀缓存的多 worker LLM 服务量身定制的调度系统。CacheSched 由一个轻量级分析性能模型驱动，该模型可估算批次执行时间与数据传输时间。在此模型基础上，CacheSched 引入两项关键机制：（1）一种异构自适应路由算法，它依据预测的预填充开销来分派请求，成功地在缓存层级局部性与集群范围的 worker 负载之间取得平衡；（2）一种 worker 级的动态批次匹配算法，它将主机内存中的前缀加载限制在活跃批次的预测计算窗口之内，从而减少 GPU 流水线停顿。评测表明，CacheSched 相比最先进的系统可将整体服务吞吐提升最高 2.58 倍，同时满足严格的 TTFT SLO。

## 英文关键词
Large Language Models, Prefix Cache, Request Scheduling

## 中文关键词
大语言模型，前缀缓存，请求调度

[返回 Session 1](index.md) · [返回 ATC 2026](../index.md)
