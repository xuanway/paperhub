---
title: "Cacheman: A Comprehensive Last-Level Cache Management System for Multi-tenant Clouds"
description: "PPoPP 2026 Session 7（Cluster and Cloud Computing）：梯度式 LLC way 共享+秒级重分配，生产环境显著降低争用 SLA 违约"
tags:
  - "PPoPP2026"
  - "Session-7"
  - "Cluster and Cloud Computing"
  - "last-level cache"
  - "resource management"
  - "multi-tenant cloud"
authors:
  - "Xiaokang Hu"
  - "Yuchao Cao"
  - "Naixuan Guan"
  - "Yifan Wu"
  - "Xishi Qiu"
  - "Shengdong Dai"
  - "Ben Luo"
  - "Sanchuan Cheng"
  - "Fudong Qiu"
  - "Yibin Shen"
  - "Jiesheng Wu"
session: "Session 7: Cluster and Cloud Computing"
session_number: 7
session_chair: "Ruslan Nikolaev"
date: "2026-02-03"
time: "11:30–11:50"
room: "Pyrmont"
doi: "10.1145/3774934.3786415"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Cacheman: A Comprehensive Last-Level Cache Management System for Multi-tenant Clouds

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出多租户云 LLC 管理系统 Cacheman，用梯度式 way 共享与秒级实时分配兼顾公平和利用率，以协商上界保障分布式应用性能一致性，生产部署显著减少 LLC 争用引发的 SLA 违约。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 7: Cluster and Cloud Computing</p>
</div>

**作者**：Xiaokang Hu, Yuchao Cao, Naixuan Guan, Yifan Wu, Xishi Qiu, Shengdong Dai, Ben Luo, Sanchuan Cheng, Fudong Qiu, Yibin Shen, and Jiesheng Wu — Alibaba Cloud Computing, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 11:30–11:50 · Session 7: Cluster and Cloud Computing（主席：Ruslan Nikolaev）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786415) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Competition for the last-level cache (LLC) is a long-standing issue in multi-tenant cloud environments, often leading to severe performance interference among co-located virtual machines. LLC management in the cloud faces unique challenges, including unpredictable tenant workloads, misaligned performance metrics, and the need to ensure fairness under service level agreements (SLAs). Existing LLC allocation methods fall short in addressing these challenges. We present Cacheman, a comprehensive LLC management system designed from real-world cloud deployment experience. Cacheman introduces a novel gradient-based sharing mechanism for LLC ways, enabling smooth LLC allocation adjustments that simultaneously improve fairness and utilization efficiency. Its real-time allocation algorithm promptly detects and mitigates unfair LLC allocation, adapting to dynamic workloads with second-scale responsiveness. Additionally, Cacheman supports performance consistency for tenants running distributed applications by enforcing negotiated upper bounds on cache usage. Extensive experiments These authors contributed equally to this work. demonstrate that Cacheman effectively achieves its multidimensional goals, and long-term production deployment further shows that it significantly reduces SLA violations caused by LLC contention.

## 中文摘要

对末级缓存（LLC）的竞争是多租户云环境中长期存在的问题，往往导致同宿虚拟机上出现严重的性能干扰。云环境中的 LLC 管理面临独特挑战，包括租户负载不可预测、性能指标口径不一致，以及需要在服务等级协议（SLA）约束下确保公平性。现有的 LLC 分配方法难以应对这些挑战。我们提出 Cacheman，一个基于真实云部署经验设计的综合性 LLC 管理系统。Cacheman 引入了一种新颖的基于梯度的 LLC 路（way）共享机制，能够平滑地调整 LLC 分配，同时提升公平性与利用率效率。其实时分配算法可及时检测并缓解不公平的 LLC 分配，以秒级响应速度适应动态负载。此外，Cacheman 通过对缓存使用施加协商确定的上界，为运行分布式应用的租户提供性能一致性保障。大量实验表明，Cacheman 有效实现了其多维目标，长期的生产环境部署进一步表明，它显著减少了由 LLC 竞争引发的 SLA 违规。

## 英文关键词

last-level cache, virtual machines, multi-tenancy, cloud computing, resource allocation, fairness, SLA compliance

## 中文关键词

末级缓存（last-level cache）；虚拟机；多租户；云计算；资源分配；公平性；SLA 合规性

---

## 一句话总结

> 提出多租户云 LLC 管理系统 Cacheman，用梯度式 way 共享与秒级实时分配兼顾公平和利用率，以协商上界保障分布式应用性能一致性，生产部署显著减少 LLC 争用引发的 SLA 违约。

## 研究问题

多租户云中最后一层缓存（LLC）争用造成同宿虚拟机间严重的性能干扰，而租户负载不可预测、性能指标口径不一致，且必须在 SLA 约束下保证公平，现有 LLC 分配方法难以应对这些挑战。

## 方法简述

- 提出基于梯度的 LLC way 共享机制，使 LLC 分配能够平滑调整，同时改善公平性与利用率。
- 设计实时分配算法，及时发现并缓解不公平的 LLC 分配，以秒级响应适应动态变化的租户负载。
- 采用协商确定的缓存使用上界，为运行分布式应用的租户提供性能一致性保障。
- 基于真实云环境的部署经验设计整套 LLC 管理系统，覆盖分配、调整与一致性保障。

## 主要结果

- 大量实验表明 Cacheman 能够同时达成公平性、利用率等多维管理目标（摘要未给出具体量化数值）。
- 长期生产环境部署显示，Cacheman 显著减少了由 LLC 争用引起的 SLA 违约。

---

> 所属 Session：[Session 7: Cluster and Cloud Computing](index.md) · 返回 [PPoPP 2026 总览](../index.md)
