# Everything you always wanted to know about RDMA-based distributed Key-Value Stores

**中文标题**：关于基于 RDMA 的分布式键值存储的一切

**所属 Session**：[Session 15: Remote Memory and RDMA](index.md) · [ATC 2026](../index.md)

**作者**：Paul Breuil (Inria and University of Sydney), Sumit Kumar Monga (Inria), Baptiste Lepers (Inria)

## 英文摘要
Multiple designs have been proposed for RDMA-based key-value stores (KVs). In the server-centric model, clients issue RPCs to servers that handle all KV operations. In disaggregated KVs, clients manage the KV over the network, manipulating the server’s memory using one-sided RDMA operations. Finally, hybrid systems try to strike a balance by offloading some operations to the clients while keeping complex-to-offload tasks on the server. Prior evaluations are typically conducted within a single design family (e.g., disaggregated systems are compared against other disaggregated systems). As a result, existing studies provide limited insight into the relative performance and resource usage of these designs. Furthermore, comparing these designs by reading publications or running the artifacts is challenging because published systems differ substantially in their implementations, workloads, and evaluation methodologies. In this paper, we take a different approach. We present the first unified comparison of representative server-centric, hybrid, and disaggregated key-value store designs. We reimplement four state-of-the-art designs within a common code base and evaluate them under identical workloads while measuring not only throughput and latency, but also CPU, memory, and network resource consumption. Our results challenge several assumptions commonly associated with RDMA-based key-value stores. We show that an optimized server-centric design achieves substantially higher throughput than hybrid and disaggregated KVs while maintaining low CPU utilization. Contrary to the prevailing narrative, server CPUs are not the dominant bottleneck in our experiments; instead, all designs are limited by the cost and throughput of RDMA operations, particularly for write-intensive workloads. Counterintuitively, we further show that disaggregated and hybrid approaches increase the total CPU and memory consumption of key-value stores but have overall lower latency than server-centric designs.

## 中文摘要
针对基于 RDMA 的键值存储（KV），已有多种设计被提出。在服务器中心模型中，客户端向服务器发起 RPC，由服务器处理所有 KV 操作。在分离式 KV 中，客户端在网络上管理 KV，使用单边 RDMA 操作直接操作服务器内存。最后，混合式系统试图取得平衡，将部分操作卸载到客户端，同时把难以卸载的任务留在服务器端。以往的评估通常只在单一设计家族内部进行（例如将分离式系统与其他分离式系统相比较）。因此，现有研究对这些设计之间的相对性能与资源使用情况提供的洞见有限。此外，通过阅读论文或运行工件来比较这些设计颇具挑战，因为已发表的系统在实现、工作负载和评估方法上差异很大。本文采取不同的做法。我们首次对代表性的服务器中心、混合式与分离式键值存储设计进行统一比较。我们在统一代码库中重新实现了四种最先进的设计，并在相同工作负载下评估它们，不仅测量吞吐和延迟，还测量 CPU、内存和网络资源消耗。我们的结果挑战了若干通常与基于 RDMA 的键值存储相关联的假设。我们表明，经过优化的服务器中心设计在保持低 CPU 利用率的同时，其吞吐显著高于混合式和分离式 KV。与流行说法相反，在我们的实验中服务器 CPU 并非主导瓶颈；相反，所有设计都受限于 RDMA 操作的成本与吞吐，尤其是在写密集型工作负载下。与直觉相反，我们进一步表明，分离式与混合式方法会增加键值存储的总 CPU 和内存消耗，但整体延迟低于服务器中心设计。

## 英文关键词
RDMA, Key-Value Stores, Disaggregated Memory

## 中文关键词
RDMA，键值存储，分离式内存

[返回 Session 15](index.md) · [返回 ATC 2026](../index.md)
