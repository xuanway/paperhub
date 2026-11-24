# Model-as-a-Service in the Wild: Characterizing Production LLM Inference Clusters at Scale

**中文标题**：真实环境中的模型即服务：大规模生产 LLM 推理集群的负载刻画

**所属 Session**：[Session 22: Large-scale AI](index.md) · [ATC 2026](../index.md)

**作者**：Yiyun Zheng (The Chinese University of Hong Kong, Shenzhen), Lingyun Yang (Alibaba Group & Shanghai Jiao Tong University), Yinghao Yu (Alibaba Group), Guodong Yang (Alibaba Group), Liping Zhang (Alibaba Group), Minchen Yu (The Chinese University of Hong Kong, Shenzhen)

## 英文摘要
Large language model (LLM) inference has been widely deployed in modern cloud platforms as Model-as-a-Service (MaaS), serving both online and offline applications on shared, heterogeneous GPU clusters. Recent characterization studies have examined request-level workload patterns, but cluster-wide resource patterns and system-level deployment behaviors remain largely unexplored. This missing view is critical for diagnosing production bottlenecks and for understanding whether and how existing inference techniques should be applied in real MaaS systems. In this paper, we analyze a six-month production LLM inference trace from xMaaS, a large-scale MaaS platform with over 100K GPUs. xMaaS provides a detailed system view of cluster resources and their allocation across 300K applications and 70K model variants, enabling a resource-centric analysis across cluster, application, and model levels. Our study characterizes how heterogeneous GPU resources are supplied and utilized, how application resource demand is distributed and evolves over time, and how model variants and serving modes affect resource allocation on heterogeneous hardware. Based on these observations, we further analyze deployment implications and identify open problems for production MaaS systems, which we hope will motivate future research on resource-efficient LLM inference.

## 中文摘要
大语言模型（LLM）推理已作为模型即服务（MaaS）在现代云平台中广泛部署，在共享的异构 GPU 集群上同时服务在线与离线应用。近期的负载刻画研究考察了请求级的负载模式，但集群级资源模式与系统级部署行为仍基本未被探索。这一缺失的视角对于诊断生产瓶颈、以及理解现有推理技术是否应以及如何应用于真实 MaaS 系统至关重要。本文分析了来自 xMaaS 的为期六个月的生产 LLM 推理 trace，xMaaS 是一个拥有超过 10 万块 GPU 的大规模 MaaS 平台。xMaaS 提供了集群资源及其在 30 万个应用与 7 万个模型变体之间分配情况的详细系统视图，使我们能够开展跨集群、应用与模型三个层次的以资源为中心的分析。我们的研究刻画了异构 GPU 资源如何被供给与利用、应用资源需求如何分布并随时间演化，以及模型变体与服务模式如何影响异构硬件上的资源分配。基于这些观察，我们进一步分析了对部署的启示，并识别出生产 MaaS 系统面临的开放问题，期望能推动未来面向资源高效 LLM 推理的研究。

## 英文关键词
LLM inference, Model-as-a-Service, workload characterization, production traces, heterogeneous GPU clusters, resource management

## 中文关键词
LLM 推理，模型即服务，负载刻画，生产 trace，异构 GPU 集群，资源管理

[返回 Session 22](index.md) · [返回 ATC 2026](../index.md)
