---
title: "AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving"
description: "EuroSys 2026 · LLM Serving & Agents · Sudipta Saha Shubha (University of Virginia), Ayush Goel (HPE Labs), Diman Zad T"
tags:
  - "EuroSys2026"
  - "LLM Serving & Agents"
---

# AdaGen: Workload-Adaptive Cluster Scheduler for Latency-Optimal LLM Inference Serving

**中文标题：** AdaGen：面向延迟最优LLM推理服务的工作负载自适应集群调度器

**所属 Session：** [Session 8.1: LLM Serving & Agents](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Serving & Agents。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Serving & Agents</p>
</div>

**作者**：Sudipta Saha Shubha (University of Virginia), Ayush Goel (HPE Labs), Diman Zad Tootaghaj (HPE Labs), Khaled Diab (HPE Labs), Hardik Soni (HPE Labs), K. K. Ramakrishnan (University of California, Riverside), Puneet Sharma (HPE Labs), Haiying Shen (University of Virginia)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769345)

## 英文摘要

The inference workloads of Large Language Models (LLMs) pose significant latency and cost challenges due to increasing model sizes and demand for real-time responses. Existing cluster schedulers for multi-instance LLM serving primarily focus on load balancing to optimize memory usage, which is insufficient for workloads with diverse request characteristics. In such cases, the compute layout—the arrangement of tokens across iterations within each instance—plays a crucial role in determining latency. We propose AdaGen, a workload-adaptive cluster scheduler that minimizes latency and thus maximizes SLO attainment by optimizing compute layouts across instances. AdaGen employs a multi-step scheduling strategy: it first classifies requests based on prefill and decode lengths, then balances load, and finally performs selective distributed execution across instances. Each step incrementally refines the scheduling based on the compute layouts derived from the decision of the previous step. To avoid the overhead of actual execution to generate the layouts, AdaGen introduces a novel simulation-based estimator. Extensive experiments using production workloads show that AdaGen achieves up to 3.6× higher SLO attainment and 2× better cost-efficiency compared to the existing systems, while ensuring scalability.

## 中文摘要

由于模型规模不断增大以及实时响应的需求，大语言模型（LLM）的推理工作负载带来了显著的延迟与成本挑战。现有多实例LLM服务的集群调度器主要关注负载均衡以优化内存使用，这对于请求特征多样的工作负载而言是不够的。在此类情况下，计算布局——即每个实例内各次迭代之间token的排布方式——在决定延迟方面起着关键作用。我们提出AdaGen，一个工作负载自适应的集群调度器，通过优化各实例间的计算布局来最小化延迟，从而最大化SLO达成率。AdaGen采用多步调度策略：首先根据预填充和解码长度对请求分类，然后进行负载均衡，最后在实例间执行选择性的分布式执行。每一步都基于前一步决策所导出的计算布局逐步细化调度。为避免实际执行以生成布局的开销，AdaGen引入了一种新颖的基于仿真的估计器。使用生产工作负载的大量实验表明，与现有系统相比，AdaGen的SLO达成率最高提升3.6倍，成本效益提升2倍，同时保证了可扩展性。

**英文关键词：** LLM, Inference, Infrastructure, Scheduling

**中文关键词：** LLM、推理、基础设施、调度

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
