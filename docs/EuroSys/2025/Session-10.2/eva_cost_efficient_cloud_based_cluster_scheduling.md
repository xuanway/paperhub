---
title: "Eva: Cost-Efficient Cloud-Based Cluster Scheduling"
description: "EuroSys 2025 · Cloud and Networking - Rotterdam hall 1B · Tzu-Tao Chang (University of Wisconsin-Madison), Shivaram Venkataraman (Universi"
tags:
  - "EuroSys2025"
  - "Cloud and Networking - Rotterdam hall 1B"
---

# Eva: Cost-Efficient Cloud-Based Cluster Scheduling

**中文标题：** 成本高效的云端集群调度

**所属 Session：** [Session 10.2: Cloud and Networking](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Networking - Rotterdam hall 1B。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Networking - Rotterdam hall 1B</p>
</div>

**作者**：Tzu-Tao Chang (University of Wisconsin-Madison), Shivaram Venkataraman (University of Wisconsin-Madison)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717483)

## 英文摘要

Cloud computing offers flexibility in resource provisioning, allowing an organization to host its batch processing workloads cost-efficiently by dynamically scaling the size and composition of a cloud-based cluster – a collection of instances provisioned from the cloud. However, existing schedulers fail to minimize total cost due to suboptimal task and instance scheduling strategies, interference between co-located tasks, and instance provisioning overheads. We present Eva, a scheduler for cloud-based clusters that reduces the overall cost of hosting long-running batch jobs. Eva leverages reservation price from economics to derive the optimal set of instances to provision and task-to-instance assignments. Eva also takes into account performance degradation when co-locating tasks and quantitatively evaluates the trade-off between short-term migration overhead and long-term provision savings when considering a change in cluster configuration. Experiments on AWS EC2 and large-scale trace-driven simulations demonstrate that Eva reduces costs by 42% while incurring only a 15% increase in JCT, compared to provisioning a separate instance for each task.

## 中文摘要

云计算在资源配置上提供了灵活性，使组织能够通过动态调整基于云的集群（即从云中申请的实例集合）的规模与构成，以成本高效的方式承载其批处理工作负载。然而，由于任务与实例调度策略次优、共置任务之间的干扰以及实例申请开销，现有调度器未能最小化总成本。我们提出 Eva，一个面向基于云的集群的调度器，可降低承载长时间运行批处理作业的总体成本。Eva 借助经济学中的保留价格来推导最优的实例申请集合与任务到实例的分配。Eva 还考虑共置任务时的性能退化，并在考虑变更集群配置时定量评估短期迁移开销与长期申请节省之间的权衡。在 AWS EC2 上的实验以及大规模 trace 驱动的仿真表明，与为每个任务单独申请实例相比，Eva 将成本降低 42%，而 JCT 仅增加 15%。

**英文关键词：** Cloud Computing, Cluster Scheduling

**中文关键词：** 云计算、集群调度

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
