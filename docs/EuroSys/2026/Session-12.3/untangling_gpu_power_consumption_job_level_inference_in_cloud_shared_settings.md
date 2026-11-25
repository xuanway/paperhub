---
title: "Untangling GPU Power Consumption: Job-Level Inference in Cloud Shared Settings"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Pierre Jacquet (École de technologie supérieure), Maxime Agusti (Univ Lyon1, Inr"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# Untangling GPU Power Consumption: Job-Level Inference in Cloud Shared Settings

**中文标题：** 厘清 GPU 功耗：云共享环境中的作业级推理

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Pierre Jacquet (École de technologie supérieure), Maxime Agusti (Univ Lyon1, Inria, OVHcloud), Eddy Caron (Univ Lyon1, Inria, ENS de Lyon, CNRS), Camille Coti (École de technologie supérieure), Marcos Dias De Assunção (École de technologie supérieure), Laurent Lefèvre (Univ Lyon1, Inria, ENS de Lyon, CNRS), Anne-Cécile Orgerie (CNRS, IRISA, Rennes - France)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769333)

## 英文摘要

As the demand for AI-driven workloads increases, the energy consumption of Graphics Processing Units (GPUs) devices has come under intense scrutiny, particularly in hyperscale data centers where large numbers of accelerators are centralized and leased to diverse clients.

In the context of cloud hyperscalers, GPUs power monitoring presents several challenges that vary depending on the product offered. The monitoring capabilities of physical devices may be limited or even absent for some products. However, given the substantial energy demands of GPUs, power monitoring is essential for both cloud providers and clients. Operators require tools to manage power distribution effectively, such as balancing workloads across Power Distribution Units (PDUs), while clients need visibility into power usage to optimize their workloads for energy efficiency.

To address these challenges, we propose methods for estimating the energy consumption of jobs running on GPU devices in cloud environments, spanning from shared and managed offerings like ML-as-a-Service (MLaaS) to less managed products (e.g., Infrastructure-as-a-Service (IaaS)). Our models demonstrate the benefits of sharing GPUs for small AI workloads, as well as the current sub-optimal utilization of GPUs in cloud hyperscalers, based on insights from an IaaS GPU cluster.

## 中文摘要

随着 AI 驱动负载需求的增长，图形处理器（GPU）设备的能耗受到密切关注，尤其是在集中部署大量加速器并将其租给不同客户的大规模数据中心。

在云超大规模服务商场景中，GPU 功耗监控面临若干因产品类型而异的挑战。某些产品的物理设备监控能力可能受限甚至缺失。然而，鉴于 GPU 巨大的能耗需求，功耗监控对云服务商和客户都至关重要。运维人员需要工具来有效管理功率分配，例如在电源分配单元（PDU）之间均衡负载；客户则需要了解功耗使用情况，以优化其工作负载的能效。

为应对这些挑战，我们提出在云环境中估算 GPU 设备上运行作业能耗的方法，涵盖从机器学习即服务（MLaaS）等共享托管型产品到托管程度较低的产品（如基础设施即服务，IaaS）。基于来自一个 IaaS GPU 集群的洞见，我们的模型展示了共享 GPU 对小型 AI 负载的益处，以及当前云超大规模服务商中 GPU 利用尚未达到最优的现状。

**英文关键词：** Cloud computing, GPU, Power consumption

**中文关键词：** 云计算、GPU、功耗

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
