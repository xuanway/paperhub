---
title: "gShare: Efficient GPU Sharing with Aggressive Scheduling in Multi-tenant FaaS platform"
description: "ASPLOS 2026 · Session 2C · gShare：多租户 FaaS 平台中采用激进调度的高效 GPU 共享"
tags:
  - "ASPLOS2026"
  - "Session 2C"
  - "GPU Systems & Scheduling"
---

# gShare: Efficient GPU Sharing with Aggressive Scheduling in Multi-tenant FaaS platform

**中文标题：** gShare：多租户 FaaS 平台中采用激进调度的高效 GPU 共享

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yanan Yang (China Telecom Cloud Computing Research Institute), Zhengxiong Jiang (China Telecom Cloud Technology Co. Ltd.), Meiqi Zhu (China Telecom Cloud Technology Co. Ltd.), Hongqiang Xu (China Telecom Cloud Technology Co. Ltd.), Yujun Wang (China Telecom Cloud Technology Co. Ltd.), Liang Li (China Telecom Cloud Computing Research Institute), Jiansong zhang (China Telecom Cloud Computing Research Institute), Jie Wu (China Telecom Cloud Computing Research Institute)

**单位：** China Telecom Cloud Computing Research Institute；China Telecom Cloud Technology Co. Ltd.

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790168) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Serving ML models with serverless computing has become increasingly popular in recent years. Many of today's cloud vendors have provided GPU functions to meet the performance requirements of different ML scenarios. However, existing production FaaS platforms suffer from GPU underutilization and high cloud costs due to poor GPU resource management. In this paper, we propose gShare, an on-demand and efficient GPU function management policy in FaaS platforms. gShare provides a fine-grained GPU virtualization solution for a VM-based multi-tenant FaaS environment. It further decouples the GPU resource from the existing CPUoriented function management paradigm, enabling flexible GPU sharing across tenants. With a user-transparent vGPU remapping design and aggressive request scheduling policy, gShare can significantly improve the cost-efficiency of GPU functions without causing appreciable function performance degradation. Experimental results show that gShare can reduce GPU usage by 43%–63% compared to the baseline Compared with the state-of-the-art method, it can also reduce cloud costs by 24%-58% while maintaining better function performance, benefiting both the cloud provider and users.

## 中文摘要

近年来，使用无服务器计算来服务 ML 模型已变得越来越流行。当今许多云厂商已提供 GPU 函数，以满足不同 ML 场景的性能需求。然而，现有的生产 FaaS 平台因 GPU 资源管理不佳而遭受 GPU 利用率不足和高昂云成本的问题。在本文中，我们提出 gShare，一种 FaaS 平台中按需且高效的 GPU 函数管理策略。gShare 为基于 VM 的多租户 FaaS 环境提供细粒度的 GPU 虚拟化方案。它进一步将 GPU 资源与现有的面向 CPU 的函数管理范式解耦，从而实现跨租户的灵活 GPU 共享。借助对用户透明的 vGPU 重映射设计和激进的请求调度策略，gShare 能显著提升 GPU 函数的成本效率，而不会造成可察觉的函数性能下降。实验结果表明，与基线相比，gShare 可将 GPU 使用量降低 43%–63%；与最先进的方法相比，它还能在保持更好函数性能的同时将云成本降低 24%-58%，使云提供商和用户双方受益。

## 英文关键词

FaaS-as-a-Service, GPU function, Hardware virtualization

## 中文关键词

FaaS 即服务；GPU 函数；硬件虚拟化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790168)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2026](../index.md)
