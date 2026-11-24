# Axon: Asynchronous Global KV-Aware Scheduling Across Distributed Instances for Agentic Workloads

**中文标题**：Axon：面向智能体负载的跨分布式实例异步全局 KV 感知调度

**所属 Session**：[Session 22: Large-scale AI](index.md) · [ATC 2026](../index.md)

**作者**：Yuqi Qiu (University of Macau), Jinting Zou (University of Macau), Zizhao Mo (Great Bay University and University of Macau), Junlin Chen (University of Macau), Liao Chen (University of Macau, Macau SAR, China), Huanle Xu (University of Macau), Guoyao Xu (Alibaba Group), Guodong Yang (Alibaba Group), Liping Zhang (Alibaba Group), ChengZhong Xu (University of Macau)

## 英文摘要
Large language model (LLM) applications are increasingly moving toward agentic workflows, where models interact with users and tools over many turns, causing context lengths to dominate sequence composition and accumulate across dozens of turns. Existing serving systems fail to address this setting because they often overlook the reuse of KV caches across distributed instances within a cluster. We present Axon, an asynchronous global serving architecture that treats distributed GPU HBM as a unified KV cache resource pool for multi-turn agentic workloads. Axon introduces Asymmetric Query Context Parallelism to distribute attention over context shards across instances by communicating only query tensors, eliminating the synchronization bubbles and heavy KV traffic of conventional sequence-parallel designs. Its fully asynchronous scheduler decouples new-request allocation, KV cache restoration, and batch preparation from GPU execution, leveraging aggregated PCIe bandwidth to restore missing fragments in parallel, while a context-locality-aware scheduling policy jointly optimizes cache hit ratio and per-instance load. Evaluation on production agent traces shows that Axon reduces prefill latency by up to 4.14×, decode latency by 1.87×, and end-to-end latency by 2.27× compared to existing systems.

## 中文摘要
大语言模型（LLM）应用正日益转向智能体化工作流，模型在此类工作流中与用户和工具进行多轮交互，使得上下文长度在序列构成中占据主导地位，并在数十轮交互中不断累积。现有服务系统未能应对这一场景，因为它们往往忽视了集群内跨分布式实例的 KV 缓存复用。我们提出 Axon，一种异步全局服务架构，将分布式 GPU HBM 视为面向多轮智能体负载的统一 KV 缓存资源池。Axon 引入非对称查询上下文并行，通过仅通信 query 张量把注意力分布到各实例上的上下文分片，从而消除传统序列并行设计中的同步气泡与大量 KV 流量。其全异步调度器将新请求分配、KV 缓存恢复与批次准备同 GPU 执行解耦，利用聚合的 PCIe 带宽并行恢复缺失片段；同时，上下文局部性感知的调度策略联合优化缓存命中率与各实例负载。在生产智能体 trace 上的评估表明，与现有系统相比，Axon 将预填充延迟最多降低 4.14×，解码延迟降低 1.87×，端到端延迟降低 2.27×。

## 英文关键词
LLM Serving, KV Cache, Agentic Workloads

## 中文关键词
LLM 服务，KV 缓存，智能体负载

[返回 Session 22](index.md) · [返回 ATC 2026](../index.md)
