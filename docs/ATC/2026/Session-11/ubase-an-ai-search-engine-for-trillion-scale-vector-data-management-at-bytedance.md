# UBASE: An AI Search Engine for Trillion-Scale Vector Data Management at ByteDance

**中文标题**：UBASE：面向字节跳动万亿规模向量数据管理的 AI 搜索引擎

**官方议程标题**：UBASE: An AI Search Engine for Trillion-Scale Vector Data Management

**所属 Session**：[Session 11: Search, Recommender and Graph Systems](index.md) · [ATC 2026](../index.md)

**作者**：Yao Tian (Bytedance), Yuncheng Lu (Bytedance), Liyao Xiong (Bytedance), Yuming Xu (ByteDance), Hao Zhang (Bytedance), Weichen Zhao (Bytedance), Xi Zhao (ByteDance), Bo Kuang (ByteDance), Dongyu Wang (ByteDance), Jiehui Li (ByteDance), Yakun Li (ByteDance), Lei Zhang (ByteDance)

## 英文摘要
Since 2016, UBASE has been the foundation of ByteDance’s search infrastructure, scaling to more than 7,000 clusters and 300 PB of indexed data. Driven by the demands of AI workloads, UBASE has evolved from a text search engine into a unified AI search system supporting vector retrieval, lexical matching, and predicate filtering. Its largest deployment indexes nearly one trillion high-dimensional vectors. This scale exposes two central bottlenecks in AI-era retrieval: memory-intensive graph-index construction under sustained ingestion, and the prohibitive cost of keeping vector indexes entirely in memory. UBASE addresses these bottlenecks with two techniques. First, it introduces a quantization-aware vector kernel based on SymRaBitQ, a new symmetric quantization scheme with theoretical analysis that allows index construction to run directly in the quantized space accurately and efficiently without retaining a copy of full-precision vectors. Second, it provides a hybrid storage engine that supports memory-resident, hybrid, and SSD-resident deployments, with fine-grained record-level caching to trade memory for latency under operational control. On large-scale benchmarks, UBASE improves throughput by up to 3×, reduces indexing memory by 80%, and lowers serving cost ($/QPS) by up to 99.4% compared to prior systems, while supporting trillion-vector scale, write-heavy or latency-sensitive workloads in production.

## 中文摘要
自 2016 年以来，UBASE 一直是字节跳动搜索基础设施的基石，已扩展到 7000 多个集群和 300 PB 的索引数据。在 AI 负载需求的驱动下，UBASE 已从文本搜索引擎演进为支持向量检索、词法匹配和谓词过滤的统一 AI 搜索系统。其最大的部署索取了近一万亿条高维向量。这一规模暴露出 AI 时代检索的两个核心瓶颈：在持续写入下内存密集型图索引的构建，以及将向量索引完全保留在内存中所带来的高昂成本。UBASE 通过两项技术应对这些瓶颈。第一，它引入了基于 SymRaBitQ 的量化感知向量内核，SymRaBitQ 是一种新的对称量化方案，并给出了理论分析，使索引构建能够直接在量化空间中准确、高效地进行，而无需保留全精度向量的副本。第二，它提供了一种混合存储引擎，支持内存驻留、混合以及 SSD 驻留的部署形态，并具备细粒度记录级缓存，可在运维可控的前提下以内存换取延迟。在大规模基准上，相比此前系统，UBASE 最高提升 3 倍吞吐，将索引内存降低 80%，并把服务成本（$/QPS）最多降低 99.4%，同时在生产环境中支持万亿向量规模以及写密集或延迟敏感的负载。

## 英文关键词
Vector Search, AI Search Engine, Large-Scale Indexing

## 中文关键词
向量检索，AI 搜索引擎，大规模索引

[返回 Session 11](index.md) · [返回 ATC 2026](../index.md)
