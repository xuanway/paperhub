---
title: "Pyramid: A Secure, Resource-Efficient, and Pluggable Kubernetes for Multi-Tenancy"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Xiang Li (Tsinghua University, China Telecom eSurfing Cloud (State Cloud)), Weij"
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Pyramid: A Secure, Resource-Efficient, and Pluggable Kubernetes for Multi-Tenancy

**中文标题：** Pyramid：面向多租户的安全、资源高效且可插拔的Kubernetes

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Xiang Li (Tsinghua University, China Telecom eSurfing Cloud (State Cloud)), Weijie Liu (Nankai University), Fabing Li (Ant Group), Hongliang Tian (Ant Group), Zheli Liu (Nankai University), Shoumeng Yan (Ant Group), Mingyu Gao (Tsinghua University, Shanghai Qi Zhi Institute)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769324)

## 英文摘要

This work aims to achieve the best of both worlds with two prominent techniques adopted in cloud computing systems: hardware trusted execution environments (TEEs) for data processing security, and Kubernetes (k8s) for efficient container orchestration and resource management for multitenancy. A secure, resource-efficient, and pluggable container orchestration system, called Pyramid, is proposed, which incurs minimal intrusive modifications to the commercial k8s. Pyramid puts a separate trusted k8s on top of the original k8s cluster and carefully cooperates between the two layers. The workflow within each layer is maximally preserved without significant changes. The untrusted layer manages resource scheduling across different tenants to improve utilization and passes the resource information to the trusted layer to launch actual computations secured by TEEs, with the help of carefully designed interface and protection mechanisms. Evaluation results show that Pyramid achieves 1.4× higher throughput on the data plane, with comparable control-plane performance to previous work.

## 中文摘要

本工作旨在兼得云计算系统中两种主流技术的优势：用于数据处理安全的硬件可信执行环境（TEE），以及用于多租户高效容器编排与资源管理的Kubernetes（k8s）。我们提出一个安全、资源高效且可插拔的容器编排系统Pyramid，它对商用k8s的侵入式修改极少。Pyramid在原有k8s集群之上放置一个独立的可信k8s，并让两层之间谨慎协作。每一层内部的工作流在不发生重大变化的情况下得到最大程度保留。不可信层负责跨不同租户的资源调度以提升利用率，并借助精心设计的接口与保护机制，将资源信息传递给可信层，以启动受TEE保护的实际计算。评估结果表明，Pyramid在数据平面上实现了1.4倍的吞吐量提升，控制平面性能与先前工作相当。

**英文关键词：** Trusted Execution Environment, Kubernetes, Container, Resource Management, Isolation

**中文关键词：** 可信执行环境、Kubernetes、容器、资源管理、隔离

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
