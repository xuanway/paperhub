# Octopus: Unlocking SSD Parallelism for Sparse KVCache Retrieval

**中文标题**：Octopus：释放 SSD 并行性以加速稀疏 KVCache 检索

**所属 Session**：[Session 28: LLM Inference IV](index.md) · [ATC 2026](../index.md)

**作者**：Tuowei Wang (Tsinghua University), Liyun Chu (Tsinghua University), Ruwen Fan (Tsinghua University), Ju Ren (Tsinghua University)

## 英文摘要
The key-value (KV) cache has become the dominant contributor to memory consumption in large language model (LLM) inference. Although offloading KVCache from GPU high-bandwidth memory (HBM) to CPU DRAM alleviates device memory pressure, DRAM remains capacity-limited and costly for large, persistent workloads. Solid-state drives (SSDs) provide a cost-effective alternative, but naive SSD-based paging is fundamentally bandwidth-bound due to limited PCIe throughput and per-device bandwidth constraints. In this paper, we observe that KVCache activations in real-world workloads exhibit strong and stable correlations. We term this phenomenon KVCache Co-Activation, where accessing a KV entry is often accompanied by a recurring set of other KV entries. Leveraging this property, we present Octopus, an SSD-based KVCache offloading system that converts bandwidth-bound single-device access into parallel I/O across multiple SSDs. Specifically, Octopus clusters co-activated KV entries offline and distributes the resulting clusters across SSDs using graph-based placement with selective replication to maximize parallel bandwidth. At runtime, Octopus performs load-balanced cluster retrieval and dynamically adapts clustering and caching decisions to sustain high bandwidth utilization under evolving access patterns. Evaluations show that Octopus improves serving throughput by 1.42× and effective bandwidth utilization by 2.67×. The code is available at https://github.com/omnimind-ai/Octopus.

## 中文摘要
键值（KV）缓存已成为大语言模型（LLM）推理中内存消耗的主要来源。尽管将 KVCache 从 GPU 高带宽内存（HBM）卸载到 CPU DRAM 可缓解设备内存压力，但 DRAM 的容量仍然受限，且对于大规模持久化工作负载而言成本高昂。固态硬盘（SSD）提供了具有成本效益的替代方案，然而由于 PCIe 吞吐有限与单设备带宽约束，朴素的基于 SSD 的分页在根本上受制于带宽。本文观察到，真实工作负载中的 KVCache 激活呈现出强且稳定的相关性。我们将此现象称为 KVCache 共激活（Co-Activation），即访问某个 KV 条目时往往伴随一组反复出现的其他 KV 条目。利用这一特性，我们提出 Octopus，一个基于 SSD 的 KVCache 卸载系统，它将受带宽约束的单设备访问转化为跨多个 SSD 的并行 I/O。具体而言，Octopus 在离线阶段对共激活的 KV 条目进行聚类，并使用带选择性复制的基于图的放置策略将所得簇分布到各个 SSD 上，以最大化并行带宽。在运行时，Octopus 执行负载均衡的簇检索，并动态调整聚类与缓存决策，以在不断变化的访问模式下维持高带宽利用率。评估表明，Octopus 将服务吞吐提升 1.42×，有效带宽利用率提升 2.67×。代码见 https://github.com/omnimind-ai/Octopus。

## 英文关键词
Large Language Model Inference, KVCache Offloading, SSD Parallelism, Sparse KVCache Retrieval

## 中文关键词
大语言模型推理，KVCache 卸载，SSD 并行性，稀疏 KVCache 检索

## 代码与研究制品

- [code](https://github.com/omnimind-ai/Octopus)

[返回 Session 28](index.md) · [返回 ATC 2026](../index.md)
